"""SAR REM repair v0.2. Python 3.10+, standard library only.

Explicit geometry, compliant-boundary mechanics, recovery and handoff.
Author of originating framework: Steve Brown / SAR. Repair: OpenAI assistant.
This companion does not replace the existing WIF reference kernel.
"""
from dataclasses import dataclass, asdict, replace
from math import sqrt, sin, pi, isfinite
from statistics import mean
import hashlib
import json


def tetrahedron(a=1.0):
    if not isfinite(a) or a <= 0:
        raise ValueError('a must be finite and positive')
    return [(a,a,a),(a,-a,-a),(-a,a,-a),(-a,-a,a)]


def segment_intersection(p, q, r, s, tol=1e-10):
    """Finite 2D segments: none, point, or collinear overlap; degenerate supported."""
    sub=lambda a,b:(a[0]-b[0],a[1]-b[1])
    add=lambda a,b:(a[0]+b[0],a[1]+b[1])
    mul=lambda a,t:(a[0]*t,a[1]*t)
    cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
    dot=lambda a,b:a[0]*b[0]+a[1]*b[1]
    u,v,w=sub(q,p),sub(s,r),sub(r,p)
    uu,vv=dot(u,u),dot(v,v)
    if uu <= tol*tol:
        if vv <= tol*tol:
            return {'kind':'point','point':p} if dot(w,w)<=tol*tol else {'kind':'none'}
        t=dot(sub(p,r),v)/vv
        return {'kind':'point','point':p} if abs(cross(sub(p,r),v))<=tol*sqrt(vv) and -tol<=t<=1+tol else {'kind':'none'}
    if vv <= tol*tol:
        return segment_intersection(r,s,p,q,tol)
    den=cross(u,v)
    if abs(den)>tol*sqrt(uu*vv):
        t,b=cross(w,v)/den,cross(w,u)/den
        if -tol<=t<=1+tol and -tol<=b<=1+tol:
            return {'kind':'point','point':add(p,mul(u,t))}
        return {'kind':'none'}
    if abs(cross(w,u))>tol*sqrt(uu):
        return {'kind':'none'}
    t0,t1=dot(w,u)/uu,dot(sub(s,p),u)/uu
    lo,hi=max(0,min(t0,t1)),min(1,max(t0,t1))
    if hi<lo-tol:return {'kind':'none'}
    if abs(hi-lo)<=tol:return {'kind':'point','point':add(p,mul(u,lo))}
    return {'kind':'overlap','segment':[add(p,mul(u,lo)),add(p,mul(u,hi))]}


def simple_enclosure(vertices, tol=1e-9):
    """Ordered, explicitly closed polygon; reject crossing/touching nonadjacent edges."""
    if len(vertices)<4 or sum((vertices[0][i]-vertices[-1][i])**2 for i in (0,1))>tol**2:
        return {'closed':False,'reason':'open path or fewer than three edges'}
    n=len(vertices)-1
    for i in range(n):
        if sum((vertices[i][k]-vertices[i+1][k])**2 for k in (0,1))<=tol**2:
            return {'closed':False,'reason':'zero-length edge'}
        for j in range(i+1,n):
            hit=segment_intersection(vertices[i],vertices[i+1],vertices[j],vertices[j+1],tol)
            adjacent=j==i+1 or (i==0 and j==n-1)
            if (not adjacent and hit['kind']!='none') or (adjacent and hit['kind']=='overlap'):
                return {'closed':False,'reason':'self-intersection or overlap'}
    area=abs(sum(vertices[i][0]*vertices[i+1][1]-vertices[i+1][0]*vertices[i][1] for i in range(n)))/2
    return {'closed':area>tol,'area':area,'dimension':2}


@dataclass(frozen=True)
class Parameters:
    m:float=1.0
    k:float=4.0
    c:float=0.15
    M:float=3.0
    K:float=8.0
    C:float=0.5
    kc:float=40.0
    L0:float=0.75
    Lmax:float=2.0
    amplitude:float=3.0
    omega:float=1.7
    dt:float=0.002
    compliant:bool=True
    energy_limit:float=100.0
    settle_energy:float=1e-5
    settle_seconds:float=1.0

    def validate(self):
        if not all(isfinite(v) for v in asdict(self).values()):raise ValueError('nonfinite parameter')
        if min(self.m,self.k,self.M,self.K,self.kc,self.L0,self.dt,self.settle_seconds)<=0:raise ValueError('positive parameters required')
        if min(self.c,self.C,self.amplitude,self.omega,self.settle_energy)<0:raise ValueError('negative parameter')
        if self.Lmax<=self.L0 or self.energy_limit<=0:raise ValueError('invalid constraint')


