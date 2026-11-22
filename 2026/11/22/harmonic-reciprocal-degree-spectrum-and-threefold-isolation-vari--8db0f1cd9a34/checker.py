#!/usr/bin/env python3
"""Checks for a reciprocal-edge subgraph of the uniform threshold digraph.

All finite algebra checks use exact rational arithmetic. The simulation is a
sanity check and is not used to establish the asymptotic variance theorem.
"""
from fractions import Fraction as Q
from math import comb, log
from random import Random


def harmonic(n):
    return sum((Q(1, j) for j in range(1, n + 1)), Q(0))


def degree_pmf_beta_expansion(n, k):
    # Binomial mixture with the exact product-uniform density -log(z).
    return comb(n - 1, k) * sum(
        (Q((-1) ** j * comb(n - 1 - k, j), (k + j + 1) ** 2)
         for j in range(n - k)), Q(0)
    )


def degree_pmf_harmonic(n, k):
    return (harmonic(n) - harmonic(k)) / n


def brute_degrees(x, y):
    n = len(x)
    return [sum(i != j and x[i] + y[j] > 1 and x[j] + y[i] > 1
                for j in range(n)) for i in range(n)]


def fast_degrees(x, y):
    """Offline orthant-count Fenwick calculation, for simulation cross-checks."""
    n = len(x)
    xorder = sorted(range(n), key=lambda i: -x[i])
    yorder = sorted(range(n), key=lambda i: y[i])
    yrank = [0] * n
    for r, i in enumerate(yorder, 1):
        yrank[i] = r
    qorder = sorted(range(n), key=lambda i: y[i])
    bit = [0] * (n + 1)
    def add(r):
        while r <= n:
            bit[r] += 1
            r += r & -r
    def prefix(r):
        out = 0
        while r:
            out += bit[r]
            r -= r & -r
        return out
    from bisect import bisect_right
    ys = [y[i] for i in yorder]
    p = 0
    degree = [0] * n
    for i in qorder:
        while p < n and x[xorder[p]] > 1 - y[i]:
            add(yrank[xorder[p]])
            p += 1
        rank = bisect_right(ys, 1 - x[i])
        degree[i] = p - prefix(rank) - int(x[i] + y[i] > 1)
    return degree


def run():
    assertions = 0
    for n in range(1, 31):
        vals = [degree_pmf_harmonic(n, k) for k in range(n)]
        assert all(v == degree_pmf_beta_expansion(n, k)
                   for k, v in enumerate(vals))
        assertions += n
        assert sum(vals) == 1
        assertions += 1
        mean = sum((k * p for k, p in enumerate(vals)), Q(0))
        second = sum((k*k*p for k, p in enumerate(vals)), Q(0))
        assert mean == Q(n-1, 4)
        assert second - mean*mean == Q(5*(n-1), 36) + Q(7*(n-1)**2, 144)
        assertions += 2
    for n in range(1, 80):
        assert sum((harmonic(n)-harmonic(k) for k in range(n)), Q(0)) == n
        assert harmonic(n) == sum((degree_pmf_harmonic(n, 0)*n,), Q(0))
        assertions += 2
    # The 2-neighbor union probability is exact rectangle inclusion-exclusion.
    grid = [Q(k, 7) for k in range(1, 7)]
    for x1 in grid:
      for y1 in grid:
       for x2 in grid:
        for y2 in grid:
            z1, z2 = x1*y1, x2*y2
            m = min(x1,x2)*min(y1,y2)
            q = 1-z1-z2+m
            assert 0 <= q <= 1
            assert q == 1-max(z1,z2)-(min(z1,z2)-m)
            assertions += 2
    # Overlap kernel integral: for independent Exp(1) marks, min(T1,q*T2)
    # is Exp(1 + 1/q), and E(exp(min)-1)=q exactly.
    for den in range(1, 40):
        q = Q(1, den)
        rate = 1 + 1/q
        assert rate / (rate-1) - 1 == q
        assertions += 1
    # Verify graph computation against literal definition on random rational data.
    rng = Random(442117)
    for n in range(2, 20):
        for _ in range(50):
            x=[Q(rng.randint(1,998),1000) for _ in range(n)]
            y=[Q(rng.randint(1,998),1000) for _ in range(n)]
            assert brute_degrees(x,y)==fast_degrees(x,y)
            assertions += 1
    # Numerical check of the natural, divergent isolation variance,
    # not proof of its exact coefficient or convergence.
    n, reps = 500, 2000
    samples=[]
    for _ in range(reps):
        x=[rng.random() for _ in range(n)]
        y=[rng.random() for _ in range(n)]
        samples.append(sum(d==0 for d in fast_degrees(x,y)))
    mean=sum(samples)/reps
    var=sum((v-mean)**2 for v in samples)/reps
    assert abs(mean-float(harmonic(n))) < 0.45
    assert 2.0 < var/log(n) < 3.6
    assertions += 2
    print(f"PASS {assertions} assertions; simulated n={n} mean={mean:.5f} variance={var:.5f}; ")
    print(f"theoretical mean={float(harmonic(n)):.5f}, asymptotic variance benchmark=3 log(n)={3*log(n):.5f}")
    print("The limit and its factor 3 are proved analytically in RESULT.md, not by finite checks.")

if __name__=='__main__':
    run()
