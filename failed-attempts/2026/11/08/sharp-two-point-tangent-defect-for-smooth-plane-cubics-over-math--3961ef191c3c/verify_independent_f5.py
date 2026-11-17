"""Independent vectorized tangent-union count for all ternary cubics over GF(5).
Usage: python verify_independent_f5.py  (requires numpy and sympy)
This verifies raw coverage and geometric smoothness of the two representatives.
"""
from collections import Counter
import numpy as np
from sympy import symbols, groebner

EXP = [(3,0,0),(2,1,0),(2,0,1),(1,2,0),(1,1,1),(1,0,2),(0,3,0),(0,2,1),(0,1,2),(0,0,3)]
P = [(a,b,1) for a in range(5) for b in range(5)] + [(a,1,0) for a in range(5)] + [(1,0,0)]
E = np.array([[np.prod([pow(pt[k],e[k],5) for k in range(3)])%5 for e in EXP] for pt in P], dtype=np.int32)
D = [np.array([[((e[k]*pow(pt[k],e[k]-1,5)*np.prod([pow(pt[t],e[t],5) for t in range(3) if t!=k]))%5 if e[k] else 0) for e in EXP] for pt in P],dtype=np.int32) for k in range(3)]

# Encode every projective nonzero gradient by its 31-bit rational-line incidence mask.
line_mask = np.zeros(125,dtype=np.uint32)
for u in range(5):
 for v in range(5):
  for w in range(5):
   if (u,v,w)==(0,0,0):continue
   line_mask[25*u+5*v+w] = sum((1<<i) for i,(a,b,c) in enumerate(P) if (u*a+v*b+w*c)%5==0)

counts = Counter(); joint=Counter(); total=0; nonsing=0; batch=4000
for first in range(10):
  n=5**(9-first)
  for lo in range(0,n,batch):
    hi=min(lo+batch,n)
    v=np.arange(lo,hi,dtype=np.int64)
    C=np.zeros((hi-lo,10),dtype=np.int32); C[:,first]=1
    for j in range(9,first,-1):C[:,j]=(v%5).astype(np.int32); v//=5
    values=(C @ E.T)%5
    zero=(values==0)
    gr=[(C @ Dj.T)%5 for Dj in D]
    bad=np.any(zero & (gr[0]==0) & (gr[1]==0) & (gr[2]==0),axis=1)
    good=~bad
    nonzero_grad=(25*gr[0]+5*gr[1]+gr[2]).astype(np.int32)
    masks=np.where(zero,line_mask[nonzero_grad],np.uint32(0))
    cover=np.bitwise_or.reduce(masks,axis=1)
    for z,q,ok in zip(cover,zero.sum(axis=1),good):
      if ok:
       cc=int(z).bit_count();counts[cc]+=1
       if cc>=27:joint[(cc,int(q))]+=1
    nonsing+=int(good.sum());total+=hi-lo

assert total==2441406 and nonsing==1895000
assert max(counts)==29 and counts[29]==186000
assert joint[(29,8)]==93000 and joint[(29,10)]==93000
print('VECTOR_CUBIC_F5_CENSUS_PASS',total,nonsing,max(counts),counts[29],joint[(29,8)],joint[(29,10)])

X,Y,Z=symbols('X Y Z')
for coeffs,expected in [('1000010200',8),('1000011040',10)]:
 F=sum(int(c)*X**i*Y**j*Z**k for c,(i,j,k) in zip(coeffs,EXP))
 for chart in [X,Y,Z]:
  part=[F,F.diff(X),F.diff(Y),F.diff(Z)]
  g=groebner([f.subs({chart:1}) for f in part],*[v for v in (X,Y,Z) if v!=chart],modulus=5)
  assert len(g.polys)==1 and g.polys[0].as_expr()==1
 on=[p for p in P if int(F.subs(dict(zip((X,Y,Z),p))))%5==0]
 cover=set()
 for p in on:
  d=[int(F.diff(v).subs(dict(zip((X,Y,Z),p))))%5 for v in (X,Y,Z)]
  assert any(d)
  cover.update(q for q in P if sum(a*b for a,b in zip(d,q))%5==0)
 assert len(on)==expected and len(cover)==29
 print('REP_SMOOTH_AND_COVER_PASS',coeffs,'rational_points',len(on),'missing',sorted(set(P)-cover))
