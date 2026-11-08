#!/usr/bin/env python3
"""Finite arithmetic checks for the dyadic pseudoperiod theorem.

The infinite statement and minimality are proved in RESULT.md; this checker
provides independent finite consistency and explicit witness-set tests.
Requires only Python 3.9+ standard library.
"""
import random


def shifts(m):
    return tuple(sorted({1 << j for j in range(m)} |
                        {(1 << m) - (1 << j) for j in range(m - 1)}))


def matches(m, n, d):
    return ((n + d).bit_count() - n.bit_count()) % m == 0


def witness_sets(m):
    B = (1 << m) - 1
    result = [("zero", 0, {B})]
    for j in range(m):
        result.append((f"singleton_{j}", (1 << j) * ((1 << (m + 1)) - 1), {1 << j}))
    for ell in range(1, m - 1):
        result.append((f"weight_{ell}", ((1 << (ell + 1)) - 1) * (1 << (m - 1)),
                       {(1 << (m - 1)) + r for r in range(1 << (m - 1))
                        if r.bit_count() == ell}))
    return result


def main():
    rng = random.Random(918202)
    checks = 0
    for m in range(2, 11):
        B = (1 << m) - 1
        S = shifts(m)
        assert len(S) == 2 * m - 1 and max(S) == B
        for d in range(1, B):
            assert not matches(m, 0, d)
            checks += 1
        witness = witness_sets(m)
        assert len(witness) == 2 * m - 1
        disjoint = set()
        for name, n, expected in witness:
            actual = {d for d in range(1, B + 1) if matches(m, n, d)}
            assert actual == expected, (m, name, actual ^ expected)
            assert disjoint.isdisjoint(actual)
            disjoint |= actual
            checks += B
        for n in range(0, 4000):
            assert any(matches(m, n, d) for d in S), (m, n)
            checks += 1
        for _ in range(700):
            n = rng.getrandbits(rng.randint(1, 180))
            assert any(matches(m, n, d) for d in S), (m, n)
            checks += 1
    print(f"VERIFY_OK moduli=9 assertions={checks}")


if __name__ == "__main__":
    main()
