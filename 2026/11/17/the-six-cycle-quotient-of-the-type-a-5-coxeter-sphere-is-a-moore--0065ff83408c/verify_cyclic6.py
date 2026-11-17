#!/usr/bin/env python3
"""Standalone finite-chain check for cyclic quotient of the six-vertex simplex boundary."""
from collections import defaultdict
from itertools import combinations

def rot(mask,r):
    return ((mask<<r)|(mask>>(6-r))) & 63 if r else mask

def can(chain):
    return min(tuple(rot(s,r) for s in chain) for r in range(6))

proper=range(1,63)
# All nonempty chains of proper subsets, each appended mask a proper strict superset
bydim={}
chains={(s,) for s in proper}
for dim in range(5):
    orbits={can(c) for c in chains}
    bydim[dim]=sorted(orbits)
    print('dim',dim,'labeled',len(chains),'orbits',len(orbits))
    nxt=set()
    for c in chains:
      s=c[-1]
      rem=63^s
      t=rem
      while t:
        new=s|t
        if new!=63:nxt.add(c+(new,))
        t=(t-1)&rem
    chains=nxt

inds={d:{c:i for i,c in enumerate(cs)} for d,cs in bydim.items()}
# pivot reduction over finite field
def matrix_rank(d,p):
    if d==0:return 0
    pivots={}
    for c in bydim[d]:
      col={}
      for j in range(d+1):
        t=can(c[:j]+c[j+1:]); r=inds[d-1][t]
        a=(1 if j%2==0 else -1)%p
        b=(col.get(r,0)+a)%p
        if b:col[r]=b
        elif r in col:del col[r]
      while col:
        idx=max(col)
        if idx not in pivots:
          inv=pow(col[idx],-1,p)
          pivots[idx]={r:(v*inv)%p for r,v in col.items()}
          break
        q=pivots[idx];a=col[idx]
        for r,v in q.items():
          new=(col.get(r,0)-a*v)%p
          if new:col[r]=new
          elif r in col: del col[r]
    return len(pivots)
# Construct exact quotient boundaries and verify all consecutive compositions.
def boundary(d, chain):
    ans={}
    for j in range(d+1):
        face=can(chain[:j]+chain[j+1:])
        k=inds[d-1][face]
        ans[k]=ans.get(k,0)+(1 if j%2==0 else -1)
    return {k:v for k,v in ans.items() if v}

for d in range(2,5):
    for c in bydim[d]:
        out={}
        for j,a in boundary(d,c).items():
            for k,b in boundary(d-1,bydim[d-1][j]).items():
                out[k]=out.get(k,0)+a*b
        assert all(v==0 for v in out.values()), (d,c,out)
print('exact_integral_boundary_squared_zero PASS')

for p in (2,3,5,7):
 r=[matrix_rank(d,p) for d in range(5)]
 beta=[len(bydim[d])-r[d]- (r[d+1] if d<4 else 0) for d in range(5)]
 print('field',p,'ranks',r,'betti',beta)
print('euler',sum((-1)**d*len(cs) for d,cs in bydim.items()))

assert [len(bydim[k]) for k in range(5)] == [12,91,260,300,120]
print('CYCLIC_SIX_SIMPLEX_QUOTIENT_CHECK_PASS')
