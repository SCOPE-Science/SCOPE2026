"""Exact finite diagnostics for Gini sensitivity of weighted isotonic projection.

Run with Python 3.10+; standard library only.  The unrestricted assertions
are proved analytically in RESULT.md, not inferred from finite tests.
"""
from fractions import Fraction as F
from itertools import product
from math import floor


def partitions(n):
    for cuts in product((0, 1), repeat=n-1):
        blocks = []
        start = 0
        for j, cut in enumerate(cuts):
            if cut:
                blocks.append(tuple(range(start, j+1)))
                start = j+1
        blocks.append(tuple(range(start, n)))
        yield tuple(blocks)


def gini(x):
    return sum((abs(x[i]-x[j]) for i in range(len(x))
                for j in range(i+1, len(x))), F(0))


def exact_branch_norm(mu, blocks):
    n = len(mu)
    totals = [sum((mu[i] for i in b), F(0)) for b in blocks]
    best = F(0)
    for bits in product((0, 1), repeat=n):
        s = sum(bits)
        if s == 0 or s == n:
            continue
        out = [F(0)]*n
        for block, total in zip(blocks, totals):
            average = sum((mu[i]*bits[i] for i in block), F(0))/total
            for i in block:
                out[i] = average
        ratio = gini(out)/F(s*(n-s))
        if ratio > best:
            best = ratio
    return best


def exact_norm(mu):
    return max(exact_branch_norm(mu, b) for b in partitions(len(mu)))


def four_formula(mu):
    adjacent = max(max(mu[i], mu[i+1])/(mu[i]+mu[i+1])
                   for i in range(3))
    return max(F(1), F(4, 3)*adjacent)


def isotonic(y, weights):
    """Independent PAV implementation for rational inputs."""
    stack = []
    for i, (v, w) in enumerate(zip(y, weights)):
        stack.append([w, w*v, [i]])
        while len(stack) > 1 and stack[-2][1]/stack[-2][0] > stack[-1][1]/stack[-1][0]:
            b = stack.pop()
            a = stack.pop()
            stack.append([a[0]+b[0], a[1]+b[1], a[2]+b[2]])
    result = [F(0)]*len(y)
    for w, sx, idx in stack:
        for j in idx:
            result[j] = sx/w
    return result


def check():
    cases = 0
    for n in range(2, 8):
        for seed in range(1, 6):
            mu = [F(((19*i+11*seed+3*i*seed) % 17)+1) for i in range(n)]
            val = exact_norm(mu)
            ceiling = F((n*n)//4, n-1)
            assert F(1) <= val <= ceiling, (n, mu, val, ceiling)
            if n >= 4:
                assert val < ceiling, (n, mu, val)
            if n == 4:
                assert val == four_formula(mu), (mu,val,four_formula(mu))
            cases += 1
        assert exact_norm([F(1)]*n) == 1
        cases += 1
    print('EXACT_ALL_PARTITIONS_AND_BINARY_CUTS_PASSED', cases)

    # More exhaustive four-site mass tests, including highly unbalanced cases.
    four_cases = 0
    for a, b, c, d in product((1, 2, 5, 19), repeat=4):
        mu = [F(t) for t in (a,b,c,d)]
        assert exact_norm(mu) == four_formula(mu)
        four_cases += 1
    print('EXACT_FOUR_SITE_MASS_RATIO_FORMULA_PASSED', four_cases)

    # The sharp dimension envelope is approached by a dominant observation mass.
    limits = 0
    for n in range(4, 16):
        k = n//2
        for mass in (10, 10000, 100000000):
            mu = [F(1)]*n
            mu[0] = F(mass)
            # Realizable first block B={0,...,k-1}; other sites singleton.
            ratio = F(k*(n-k), n-1)*mu[0]/sum(mu[:k])
            assert ratio <= F((n*n)//4, n-1)
            assert F((n*n)//4, n-1)-ratio == F(k*(n-k), n-1)*F(k-1, mass+k-1)
            limits += 1
    print('EXACT_DOMINANT_MASS_SHARP_ENVELOPE_WITNESSES_PASSED', limits)

    # Independent exact PAV consistency and nonlinear two-input perturbation.
    pairs = 0
    for n in range(4, 9):
        k = n//2
        for dominant in (5, 101):
            mu = [F(1)]*n
            mu[0] = F(dominant)
            base = [F(k-i) for i in range(k)] + [F(2*k+i) for i in range(n-k)]
            h = [F(1)] + [F(0)]*(n-1)
            delta = F(1, 1000)
            before = isotonic(base,mu)
            after = isotonic([a+delta*b for a,b in zip(base,h)],mu)
            slope = [(a-b)/delta for a,b in zip(after,before)]
            expected = [mu[0]/sum(mu[:k])]*k + [F(0)]*(n-k)
            assert slope == expected, (n, dominant,slope,expected)
            assert gini(slope)/gini(h) == F(k*(n-k),n-1)*mu[0]/sum(mu[:k])
            pairs += 1
    print('INDEPENDENT_EXACT_PAV_TWO_INPUT_WITNESSES_PASSED',pairs)
    print('ALL_WEIGHTED_ISOTONIC_GINI_DIAGNOSTICS_PASSED')


if __name__ == '__main__':
    check()
