"""Exact finite comparisons for the three-denomination one-representation theorem.

The checks are independent finite evidence; the all-parameter theorem is symbolic.
Run: python3 verify.py
"""
from fractions import Fraction
from math import gcd


def predicted(a, b, c):
    thresholds = [a*b+b*j if j < c else a+b*j for j in range(a)]
    f = max(thresholds) - a
    genus = c*b+(a-c)+((a-1)*(b-1))//2
    sylvester = (Fraction(sum(v*v for v in thresholds), 2*a)
                 -Fraction(sum(thresholds), 2)+Fraction(a*a-1, 12))
    assert sylvester.denominator == 1
    return thresholds, f, genus, int(sylvester)


def check(a, b, c):
    t, f, genus, sylvester = predicted(a, b, c)
    lim = f+a+b+1
    counts = [0]*lim
    for n in range(0, lim, a):
        counts[n] = 1
    for d in (b, a+c*b):
        for n in range(d, lim):
            counts[n] += counts[n-d]
    observed = [n for n, z in enumerate(counts) if z <= 1]
    assert max(observed) == f, (a, b, c, 'f')
    assert len(observed) == genus, (a, b, c, 'genus')
    assert sum(observed) == sylvester, (a, b, c, 'sylvester')
    inv = {((b*j) % a):t[j] for j in range(a)}
    assert len(inv) == a
    assert all((counts[n] >= 2) == (n >= inv[n % a])
               for n in range(lim)), (a, b, c, 'Apéry')
    return lim


def pell(u, k):
    p, q = 0, 1
    for _ in range(k):
        p, q = q, u*q+p
    return p


def main():
    configurations = comparisons = 0
    for a in range(2, 23):
        for b in range(a+1, a+21):
            if gcd(a,b) != 1:
                continue
            for c in range(1, a):
                comparisons += check(a, b, c)
                configurations += 1
    pell_configurations = 0
    for u in range(2, 6):
        for i in range(3, 6):
            a,b = pell(u,i), pell(u,i+1)
            if a*b > 15000:
                continue
            assert gcd(a,b)==1 and a>u
            check(a, b, u)
            pell_configurations += 1
    print('PASS: %d coprime triples, %d target comparisons, %d Pell specializations'
          % (configurations, comparisons, pell_configurations))

if __name__ == '__main__':
    main()
