#!/usr/bin/env python3
"""Independent orbit formula verification, all group elements."""
from itertools import product
import json
from pathlib import Path
S={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
nb=[0]*16
for x,y in product(range(4),repeat=2):
 i=4*x+y
 for dx,dy in S:
  u,v=(x+dx)%4,(y+dy)%4
  nb[i]|=1<<(4*u+v)
nb=[nb[i]|1<<i for i in range(16)]
# independent orbit-product character calculation
transforms=[]
for a,b,c,d in product(range(4),repeat=4):
 images={((a*x+b*y)%4,(c*x+d*y)%4) for x,y in S}
 if images==S:transforms.append((a,b,c,d))
assert len(transforms)==12
aut=[]; traces=[]
for a,b,c,d in transforms:
 for tx,ty in product(range(4),repeat=2):
  perm=tuple(4*((a*x+b*y+tx)%4)+((c*x+d*y+ty)%4) for x,y in product(range(4),repeat=2))
  assert len(set(perm))==16
  aut.append(perm)
  orbits=[];seen=set()
  for v in range(16):
   if v in seen:continue
   m=0;u=v
   while u not in seen:
    seen.add(u);m|=1<<u;u=perm[u]
   orbits.append(m)
  trace=0
  for subset in range(1<<len(orbits)):
   m=0;q=subset
   while q:
    z=q&-q;q^=z;m|=orbits[z.bit_length()-1]
   if not any((m&x)==x for x in nb):trace+=-1 if subset.bit_count()%2 else 1
  traces.append(trace)
assert len(aut)==192
with open(Path(__file__).with_name('certificate.json')) as f:cert=json.load(f)
assert traces==cert['Shrikhande']['character_by_group_element']
assert sum(traces)==0
assert sum(x*x for x in traces)==3*192
print('ALTERNATE_ORBIT_LEFSCHETZ_CHECK_PASS')
