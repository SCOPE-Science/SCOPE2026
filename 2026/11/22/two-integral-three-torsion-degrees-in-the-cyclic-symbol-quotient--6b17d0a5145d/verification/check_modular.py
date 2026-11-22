"""Independent, directly reduced field-chain check of the three-symbol quotient.
This uses a different face generator and modular elimination, not the integral cancellations.
"""
from itertools import combinations
from collections import defaultdict
from math import prod
# Project onto 9 board cells: a simplex is a partial assignment of symbols
# with no repeat within any row or column. Enumerate in cell order.
def faces():
 F=[set() for _ in range(10)]
 def rec(cell,chosen,rows,cols):
  if cell==9:
   F[len(chosen)].add(tuple(chosen));return
  r,c=divmod(cell,3)
  rec(cell+1,chosen,rows,cols)
  for s in range(3):
   if rows[r]>>s&1 or cols[c]>>s&1: continue
   chosen.append((cell,s))
   a=list(rows);b=list(cols);a[r]|=1<<s;b[c]|=1<<s
   rec(cell+1,chosen,a,b)
   chosen.pop()
 rec(0,[],[0]*3,[0]*3)
 return F
F=faces()
assert [len(z) for z in F]==[1,27,270,1278,3078,3834,2412,756,108,12]
def orbit(face):
 return min(tuple((i,(s+d)%3) for i,s in face) for d in range(3))
Q=[sorted({orbit(f) for f in dim}) for dim in F]
assert [len(q) for q in Q]==[1,9,90,426,1026,1278,804,252,36,4]
inds=[{z:i for i,z in enumerate(s)} for s in Q]

def rank_mod_p(k,p):
 pivots={};n=0
 for face in Q[k+1]:
  col={}
  for i in range(len(face)):
   smaller=face[:i]+face[i+1:];r=inds[k][orbit(smaller)]
   assert r not in col
   col[r]=(1 if i%2==0 else p-1)
  while col:
   pivot=max(col); val=col[pivot]
   if pivot not in pivots:
    inv=pow(val,-1,p)
    pivots[pivot]={i:v*inv%p for i,v in col.items()}
    n+=1;break
   src=pivots[pivot]
   for i,coeff in src.items():
    new=(col.get(i,0)-val*coeff)%p
    if new:col[i]=new
    else:col.pop(i,None)
 return n
for p in (2,3,5):
 ranks=[0]+[rank_mod_p(k,p) for k in range(1,9)]+[0]
 dims=[len(q) for q in Q[1:]]
 betti=[dims[k]-ranks[k]-ranks[k+1] for k in range(9)]
 assert all(z>=0 for z in betti)
 print('p',p,'ranks',ranks,'betti',betti,flush=True)
 assert betti == ([1,0,0,0,12,0,0,0,0] if p!=3 else [1,1,1,1,13,0,0,0,0])
print('LATIN_CYCLIC_QUOTIENT_MODULAR_OK')
