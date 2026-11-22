"""Exact rational checks for the joint cyclic Voronoi length law (stdlib only)."""
from fractions import Fraction as F
from random import Random


def forward(g):
    n = len(g)
    return [(g[(i - 1) % n] + g[i]) / 2 for i in range(n)]


def odd_inverse(l):
    n = len(l)
    assert n % 2
    return [sum((1 if j % 2 == 0 else -1) * l[(i - j) % n]
                for j in range(n)) for i in range(n)]


def even_fiber(l):
    n = len(l)
    assert n % 2 == 0
    b = [F(0)] * n
    for i in range(1, n):
        b[i] = 2 * l[i] - b[i - 1]
    lo = max(-b[i] for i in range(0, n, 2))
    hi = min(b[i] for i in range(1, n, 2))
    return lo, hi, b


def determinant(a):
    a = [[F(v) for v in row] for row in a]
    d = F(1)
    for j in range(len(a)):
        piv = next((i for i in range(j, len(a)) if a[i][j]), None)
        if piv is None:
            return F(0)
        if piv != j:
            a[j], a[piv] = a[piv], a[j]
            d = -d
        val = a[j][j]
        d *= val
        for i in range(j + 1, len(a)):
            factor = a[i][j] / val
            for k in range(j, len(a)):
                a[i][k] -= factor * a[j][k]
    return d


def varying_coords(s):
    return [F(v) for v in s] + [1 - sum(s)]


rng = Random(1729)
checks = 0
for n in range(3, 15):
    z = [F(0)] * (n - 1)
    baseline = varying_coords(z)
    f0 = forward(baseline)
    columns = []
    for j in range(n - 1):
        zz = list(z)
        zz[j] = 1
        columns.append([a - b for a, b in zip(forward(varying_coords(zz)), f0)])
    if n % 2:
        a = [[columns[j][i] for j in range(n - 1)] for i in range(n - 1)]
        assert abs(determinant(a)) == F(1, 2 ** (n - 1))
    else:
        a = [[F(i == 0) for i in range(n - 1)]] + [
            [columns[j][i] for j in range(n - 1)] for i in range(1, n - 1)
        ]
        assert abs(determinant(a)) == F(1, 2 ** (n - 2))
    checks += 1
    for _ in range(100):
        zz = [rng.randrange(1, 300) for _ in range(n)]
        s = [F(v, sum(zz)) for v in zz]
        l = forward(s)
        assert sum(l) == 1
        checks += 1
        if n % 2:
            assert odd_inverse(l) == s
            checks += 1
        else:
            assert sum(l[::2]) == sum(l[1::2]) == F(1, 2)
            lo, hi, b = even_fiber(l)
            assert lo < s[0] < hi
            ss = [((1 if i % 2 == 0 else -1) * s[0] + b[i])
                  for i in range(n)]
            assert ss == s
            checks += 3
            for x in [lo + (hi - lo) / 3, lo + 2 * (hi - lo) / 3]:
                ss = [(1 if i % 2 == 0 else -1) * x + b[i]
                      for i in range(n)]
                assert min(ss) > 0 and sum(ss) == 1 and forward(ss) == l
                checks += 1
print(f'PASS: {checks} deterministic exact rational tests, n=3,...,14.')
