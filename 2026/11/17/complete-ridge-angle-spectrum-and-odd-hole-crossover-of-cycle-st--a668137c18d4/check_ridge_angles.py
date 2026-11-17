"""Exact finite-dimensional checks of the cycle stable-set ridge-angle theorem.

Requires Python 3 standard library only. Enumeration verifies finite cases, not
proof for all cycle orders.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations


def independent_masks(n):
    return [a for a in range(1 << n) if all(not ((a >> i) & 1 and (a >> ((i + 1) % n)) & 1) for i in range(n))]


def rank_int_rows(rows, n, stop=None):
    """Exact rational rank; differences have integer entries."""
    piv = {}
    for row in rows:
        v = [Fraction(k) for k in row]
        for j, p in piv.items():
            if v[j]:
                a = v[j]
                v = [v[k] - a * p[k] for k in range(n)]
        j = next((k for k in range(n) if v[k]), None)
        if j is not None:
            a = v[j]
            piv[j] = [x / a for x in v]
            if stop is not None and len(piv) >= stop:
                return len(piv)
    return len(piv)


def facets(n):
    F = []
    for i in range(n):
        v = [0] * n
        v[i] = -1
        F.append(("Z", i, tuple(v), 0))
    for i in range(n):
        v = [0] * n
        v[i] = v[(i + 1) % n] = 1
        F.append(("E", i, tuple(v), 1))
    if n % 2:
        F.append(("H", 0, tuple([1] * n), (n - 1) // 2))
    return F


def expected_pair(n, a, b):
    t, i = a[:2]
    u, j = b[:2]
    if t == "Z" and u == "Z":
        return "right"
    if t == "E" and u == "E":
        if (i - j) % n in (1, n - 1):
            return "edge_obtuse"
        if n == 4 or n == 5:
            return None
        return "right"
    if t == "Z" and u == "E":
        return None if i in (j, (j + 1) % n) else "right"
    if t == "E" and u == "H":
        return "hole_obtuse"
    if t == "Z" and u == "H":
        return None
    raise AssertionError((t, u))


def check(n):
    vv = [tuple((mask >> k) & 1 for k in range(n)) for mask in independent_masks(n)]
    ff = facets(n)
    counts = Counter()
    for a, b in combinations(ff, 2):
        tight = [v for v in vv if sum(x * y for x, y in zip(a[2], v)) == a[3]
                 and sum(x * y for x, y in zip(b[2], v)) == b[3]]
        dim = -1 if not tight else rank_int_rows([[x - y for x, y in zip(v, tight[0])]
                                             for v in tight[1:]], n, stop=n-2)
        found = dim == n-2
        tag = expected_pair(n, a, b)
        assert found == (tag is not None), (n, a[:2], b[:2], dim, tag)
        if found:
            dot = sum(x * y for x, y in zip(a[2], b[2]))
            norm2a = sum(x * x for x in a[2]); norm2b = sum(x * x for x in b[2])
            if tag == "right":
                assert dot == 0
            elif tag == "edge_obtuse":
                assert dot == 1 and norm2a * norm2b == 4
            elif tag == "hole_obtuse":
                assert dot == 2 and norm2a * norm2b == 2*n
            counts[tag] += 1
    if n % 2:
        assert counts["hole_obtuse"] == n
        assert counts["edge_obtuse"] == n
        assert counts["right"] == (n * (2*n - 5) if n == 5 else 2*n*(n-2))
    else:
        assert counts["hole_obtuse"] == 0
        assert counts["edge_obtuse"] == n
        assert counts["right"] == (14 if n == 4 else 2*n*(n-2))
    return len(vv), dict(counts)


if __name__ == "__main__":
    for n in range(4, 14):
        vertex_count, counts = check(n)
        print(f"n={n} vertices={vertex_count} ridge_types={counts}")
    print("CYCLE_STAB_RIDGE_ANGLE_PASS  n=4..13  exact_rank_and_normal_products")
