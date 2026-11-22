"""Finite-sample calibration for a univariate uniform Euler-characteristic test.

Requires Python 3.10+ and mpmath 1.3+. The exact routine uses finite
inclusion-exclusion; it is not designed for large sample sizes.
"""
from itertools import combinations_with_replacement, product
from math import comb, factorial, sqrt
from random import Random
import mpmath as mp


def exact_cdf(n, z, dps=45):
    """P(sqrt(n)*Delta_n <= z), full-filtration, iid U(0,1) null."""
    if not isinstance(n, int) or n < 2:
        raise ValueError("n must be an integer >= 2")
    mp.mp.dps = dps
    z = mp.mpf(str(z))
    m = n - 1
    if z < mp.mpf("0.5"):
        return mp.mpf(0)
    if z >= m:
        return mp.mpf(1)
    pl = [max(mp.mpf(0), (k-z)/m) for k in range(1, m+1)]
    pu = [min(mp.mpf(1), (k-1+z)/m) for k in range(1, m+1)]
    if any(l > u for l, u in zip(pl, pu)):
        return mp.mpf(0)
    A = [1-u**(mp.mpf(1)/n) for u in pu]
    B = [1-l**(mp.mpf(1)/n) for l in pl]
    edges = sorted(set([mp.mpf(0), mp.mpf(1)] + A + B))
    L = len(edges)-1
    answer = mp.mpf(0)
    for cell_multiset in combinations_with_replacement(range(L), m):
        ranked = sorted(cell_multiset, reverse=True)
        if any(edges[j] < A[k] or edges[j+1] > B[k]
               for k, j in enumerate(ranked)):
            continue
        counts = [cell_multiset.count(j) for j in range(L)]
        denom = 1
        for c in counts:
            denom *= factorial(c)
        multiplicity = factorial(m)//denom
        shift = sum(counts[j]*edges[j] for j in range(L))
        widths = [edges[j+1]-edges[j] for j in range(L)]
        contribution = mp.mpf(0)
        for h in product(*[range(c+1) for c in counts]):
            remaining = 1-shift-sum(hj*w for hj, w in zip(h, widths))
            if remaining > 0:
                coefficient = (-1)**sum(h)
                for c, hj in zip(counts, h):
                    coefficient *= comb(c, hj)
                contribution += coefficient * remaining**n
        answer += multiplicity*contribution
    return answer


def left_transition(n):
    """Largest z for which the simple product formula holds."""
    if n == 2:
        return mp.mpf(1)
    m = n-1
    f = lambda z: sum(1-((k-z)/m)**(mp.mpf(1)/n)
                      for k in range(1, m+1))-1
    lo, hi = mp.mpf("0.5"), mp.mpf(1)
    for _ in range(180):
        mid = (lo+hi)/2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def left_cdf(n, z):
    """Exact cdf for 1/2 <= z <= left_transition(n)."""
    z = mp.mpf(str(z))
    if not mp.mpf("0.5") <= z <= left_transition(n):
        raise ValueError("outside the product-law interval")
    m = n-1
    l = [((k-z)/m)**(mp.mpf(1)/n) for k in range(1, m+1)]
    u = [((k-1+z)/m)**(mp.mpf(1)/n) for k in range(1, m+1)]
    return (factorial(m)*factorial(n)*mp.fprod(b-a for a, b in zip(l,u))
            *(1-m+sum(a+b for a,b in zip(l,u))/2))


def left_coefficient(n):
    """lim_{e downarrow 0} P(sqrt(n)*Delta<=1/2+e)/e**(n-1)."""
    m = n-1
    p = [(mp.mpf(k)-mp.mpf("0.5"))/m for k in range(1,m+1)]
    slack = 1-m+sum(v**(mp.mpf(1)/n) for v in p)
    return (factorial(n)*factorial(m)*slack
            *(mp.mpf(2)/(n*m))**m
            *mp.fprod(v**(mp.mpf(1)/n-1) for v in p))


def statistic_z(sample):
    """sqrt(n) times the exact centered full-filtration discrepancy."""
    n = len(sample)
    g = sorted((b-a for a,b in zip(sorted(sample)[:-1],
                                  sorted(sample)[1:])), reverse=True)
    m = n-1
    return max(max(abs(k-m*(1-d)**n), abs(k-1-m*(1-d)**n))
               for k,d in enumerate(g,1))


def check():
    tests = 0
    for n in range(2,8):
        assert left_transition(n) > mp.mpf("0.5"); tests += 1
        for z in ["0.51", "0.60", "0.70", "0.85"]:
            p = exact_cdf(n,z)
            q = left_cdf(n,z)
            assert abs(p-q) < mp.mpf("1e-32"), (n,z,p,q)
            tests += 1
        for e in ["0.02", "0.002"]:
            ratio = left_cdf(n,mp.mpf("0.5")+mp.mpf(e))/mp.mpf(e)**(n-1)
            assert abs(ratio/left_coefficient(n)-1) < mp.mpf("0.003")
            tests += 1
    for z in ["0.5", "0.7", "0.9", "0.999"]:
        assert abs(exact_cdf(2,z)-(2*mp.mpf(z)-1)) < mp.mpf("1e-35")
        tests += 1
    for n,z,v in [(3,"1.0","0.5946462869292811"),
                  (4,"1.3","0.6152789086648785"),
                  (5,"1.8","0.8385280484507918")]:
        assert abs(exact_cdf(n,z)-mp.mpf(v)) < mp.mpf("1e-15")
        tests += 1
    rng = Random(20261116)
    for n in [2,3,4,5]:
        z = 0.7
        N = 60000
        hits = sum(statistic_z([rng.random() for _ in range(n)]) <= z
                   for _ in range(N))
        p = float(left_cdf(n,z))
        assert abs(hits/N - p) < 6*sqrt(max(p*(1-p),0)/N)+0.002
        tests += 1
    print("PASS", tests, "checks")
    print("CDF n=3, z=0.7", mp.nstr(exact_cdf(3,"0.7"), 18))
    print("CDF n=4, z=1.3", mp.nstr(exact_cdf(4,"1.3"), 18))
    print("Left coefficient n=3", mp.nstr(left_coefficient(3),18))
    print("Transition n=3", mp.nstr(left_transition(3),18))

if __name__ == "__main__":
    check()
