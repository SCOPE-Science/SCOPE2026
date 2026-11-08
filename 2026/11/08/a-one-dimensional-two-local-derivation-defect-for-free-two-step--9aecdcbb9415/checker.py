#!/usr/bin/env python3
"""Independent finite-field witness tests for linear two-local derivations of free class-two Lie algebras."""
from itertools import product, combinations
from random import Random


def data(m,p):
    pairs=list(combinations(range(m),2)); c=len(pairs); n=m+c
    derivations=[]
    for i in range(m):
      for j in range(m):
        D=[[0]*n for _ in range(n)]
        D[i][j]=1
        for k,(a,b) in enumerate(pairs):
          if a==j:
            for ell, (u,v) in enumerate(pairs):
              if (u,v)==tuple(sorted((i,b))) and i!=b:
                D[m+ell][m+k]=(1 if i<b else -1)%p
          if b==j:
            for ell,(u,v) in enumerate(pairs):
              if (u,v)==tuple(sorted((a,i))) and a!=i:
                D[m+ell][m+k]=(D[m+ell][m+k]+(1 if a<i else -1))%p
        derivations.append(D)
    for j in range(m):
      for k in range(c):
        D=[[0]*n for _ in range(n)];D[m+k][j]=1
        derivations.append(D)
    return derivations,pairs

def apply(D,x,p):
    return tuple(sum(D[i][j]*x[j] for j in range(len(x)))%p for i in range(len(x)))

def rank_mod(vectors,p):
    basis={}
    for v in vectors:
      a=list(v)
      while True:
        j=next((j for j,u in enumerate(a) if u%p),None)
        if j is None:break
        if j not in basis:
          inv=pow(a[j]%p,-1,p)
          basis[j]=[(u*inv)%p for u in a]
          break
        mult=a[j]
        a=[(u-mult*w)%p for u,w in zip(a,basis[j])]
    return len(basis)

def span_contains(cols,target,p):
    return rank_mod(cols,p)==rank_mod(cols+[target],p)

def two_local_test(Ds,m,p,x,y,operator):
    return span_contains([apply(d,x,p)+apply(d,y,p) for d in Ds],operator(x)+operator(y),p)

def local_test(Ds,m,p,x,operator):
    return span_contains([apply(d,x,p) for d in Ds],operator(x),p)

def test(m,p,N=2000,exhaust=False):
    Ds,pairs=data(m,p); c=len(pairs); dim=m+c
    assert len(Ds)==m*m+m*c
    # Scalar center dilation S, never an ordinary derivation.
    def S(x):return (0,)*m+x[m:]
    # A non-scalar horizontal projection. It is local but not two-local when m>=3.
    def P(x):return (x[0],)+(0,)*(dim-1)
    allvec=[tuple(v) for v in product(range(p), repeat=dim)] if exhaust else None
    rng=Random(173*m+29*p)
    def randvec():return tuple(rng.randrange(p) for _ in range(dim))
    tested=0
    if allvec is not None:
      for x in allvec:
        assert local_test(Ds,m,p,x,S)
      for x in allvec:
        for y in allvec:
          assert two_local_test(Ds,m,p,x,y,S), (m,p,x,y)
          tested+=1
    else:
      for _ in range(N):
        x,y=randvec(),randvec()
        assert two_local_test(Ds,m,p,x,y,S),(m,p,x,y)
        tested+=1
    if m>=3:
      v=[0]*m;v[0]=v[1]=1
      z=[0]*c;z[pairs.index((0,2))]=1;z[pairs.index((1,2))]=1
      x=tuple(v+[0]*c);y=tuple(v+z)
      assert local_test(Ds,m,p,x,P) and local_test(Ds,m,p,y,P)
      assert not two_local_test(Ds,m,p,x,y,P)
      for _ in range(min(N,150)):
        x=randvec();assert local_test(Ds,m,p,x,P)
    print(f'm={m} p={p}: derivation_dimension={len(Ds)}; S two-local witness tests={tested}; local-not-two-local projection={"verified" if m>=3 else "not tested"}; PASS')

if __name__=='__main__':
    test(2,3,exhaust=True)
    test(3,3,N=2500)
    test(3,5,N=600)
    test(4,3,N=350)
    print('FREE_TWO_STEP_LINEAR_TWO_LOCAL_PASS')