class StrokeField:
    """Seven named operations; an explicit design vocabulary, not proven minimal."""
    def __init__(self):
        self.points=[];self.segments=[];self.ledger=[]
    def puncture(self,p):
        if len(p)!=2 or not all(isfinite(v) for v in p):raise ValueError('finite 2D point required')
        self.points.append(tuple(p));self.ledger.append({'op':'puncture','point':list(p)})
        return len(self.points)-1
    def vector(self,i,j):
        if i not in range(len(self.points)) or j not in range(len(self.points)):raise ValueError('unknown vertex')
        self.segments.append((i,j));self.ledger.append({'op':'vector','from':i,'to':j})
        return len(self.segments)-1
    def _transform(self,k,func,name,param):
        i,j=self.segments[k];p,q=self.points[i],self.points[j];u=func(q[0]-p[0],q[1]-p[1])
        new=self.puncture((p[0]+u[0],p[1]+u[1]));edge=self.vector(i,new)
        self.ledger.append({'op':name,'source_segment':k,'new_segment':edge,'parameter':param})
        return edge
    def yield_turn(self,k,angle=pi/2):
        from math import cos
        return self._transform(k,lambda x,y:(x*cos(angle)-y*sin(angle),x*sin(angle)+y*cos(angle)),'yield',angle)
    def angle(self,k,shear):
        # Shear changes even a horizontal segment; unlike y *= factor in the draft.
        return self._transform(k,lambda x,y:(x,y+shear*x),'angle_shear',shear)
    def enclosure(self,indices):
        for a,b in zip(indices,indices[1:]):
            if (a,b) not in self.segments and (b,a) not in self.segments:
                return {'closed':False,'reason':'missing connecting segment'}
        r=simple_enclosure([self.points[i] for i in indices]);self.ledger.append({'op':'enclosure','indices':indices,'result':r});return r
    def intersection(self,a,b):
        i,j=self.segments[a];k,l=self.segments[b];r=segment_intersection(self.points[i],self.points[j],self.points[k],self.points[l]);self.ledger.append({'op':'intersection','segments':[a,b],'result':r});return r
    def reentry(self,state,update):
        new=update(state);self.ledger.append({'op':'reentry','before':state,'after':new});return new


def audit_flow(record,tolerance=1e-9):
    """One declared extensive quantity per balance. Unknown is never a zero."""
    keys=('input','output','loss','inventory_change')
    if not record.get('quantity') or not record.get('unit') or any(record.get(k) is None for k in keys):
        return {'status':'UNRESOLVED','reason':'missing quantity, unit, or measurement'}
    if any(not isfinite(record[k]) for k in keys) or min(record[k] for k in ('input','output','loss'))<0:
        raise ValueError('invalid balance measurements')
    residual=record['input']-record['output']-record['loss']-record['inventory_change']
    return {'status':'BALANCED' if abs(residual)<=tolerance else 'DISCREPANCY','residual':residual,
            'unit':record['unit'],'quantity':record['quantity'],'loss_fraction':record['loss']/record['input'] if record['input'] else None}


def energy(y,p):
    x,v,L,w=y[:4];d=max(abs(x)-L,0)
    return .5*p.m*v*v+.5*p.k*x*x+.5*p.M*w*w+.5*p.K*(L-p.L0)**2+.5*p.kc*d*d


def constraint(y,p):
    return {'Lmin':p.L0,'Lmax':p.Lmax,'energy_limit':p.energy_limit,
            'admissible_actions':['off','drive'] if y[2]<=p.Lmax else ['off']}


def evaluate(y,p,c):
    return {'energy':energy(y,p),'contact_extension':max(abs(y[0])-y[2],0),
            'boundary_margin':c['Lmax']-y[2]}


def choose(metrics,c,policy='drive'):
    if policy not in ('drive','off'):raise ValueError('unknown policy')
    return 'drive' if policy=='drive' and 'drive' in c['admissible_actions'] and metrics['energy']<c['energy_limit'] else 'off'


