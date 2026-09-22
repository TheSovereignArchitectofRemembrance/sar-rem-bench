import sys,json
from pathlib import Path
ROOT=Path(__file__).parent
sys.path.insert(0,str(ROOT))
from engine import *
r=[]
for dt in [.0005,.001,.002,.004]:
 q=simulate(replace(Parameters(),dt=dt));r.append({'dt':dt,**q['summary'],'final_x':q['rows'][-1]['x']})
(ROOT/'results/timestep_sweep.json').write_text(json.dumps(r,indent=2))
print(json.dumps(r,indent=2))
