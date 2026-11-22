#!/usr/bin/env python3
"""Exact rational and independent sampling checks of a conditional cyclic-angle law.

The analytic proof, not this finite checker, establishes all sample sizes and limits.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F
from math import factorial, comb
from random import Random


def expected_powers(n, p, q):
    """Integral of u**p*v**q times the claimed conditional joint density."""
    return (F((n-1)*(n-2), 2**(p+q+1)) *
            (F(1,p+1)+F(1,q+1)) *
            F(factorial(p+q+1)*factorial(n-3),factorial(n+p+q-1)))


def max_ratio_moment(n, a, b):
    """E[max(U,V)**a * (min(U,V)/max(U,V))**b]."""
    return F(1,2**a) * F(factorial(a+1)*factorial(n-1),factorial(n+a-1)) * F(1,b+1)


def independent_integral(n,p,q):
    """Independently integrate the piecewise polynomial f(u,v), no beta functions."""
    # On upper and lower triangles, reduce integral to polynomial in t,
    # and expand (1-2t)**(n-3). Check rationally.
    s=F(0)
    for k in range(n-2):
        coeff=F(comb(n-3,k)*(-2)**k,1)
        s+=coeff * F(1,2**(p+q+2+k)*(p+q+2+k))
    return 2*(n-1)*(n-2)*(F(1,p+1)+F(1,q+1))*s


def check():
    count=0
    for n in range(4,25):
        assert expected_powers(n,0,0)==1; count+=1
        assert expected_powers(n,1,0)==F(3,4*n);count+=1
        assert expected_powers(n,2,0)==F(1,n*(n+1));count+=1
        assert expected_powers(n,1,1)==F(3,4*n*(n+1));count+=1
        cov=expected_powers(n,1,1)-expected_powers(n,1,0)**2
        var=expected_powers(n,2,0)-expected_powers(n,1,0)**2
        assert cov==F(3*(n-3),16*n*n*(n+1));count+=1
        assert cov/var==F(3*(n-3),7*n-9);count+=1
        # integrals from transformed density and an independent polynomial expansion
        for p in range(5):
            for q in range(5):
                assert independent_integral(n,p,q)==expected_powers(n,p,q)
                count+=1
        # Beta(2,n-2) and independent uniform ratio gives exact moments
        for a in range(5):
            for b in range(5):
                m=F(1,2**a)*F(factorial(a+1)*factorial(n-1),factorial(n+a-1))
                assert max_ratio_moment(n,a,b)==m*F(1,b+1)
                count+=1
        assert max_ratio_moment(n,1,0)==F(1,n);count+=1
        assert max_ratio_moment(n,1,1)==F(1,2*n);count+=1
        pair_mass=2*(n-1)*(n-2)*F(1,2**(n-1))*F(factorial(n-3),factorial(n-1))
        assert pair_mass==F(1,2**(n-2));count+=1
    # Monte Carlo: Generate truly exchangeable circular spacings using exponentials.
    # Check event rate and first moments independently of derived integrals.
    rng=Random(46051)
    for n,trials in ((4,100000),(6,160000),(8,240000)):
        count_two=0; total_u=0.;total_v=0.;total_max=0.;total_ratio=0.
        for _ in range(trials):
            e=[rng.expovariate(1) for j in range(n)]
            s=sum(e)
            g=[x/s for x in e]
            deficits=[g[i]+g[(i+1)%n]-.5 for i in range(n)]
            idx=[i for i,d in enumerate(deficits) if d>0]
            if len(idx)!=2:
                continue
            count_two+=1
            u,v=deficits[idx[0]],deficits[idx[1]]
            big=max(u,v)
            total_u+=u;total_v+=v;total_max+=big;total_ratio+=min(u,v)/big
        p=count_two/trials
        exact=n/2**(n-2)
        # Broad deterministic tolerance for standard random sampling.
        assert abs(p-exact)<.012,(n,p,exact)
        assert abs((total_u+total_v)/(2*count_two)-3/(4*n))<.012
        assert abs(total_max/count_two-1/n)<.013
        assert abs(total_ratio/count_two-.5)<.012
        count+=4
    return count


if __name__=='__main__':
    print(f'PASS: {check()} deterministic exact rational identities plus independent Monte Carlo tolerances')
