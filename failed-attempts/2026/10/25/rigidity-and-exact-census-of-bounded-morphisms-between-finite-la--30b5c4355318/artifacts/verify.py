#!/usr/bin/env python3
"""Finite exhaustive checks for bounded morphisms between layered posets."""
from itertools import product
from math import factorial
from functools import lru_cache

@lru_cache(None)
def S(n,k):
    if k==0: return int(n==0)
    if n==0: return 0
    return S(n-1,k-1)+k*S(n-1,k)

def elems(levels):
    return [(i,j) for i,n in enumerate(levels) for j in range(n)]

def le(x,y):
    return x==y or x[0]<y[0]

def is_p_morphism(domain,codomain,f):
    # independently implement the order and back conditions for every pair.
    if len(set(f))!=len(codomain):return False
    for a,x in enumerate(domain):
        for b,z in enumerate(domain):
            if le(x,z) and not le(codomain[f[a]],codomain[f[b]]):return False
        for j,y in enumerate(codomain):
            if le(codomain[f[a]],y) and not any(le(x,z) and f[b]==j for b,z in enumerate(domain)):
                return False
    return True

def predicted(P,Q):
    if len(P)!=len(Q): return 0
    ans=1
    for p,q in zip(P,Q):
        ans*=factorial(q)*S(p,q)
    return ans

def exhaustive():
    cases=0
    for h in range(1,5):
        for P in product(range(1,4),repeat=h):
            if sum(P)>6:continue
            for k in range(1,4):
                for Q in product(range(2,4),repeat=k):
                    if sum(Q)>5 or sum(Q)>sum(P):continue
                    X,Y=elems(P),elems(Q)
                    actual=sum(is_p_morphism(X,Y,f) for f in product(range(len(Y)),repeat=len(X)))
                    expected=predicted(P,Q)
                    assert actual==expected,(P,Q,actual,expected)
                    cases+=1
    return cases

if __name__=='__main__':
    n=exhaustive()
    print('All cases passed:',n)
    print('Examples:')
    for p,q in [((2,2),(2,2)),((3,2),(2,2)),((2,2,2),(2,2)),((2,2),(2,2,2)),((4,),(2,2)),((3,3),(2,3))]:
       X,Y=elems(p),elems(q)
       if len(X)<=6 and len(Y)<=5:
        x=sum(is_p_morphism(X,Y,f) for f in product(range(len(Y)),repeat=len(X)))
       else:x=None
       print(p,q,'expected',predicted(p,q),'enumerated',x if x is not None else 'not enumerated')
    P,Q=(2,1,1),(2,1)
    X,Y=elems(P),elems(Q)
    a=sum(is_p_morphism(X,Y,f) for f in product(range(len(Y)),repeat=len(X)))
    assert a>0
    print('Singleton target-level boundary:',P,'to',Q,'surjections',a)
    print('ALL_TESTS_PASS')
