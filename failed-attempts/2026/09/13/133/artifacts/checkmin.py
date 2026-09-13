import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from delta import Delta
x=np.array([0.6325,0.115])
scales=[0.05,0.04,0.03,0.02,0.015,0.01]
menu=[(s1*h1,s2*h2) for h1 in scales for h2 in scales for s1 in (1,-1) for s2 in (1,-1)]
vals=sorted((abs(Delta(x,a,b,N=16))/abs(a*b),(a,b)) for (a,b) in menu)
for v,p in vals[:6]: print(v,p)
# continuous local opt of maxratio? try small perturbations
print("N=18 check:", [(abs(Delta(x,a,b,N=18))/abs(a*b),(a,b)) for _,(a,b) in vals[:3]])
# neighborhood
rng=np.random.default_rng(3)
best=(1e9,None,None)
for t in range(3000):
    z=(x+0.005*rng.standard_normal(2))%1.0
    m=min(abs(Delta(z,a,b,N=12))/abs(a*b) for (a,b) in menu)
    if m<best[0]: best=(m,z,None)
print("neighborhood min",best[0],best[1])
