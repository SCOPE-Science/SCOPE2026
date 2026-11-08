"""Exact finite checks for the fixed-content periodic pair-count moment formula.

Run: python verify.py
No external packages are required.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def fall(x, r):
    z = 1
    for j in range(r):
        z *= x - j
    return z


def moment(n, k, r):
    if k < r:
        return Fraction(0)
    return Fraction(fall(k, r), fall(n, r))


def predicted(n, k, d):
    p = {r: moment(n, k, r) for r in range(2, 7)}
    mean = Fraction(k * (k - 1), n - 1)
    variance = Fraction(k * (k - 1) * (n - k) * (n - k - 1),
                        (n - 2) * (n - 1)**2)
    baseline = Fraction(k * (k - 1) * (n - k) * (n - k - 1)
                        * ((2*k - n)**2 - 1),
                        (n - 3) * (n - 2) * (n - 1)**3)
    t = n // 3 if n % 3 == 0 and d == n // 3 else 0
    excess = 6 * t * (p[3] - 3*p[4] + 3*p[5] - p[6])
    central3 = baseline + excess
    # Check independent edge-motif expression for the raw third moment.
    disjoint = comb(n, 3) - n * (n - 3) - t
    raw3 = (n*p[2] + 3*(2*n*p[3] + n*(n-3)*p[4])
            + 6*(t*p[3] + (n-3*t)*p[4]
                 + (n*(n-4)+3*t)*p[5] + disjoint*p[6]))
    raw2 = n*p[2] + 2*n*p[3] + n*(n-3)*p[4]
    assert raw2 - mean**2 == variance
    assert raw3 - 3*mean*raw2 + 2*mean**3 == central3
    if t:
        assert excess == Fraction(2*n * fall(k, 3) * fall(n-k, 3),
                                  fall(n, 6))
    return mean, variance, central3


def observed(n, k, d):
    edges = set(tuple(sorted((i, (i+d) % n))) for i in range(n))
    assert len(edges) == n
    counts = []
    for supp in combinations(range(n), k):
        s = set(supp)
        counts.append(sum(u in s and v in s for u, v in edges))
    z = len(counts)
    avg = Fraction(sum(counts), z)
    return (avg,
            sum((a-avg)**2 for a in counts) / z,
            sum((a-avg)**3 for a in counts) / z)


def main():
    cases = 0
    assertions = 0
    for n in range(6, 13):
        for k in range(n+1):
            for d in range(1, (n-1)//2+1):
                exact = observed(n,k,d)
                formula = predicted(n,k,d)
                for a,b in zip(exact,formula):
                    assert a == b, (n,k,d,a,b)
                    assertions += 1
                cases += 1
    for n in (6,12,18):
        k = n//2
        base = predicted(n,k,1)[2]
        exceptional = predicted(n,k,n//3)[2]
        assert base < 0 < exceptional
        assertions += 1
    assert predicted(6,3,1)[2] == Fraction(-3,125)
    assert predicted(6,3,2)[2] == Fraction(72,125)
    assertions += 2
    print(f"PASS: {assertions} exact comparisons across {cases} exhaustively enumerated (n,k,d) cases; three balanced sign reversals.")

if __name__ == '__main__':
    main()
