#!/usr/bin/env python3
"""Exact subalgebra and permutability counts for two-eigenvalue almost-abelian Lie algebras.
Uses prime fields and no external packages. Run: python3 two_eigenspace_verify.py
"""
from itertools import combinations, product
from functools import lru_cache

@lru_cache(None)
def gaussian(n, k, q):
    if not 0 <= k <= n: return 0
    if k in (0, n): return 1
    return gaussian(n - 1, k - 1, q) + q**k * gaussian(n - 1, k, q)

def formulas(a, b, q):
    n = a + b
    v = sum(gaussian(n, i, q) for i in range(n + 1))
    ext = mixed = outside = 0
    for p in range(a + 1):
      for z in range(b + 1):
        w = p + z; nw = gaussian(a, p, q) * gaussian(b, z, q)
        ext += nw*q**(n-w)
        f = 0
        for i in range(a-p+1):
          for j in range(b-z+1):
            d=i+j
            f += gaussian(a-p, i, q)*gaussian(b-z,j,q)*sum(gaussian(w,h,q)*q**(d*(w-h)) for h in range(w+1))
        mixed += nw*q**(n-w)*f
        for pp in range(a+1):
          for zz in range(b+1):
            ww=pp+zz
            for t in range(max(0,p+pp-a),min(p,pp)+1):
              for tt in range(max(0,z+zz-b),min(z,zz)+1):
                pairE=gaussian(a,p,q)*gaussian(p,t,q)*gaussian(a-p,pp-t,q)*q**((p-t)*(pp-t))
                pairF=gaussian(b,z,q)*gaussian(z,tt,q)*gaussian(b-z,zz-tt,q)*q**((z-tt)*(zz-tt))
                ke=p+pp-t; kf=z+zz-tt; k=ke+kf
                outside+=pairE*pairF*q**(n-w-ww+k)*(q**(a-ke)+q**(b-kf)-1)
    return v+ext, v*v+2*mixed+outside

def rref(vectors, q, n):
    rows=[list(v) for v in vectors if any(v)]
    lead=0; keep=[]
    for col in range(n):
      pivot=next((i for i in range(lead,len(rows)) if rows[i][col]%q),None)
      if pivot is None: continue
      rows[lead],rows[pivot]=rows[pivot],rows[lead]
      t=pow(rows[lead][col],-1,q)
      rows[lead]=[(x*t)%q for x in rows[lead]]
      for j in range(len(rows)):
        if j!=lead and rows[j][col]%q:
          s=rows[j][col]
          rows[j]=[(x-s*y)%q for x,y in zip(rows[j],rows[lead])]
      keep.append(lead)
      lead+=1
      if lead==len(rows):break
    return tuple(tuple(rows[i]) for i in keep)

def all_subspaces(n,q):
    for rank in range(n+1):
      for pivots in combinations(range(n),rank):
        free=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,n) if j not in pivots]
        for digits in product(range(q),repeat=len(free)):
          rows=[[0]*n for _ in pivots]
          for i,p in enumerate(pivots):rows[i][p]=1
          for (i,j),val in zip(free,digits):rows[i][j]=val
          yield tuple(map(tuple,rows))

def bracket(x,y,a,b,q,lamb):
    # basis: (t,e_1,..,e_a,f_1,..,f_b)
    out=[0]*(a+b+1)
    for i in range(1,a+1):out[i]=(x[0]*y[i]-y[0]*x[i])%q
    for i in range(a+1,a+b+1):out[i]=(lamb*(x[0]*y[i]-y[0]*x[i]))%q
    return tuple(out)

def in_span(v, basis, q):
    t=list(v)
    for row in basis:
      pivot=next(i for i,x in enumerate(row) if x)
      factor=t[pivot]
      if factor:
        t=[(x-factor*y)%q for x,y in zip(t,row)]
    return not any(t)

def brute(a,b,q,lamb):
    n=a+b+1
    subs=[]
    for rows in all_subspaces(n,q):
      if all(in_span(bracket(x,y,a,b,q,lamb),rows,q) for x,y in combinations(rows,2)):
        subs.append(rows)
    good=0
    for i,A in enumerate(subs):
      for B in subs:
        span=rref(A+B,q,n)
        if all(in_span(bracket(x,y,a,b,q,lamb),span,q) for x in A for y in B):good+=1
    return len(subs),good


if __name__=='__main__':
    cases=((1,1,3,2),(2,1,3,2),(2,1,5,2),(2,2,2,0),(2,2,3,0))
    for a,b,q,lamb in cases:
      expected=formulas(a,b,q); actual=brute(a,b,q,lamb)
      print((a,b,q,lamb),expected,actual,flush=True)
      assert expected==actual
    print('TWO_EIGEN_LIE_VERIFY_OK',len(cases))
