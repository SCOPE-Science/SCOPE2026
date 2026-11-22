"""Reproduce exact one-sweep path averaging identities using rational arithmetic.

Run with Python 3: python verify.py. Assertions test examples and finite cases;
the accompanying argument proves statements in arbitrary dimension.
"""
from fractions import Fraction as F
from itertools import permutations, product
from random import Random


def word(order):
    p = {e: t for t, e in enumerate(order)}
    return tuple(0 if p[j] < p[j + 1] else 1 for j in range(len(order) - 1))


def topological_order(bits):
    m = len(bits) + 1
    successors = [[] for _ in range(m)]
    indegree = [0] * m
    for j, b in enumerate(bits):
        a, c = (j, j + 1) if b == 0 else (j + 1, j)
        successors[a].append(c)
        indegree[c] += 1
    available = [j for j in range(m) if indegree[j] == 0]
    result = []
    while available:
        j = available.pop(0)
        result.append(j)
        for k in successors[j]:
            indegree[k] -= 1
            if indegree[k] == 0:
                available.append(k)
    assert len(result) == m
    assert word(result) == bits
    return result


def exact_loss(order):
    n = len(order) + 1
    a = [[F(i == j) for j in range(n)] for i in range(n)]
    for j in order:
        for k in range(n):
            v = (a[j][k] + a[j + 1][k]) / 2
            a[j][k] = v
            a[j + 1][k] = v
    return sum((v * v for row in a for v in row), F(0)) - 1


def formula(bits):
    if not bits:
        return F(0)
    runs = []
    current, count = bits[0], 0
    for b in bits:
        if b != current:
            runs.append(count)
            current, count = b, 0
        count += 1
    runs.append(count)
    return sum((sum((F(1, 3) * (1 - F(1, 4**k))
                      for k in range(1, length + 1)), F(0))
                for length in runs), F(0))


def bounds(n):
    ell = n - 2
    best = F(ell, 4)
    worst = F(ell, 3) - (1 - F(1, 4**ell)) / 9
    return best, worst


def main():
    tests = 0
    for n in range(2, 9):
        m = n - 1
        for order in permutations(range(m)):
            assert exact_loss(order) == formula(word(order))
            tests += 1
    for n in range(2, 13):
        m = n - 1
        best, worst = bounds(n)
        best_words, worst_words = [], []
        for bits in product((0, 1), repeat=m - 1):
            loss = exact_loss(topological_order(bits))
            assert loss == formula(bits)
            assert best <= loss <= worst
            if loss == best:
                best_words.append(bits)
            if loss == worst:
                worst_words.append(bits)
            tests += 1
        if n == 2:
            assert best_words == [()]
            assert worst_words == [()]
        else:
            assert best_words == [tuple(j % 2 for j in range(m - 1)),
                                  tuple((j + 1) % 2 for j in range(m - 1))]
            assert worst_words == [tuple([0] * (m - 1)),
                                   tuple([1] * (m - 1))]
    rng = Random(20261120)
    for n in (13, 15, 20, 30):
        m = n - 1
        for _ in range(60):
            order = list(range(m))
            rng.shuffle(order)
            assert exact_loss(order) == formula(word(order))
            tests += 1
    assert formula((0, 1)) == F(1, 2)
    assert formula((0, 0)) == F(9, 16)
    assert bounds(5) == (F(3, 4), F(57, 64))
    print(f"PASS: {tests} exact-arithmetic sweep identities and sharp-bound cases")


if __name__ == '__main__':
    main()
