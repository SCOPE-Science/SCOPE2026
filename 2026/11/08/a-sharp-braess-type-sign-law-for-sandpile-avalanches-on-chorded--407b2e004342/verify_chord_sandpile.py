"""Exact checks for mean sandpile topplings after one added cycle chord.

No external dependencies. All arithmetic is rational or integral.
"""
from fractions import Fraction
from itertools import product
from math import isqrt


def laplacian(n, chord=None):
    edges = {(i, (i + 1) % n) for i in range(n)}
    if chord is not None:
        edges.add(chord)
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def solve(matrix, rhs):
    n = len(rhs)
    a = [[Fraction(x) for x in row] + [Fraction(y)]
         for row, y in zip(matrix, rhs)]
    for k in range(n):
        p = next(i for i in range(k, n) if a[i][k] != 0)
        a[k], a[p] = a[p], a[k]
        f = a[k][k]
        a[k] = [x / f for x in a[k]]
        for i in range(n):
            if i != k:
                f = a[i][k]
                if f:
                    a[i] = [x - f*y for x, y in zip(a[i], a[k])]
    return [row[-1] for row in a]


def stationary_mean(adj):
    n = len(adj)
    mat = [[len(adj[a]) * (a == b) - (b in adj[a])
            for b in range(1, n)] for a in range(1, n)]
    return solve(mat, [1]*(n-1))[0]


def relax(adj, state, sink=0):
    x = list(state)
    topplings = [0] * len(adj)
    while True:
        v = next((v for v in range(len(adj))
                  if v != sink and x[v] >= len(adj[v])), None)
        if v is None:
            return tuple(x), tuple(topplings)
        x[v] -= len(adj[v])
        topplings[v] += 1
        for w in adj[v]:
            if w != sink:
                x[w] += 1


def enumerate_mean(adj):
    n = len(adj)
    total = 0
    rec = 0
    for heights in product(*(range(len(adj[i])) for i in range(1,n))):
        state = (0,) + heights
        burnt = list(state)
        for v in adj[0]:
            burnt[v] += 1
        _end, burn = relax(adj, burnt)
        if any(burn[i] != 1 for i in range(1,n)):
            continue
        rec += 1
        grain = list(state)
        grain[1] += 1
        _end, fired = relax(adj, grain)
        total += sum(fired)
    return Fraction(total, rec), rec


def delta(n, i, j):
    d = j - i
    return Fraction(d*d*(n-i-j), 2*(n + d*(n-d)))


def verify():
    tested = 0
    burn_tests = 0
    for n in range(4, 12):
        base_graph = laplacian(n)
        base = stationary_mean(base_graph)
        assert base == Fraction(n-1, 2), (n, base)
        if n <= 7:
            base_burn, base_states = enumerate_mean(base_graph)
            assert base_burn == base
            assert base_states == n  # cycle spanning-tree count
        for i in range(1, n):
            for j in range(i+2, n):
                chord_graph = laplacian(n, (i, j))
                expected = base + delta(n, i, j)
                actual = stationary_mean(chord_graph)
                assert actual == expected, (n, i, j, actual, expected)
                assert (actual > base) == (i+j < n)
                assert (actual < base) == (i+j > n)
                if n <= 7:
                    direct, recurrent_count = enumerate_mean(chord_graph)
                    assert direct == actual, (n,i,j,direct,actual)
                    d=j-i
                    assert recurrent_count == n + d*(n-d), (n,i,j,recurrent_count)
                    burn_tests += 1
                tested += 1
    for n in (100, 1000, 10000, 100000):
        k = n - isqrt(n)
        ratio = Fraction(n-1,2).__add__(delta(n,1,k)) / Fraction(n-1,2)
        assert 1 < ratio < 2
        print('near_double',n,ratio,format(float(ratio),'.10f'))
    print('PASS exact_laplacian_cases=', tested,
          'independent_burning_cases=',burn_tests)


if __name__ == '__main__':
    verify()
