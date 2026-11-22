"""Exact finite checks for common ancestral paths in independent recursive trees.
Runs with Python standard library only: python check.py
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial, gamma, lgamma, exp, sqrt, log, pi, sinh, sin


def transition_distribution(q, n):
    pmf = {1: Fraction(1)}
    for j in range(2, n + 1):
        k = j - 1
        nxt = {}
        for s, prob in pmf.items():
            attach = Fraction(s, k**q)
            assert 0 <= attach <= 1
            nxt[s] = nxt.get(s, Fraction(0)) + prob * (1 - attach)
            nxt[s + 1] = nxt.get(s + 1, Fraction(0)) + prob * attach
        pmf = {s: p for s, p in nxt.items() if p}
        assert sum(pmf.values()) == 1
    return pmf


def brute_distribution(q, n):
    tree_choices = list(product(*(range(1, j) for j in range(2, n + 1))))
    single_tree_count = factorial(n - 1)
    assert len(tree_choices) == single_tree_count
    tally = Counter()
    for trees in product(tree_choices, repeat=q):
        good = [False]*(n + 1)
        good[1] = True
        for j in range(2, n + 1):
            parents = [t[j - 2] for t in trees]
            if len(set(parents)) == 1 and good[parents[0]]:
                good[j] = True
        tally[sum(good)] += 1
    denom = single_tree_count**q
    return {s: Fraction(v, denom) for s, v in sorted(tally.items())}


def exact_mean(q, n):
    mean = Fraction(1)
    for k in range(1, n):
        mean *= 1 + Fraction(1, k**q)
    return mean


def check():
    comparisons = 0
    enumerations = 0
    for q, biggest in [(2,7), (3,5)]:
        for n in range(2, biggest + 1):
            expected = transition_distribution(q, n)
            observed = brute_distribution(q, n)
            assert observed == expected, (q,n,observed,expected)
            assert sum(s*p for s,p in expected.items()) == exact_mean(q,n)
            comparisons += len(set(observed)|set(expected)) + 2
            enumerations += factorial(n - 1)**q
    for q in [2, 3, 4]:
        for n in range(2,40):
            pmf = transition_distribution(q,n)
            assert sum(s*p for s,p in pmf.items()) == exact_mean(q,n)
            assert sum(pmf.values()) == 1
            comparisons += 2
    # P(S_n=2): no further shared-ancestry join after birth 2.
    for q in [2, 3, 4]:
        for n in range(3,35):
            product_value = Fraction(1)
            for k in range(2,n):
                product_value *= 1 - Fraction(2,k**q)
            assert transition_distribution(q,n)[2] == product_value
            comparisons += 1
    # A second, analytic representation of conditional stabilization: Gamma ratio.
    # Compare with a long finite product for several finite states.
    for n in range(2, 14):
        for s in range(2, n+1):
            z = sqrt(s)
            exact_formula = exp(2*lgamma(n)-lgamma(n-z)-lgamma(n+z))
            truncated = 1.
            for k in range(n, 20000):
                truncated *= 1-s/k**2
            assert abs(exact_formula-truncated) < 8e-4, (n,s,exact_formula,truncated)
            comparisons += 1
    # Euler-product consequences, checked against numerical partial products.
    mu = 1.
    prob_two = 1.
    for k in range(1,10000):
        mu *= 1+1/k**2
        if k >= 2:
            prob_two *= 1-2/k**2
    assert abs(mu - sinh(pi)/pi) < 5e-4
    assert abs(prob_two + sin(pi*sqrt(2))/(pi*sqrt(2))) < 5e-4
    comparisons += 2
    print(f"PASS: {comparisons} assertions (375 exact rational baseline and numerical analytic identities); {enumerations:,} full tuples of recursive trees enumerated")

if __name__ == '__main__':
    check()
