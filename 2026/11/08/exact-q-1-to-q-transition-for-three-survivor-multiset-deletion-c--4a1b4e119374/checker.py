#!/usr/bin/env python3
"""Finite consistency checks for the three-survivor multiset-code theorem."""
from itertools import combinations


def profiles(total, alphabet):
    if alphabet == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in profiles(total - first, alphabet - 1):
            yield (first,) + tail


def overlap(x, y):
    return sum(min(a, b) for a, b in zip(x, y))


def outputs3(x):
    return {z for z in profiles(3, len(x)) if all(a <= b for a, b in zip(z, x))}


def pure(q, n):
    return [tuple(n if i == j else 0 for i in range(q)) for j in range(q)]


def light(q, n):
    entries = []
    for _ in range(q):
        take = min(2, n)
        entries.append(take)
        n -= take
    assert n == 0
    return tuple(entries)


def boundary(q):
    if q % 2:
        m = q // 2
        u = tuple(2 if i <= m else 0 for i in range(q))
        v = tuple(2 if i >= m else 0 for i in range(q))
    else:
        m = q // 2
        u = tuple(2 if i < m else 1 if i == m else 0 for i in range(q))
        v = tuple(2 if i >= m else 1 if i == m - 1 else 0 for i in range(q))
    return u, v


def check_code(code, n, explicit_outputs=False):
    assert len(code) == len(set(code))
    assert all(sum(x) == n for x in code)
    for x, y in combinations(code, 2):
        assert overlap(x, y) <= 2
        if explicit_outputs:
            assert outputs3(x).isdisjoint(outputs3(y))


def main():
    checked = 0
    for q in range(2, 9):
        for n in range(q + 2, 2 * q + 5):
            code = pure(q, n)
            if n <= 2 * q:
                code.append(light(q, n))
            assert len(code) == (q + 1 if n <= 2 * q else q)
            check_code(code, n, explicit_outputs=(q <= 6))
            checked += 1
            if q <= 5 and n <= 2 * q + 1:
                lights = [x for x in profiles(n, q) if max(x) <= 2]
                for x, y in combinations(lights, 2):
                    assert overlap(x, y) >= 3
        u, v = boundary(q)
        assert sum(u) == sum(v) == q + 1
        assert max(u) <= 2 and max(v) <= 2 and overlap(u, v) == 2
        check_code(pure(q, q + 1) + [u, v], q + 1, explicit_outputs=(q <= 6))
        checked += 1
    print(f"PASS: {checked} constructed code instances, exhaustive light pairs for q<=5")


if __name__ == "__main__":
    main()
