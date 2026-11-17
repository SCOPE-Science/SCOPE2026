"""Standalone exact-arithmetic tests for the weighted-wheel anti-coordination theorem.

Run: python verify.py
No external dependencies. The unrestricted infinite-order result rests on the
mathematical proof, not on finite enumeration.
"""
from fractions import Fraction
from itertools import product
from math import comb


def perrin(n):
    p = [3, 0, 2]
    for k in range(3, n + 1):
        p.append(p[k - 2] + p[k - 3])
    return p[n]


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def neq(a, b):
    return int(a != b)


def cut(n, t, s):
    h, rim = s[0], s[1:]
    return (t * sum(neq(h, x) for x in rim)
            + sum(neq(rim[i], rim[(i + 1) % n]) for i in range(n)))


def is_nash(n, t, s):
    h, rim = s[0], s[1:]
    for i, a in enumerate(rim):
        left, right = rim[i - 1], rim[(i + 1) % n]
        keep = t * neq(a, h) + neq(a, left) + neq(a, right)
        swap = t * neq(1 - a, h) + neq(1 - a, left) + neq(1 - a, right)
        if keep < swap:
            return False
    return sum(neq(h, x) for x in rim) >= sum(neq(1 - h, x) for x in rim)


def classify(n, t, s):
    h, rim = s[0], s[1:]
    zero = [i for i, x in enumerate(rim) if x == h]
    indep = all((i + 1) % n not in zero for i in zero)
    maximal = indep and all(rim[i] == h or
                            rim[(i - 1) % n] == h or rim[(i + 1) % n] == h
                            for i in range(n))
    return maximal if t < 2 else indep if t == 2 else len(zero) == 0


def predicted_min(n, t):
    if t < 2:
        z = (n + 2) // 3
        return t * (n - z) + 2 * z
    return t * n if t > 2 else 2 * n


def predicted_max(n, t):
    return (t * (n - n // 2) + 2 * (n // 2)) if t < 2 else t * n


def predicted_count(n, t):
    return 2 * (perrin(n) if t < 2 else lucas(n) if t == 2 else 1)


def cycle_mis_by_size(n, z):
    if not 0 < z <= n // 2 or not 2 * z <= n <= 3 * z:
        return 0
    return n * comb(z, n - 2 * z) // z


def main():
    test_values = (Fraction(1, 7), Fraction(1), Fraction(3, 2),
                   Fraction(2), Fraction(5, 2), Fraction(4))
    states_tested = 0
    settings_tested = 0
    for n in range(4, 13):
        assert sum(cycle_mis_by_size(n, z) for z in range(n + 1)) == perrin(n)
        for t in test_values:
            equilibria = []
            best = None
            for s in product((0, 1), repeat=n + 1):
                states_tested += 1
                got_nash = is_nash(n, t, s)
                assert got_nash == classify(n, t, s), (n, t, s)
                w = cut(n, t, s)
                best = w if best is None else max(best, w)
                if got_nash:
                    equilibria.append((s, w))
            assert len(equilibria) == predicted_count(n, t), (n, t, len(equilibria))
            assert best == predicted_max(n, t), (n, t, best)
            assert min(x[1] for x in equilibria) == predicted_min(n, t), (n, t)
            assert any(x[1] == best for x in equilibria), (n, t)
            settings_tested += 1
    for n in range(4, 101):
        assert sum(cycle_mis_by_size(n, z) for z in range(n + 1)) == perrin(n)
    print(f"VERIFY_OK states={states_tested} settings={settings_tested} ")
    print("infinite statements established in RESULT.md proof, not by this finite test")

if __name__ == '__main__':
    main()
