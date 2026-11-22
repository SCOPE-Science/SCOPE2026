#!/usr/bin/env python3
"""Exact small-case checks for terminal birth-label distributions in uniform recursive directed multigraphs."""
from fractions import Fraction
from itertools import product, combinations
from collections import Counter
from math import factorial, comb


def survival_formula(n, k, subset):
    """For n vertices 0,...,n-1, with k independent parents per new vertex."""
    subset = tuple(sorted(subset))
    if not subset:
        return Fraction(1)
    if 0 in subset and n > 1:
        return Fraction(0)
    val = Fraction(1)
    for a, i in enumerate(subset, 1):
        val *= Fraction(i - a + 1, n - a) ** k
    return val


def exact_survival(n, k):
    """Enumerate all equally likely parent choices and compute exact terminal-subset moments."""
    steps = [list(product(range(t), repeat=k)) for t in range(1, n)]
    count = 0
    sums = Counter()
    for selections in product(*steps):
        par = set(x for parents in selections for x in parents)
        leaves = frozenset(range(n)) - par
        count += 1
        for r in range(n + 1):
            for S in combinations(range(n), r):
                if set(S).issubset(leaves):
                    sums[S] += 1
    tests = 0
    for r in range(n+1):
        for S in combinations(range(n),r):
            assert Fraction(sums[S],count) == survival_formula(n,k,S), (n,k,S,sums[S],count)
            tests += 1
    return tests


def check_finite_moments(n, k):
    p = [survival_formula(n,k,(i,)) for i in range(n)]
    assert sum(p) == sum(Fraction(i, n-1)**k for i in range(1,n))
    var = sum(x*(1-x) for x in p)
    for i in range(1,n):
        for j in range(i+1,n):
            joint=survival_formula(n,k,(i,j))
            assert joint<=p[i]*p[j]
            assert joint == (Fraction(i*(j-1),(n-1)*(n-2))**k)
            var += 2*(joint-p[i]*p[j])
    assert var>=0
    return 2*n+n*(n-1)//2


def mean_window(n,k,x):
    return sum((i/(n-1))**k for i in range(1,min(int(x),n-1)+1))


def check_asymptotic_trend():
    # Deterministic first moment probes; NOT evidence of infinite-limit proof.
    for k in (2,3,4):
        for n in (10000,50000):
            b=(n-1)**(k/(k+1))
            approx=mean_window(n,k,b)
            assert abs(approx-1/(k+1))<0.04, (k,n,approx)
    import math
    for c in (0.5,1.0,2.0):
        n=100000
        k=max(2,round(c*math.log(n)))
        b=((k+1)*(n-1)**k)**(1/(k+1))
        assert abs(mean_window(n,k,b)-1)<0.06, (c,n,k,b,mean_window(n,k,b))
    return 9


def main():
    total=0
    for n,k in [(2,1),(3,1),(4,1),(5,1),(6,1),(3,2),(4,2),(5,2),(6,2),(3,3),(4,3),(5,3)]:
        count=exact_survival(n,k)
        total+=count+check_finite_moments(n,k)
    total+=check_asymptotic_trend()
    print(f"PASS: {total} exact moment identities, negative-covariance inequalities, and deterministic mean-window probes. The asymptotic theorem requires its independent analytic proof.")

if __name__=='__main__':
    main()
