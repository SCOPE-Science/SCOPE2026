#!/usr/bin/env python3
"""Independent exact-arithmetic and direct Fourier checks of the cubic moment-curve remainder."""
from fractions import Fraction as Q
from itertools import product
from math import factorial, pi
import cmath


def compositions(q, total):
    if q == 1:
        yield (total,)
    else:
        for a in range(total + 1):
            for tail in compositions(q - 1, total - a):
                yield (a,) + tail


def permutation_expectation(p):
    # Three independent draws and the number of distinct permutations of each multiset.
    q = len(p)
    out = Q(0)
    for a, b, c in product(range(q), repeat=3):
        m = (6 if a != b and a != c and b != c else
             1 if a == b == c else 3)
        out += m * p[a] * p[b] * p[c]
    return out


def polynomial_expectation(p):
    s2 = sum((x*x for x in p), Q(0))
    s3 = sum((x*x*x for x in p), Q(0))
    return Q(6)-9*s2+4*s3


def check_grid(q, denominator):
    a = Q(6) - Q(9,q) + Q(4,q*q)
    c = Q(5) - Q(4,q)
    checked = 0
    equality_types = set()
    for counts in compositions(q, denominator):
        p = tuple(Q(v,denominator) for v in counts)
        s2 = sum((x*x for x in p), Q(0))
        s3 = sum((x*x*x for x in p), Q(0))
        e2 = (1-s2)/2
        e3 = (1-3*s2+2*s3)/6
        deficit = a-polynomial_expectation(p)
        variance = s2-Q(1,q)
        remainder = deficit-c*variance
        assert remainder == Q(4,q)*((q-2)*e2-3*q*e3)
        assert remainder >= 0, (q,p,remainder)
        assert polynomial_expectation(p) == permutation_expectation(p)
        if remainder == 0:
            assert len(set(p)) == 1 or max(p) == 1
            equality_types.add('uniform' if len(set(p)) == 1 else 'point_mass')
        checked += 1
    return checked, equality_types


def direct_fourier(q, f):
    # Curve measure and target counting measure follow the theorem's normalization.
    norm2 = sum(abs(z)**2 for z in f)/q
    p = [Q(0)]*q
    # The direct test uses complex f; compare floating power sums of squared amplitudes.
    powers = [abs(z)**2/(q*norm2) for z in f]
    predicted = (6-9*sum(x*x for x in powers)+4*sum(x*x*x for x in powers))*norm2**3
    zeta = cmath.exp(2j*pi/q)
    got = 0.0
    for a,b,c in product(range(q),repeat=3):
        amp = sum(f[t]*zeta**((a*t+b*t*t+c*t*t*t)%q) for t in range(q))/q
        got += abs(amp)**6
    assert abs(predicted-got) <= 3e-9*(1+abs(got)), (q,predicted,got)
    return got


def main():
    totals=[]
    for q,n in [(5,5),(7,3),(11,2)]:
        counts,equalities=check_grid(q,n)
        totals.append((q,counts,','.join(sorted(equalities))))
    assert check_grid(5,5)[1] == {'point_mass','uniform'}
    direct_count=0
    for q in (5,7):
        families=[
            [1+0j]*q,
            [1+0j]+[0j]*(q-1),
            [complex((3*t+1)%5-2,(t*t+1)%7-3) for t in range(q)],
            [cmath.exp(1j*(t*t+t/3))*(t+1)**0.5 for t in range(q)],
        ]
        for f in families:
            direct_fourier(q,f)
            direct_count += 1
    print('CHECK_OK exact_probability_vectors=',sum(x[1] for x in totals),
          'direct_Fourier_tests=', direct_count,
          'cases=', totals)


if __name__ == '__main__':
    main()
