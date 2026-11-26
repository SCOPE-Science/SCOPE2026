#!/usr/bin/env python3
"""Check the exact first-pivot probabilities and error laws with Python's standard library.

The independent analytic argument is supplied in RESULT.md. Finite checks do not prove
universal probabilistic statements.
"""
import math
import random

def cauchy_miss(k):
    return 2.0/math.pi*math.atan(1/k)

def beta_even_cdf(z,m):
    # For Beta(m,m), polynomial/binomial tail identity, integer m>=1.
    return sum(math.comb(2*m-1,j)*z**j*(1-z)**(2*m-1-j)
               for j in range(m,2*m))

def cross_error(k,j):
    a=((k,0.),(0.,1.))
    v=(a[0][j],a[1][j])
    pivot=a[j][j]
    row=a[j]
    approx=tuple(tuple(v[i]*row[t]/pivot for t in range(2)) for i in range(2))
    return max(abs(a[i][t]-approx[i][t]) for i in range(2) for t in range(2))

def run():
    checks=0
    for k in (1.01,1.5,2.,3.,10.,100.,1000.,10000.):
        assert cross_error(k,0)==1.; checks+=1
        assert cross_error(k,1)==k; checks+=1
        for m in (1,2,3,4,5):
            z=1/(1+k*k)
            p=beta_even_cdf(z,m)
            assert 0<p<1;checks+=1
            if m==1: assert math.isclose(p,z,rel_tol=1e-13); checks+=1
            if m==2: assert math.isclose(p,3*z*z-2*z**3,rel_tol=1e-13); checks+=1
            if m==3: assert math.isclose(p,10*z**3-15*z**4+6*z**5,rel_tol=1e-13);checks+=1
            for q in (0.5,1.,1.5,2.,4.,10.):
                expected=1+(k**q-1)*p
                assert 1<=expected<=k**q; checks+=1
        for q in (.5,1.,2.,3.):
            expected=1+(k**q-1)*cauchy_miss(k)
            assert 1<=expected<=k**q; checks+=1
    for s in (2,4,6,8,10):
        m=s//2
        cs=2*math.gamma(s)/(s*math.gamma(s/2)**2)
        k=10000.
        assert abs(beta_even_cdf(1/(1+k*k),m)*k**s/cs-1)<1e-6
        checks+=1
    k=100000.
    assert abs(k*cauchy_miss(k)-2/math.pi)<1e-10;checks+=1
    print('VERIFY_OK',checks,'exact/polynomial/limit checks')

if __name__=='__main__':run()
