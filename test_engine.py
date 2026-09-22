import copy,json,math,unittest
from dataclasses import replace
from engine import *

class Geometry(unittest.TestCase):
    def test_operators_retain_source_and_transform(self):
        f=StrokeField();a=f.puncture((0,0));b=f.puncture((1,0));e=f.vector(a,b)
        turn=f.yield_turn(e);skew=f.angle(e,1)
        self.assertAlmostEqual(f.points[f.segments[turn][1]][1],1)
        self.assertEqual(f.points[f.segments[skew][1]],(1,1));self.assertEqual(f.points[b],(1,0))
        self.assertEqual(f.reentry(1,lambda x:1-x),0)
        self.assertEqual(f.reentry(0,lambda x:1-x),1)
    def test_enclosure_requires_edges(self):
        f=StrokeField();[f.puncture(p) for p in [(0,0),(1,0),(0,1)]]
        self.assertFalse(f.enclosure([0,1,2,0])['closed'])
        [f.vector(a,b) for a,b in [(0,1),(1,2),(2,0)]]
        self.assertTrue(f.enclosure([0,1,2,0])['closed'])
    def test_regular_tetrahedron(self):
        import itertools
        v=tetrahedron(2)
        self.assertTrue(all(abs(math.dist(a,b)-4*sqrt(2))<1e-12 for a,b in itertools.combinations(v,2)))
        self.assertEqual([sum(p[i] for p in v) for i in range(3)],[0,0,0])
    def test_open_chain_rejected(self):
        self.assertFalse(simple_enclosure([(0,0),(1,0),(1,1),(0,1)])['closed'])
    def test_triangle_and_bowtie(self):
        self.assertTrue(simple_enclosure([(0,0),(1,0),(0,1),(0,0)])['closed'])
        self.assertFalse(simple_enclosure([(0,0),(1,1),(0,1),(1,0),(0,0)])['closed'])
    def test_finite_segments(self):
        self.assertEqual(segment_intersection((0,0),(1,0),(2,-1),(2,1))['kind'],'none')
        self.assertEqual(segment_intersection((0,0),(1,1),(0,1),(1,0))['point'],(.5,.5))
    def test_overlap_and_point(self):
        self.assertEqual(segment_intersection((0,0),(2,0),(1,0),(3,0))['kind'],'overlap')
        self.assertEqual(segment_intersection((1,0),(1,0),(0,0),(2,0))['kind'],'point')

class Dynamics(unittest.TestCase):
    def test_unforced_energy_and_frequency(self):
        p=replace(Parameters(),c=0,C=0,amplitude=0)
        r=simulate(p,seconds=15,policy='off')
        self.assertLess(abs(r['summary']['energy_residual']),1e-8)
        self.assertAlmostEqual(r['summary']['mean_crossing_rate_hz'],sqrt(p.k/p.m)/(2*pi),places=6)
        self.assertEqual(r['summary']['max_L'],p.L0)
        self.assertEqual(r['summary']['closure'],'CONTINUE')
    def test_damping_settles(self):
        r=simulate(replace(Parameters(),c=1.5,amplitude=0),seconds=25,policy='off')
        self.assertEqual(r['summary']['closure'],'STABLE')
        self.assertLess(r['summary']['final_energy'],r['summary']['initial_energy'])
    def test_expansion_depends_on_compliance(self):
        fixed=simulate(replace(Parameters(),compliant=False),seconds=10)
        flex=simulate(seconds=10)
        self.assertEqual(fixed['summary']['max_L'],.75)
        self.assertGreater(flex['summary']['max_L'],.8)
        self.assertLess(abs(flex['summary']['energy_residual']),.005)
    def test_dt_refinement(self):
        a=simulate(seconds=6);b=simulate(replace(Parameters(),dt=.001),seconds=6)
        self.assertLess(abs(a['rows'][-1]['x']-b['rows'][-1]['x']),.002)
        self.assertLess(abs(a['summary']['max_L']-b['summary']['max_L']),.002)
    def test_breach_is_not_forced_growth(self):
        r=simulate(replace(Parameters(),Lmax=.751),x0=1.2,policy='off')
        self.assertEqual(r['summary']['closure'],'CONSTRAINT_BREACH')
    def test_policy_separable(self):
        p=Parameters();y=[.5,0,.75,0,0,0,0];c=constraint(y,p);m=evaluate(y,p,c)
        self.assertEqual(choose(m,c,'off'),'off');self.assertEqual(choose(m,c,'drive'),'drive')
        self.assertNotEqual(propagate(1,y,p,'off')[1],propagate(1,y,p,'drive')[1])
        self.assertEqual(y,[.5,0,.75,0,0,0,0])
    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):simulate(replace(Parameters(),m=0))

