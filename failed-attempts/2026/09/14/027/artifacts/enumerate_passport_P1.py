"""Exhaustive enumeration for the genus-0 degree-12 Belyi passport
P1 = (2^6, 3^4, 5-4-2-1).

Question: do permutations (s0, s1, sinf) in S12 exist with
  ctype(s0) = (2,2,2,2,2,2), ctype(s1) = (3,3,3,3),
  ctype(s0*s1) = (5,4,2,1)   [sinf = (s0*s1)^{-1} has the same cycle type]?

Method: two independent conjugacy normalizations.
  A. Fix s0 = (0 1)(2 3)(4 5)(6 7)(8 9)(10 11); enumerate all 246400
     distinct elements of class 3^4 (set partitions of {0..11} into 4
     labelled triples); record ctype(s0*s1).
  B. Fix s1 = (0 1 2)(3 4 5)(6 7 8)(9 10 11); enumerate all 10395
     fixed-point-free involutions (perfect matchings); record ctype(s0*s1).

Both normalizations are valid: any triple is simultaneously conjugate to
one with s0 (resp. s1) in the chosen canonical form, and conjugation
preserves every cycle type. Both report ZERO hits for (5,4,2,1).

Usage: python3 enumerate_passport_P1.py
Requires: only the Python standard library. Deterministic.
"""
import itertools
import time
from collections import Counter


def compose(a, b):
    """Product (a*b)(i) = a[b[i]] (apply b, then a)."""
    return [a[b[i]] for i in range(len(a))]


def ctype(p):
    n = len(p)
    vis = [False] * n
    lens = []
    for i in range(n):
        if not vis[i]:
            j = i
            length = 0
            while not vis[j]:
                vis[j] = True
                j = p[j]
                length += 1
            lens.append(length)
    return tuple(sorted(lens, reverse=True))


def gen_s1_triples(rem):
    """Yield all oriented triple decompositions of the remaining set."""
    rem = sorted(rem)
    if not rem:
        yield []
        return
    a = rem[0]
    rest = rem[1:]
    for b, c in itertools.combinations(rest, 2):
        nr = [x for x in rest if x != b and x != c]
        for tail in gen_s1_triples(nr):
            yield [(a, b, c)] + tail
            yield [(a, c, b)] + tail


def gen_matchings(rem):
    """Yield all perfect matchings (pair lists) of the remaining set."""
    rem = sorted(rem)
    if not rem:
        yield []
        return
    a = rem[0]
    for b in rem[1:]:
        nr = [x for x in rem if x != a and x != b]
        for tail in gen_matchings(nr):
            yield [(a, b)] + tail


def run_A():
    s0 = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]
    assert ctype(s0) == (2,) * 6
    target = (5, 4, 2, 1)
    n = 0
    hits = 0
    dist = Counter()
    seen = set()
    t0 = time.time()
    for trips in gen_s1_triples(set(range(12))):
        s1 = [-1] * 12
        for (x, y, z) in trips:
            s1[x] = y
            s1[y] = z
            s1[z] = x
        t = tuple(s1)
        assert t not in seen, "duplicate s1 generated"
        seen.add(t)
        n += 1
        ct = ctype(compose(s0, s1))
        assert ct == ctype(compose(s1, s0)), "ab/ba type mismatch"
        dist[ct] += 1
        if ct == target:
            hits += 1
    dt = time.time() - t0
    print("=== Normalization A: s0 fixed, all s1 of type 3^4 ===")
    print("distinct s1 enumerated:", n, "(expected 246400)")
    assert n == 246400, n
    assert len(seen) == 246400
    print("hits with ctype(s0*s1) = (5,4,2,1):", hits)
    assert hits == 0
    print("full product-type distribution (%d distinct types):" % len(dist))
    for k in sorted(dist):
        print("  ", k, dist[k])
    assert sum(dist.values()) == 246400
    print("elapsed: %.1fs" % dt)
    return hits


def run_B():
    s1 = [-1] * 12
    for base in (0, 3, 6, 9):
        s1[base] = base + 1
        s1[base + 1] = base + 2
        s1[base + 2] = base
    assert ctype(s1) == (3, 3, 3, 3)
    target = (5, 4, 2, 1)
    n = 0
    hits = 0
    dist = Counter()
    seen = set()
    t0 = time.time()
    for pairs in gen_matchings(set(range(12))):
        s0 = [-1] * 12
        for (a, b) in pairs:
            s0[a] = b
            s0[b] = a
        t = tuple(s0)
        assert t not in seen, "duplicate s0 generated"
        seen.add(t)
        n += 1
        ct = ctype(compose(s0, s1))
        dist[ct] += 1
        if ct == target:
            hits += 1
    dt = time.time() - t0
    print("=== Normalization B: s1 fixed, all s0 of type 2^6 ===")
    print("distinct s0 enumerated:", n, "(expected 10395)")
    assert n == 10395, n
    assert len(seen) == 10395
    print("hits with ctype(s0*s1) = (5,4,2,1):", hits)
    assert hits == 0
    print("full product-type distribution (%d distinct types):" % len(dist))
    for k in sorted(dist):
        print("  ", k, dist[k])
    assert sum(dist.values()) == 10395
    assert (5, 4, 2, 1) not in dist
    print("elapsed: %.1fs" % dt)
    return hits


if __name__ == "__main__":
    a = run_A()
    b = run_B()
    print("RESULT: target type (5,4,2,1) occurs", a + b, "times in",
          246400 + 10395, "products. Passport P1 has NO triple; it is unrealizable.")
