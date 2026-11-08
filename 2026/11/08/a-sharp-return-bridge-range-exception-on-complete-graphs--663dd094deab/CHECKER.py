"""Exact rational checks for complete-graph return-bridge range comparisons.

Run with Python 3, no external packages required. Numerical enumeration is a
finite diagnostic, while the accompanying proof establishes the theorem for all
orders and lengths.
"""
from fractions import Fraction


def formula(n, t):
    assert n >= 3 and t >= 2
    a, b, sign = (n - 1) ** t, (n - 2) ** t, (-1) ** t
    open_mean = Fraction(n) - Fraction(b, (n - 1) ** (t - 1))
    bridge_mean = Fraction(n) - Fraction(n * (b + (n - 2) * sign), a + (n - 1) * sign)
    return open_mean, bridge_mean


def count(n, t):
    # Count all no-loop paths by (number of visited vertices, endpoint at root).
    root = {1: 1}
    away = {}
    for _ in range(t):
        next_root, next_away = {}, {}
        for k, c in root.items():
            if k > 1:
                next_away[k] = next_away.get(k, 0) + (k - 1) * c
            if k < n:
                next_away[k + 1] = next_away.get(k + 1, 0) + (n - k) * c
        for k, c in away.items():
            next_root[k] = next_root.get(k, 0) + c
            if k > 2:
                next_away[k] = next_away.get(k, 0) + (k - 2) * c
            if k < n:
                next_away[k + 1] = next_away.get(k + 1, 0) + (n - k) * c
        root, away = next_root, next_away
    total = sum(root.values()) + sum(away.values())
    returned = sum(root.values())
    assert total == (n - 1) ** t
    assert returned > 0
    mu_open = Fraction(sum(k * v for k, v in root.items()) + sum(k * v for k, v in away.items()), total)
    mu_bridge = Fraction(sum(k * v for k, v in root.items()), returned)
    return mu_open, mu_bridge, root, away


def main():
    assertions = 0
    for n in range(3, 17):
        for t in range(2, 27):
            a, b, root, away = count(n, t)
            fa, fb = formula(n, t)
            assert a == fa and b == fb
            assertions += 2
            assert (b > a) == (n == 3 and t % 2 == 1)
            assertions += 1
            if t % 2 == 1 and t >= 3 and n >= t + 1:
                assert root.get(2, 0) == 0
                assert root.get(t + 1, 0) == 0
                assert away.get(2, 0) > 0 and away.get(t + 1, 0) > 0
                assertions += 4
    print(f"PASS: {assertions} exact integer/rational assertions")


if __name__ == "__main__":
    main()
