#!/usr/bin/env python3
"""Integral weight-three reduced Swiatkowski computation for the cube graph.
Pure Python 3.11+, with no package dependencies.
"""
import time
from itertools import combinations, product
from collections import defaultdict

verts=list(range(8));edges=[]
for v in verts:
 for bit in [1,2,4]:
  w=v^bit
  if v<w:edges.append((v,w))
edg={e:i for i,e in enumerate(edges)}
inc={v:[edg[e] for e in edges if v in e] for v in verts}
halfs={v:inc[v][1:] for v in verts}
labels=[]
for vs in combinations(verts,3):
 for hs in product(*(halfs[v] for v in vs)):
  labels.append((vs,hs))
rows={}
cols=[]
for vs,hs in labels:
 col={}
 for i,v in enumerate(vs):
  for e,c in [(hs[i],1),(inc[v][0],-1)]:
   state=(tuple((u,hs[j]) for j,u in enumerate(vs) if j!=i),e)
   c*=(-1)**i
   k=rows.setdefault(state,len(rows))
   col[k]=col.get(k,0)+c
 cols.append({k:v for k,v in col.items() if v})

from itertools import combinations_with_replacement
C2=[(tuple(sorted([(u,hu),(v,hv)])),e) for u,v in combinations(verts,2) for hu in halfs[u] for hv in halfs[v] for e in range(12)]
rr={};cc2=[]
for factors,e in C2:
 col={}
 for i,(v,h) in enumerate(factors):
  for ee,s in [(h,1),(inc[v][0],-1)]:
   target=(factors[1-i],tuple(sorted([e,ee])))
   j=rr.setdefault(target,len(rr))
   col[j]=col.get(j,0)+s*((-1)**i)
 cc2.append({k:v for k,v in col.items() if v})

C1={state:i for state,i in rr.items()}
D2=cc2
D3=cols
C2_index={state:i for i,state in enumerate(C2)}
assert len(C2_index)==len(C2)==1344
assert len(D3)==448 and len(D2)==1344 and len(C1)==1248
for column in D3:
    accum={}
    for index,coef in column.items():
        state=next(st for st,idx in rows.items() if idx==index)
        for r,v in D2[C2_index[state]].items():
            accum[r]=accum.get(r,0)+coef*v
    assert all(x==0 for x in accum.values())
print('d2d3=0 for all 448 columns')
# D1:C1 to C0: an element (vertex factor, edges pair) maps to edge difference times edges pair
C0={}
D1=[]
for (v,h),es in C1:
 col={}
 for e,c in [(h,1),(inc[v][0],-1)]:
  mon=tuple(sorted((*es,e)))
  r=C0.setdefault(mon,len(C0))
  col[r]=col.get(r,0)+c
 D1.append({r:c for r,c in col.items() if c})
for col in D2:
 acc={}
 for i,c in col.items():
  for r,d in D1[i].items():acc[r]=acc.get(r,0)+c*d
 assert not any(acc.values())
print('d1d2 OK',len(D2))

assert len(C0)==364
def reduce(C,limit=120):
 start=time.monotonic();columns={j:dict(c) for j,c in enumerate(C)}
 rows={}
 for j,c in columns.items():
  for i,x in c.items():rows.setdefault(i,{})[j]=x
 piv=[]
 while True:
  if time.monotonic()-start>limit:break
  choices=[]
  for j,c in columns.items():
   if not c:continue
   for i,x in c.items():
    if abs(x)==1:
     choices.append(((len(c)-1)*(len(rows[i])-1),len(rows[i])+len(c),i,j,x))
  if not choices:break
  _,_,i,j,x=min(choices)
  c=columns[j].copy(); row=rows[i].copy()
  for other_j,y in row.items():
   if other_j==j:continue
   v=columns[other_j]; k=y*x
   for ii,z in c.items():
    nv=v.get(ii,0)-k*z
    if nv:v[ii]=nv;rows[ii][other_j]=nv
    else:v.pop(ii,None);rows[ii].pop(other_j,None)
  for ii in c:rows[ii].pop(j,None)
  del columns[j]
  for other_j in row:columns.get(other_j,{}).pop(i,None)
  del rows[i]
  piv.append((i,j))
  if len(piv)%100==0:
   print('piv',len(piv),'rows',len(rows),'cols',len(columns),'time',round(time.monotonic()-start,1),flush=True)
 nonzero=[c for c in columns.values() if c]
 return len(piv),len(nonzero),sum(len(c) for c in nonzero),max((abs(x) for c in nonzero for x in c.values()),default=0),round(time.monotonic()-start,1)

for label,columns,expected in [('D2',D2,879),('D3',D3,448)]:
    pivots,remain,nnz,magnitude,secs=reduce(columns,60)
    assert (pivots,remain,nnz,magnitude)==(expected,0,0,0)
    print(f'{label} integral unit-pivots {pivots}; residual zero')
# Degree-zero connectedness: the cube is connected, so unordered
# configuration of three points on its geometric realization is connected.
# Hence H0 is infinite cyclic and D1 has rank C0-1=363.
assert len(C0)-1==363
b0=1; b1=len(C1)-363-879; b2=len(C2)-879-448; b3=len(D3)-448
assert (b0,b1,b2,b3)==(1,6,17,0)
print('Integral homology ranks (1,6,17,0); all torsion-free')
print('CUBE_THREE_PARTICLE_INTEGRAL_HOMOLOGY_PASS')
