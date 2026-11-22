#!/usr/bin/env python3
"""Independent finite checks of cycle Lipschitz Fourier projection norms.

Python >=3.9, standard library only.  The analytic argument is not
replaced by finite checks; this script compares the asserted formula with
independent enumeration of vertices of the centered increment cube.
"""
from itertools import combinations
from math import cos, pi, sin, tan, gcd, isclose
from fractions import Fraction


def predicted(period):
    if period == 2:
        return 1.0
    if period % 2:
        z = pi / (2 * period)
        return 2 / period * (1 / sin(z) - sin(z))
    if period % 4 == 0:
        return 4 / period / tan(pi / period)
    return 4 / period / sin(pi / period)


def signed_zero_sum_vertices(n):
    """All vertices of {u: -1<=u_i<=1, sum u_i=0}."""
    if n % 2 == 0:
        for plus in combinations(range(n), n // 2):
            p = set(plus)
            yield tuple(1 if i in p else -1 for i in range(n))
    else:
        for zero in range(n):
            remaining = [i for i in range(n) if i != zero]
            for plus in combinations(remaining, (n - 1) // 2):
                p = set(plus)
                yield tuple(0 if i == zero else (1 if i in p else -1) for i in range(n))


def independently_enumerated_norm(n, k):
    a = [cos(2*pi*k*j/n) for j in range(n)]
    mx = 0.0
    for u in signed_zero_sum_vertices(n):
        value = abs(sum(x*y for x,y in zip(a,u)))*(1 if 2*k == n else 2)/n
        if value > mx:
            mx = value
    return mx


def main():
    cases = 0
    for n in range(3, 17):
        for k in range(1, n // 2 + 1):
            # Rank-one Nyquist mode when n is even and 2k=n.
            if 2*k > n:
                continue
            calculated = independently_enumerated_norm(n,k)
            period = n // gcd(n,k)
            expected = predicted(period)
            assert isclose(calculated, expected, rel_tol=0, abs_tol=3e-12), (
                n,k,calculated,expected)
            cases += 1
    print('DIRECT_CENTERED_CUBE_VERTEX_ENUMERATIONS_PASSED', cases)

    # The six-cycle norm is also verified without floating-point arithmetic.
    # a = [1, 1/2,-1/2,-1,-1/2,1/2]; optimum at the balanced signs.
    a = list(map(Fraction, [1, Fraction(1,2), -Fraction(1,2), -1, -Fraction(1,2), Fraction(1,2)]))
    mx = max(abs(sum(x*y for x,y in zip(a, u)))*Fraction(1,3)
             for u in signed_zero_sum_vertices(6))
    assert mx == Fraction(4,3)
    print('EXACT_RATIONAL_SIX_CYCLE_MAXIMUM', str(mx))

    # Separate closed-form comparison with the sampled centered median formula.
    medchecks=0
    for period in range(3, 301):
        cosine = sorted(cos(2*pi*j/period) for j in range(period))
        median = cosine[period//2]
        medvalue = 2 / period * sum(abs(x-median) for x in cosine)
        assert abs(medvalue-predicted(period)) < 3e-12, (period, medvalue, predicted(period))
        medchecks += 1
    print('CENTERED_MEDIAN_FORMULA_TESTS_PASSED', medchecks)

    # Nontrivial divisibility (repeated period) profiles with n up to 120.
    periodic=0
    for n in range(3,121):
        for k in range(1,n//2+1):
            period=n//gcd(n,k)
            if period==2:
                continue
            arr=sorted((2/n)*cos(2*pi*k*j/n) for j in range(n))
            c=arr[n//2]
            val=sum(abs(x-c) for x in arr)
            assert abs(val-predicted(period)) < 5e-12,(n,k)
            periodic+=1
    print('ARBITRARY_FREQUENCY_GCD_COLLAPSES_PASSED', periodic)

    # Numerical asymptotics: coefficient of the N^-2 phase defect.
    for rem, coeff in [(1,-5*pi/6),(0,-4*pi/3),(2,2*pi/3)]:
        ns = [n for n in (20001,20002,20004,40001,40002,40004,80001,80002,80004)
              if (n%2 and rem==1) or (n%4==rem and rem!=1)]
        for n in ns:
            empirical=(predicted(n)-4/pi)*n*n
            assert abs(empirical-coeff)<0.0005, (n, empirical,coeff)
    print('THREE_RESIDUE_ASYMPTOTICS_PASSED')
    print('ALL_LIPSCHITZ_CYCLE_FOURIER_CHECKS_PASSED')


if __name__ == '__main__':
    main()