class Recovery(unittest.TestCase):
    def test_flow_audit_and_missingness(self):
        r={'quantity':'mass','unit':'kg','input':10,'output':7,'loss':2,'inventory_change':1}
        self.assertEqual(audit_flow(r)['status'],'BALANCED')
        self.assertEqual(audit_flow({**r,'loss':None})['status'],'UNRESOLVED')
        self.assertEqual(audit_flow({**r,'output':8})['status'],'DISCREPANCY')
    def test_interference(self):
        self.assertAlmostEqual(interference([1,1],[0,0])['intensity'],4)
        self.assertAlmostEqual(interference([1,1],[0,pi])['intensity'],0)
        r=interference([1,.6,.3],[.7,2.1,5.2])
        self.assertAlmostEqual(r['intensity'],r['expanded_intensity'])
    def test_contraction_and_duplicate(self):
        self.assertEqual([len(recover_square()),len(recover_square([('start',0)])),len(recover_square([('start',0),('direction',1)]))],[8,2,1])
        self.assertEqual(recover_square([('start',0)]),recover_square([('start',0),('start',0)]))
    def test_conflict_and_action(self):
        self.assertEqual(safe_actions(recover_square([('start',0),('start',1)])),['ABSTAIN_INCONSISTENT'])
        self.assertNotIn('replay_0_1',safe_actions(recover_square()))
        self.assertIn('replay_0_1',safe_actions(recover_square([('start',0),('direction',1)])))
    def test_handoff_integrity(self):
        p=handoff_packet();self.assertTrue(verify_packet(json.loads(json.dumps(p))))
        self.assertEqual(recover_square(json.loads(json.dumps(p))['body']['evidence']),recover_square([('start',0),('direction',1)]))
        bad=copy.deepcopy(p);bad['body']['evidence'][0][1]=2;self.assertFalse(verify_packet(bad))
    def test_safe_actions_expand_under_nonempty_contraction(self):
        a=set(safe_actions(recover_square()));b=set(safe_actions(recover_square([('start',0)])));c=set(safe_actions(recover_square([('start',0),('direction',1)])))
        self.assertTrue(a<=b<c)
    def test_reachable_gain_and_no_gain(self):
        d=handoff_demo();self.assertEqual(len(d['own_reachable']),2);self.assertEqual(len(d['shared_reachable']),4)
        self.assertEqual(d['duplicate_reachable'],d['own_reachable'])
    def test_legacy_receipt(self):
        self.assertEqual(legacy_replay()['final_scale'],256)

class Refinements(unittest.TestCase):
    def test_numerical_failure_precedes_breach(self):
        self.assertEqual(closure([float('nan'),0,3,0,0,0,0],Parameters(),0),'NUMERICAL_FAILURE')
        from unittest.mock import patch
        with patch('engine.propagate',return_value=[float('nan'),0,.75,0,0,0,0]):
            self.assertEqual(simulate(seconds=.01)['summary']['closure'],'NUMERICAL_FAILURE')
    def test_stop_ledger_reconciles(self):
        r=simulate();s=r['summary']
        self.assertGreater(s['stop_event_count'],0)
        self.assertGreater(s['stop_loss'],0)
        self.assertAlmostEqual(s['stop_loss'],sum(e['energy_correction'] for e in r['stop_events']),places=12)
        self.assertAlmostEqual(s['total_loss'],s['loss']+s['stop_loss'],places=12)
        self.assertAlmostEqual(s['energy_residual'],s['final_energy']-s['initial_energy']-s['work']+s['total_loss'],places=12)
        fixed=simulate(replace(Parameters(),compliant=False),seconds=3)['summary']
        self.assertEqual(fixed['stop_loss'],0)
    def test_cv_requires_two_periods(self):
        p=replace(Parameters(),c=0,C=0,amplitude=0)
        r=simulate(p,seconds=6,policy='off')
        self.assertEqual(len(r['crossings']),2)
        self.assertIsNone(r['summary']['period_cv'])
        self.assertIsNotNone(r['summary']['mean_crossing_rate_hz'])
        self.assertIsNotNone(simulate(p,seconds=10,policy='off')['summary']['period_cv'])
    def test_reachable_nondefault_start(self):
        self.assertEqual(reachable([('A','B'),('B','C')],'B'),['B','C'])

if __name__=='__main__':unittest.main(verbosity=2)
