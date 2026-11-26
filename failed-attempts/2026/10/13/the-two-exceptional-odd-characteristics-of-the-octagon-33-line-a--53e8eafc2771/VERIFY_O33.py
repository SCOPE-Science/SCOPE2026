"""Exact incidence and reduction certificate for the octagon 33-line arrangement.

Python 3 standard library only. All characteristic-zero operations are exact in
Q[r] /(r*r - 2). Finite-field calculations use genuine fields, not samples.
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter, defaultdict


def elt(a=0, b=0):
    return Q(a), Q(b)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[0], -x[1]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def inverse(x):
    den = x[0] * x[0] - 2 * x[1] * x[1]
    assert den != 0
    return x[0] / den, -x[1] / den


def norm(x):
    return x[0] * x[0] - 2 * x[1] * x[1]


def cross(x, y, plus=add, minus=sub, times=mul):
    return tuple(minus(times(x[(i + 1) % 3], y[(i + 2) % 3]),
                       times(x[(i + 2) % 3], y[(i + 1) % 3])) for i in range(3))


def scalar(x, y):
    ans = elt()
    for a, b in zip(x, y):
        ans = add(ans, mul(a, b))
    return ans


def projective(v):
    for x in v:
        if x != elt():
            inv = inverse(x)
            return tuple(mul(y, inv) for y in v)
    return None


# The eight original octagon side lines, with (a,b) denoting a+b*sqrt(2).
OCTAGON = [
    ((1, 0), (-1, 1), (-1, 0)),
    ((1, 0), (1, 1), (-1, -1)),
    ((1, 0), (-1, -1), (1, 1)),
    ((1, 0), (1, -1), (1, 0)),
    ((1, 0), (-1, 1), (1, 0)),
    ((1, 0), (1, 1), (1, 1)),
    ((1, 0), (-1, -1), (-1, -1)),
    ((1, 0), (1, -1), (-1, 0)),
]


def octagon_closure():
    lines = [tuple(elt(*x) for x in v) for v in OCTAGON]
    points = sorted({projective(cross(a, b)) for a, b in combinations(lines, 2)})
    assert len(points) == 28
    rich = {}
    for a, b in combinations(points, 2):
        line = projective(cross(a, b))
        if line not in rich:
            m = sum(scalar(line, p) == elt() for p in points)
            if m >= 3:
                rich[line] = m
    assert len(rich) == 33
    assert Counter(rich.values()) == Counter({3:20, 4:5, 7:8})
    result = sorted(rich)
    assert len(set(result)) == 33
    # No reductions are made using denominators: all 33 coefficient pairs are integral.
    assert all(x.denominator == 1 for line in result for q in line for x in q)
    return result


def pair_histogram(lines):
    points = defaultdict(set)
    for i, j in combinations(range(len(lines)), 2):
        p = projective(cross(lines[i], lines[j]))
        assert p is not None
        points[p].update((i, j))
    assert sum(m * (m - 1) // 2 for m in map(len, points.values())) == 528
    return Counter(len(v) for v in points.values())


def finite_histogram(lines, p, root=None):
    # root != None specializes sqrt(2) to root in F_p, else use F_p[r]/(r^2-2).
    if root is not None:
        z = 0
        def ev(v): return (int(v[0]) + root * int(v[1])) % p
        def a(x, y): return (x + y) % p
        def b(x, y): return (x * y) % p
        def invert(x): return pow(x, p - 2, p)
        minus_one = -1 % p
    else:
        z = (0, 0)
        assert not any((r * r - 2) % p == 0 for r in range(p))
        def ev(v): return (int(v[0]) % p, int(v[1]) % p)
        def a(x, y): return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)
        def b(x, y):
            return ((x[0] * y[0] + 2 * x[1] * y[1]) % p,
                    (x[0] * y[1] + x[1] * y[0]) % p)
        def invert(x):
            den = (x[0] * x[0] - 2 * x[1] * x[1]) % p
            assert den != 0
            invden = pow(den, -1, p)
            return x[0] * invden % p, -x[1] * invden % p
        minus_one = (-1 % p, 0)
    def minus(x, y): return a(x, b(minus_one, y))
    def normal(v):
        for x in v:
            if x != z:
                y = invert(x)
                return tuple(b(t, y) for t in v)
        return None
    reduced = [tuple(ev(t) for t in line) for line in lines]
    assert len({normal(line) for line in reduced}) == 33
    points = defaultdict(set)
    for i, j in combinations(range(33), 2):
        v = normal(cross(reduced[i], reduced[j], a, minus, b))
        assert v is not None
        points[v].update((i, j))
    hist = Counter(map(len, points.values()))
    assert sum(m * (m - 1) // 2 for m, n in hist.items() for _ in range(n)) == 528
    return hist


def verify():
    lines = octagon_closure()
    good = Counter({2:108, 3:40, 5:16, 8:5})
    assert pair_histogram(lines) == good
    norms = Counter()
    zeros = 0
    witnesses = {}
    for ids in combinations(range(33), 3):
        det = scalar(lines[ids[0]], cross(lines[ids[1]], lines[ids[2]]))
        if det == elt():
            zeros += 1
            continue
        n = norm(det)
        assert n.denominator == 1
        n = abs(int(n))
        norms[n] += 1
        for p in (3, 7):
            if n % p == 0 and p not in witnesses:
                witnesses[p] = (tuple(i + 1 for i in ids), det)
    assert zeros == 480
    assert sum(norms.values()) == 4976
    norm_set = {1, 2, 4, 8, 14, 16, 28, 32, 36, 56, 64, 72}
    assert set(norms) == norm_set
    # Every nonzero 3x3 minor remains nonzero in odd characteristics !=3,7.
    for n in norms:
        for p in (2, 3, 7):
            while n % p == 0:
                n //= p
        assert n == 1
    assert set(witnesses) == {3, 7}
    bad3 = Counter({2:12, 3:40, 4:16, 5:16, 8:5})
    bad7 = Counter({2:4, 4:24, 5:24, 8:5})
    assert finite_histogram(lines, 3) == bad3     # F_9: sqrt(2) nonsquare
    assert finite_histogram(lines, 7, 3) == bad7  # F_7: 3^2=2
    assert finite_histogram(lines, 7, 4) == bad7  # conjugate embedding
    # Control evaluations: not used to prove the uniform assertion.
    assert finite_histogram(lines, 5) == good
    assert finite_histogram(lines, 11) == good
    assert finite_histogram(lines, 17, 6) == good
    print('VERIFY_OK: 33 lines; 5456 triples (480 zero); norm support', sorted(norm_set))
    print('generic odd p not 3 or 7:', dict(sorted(good.items())))
    print('p=3:', dict(sorted(bad3.items())))
    print('p=7:', dict(sorted(bad7.items())))
    print('witnesses for 3 and 7:', witnesses)


if __name__ == '__main__':
    verify()
