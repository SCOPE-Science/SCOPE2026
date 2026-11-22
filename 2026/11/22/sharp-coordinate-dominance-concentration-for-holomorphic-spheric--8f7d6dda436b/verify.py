#!/usr/bin/env python3
"""Independent exact and high-precision checks for coordinate-dominance holomorphic concentration."""
from fractions import Fraction
from math import comb, factorial
from itertools import product
import mpmath as mp


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rem in compositions(total-first, length-1):
            yield (first,)+rem


def exact_eigen(alpha):
    # Inclusion-exclusion of integer-shape gamma cumulative distributions.
    from itertools import combinations
    a1=alpha[0]; r=Fraction(0)
    other=range(1,len(alpha))
    for h in range(len(other)+1):
        for subset in combinations(other,h):
            if not subset:
                r+=1;continue
            for indices in product(*[range(alpha[j]+1) for j in subset]):
                s=sum(indices)
                r+=(-1)**h*Fraction(factorial(a1+s),factorial(a1)*
                    (h+1)**(a1+s+1)*__import__('math').prod(factorial(v) for v in indices))
    return r


def max_formula(k,m):
    return sum((Fraction((-1)**j*comb(k-1,j),(j+1)**(m+1)) for j in range(k)),Fraction(0))


def check():
    # Full finite spectrum endpoints (unproven alone; proof accompanies the data).
    cases=0
    for k in range(2,6):
        for m in range(0,8):
            spectra=[(a,exact_eigen(a)) for a in compositions(m,k)]
            upper=max_formula(k,m)
            lower=(1-upper)/(k-1)
            assert min(v for a,v in spectra)==lower,(k,m,'minimum')
            assert max(v for a,v in spectra)==upper,(k,m,'maximum')
            if m:
                assert [a for a,v in spectra if v==upper]==[(m,)+(0,)*(k-1)]
                assert sorted(a for a,v in spectra if v==lower)==sorted(
                    (0,)+tuple(m if j==i else 0 for j in range(1,k))
                    for i in range(1,k))
            else: assert upper==lower==Fraction(1,k)
            cases+=1
    assert max_formula(3,1)==Fraction(11,18)
    assert (1-max_formula(3,1))/2==Fraction(7,36)
    assert max_formula(2,4)==Fraction(31,32)
    # Independent quadrature, not based on rational inclusion-exclusion.
    mp.mp.dps=65
    tests=[(0,0),(2,0),(0,2),(2,1),(3,2),(1,3,2),(0,1,3),(2,2,2),(3,0,2,1)]
    for a in tests:
        def F(t,j):
            return 1-mp.e**(-t)*sum(t**r/mp.factorial(r) for r in range(a[j]+1))
        f=lambda t: mp.e**(-t)*t**a[0]/mp.factorial(a[0])*mp.fprod(F(t,j) for j in range(1,len(a)))
        computed=mp.quad(f,[0,1,3,10,35,mp.inf])
        exact=exact_eigen(a)
        assert abs(computed-mp.mpf(exact.numerator)/exact.denominator)<mp.mpf('1e-50'),a
    print('PASS: 32 complete rational endpoint spectra, exact equality classifications, 9 independent high-precision gamma integrals.')

if __name__=='__main__':check()
