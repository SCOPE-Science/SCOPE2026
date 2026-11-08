"""Separate variable-order Morse-chain check for the Pappus induced-forest complex."""
import pappus_forest_certificate as C
from collections import Counter,defaultdict
from functools import lru_cache
C.PIVOTS=(0,16,3,17,11,15,7,13,1,14,5,8,2,10,6,9,12,4)
e,adj=C.graph(); faces,_=C.all_faces(adj)
crit,lo,up=C.vertex_matching(faces)
print('ALTERNATE_MATCHING',len(lo),'critical',Counter(x.bit_count()-1 for x in crit))
a,z=C.directed_hasse_acyclic(faces,lo,up)
assert z==len(faces)
cs=set(crit)
@lru_cache(None)
def reduce(f):
 if f in cs:return ((f,1),)
 if f in up:return ()
 u=lo[f]; p=next(c for v,c in C.boundary(u) if v==f)
 out=defaultdict(int)
 for v,c in C.boundary(u):
  if v==f:continue
  for t,q in reduce(v):out[t]-=p*c*q
 return tuple((a,b) for a,b in out.items() if b)
upper=[x for x in crit if x.bit_count()==12]
lower=[x for x in crit if x.bit_count()==11]
M=[]
for h in upper:
 out=defaultdict(int)
 for f,c in C.boundary(h):
  for t,q in reduce(f):out[t]+=c*q
 M.append([out[x] for x in lower])

rows_map={}
for r in M:
 mask=sum((v%2)<<i for i,v in enumerate(r))
 while mask:
  i=mask.bit_length()-1
  if i in rows_map:mask^=rows_map[i]
  else:
   rows_map[i]=mask
   break
print('ALTERNATE_BOUNDARY_RANK_GF2',len(rows_map),'source_count',len(upper),'target_count',len(lower))
assert len(rows_map)==len(upper) and len(lower)-len(upper)==40
print('ALTERNATE_PAPPUS_MORSE_PASS')
