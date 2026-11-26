"""Reproducible rational checks for leaf/cherry fluctuations in uniform labelled trees.

Run: python3 verify.py
No external dependencies. Finite checks corroborate but do not replace the proof.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, e, sqrt


def moments(n):
    if n < 5:
        raise ValueError('n >= 5 required')
    a = F((n - 1) ** (n - 2), n ** (n - 2))
    b = F((n - 2) ** (n - 2), n ** (n - 2))
    ec = F(n * (n - 1) * (n - 2) * (n - 3) ** (n - 4), 2 * n ** (n - 2))
    el = n * a
    el2 = n * a + n * (n - 1) * b
    q = F((n - 4) ** (n - 4), (n - 3) ** (n - 4))
    elc = ec * (2 + (n - 3) * q)
    if n == 5:
        ec2 = ec
    else:
        second = F(factorial(n) // factorial(n - 6) * ((n - 6) ** (n - 6) if n >= 7 else 1), 4 * n ** (n - 2))
        ec2 = ec + second
    return el, ec, el2, ec2, elc


def decode_prufer(code, n):
    degrees = [1] * n
    for c in code:
        degrees[c] += 1
    neighbors = [set() for _ in range(n)]
    for c in code:
        leaf = next(i for i, d in enumerate(degrees) if d == 1)
        neighbors[leaf].add(c)
        neighbors[c].add(leaf)
        degrees[leaf] -= 1
        degrees[c] -= 1
    u, v = [i for i, d in enumerate(degrees) if d == 1]
    neighbors[u].add(v)
    neighbors[v].add(u)
    return neighbors


def counts(neighbors):
    degrees = [len(s) for s in neighbors]
    leaves = sum(d == 1 for d in degrees)
    cherries = sum(comb(sum(degrees[u] == 1 for u in neighbors[v]), 2)
                   for v in range(len(neighbors)) if degrees[v] == 3)
    return leaves, cherries


def check():
    tests = 0
    for n in range(5, 9):
        totals = [0] * 5
        for code in product(range(n), repeat=n - 2):
            l, c = counts(decode_prufer(code, n))
            for i, val in enumerate((l, c, l*l, c*c, l*c)):
                totals[i] += val
            tests += 1
        actual = tuple(F(x, n ** (n - 2)) for x in totals)
        predicted = moments(n)
        assert actual == predicted, (n, actual, predicted)
        tests += 5
    for n in range(5, 501):
        el, ec, el2, ec2, elc = moments(n)
        assert ec > 0
        assert elc - el * ec > 0
        assert el2 - el * el > 0
        if n >= 6:
            assert ec2 - ec * ec > 0
        tests += 4
    v_l = (e - 2) / e ** 2
    v_c = (e ** 3 - 3) / (2 * e ** 6)
    cov = (e - 2) / e ** 4
    rho = sqrt(2 * (e - 2) / (e ** 3 - 3))
    assert 0 < rho < 1
    assert abs(rho - cov / sqrt(v_l * v_c)) < 1e-12
    assert v_l * v_c - cov * cov > 0
    tests += 3
    print(f'VERIFY_OK {tests} exact and asymptotic-sign checks')
    print('asymptotic variances and covariance:',v_l, v_c, cov)
    print('limiting correlation:', rho)

if __name__ == '__main__':
    check()
