#!/usr/bin/env python3
"""Finite prime checks of the all-prime ghost-coordinate formulas.
The mathematical proof of the universal result is separate; these checks are
not a substitute for proof for infinitely many primes.
"""
from math import comb
from random import Random


def gaps(p):
    conductor = (p-1)*(p-2)
    semigroup = {a*(p-1)+b*p for a in range(p) for b in range(p)}
    return [n for n in range(1, conductor) if n not in semigroup]


def ghost_from_factors(u,p,n):
    return sum((d*pow(v,n//d,p)) for d,v in u.items() if n%d==0)%p


def ghost_from_coefficients(c, p, nmax):
    """Independent logarithmic-derivative recursion for f(T)=1+sum c_n T^n."""
    out=[0]*(nmax+1)
    for n in range(1,nmax+1):
        out[n]=(-n*c.get(n,0)-sum(c.get(j,0)*out[n-j] for j in c if j<n))%p
    return out


def check_prime(p):
    G=gaps(p)
    assert len(G)==(p-1)*(p-2)//2
    assert all(n%p for n in G)
    assert G==[j*p+i for j in range(p-2) for i in range(1,p-1-j)]
    rng=Random(p*131+9)
    for _ in range(10):
        u={d:rng.randrange(p) for d in G}
        # Direct normal-form chart, unrelated to the factorized-unit formula.
        c={d:rng.randrange(p) for d in G}
        w=ghost_from_coefficients(c,p,max(G)+(p-1)**2)
        for g in G:
            j,i=divmod(g,p)
            for m in range(p):
                n=g+m*(p-1)
                coeff=(-1)**m*comb(n+m,m)*w[n]%p
                if m<i: expected=(-1)**m*comb(i,m)*w[n]%p
                elif m==i: expected=(-1)**i*pow(w[j+i],p,p)%p
                else: expected=0
                assert coeff==expected,(p,g,m,coeff,expected)
        for t in range(1,p-1):
            assert w[p*t]==pow(w[t],p,p)

        for g in G:
            j,i=divmod(g,p)
            assert 1<=i<=p-2-j
            for m in range(p):
                n=g+m*(p-1)
                actual=(-1)**m*comb(n+m,m)*ghost_from_factors(u,p,n)%p
                if m<i:
                    target=(-1)**m*comb(i,m)*ghost_from_factors(u,p,n)%p
                elif m==i:
                    target=(-1)**i*pow(ghost_from_factors(u,p,j+i),p,p)%p
                else:
                    target=0
                assert actual==target,(p,g,m,actual,target)
            n=g+p-1
            observed=-g*ghost_from_factors(u,p,n)%p
            if i>1:
                assert n in G
                claimed=-i*ghost_from_factors(u,p,n)%p
            else:
                claimed=-pow(ghost_from_factors(u,p,j+1),p,p)%p
            assert observed==claimed,(p,g,observed,claimed)
        for t in range(1,p-1):
            assert ghost_from_factors(u,p,p*t)==pow(ghost_from_factors(u,p,t),p,p)
    # First-order fixed equations: each of the non-first-row variables is
    # hit as D(g) for a predecessor, and every first-row pth power occurs.
    hit=set()
    powers=set()
    for g in G:
        j,i=divmod(g,p)
        if i>1: hit.add(g+p-1)
        else: powers.add(j+1)
    assert hit=={g for g in G if g>=p}
    assert powers==set(range(1,p-1))
    print('p=%d: gaps=%d, fixed alpha_p factors=%d, ghost/coaction identities OK' % (p,len(G),p-2))


if __name__=='__main__':
    for prime in (3,5,7,11,13):
        check_prime(prime)
