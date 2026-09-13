import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
from delta import Delta
menu=[(s1*h,s2*h) for h in [0.05,0.03,0.015] for s1 in (1,-1) for s2 in (1,-1)]
def best_bruteforce(x):
    return min(abs(Delta(x,a,b,N=14))/abs(a*b) for (a,b) in menu)
# local search near worst
xc=np.array([0.8225,0.6125])
rng=np.random.default_rng(2)
best=(1e9,None)
for t in range(2000):
    x=(xc+0.01*rng.standard_normal(2))%1.0
    v=best_bruteforce(x)
    if v<best[0]: best=(v,x.copy())
print("local min",best)
# also global random
best2=(1e9,None)
for t in range(2000):
    x=rng.random(2)
    v=best_bruteforce(x)
    if v<best2[0]: best2=(v,x.copy())
print("global random min",best2)
# evaluate at global best with N=16 and more pairs
x=best2[1]
pairs=[(a,b) for a in [0.05,0.04,0.03,0.02,0.015,0.01,-0.01,-0.015,-0.02,-0.03,-0.04,-0.05] for b in [0.05,0.04,0.03,0.02,0.015,0.01,-0.01,-0.015,-0.02,-0.03,-0.04,-0.05]]
vals=sorted((abs(Delta(x,a,b,N=16))/abs(a*b),(a,b)) for (a,b) in pairs)
print("x=",x)
for v,p in vals[:8]: print(v,p)
