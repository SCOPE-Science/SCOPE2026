"""Reproducible finite checks for the stripe-cycle and winding theorem.

Python 3.9 or later; standard library only. These checks complement an analytic
argument and do not certify statements for all lattice sizes.
"""
from collections import Counter
from itertools import product
from math import comb


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    m = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            m = -m
        p += 1
    return -m if n > 1 else m


def step_1d(s):
    n = len(s)
    return tuple((s[i] + int(s[(i - 1) % n] == (s[i] + 1) % 3
        or s[(i + 1) % n] == (s[i] + 1) % 3)) % 3
        for i in range(n))


def step_2d_for_stripes(s):
    """Independent literal 8-neighbor Moore implementation for uniform rows."""
    n = len(s)
    board = [[s[i] for j in range(n)] for i in range(n)]
    new = []
    for i in range(n):
        row = []
        for j in range(n):
            succ = (board[i][j] + 1) % 3
            hits = sum(board[(i + di) % n][(j + dj) % n] == succ
                for di in (-1, 0, 1) for dj in (-1, 0, 1)
                if (di, dj) != (0, 0))
            row.append(succ if hits >= 3 else board[i][j])
        new.append(row)
    assert all(len(set(row)) == 1 for row in new)
    return tuple(row[0] for row in new)


def gradient(s):
    return tuple(((s[(i + 1) % len(s)] - s[i] + 1) % 3) - 1
                 for i in range(len(s)))


def pure(s):
    d = gradient(s)
    return all(x >= 0 for x in d) or all(x <= 0 for x in d)


def binomial_sum(n):
    return sum(comb(n, k) for k in range(0, n + 1, 3))


def cycle_prediction(p):
    if p == 1:
        return 3
    return 6 * sum(mobius(p // d) * binomial_sum(d)
                         for d in divisors(p)) // p


def winding_counts(n):
    poly = Counter({0: 1})
    for _ in range(n):
        new = Counter()
        for e, cnt in poly.items():
            for step in (-1, 0, 1):
                new[e + step] += cnt
        poly = new
    return {k // 3: 3 * v for k, v in poly.items() if k % 3 == 0}


def test(n):
    # Explore the entire 1D/stripe state-transition graph, not a sample.
    seen = set()
    cyc = Counter()
    recurrent = 0
    basin_by_winding = Counter()
    for s in product(range(3), repeat=n):
        if n <= 6:
            assert step_2d_for_stripes(s) == step_1d(s)
        d = gradient(s)
        w = sum(d) // 3
        assert sum(d) % 3 == 0
        basin_by_winding[w] += 1
        if s in seen:
            continue
        path = []
        position = {}
        x = s
        while x not in seen and x not in position:
            position[x] = len(path)
            path.append(x)
            y = step_1d(x)
            dx, dy = gradient(x), gradient(y)
            assert sum(dx) == sum(dy)
            assert dx.count(+1) >= dy.count(+1)
            assert dx.count(-1) >= dy.count(-1)
            x = y
        if x in position:
            tail = path[position[x]:]
            for t in tail:
                assert pure(t)
                gd = gradient(t)
                if any(v > 0 for v in gd):
                    assert step_1d(t) == t[1:] + t[:1]
                elif any(v < 0 for v in gd):
                    assert step_1d(t) == t[-1:] + t[:-1]
                else:
                    assert step_1d(t) == t
                recurrent += 1
            cyc[len(tail)] += 1
        seen.update(path)
    pred = {p: cycle_prediction(p) for p in divisors(n)
            if cycle_prediction(p) > 0}
    assert dict(cyc) == pred, (n, cyc, pred)
    assert recurrent == 6 * binomial_sum(n) - 3
    assert dict(basin_by_winding) == winding_counts(n)
    print("N", n, "stripe_states", 3**n,
          "recurrent", recurrent, "cycles", dict(sorted(cyc.items())),
          "winding_zero", basin_by_winding[0])


if __name__ == '__main__':
    for n in range(4, 11):
        test(n)
    seven = (0, 1, 2, 0, 1, 2, 2)
    assert gradient(seven).count(+1) == 6
    assert all(seven != seven[k:] + seven[:k]
               for k in range(1, 7))
    assert step_1d(seven) == seven[1:] + seven[:1]
    x = seven
    for j in range(7):
        x = step_1d(x)
    assert x == seven
    # Exact roots-of-unity filter using 2*cos(n*pi/3) in Z.
    twice_cos = (2, 1, -1, -2, -1, 1)
    for n in range(1, 101):
        assert 3 * binomial_sum(n) == 2**n + twice_cos[n % 6]
    print("VERIFY_OK exhaustive_n=4..10 direct_2d_n=4..6",
          "roots_unity_n=1..100 six_wall_L7=True")