def rhs(t,y,p,action):
    x,v,L,w,work,loss,stop_loss=y
    d=max(abs(x)-L,0);sign=1 if x>0 else -1 if x<0 else 0
    force=p.amplitude*sin(p.omega*t) if action=='drive' else 0
    return [v,(force-p.c*v-p.k*x-p.kc*d*sign)/p.m,
            w if p.compliant else 0,
            (p.kc*d-p.K*(L-p.L0)-p.C*w)/p.M if p.compliant else 0,
            force*v,p.c*v*v+(p.C*w*w if p.compliant else 0),0.0]


def propagate(t,y,p,action,stop_events=None):
    h=p.dt
    def plus(y,k,s):return [a+s*b for a,b in zip(y,k)]
    a=rhs(t,y,p,action);b=rhs(t+h/2,plus(y,a,h/2),p,action)
    c=rhs(t+h/2,plus(y,b,h/2),p,action);d=rhs(t+h,plus(y,c,h),p,action)
    z=[q+h*(aa+2*bb+2*cc+dd)/6 for q,aa,bb,cc,dd in zip(y,a,b,c,d)]
    # Inelastic lower stop. Book exact energy removed by the numerical projection.
    if z[2]<p.L0:
        before=energy(z,p);z[2]=p.L0;z[3]=max(0,z[3])
        delta=before-energy(z,p)
        z[6]+=delta
        if stop_events is not None:stop_events.append({"t":t+h,"energy_correction":delta})
    return z


def closure(y,p,settled_for):
    if not all(isfinite(v) for v in y):return 'NUMERICAL_FAILURE'
    if y[2]>p.Lmax:return 'CONSTRAINT_BREACH'
    if settled_for>=p.settle_seconds:return 'STABLE'
    return 'CONTINUE'


def simulate(p=Parameters(),seconds=20.0,x0=0.5,v0=0.0,policy='drive',stride=50):
    p.validate()
    if seconds<=0 or stride<1:raise ValueError('invalid run length or stride')
    y=[x0,v0,p.L0,0.0,0.0,0.0,0.0];stop_events=[];e0=energy(y,p);t=0.;settled=0.;crossings=[];rows=[];audit=[];maxL=p.L0;status='CONTINUE'
    for step in range(round(seconds/p.dt)):
        c=constraint(y,p);metrics=evaluate(y,p,c);action=choose(metrics,c,policy)
        z=propagate(t,y,p,action,stop_events)
        if y[0]<0<=z[0] and z[0]!=y[0]:crossings.append(t+p.dt*(-y[0])/(z[0]-y[0]))
        t+=p.dt;maxL=max(maxL,z[2]);en=energy(z,p)
        drive_inactive=policy=='off' or p.amplitude==0 or p.omega==0
        settled=settled+p.dt if en<=p.settle_energy and drive_inactive else 0.
        status=closure(z,p,settled)
        if step%stride==0 or status!='CONTINUE' or step==round(seconds/p.dt)-1:
            rows.append({'t':t,'x':z[0],'v':z[1],'L':z[2],'w':z[3],'energy':en,'work':z[4],'loss':z[5],'stop_loss':z[6],'total_loss':z[5]+z[6],
                         'energy_residual':en-e0-z[4]+z[5]+z[6],'closure':status})
            audit.append({'step':step,'state_before':y[:4],'constraint':c,'evaluation':metrics,'choice':action,'state_after':z[:4],'closure':status})
        y=z
        if status!='CONTINUE':break
    periods=[b-a for a,b in zip(crossings,crossings[1:])]
    return {'schema':'SAR-REM-RUN-2','parameters':asdict(p),'initial':{'x':x0,'v':v0},'policy':policy,'sample_stride':stride,
            'summary':{'closure':status,'max_L':maxL,'initial_energy':e0,'final_energy':energy(y,p),
                       'work':y[4],'loss':y[5],'stop_loss':y[6],'total_loss':y[5]+y[6],
                       'stop_event_count':len(stop_events),'energy_residual':energy(y,p)-e0-y[4]+y[5]+y[6],
                       'mean_crossing_rate_hz':1/mean(periods) if periods else None,
                       'period_cv':sqrt(mean([(q-mean(periods))**2 for q in periods]))/mean(periods) if len(periods)>=2 else None},
            'crossings':crossings,'stop_events':stop_events,'rows':rows,'audit':audit}


