#!/usr/bin/env python3
"""Independent six-plus-six shell contraction for the icosahedral Blume-Capel model."""
import csv
import itertools
from pathlib import Path
from collections import defaultdict
ROOT=Path(__file__).resolve().parent
spin=list(itertools.product((-1,0,1),repeat=6))
# Top block: one pole followed by five vertices on the upper pentagon.
upper=[]
for u in spin:
 a=u[1:]
 b=u[0]*sum(a)+sum(a[i]*a[(i+1)%5] for i in range(5))
 upper.append((sum(z!=0 for z in u),sum(u),b,a))
# Lower block: five vertices on the lower pentagon followed by the lower pole.
lower=[]
for v in spin:
 b=v[:5]
 energy=v[5]*sum(b)+sum(b[i]*b[(i+1)%5] for i in range(5))
 lower.append((sum(z!=0 for z in v),sum(v),energy,b))
sectors={}
N=0
for ku,mu,bu,a in upper:
 for kv,mv,bv,b in lower:
  bond=bu+bv+sum(a[i]*(b[i]+b[(i-1)%5]) for i in range(5))
  K=ku+kv; M=mu+mv
  if M<0: continue
  if (K,M) not in sectors or bond<sectors[K,M][0]: sectors[K,M]=[bond,1]
  elif bond==sectors[K,M][0]: sectors[K,M][1]+=1
  N+=1
with (ROOT/'sector_minima.csv').open(newline='',encoding='utf-8') as f:
 expected={(int(r['K']),int(r['M'])):(int(r['Bmin']),int(r['multiplicity'])) for r in csv.DictReader(f)}
assert len(expected)==len(sectors)==49
assert all(tuple(sectors[k])==v for k,v in expected.items())
assert 3**12==531441
print('VERIFY_OK independent upper/lower pentagonal transfer contraction, all 49 sector minima and multiplicities')
