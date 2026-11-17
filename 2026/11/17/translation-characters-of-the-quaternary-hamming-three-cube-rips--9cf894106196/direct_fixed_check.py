#!/usr/bin/env python3
"""Independent complete-face signed Lefschetz trace checker (standard library)."""
from itertools import product,combinations
from collections import defaultdict
V=list(product(range(4),repeat=3));index={v:i for i,v in enumerate(V)}
facets=[]
# Every plane in one coordinate fixed
for i in range(3):
 for a in range(4):facets.append([j for j,v in enumerate(V) if v[i]==a])
# Every Hamming radius-one ball
for v in V:facets.append([j for j,u in enumerate(V) if sum(a!=b for a,b in zip(u,v))<=1])
# Every parity tetrahedron in a 2 x 2 x 2 subcube
for aa,bb,cc in product(combinations(range(4),2),repeat=3):
 for parity in (0,1):
  facets.append([index[(aa[x],bb[y],cc[z])] for x,y,z in product(range(2),repeat=3) if (x+y+z)%2==parity])
assert len(facets)==508
faces={0}
for facet in facets:
 subs=[0]
 for i in facet:subs += [x|(1<<i) for x in subs]
 faces.update(subs)
assert len(faces)==830101
print('FULL_FACES',len(faces),flush=True)
bytype={}
for s in product(range(4),repeat=3):
 typekey=tuple(sorted(0 if t==0 else 2 if t==2 else 1 for t in s))
 bytype.setdefault(typekey,s)
for typ,s in sorted(bytype.items()):
 perm=[index[tuple((v[i]+s[i])%4 for i in range(3))] for v in V]
 n=next(k for k in (1,2,4) if all((k*x)%4==0 for x in s))
 # decompose 64-bit mask into eight input octets
 maps=[[sum(1<<perm[8*j+b] for b in range(8) if z>>b&1) for z in range(256)] for j in range(8)]
 total=0;fixed=0
 for f in faces:
  ff=maps[0][f&255]|maps[1][f>>8&255]|maps[2][f>>16&255]|maps[3][f>>24&255]|maps[4][f>>32&255]|maps[5][f>>40&255]|maps[6][f>>48&255]|maps[7][f>>56&255]
  if ff==f:
   fixed+=1;total+=(-1 if (f.bit_count()//n)&1 else 1)
 expected={(0,0,0):405,(0,0,1):9,(0,0,2):9,(0,1,1):-3,(0,1,2):-3,(0,2,2):45,(1,1,1):1,(1,1,2):1,(1,2,2):1,(2,2,2):1}[typ]
 assert total==expected,(s,total,expected)
 print('FIXED_FACE_REP',s,'FACE_COUNT',fixed,'SIGNED_SUM',total,flush=True)
print('DIRECT_FACE_LEFSCHETZ_PASS')