def square_histories():
    return [{'start':s,'direction':d,'vertices':[(s+d*k)%4 for k in range(5)]} for s in range(4) for d in (-1,1)]


def recover_square(evidence=()):
    """Finite declared family: one traversal of four fixed square edges, no pen lifts."""
    out=square_histories()
    for field,value in evidence:
        if field not in ('start','direction'):raise ValueError('unknown observation')
        out=[h for h in out if h[field]==value]
    return out


def safe_actions(histories):
    """Justified relative to Gamma and fixed U; not reality-safe if truth is excluded."""
    if not histories:return ['ABSTAIN_INCONSISTENT']
    actions=[{'preserve_trace','request_observation',f"replay_{h['start']}_{h['direction']}"} for h in histories]
    return sorted(set.intersection(*actions))


def reachable(edges,start):
    seen={start}
    while True:
        extra={b for a,b in edges if a in seen}
        if extra<=seen:return sorted(seen)
        seen|=extra


def handoff_packet():
    body={'schema':'SAR-REM-HANDOFF-1','author':'Steve Brown / SAR; synthetic demonstration',
          'field':'four fixed vertices; one closed square traversal; no lifts or retracing',
          'raw_trace':[[0,0],[1,0],[1,1],[0,1],[0,0]],'segmentation':'four consecutive straight edges',
          'evidence':[['start',0],['direction',1]],'encoding':'vertex order; +1 advances counterclockwise',
          'assumptions':['recorded order retained','vertex labels shared'],
          'provenance':['synthetic-square-v1'],'limits':'family-relative reconstruction, not historical attribution'}
    return {'body':body,'sha256':hashlib.sha256(json.dumps(body,sort_keys=True,separators=(',',':')).encode()).hexdigest()}


def verify_packet(packet):
    return hashlib.sha256(json.dumps(packet['body'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==packet['sha256']


def handoff_demo():
    own=[('A','B')];shared=[('B','C'),('C','D')]
    return {'recovery_counts':[len(recover_square()),len(recover_square([('start',0)])),len(recover_square([('start',0),('direction',1)]))],
            'own_reachable':reachable(own,'A'),'shared_reachable':reachable(own+shared,'A'),
            'duplicate_reachable':reachable(own+own,'A'),'packet':handoff_packet(),
            'note':'Synthetic compatible rule composition, not a measured human learning effect.'}


def legacy_replay():
    z=.6;scale=1;octave=1;events=[]
    for step in range(1,13):
        nxt=3.6*z*(1-z);delta=abs(nxt-z)
        if delta>.15 and step>=5:
            octave+=1;scale*=2;events.append(step);nxt=nxt/2+.1
        z=nxt
    return {'expansion_steps':events,'final_scale':scale,'octave_label':octave}


def interference(amplitudes,phases):
    """Scalar coherent phasors, common channel and compatible units."""
    from math import cos
    if len(amplitudes)!=len(phases) or not amplitudes:raise ValueError('matching nonempty arrays required')
    if any(a<0 or not isfinite(a) for a in amplitudes) or any(not isfinite(q) for q in phases):raise ValueError('invalid phasor')
    re=sum(a*cos(q) for a,q in zip(amplitudes,phases));im=sum(a*sin(q) for a,q in zip(amplitudes,phases))
    direct=re*re+im*im
    expanded=sum(a*a for a in amplitudes)+2*sum(amplitudes[i]*amplitudes[j]*cos(phases[i]-phases[j]) for i in range(len(phases)) for j in range(i+1,len(phases)))
    return {'intensity':direct,'expanded_intensity':expanded}


if __name__=='__main__':
    from pathlib import Path
    out=Path(__file__).parent/'results';out.mkdir(exist_ok=True)
    cases={
        'fixed_driven':simulate(replace(Parameters(),compliant=False)),
        'compliant_driven':simulate(),
        'free_oscillator':simulate(replace(Parameters(),c=0,C=0,amplitude=0),policy='off'),
        'damped':simulate(replace(Parameters(),c=1.5,amplitude=0),seconds=25,policy='off'),
        'breach':simulate(replace(Parameters(),Lmax=.751),x0=1.2,policy='off'),
        'handoff':handoff_demo(),'legacy':legacy_replay()}
    (out/'runs.json').write_text(json.dumps(cases,indent=2))
    print(json.dumps({k:v.get('summary',v) for k,v in cases.items()},indent=2))
