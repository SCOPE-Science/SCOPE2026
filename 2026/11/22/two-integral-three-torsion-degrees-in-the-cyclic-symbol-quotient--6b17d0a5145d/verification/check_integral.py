from collections import Counter,defaultdict
from itertools import combinations
import time,sys
T=time.monotonic()
N=27
verts=[(r,c,s) for r in range(3) for c in range(3) for s in range(3)]
comp=[0]*27
for i,(r,c,s) in enumerate(verts):
 for j,(r2,c2,s2) in enumerate(verts):
  if i!=j and sum(u==v for u,v in zip((r,c,s),(r2,c2,s2)))>=2:comp[i]|=1<<j
rot=[9*r+3*c+(s+1)%3 for r,c,s in verts]
def rotate(x):
 o=0
 while x:
  q=x&-x; i=q.bit_length()-1; o|=1<<rot[i];x-=q
 return o
def canon(x):
 y=rotate(x);z=rotate(y);return min(x,y,z)
by_card=[set() for k in range(10)]
def walk(prefix,nexti,forbid):
 by_card[prefix.bit_count()].add(canon(prefix))
 for i in range(nexti,27):
  if forbid>>i&1: continue
  walk(prefix|1<<i,i+1,forbid|comp[i])
walk(0,0,0)
assert [len(s) for s in by_card]==[1,9,90,426,1026,1278,804,252,36,4]
print('counts', [len(s) for s in by_card], 'time',time.monotonic()-T,flush=True)
# order = cell index 3r+c, no collisions within face. Rotations preserve order.
faces=[sorted(x) for x in by_card]
ord=[{x:i for i,x in enumerate(faces[d])} for d in range(10)]
B={}
for k in range(1,9):
    B[k]={}
    for col,face in enumerate(faces[k+1]):
        rowmap={}
        x=face; pos=0
        while x:
            bit=x&-x; x-=bit
            y=canon(face-bit)
            row=ord[k][y]
            assert row not in rowmap
            rowmap[row]= (-1)**pos
            pos+=1
        B[k][col]=rowmap
# k is dimension index; columns in C_k are faces[k+1].
# Boundary d0: not present, d1->C0 etc.
print('boundary built',time.monotonic()-T,flush=True)

def check_complex(B):
 for k in range(2,9):
  bk=B[k-1]
  for c,col in B[k].items():
   sums=defaultdict(int)
   for r,a in col.items():
    for rr,b in bk[r].items(): sums[rr]+=a*b
   assert all(x==0 for x in sums.values()),(k,c,sums)
check_complex(B)
print('boundary squared zero',time.monotonic()-T,flush=True)
# Algebraic unit cancellation over Z. Coface faces are removed and replaced by homotopy equivalent finite chain complexes.
# For each cancellation pivot (k,col,row), use Schur complement, and delete col/row in adjacent maps.
# deterministic best sparse fill pivot in highest dimensions first, ties by (dimension, keys).
C=[set(range(len(faces[d+1]))) for d in range(9)]
for k in range(1,9):
 assert set(B[k])==C[k]
steps=[]
while True:
  selected=None
  for k in range(8,0,-1):
    # lookup row usages
    usages=defaultdict(list)
    for c,col in B[k].items():
      for r,a in col.items():
        if abs(a)==1: usages[r].append(c)
    if not usages:continue
    candidates=[]
    for r,cols in usages.items():
      for c in cols:
        score=(len(B[k][c])-1)*(len(cols)-1)
        candidates.append((score,k,c,r))
    if candidates:
      selected=min(candidates)
      if selected[0] == 0: break
  if selected is None:break
  score,k,c,r=selected; d=B[k]; a=d[c][r]
  # update columns with nonzero at r; including nonunit coefficients
  impacted=[cc for cc,v in d.items() if cc!=c and r in v]
  pivot=dict(d[c]); pivot.pop(r)
  for cc in impacted:
    v=d[cc]; t=v.pop(r)*a  # unit inversion
    for rr,vv in pivot.items():
      z=v.get(rr,0)-t*vv
      if z:v[rr]=z
      elif rr in v:del v[rr]
  del d[c]
  for cc in d:
    assert r not in d[cc]
  C[k].remove(c); C[k-1].remove(r)
  if k+1 in B:
    for v in B[k+1].values():v.pop(c,None)
  if k-1 in B:
    del B[k-1][r]
  steps.append((k,c,r,a,score))
  if len(steps)%500==0:
    print('steps',len(steps),'remain', [len(s) for s in C], 'time',round(time.monotonic()-T,2),flush=True)
print('DONE',len(steps),'remaining',[len(s) for s in C], 'time',time.monotonic()-T,flush=True)
check_complex(B)
from collections import Counter
for k in range(1,9):
 print('boundary',k,'rows',len(C[k-1]),'columns',len(C[k]),'nonzero',sum(len(z) for z in B[k].values()),'values',Counter(a for v in B[k].values() for a in v.values()).most_common(10))
# Exact reduced boundary certificates; all integers, no modular inference.
assert [len(s) for s in C] == [1,1,1,1,13,0,0,0,0]
assert len(steps)==1954
assert B[1][next(iter(C[1]))] == {}
assert sorted(B[2][next(iter(C[2]))].values()) == [3]
assert B[3][next(iter(C[3]))] == {}
from math import gcd
from functools import reduce
assert sorted(abs(a) for col in B[4].values() for a in col.values()) == [3]*5+[6]*4
assert reduce(gcd,(abs(a) for col in B[4].values() for a in col.values()),0)==3
for k in range(5,9):assert not C[k]
print('LATIN3_CYCLIC_SYMBOL_QUOTIENT_INTEGRAL_OK')
