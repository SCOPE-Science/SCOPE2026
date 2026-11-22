"""Standalone arithmetic checks for the low-offspring birth-rank theorem.

Usage: python verify.py
This checks finite identities and numerical asymptotic diagnostics; the
infinite point-process convergence requires the proof in RESULT.md.
"""
from fractions import Fraction
from itertools import product, combinations
from math import factorial, log, sqrt


def marked_distribution(n, labels):
    """Exact law of child counts for selected birth labels."""
    labels = tuple(labels)
    law = {(0,) * len(labels): Fraction(1)}
    for child in range(2, n + 1):
        eligible = [k for k, i in enumerate(labels) if i < child]
        total = child - 1
        follow = {}
        for degs, mass in law.items():
            other = mass * Fraction(total - len(eligible), total)
            follow[degs] = follow.get(degs, Fraction(0)) + other
            for k in eligible:
                q = list(degs)
                q[k] += 1
                key = tuple(q)
                follow[key] = follow.get(key, Fraction(0)) + mass / total
        law = follow
    return {k:v for k,v in law.items() if v}


def brute_distribution(n, labels):
    labels = tuple(labels)
    law = {}
    for parents in product(*(range(1, j) for j in range(2, n + 1))):
        deg = [0] * (n + 1)
        for p in parents:
            deg[p] += 1
        key = tuple(deg[i] for i in labels)
        law[key] = law.get(key, 0) + 1
    denom = factorial(n - 1)
    return {k: Fraction(v, denom) for k, v in law.items()}


def one_vertex_probs(n, i, max_r):
    v = [1.0] + [0.0] * max_r
    for j in range(i + 1, n + 1):
        p = 1 / (j - 1)
        v = [v[k] * (1 - p) + (v[k - 1] * p if k else 0)
             for k in range(max_r + 1)]
    return v


def cumulative_expectations(n, K, t=1.0):
    # O(nK) downward recursion for the marginal offspring distributions.
    ps = [1.0] + [0.0] * K
    cutoff = [min(n, int(t * sqrt(n / log(n)**r))) for r in range(K+1)]
    sums = [0.0] * (K+1)
    root_other = None
    for i in range(n, 1, -1):
        if i <= cutoff[0]:
            for r in range(K+1):
                if i <= cutoff[r]:
                    sums[r] += ps[r]
        if i == 2:
            root_other = ps.copy()
        p = 1 / (i - 1)
        ps = [ps[k] * (1-p) + (ps[k-1]*p if k else 0)
              for k in range(K+1)]
    # The root has an obligatory child 2; distribution is 1 + D_2.
    for r in range(1, K+1):
        sums[r] += root_other[r-1]
    return sums


def main():
    assertions = 0
    for n in range(2, 9):
        choices = sorted(set([(1,), (n,), (1,n)] +
                [(a,b) for a,b in combinations(range(1,n+1),2) if (b-a)<=2]))
        for labels in choices:
            assert marked_distribution(n, labels) == brute_distribution(n, labels)
            assertions += 1
    for n in range(3, 13):
        for i in range(1, n + 1):
            joint = marked_distribution(n, (i,))
            vals = one_vertex_probs(n, i, n-1)
            for r in range(n):
                assert abs(float(joint.get((r,), 0)) - vals[r]) < 1e-12
                assertions += 1
    # Exact root and leaf marginals: the number of childless labels with
    # index i>=2 has probability (i-1)/(n-1), not i/n.
    for n in (3,7,16):
        assert marked_distribution(n,(1,)).get((0,),0) == 0
        assertions += 1
        for i in range(2,n+1):
            assert marked_distribution(n,(i,)).get((0,),0) == Fraction(i-1,n-1)
            assertions += 1
    # Non-exhaustive numerical diagnostics for the asymptotic intensity.
    # Convergence is logarithmically slow for r>=1, so no tight tolerance.
    n=400000
    K=2
    observed = cumulative_expectations(n,K,1.0)
    expected=[1/(2**(r+1)*factorial(r)) for r in range(K+1)]
    print('n =',n,'expected counts [r=0,1,2] =',observed)
    print('limiting mean counts =',expected)
    assert all(0.25*expected[r] < observed[r] < 4*expected[r] for r in range(K+1))
    assertions += K+1
    print('PASS:',assertions,'exact/finite assertions plus 3 numerical scale checks')

if __name__=='__main__':
    main()
