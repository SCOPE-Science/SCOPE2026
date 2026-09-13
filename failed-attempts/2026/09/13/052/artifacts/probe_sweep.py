import sys; sys.path.insert(0,'.'); import time
sys.setrecursionlimit(100000)
from pipeline2 import run_pattern
out = open('probe_hits.jsonl','w')
t0=time.time()
for asg in ('000000012','000001112','000111222'):
    hit = run_pattern(asg, cap=150, tlim=240, out=out)
    print('PATTERN DONE', asg, 'hit=',hit,'t=',round(time.time()-t0,1),flush=True)
    if hit: break
out.close()
