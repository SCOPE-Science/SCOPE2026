# B found NO relation -> R/K not Galois (order-81 closure). So current theta gives non-Galois R/K.
# PIVOT: search DIFFERENT thetas for the same pair (or other pairs) that DO satisfy a relation B.
# For each candidate theta (from box solutions), compute relation test B over ~40 primes (fast filter),
# then full verification for survivors.
# First: gather MANY distinct theta classes for pair (pi1,pi2)=((-5,-3),(-2,3)) with box B=6.
from eisen import *
from u3lib import *
import time
pi1=(-5,-3); pi2=(-2,3)
t0=time.time()
sols=[]
rng=range(-6,7)
for xa in rng:
 for xb in rng:
  X=(xa,xb)
  for ya in rng:
   for yb in rng:
    Y=(ya,yb)
    for za in rng:
     for zb in rng:
      Z=(za,zb)
      if X==ZERO and Y==ZERO and Z==ZERO: continue
      N=knormXYZ(X,Y,Z,pi1)
      if eeq(N,ZERO) or not edivides(pi2,N): continue
      q,_=edivmod(N,pi2)
      good=False
      for u in UNITS:
          if cube_root_Zw(emul(q,u)) is not None: good=True; break
      if good: sols.append((X,Y,Z))
print(f"nsols={len(sols)} time={time.time()-t0:.0f}s")
import json
json.dump([[list(X),list(Y),list(Z)] for X,Y,Z in sols], open('sols_19.json','w'))
print("saved")
for s in sols[:20]: print(list(map(e2str,s)))
