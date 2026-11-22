#!/usr/bin/env python3
"""Standalone finite-field checks for the Heisenberg endomorphism centralizer theorem.

Python >=3.9; no third-party dependencies. Prints exact row counts and checks.
"""
from collections import Counter
from itertools import product


def mul(A, B, p):
    return ((A[0]*B[0]+A[1]*B[2])%p,
            (A[0]*B[1]+A[1]*B[3])%p,
            (A[2]*B[0]+A[3]*B[2])%p,
            (A[2]*B[1]+A[3]*B[3])%p)


def d(A,p): return (A[0]*A[3]-A[1]*A[2])%p

def row(u,A,p):
    return ((u[0]*A[0]+u[1]*A[2])%p,
            (u[0]*A[1]+u[1]*A[3])%p)

def polynomial_spectrum(p):
    s=p*(p+1)*(2*p-3)
    j=2*(p*p-1)
    g=p**4-p-s-j
    if g<0: raise AssertionError('invalid generic count')
    ans=Counter()
    for z,c in [(p**6,2),
                (p**3*(2*p-1),2*(p*p-1)),
                (p**4,(p-2)*p*p),
                (p**3,(s+j)*p),
                (p*(2*p-1),s*(p*p-p)),
                (2*p*p,j*(p*p-p)),
                (p*p,g*p*p)]:
        ans[z]+=c
    return ans

def direct_spectrum(p):
    mats=list(product(range(p),repeat=4))
    vectors=list(product(range(p),repeat=2))
    actual=Counter()
    for A in mats:
        delta=d(A,p)
        MA=((A[0]-delta)%p,A[1],A[2],(A[3]-delta)%p)
        fibers=Counter(row(v,MA,p) for v in vectors)
        commuting=[B for B in mats if mul(A,B,p)==mul(B,A,p)]
        for u in vectors:
            count=0
            for B in commuting:
                t=d(B,p)
                uB=row(u,B,p)
                target=((uB[0]-t*u[0])%p,(uB[1]-t*u[1])%p)
                count+=fibers[target]
            actual[count]+=1
    assert actual==polynomial_spectrum(p),(p,actual,polynomial_spectrum(p))
    assert sum(actual.values())==p**6
    assert sum(k*v for k,v in actual.items())==p**8+5*p**7-8*p**5+3*p**3
    print(f'p={p}: spectrum {sorted(actual.items())}; commuting_pairs={sum(k*v for k,v in actual.items())}')

def genuine_group_checks(p=3):
    inv2=pow(2,-1,p)
    els=list(product(range(p),repeat=3))
    mats=list(product(range(p),repeat=4))
    us=list(product(range(p),repeat=2))
    def prod(g,h):
        return ((g[0]+h[0])%p,(g[1]+h[1])%p,
                (g[2]+h[2]+inv2*(g[0]*h[1]-g[1]*h[0]))%p)
    def phi(A,u,g):
        a,b=row((g[0],g[1]),(A[0],A[2],A[1],A[3]),p)
        return (a,b,(d(A,p)*g[2]+u[0]*g[0]+u[1]*g[1])%p)
    # Test every defining endomorphism on every ordered pair of group elements.
    for A in mats:
        for u in us:
            vals={g:phi(A,u,g) for g in els}
            for g in els:
                for h in els:
                    assert vals[prod(g,h)]==prod(vals[g],vals[h])
    # Verify the composition formula independently on all generator evaluations.
    gens=((1,0,0),(0,1,0),(0,0,1))
    for A in mats:
        da=d(A,p)
        for u in us:
            for B in mats:
                db=d(B,p)
                C=mul(A,B,p)
                for v in us:
                    vA=row(u,B,p)
                    w=((vA[0]+da*v[0])%p,(vA[1]+da*v[1])%p)
                    for g in gens:
                        assert phi(C,w,g)==phi(A,u,phi(B,v,g))
    print(f'p={p}: genuine-group multiplication checks passed')

if __name__=='__main__':
    for prime in (3,5,7): direct_spectrum(prime)
    genuine_group_checks(3)
    print('FINITE_HEISENBERG_ENDOMORPHISM_CENTRALIZERS_PASSED')
