#!/usr/bin/env python3
"""Exact finite checks for an equivariant circular-ladder matching-complex theorem.

Only the standard Python library is needed. The mathematical argument for arbitrary
lengths is in RESULT.md; computations provide independent finite checks.
"""
from functools import lru_cache
from itertools import product


def cycle_homology_character(n, j, reflection):
    """Reduced homology trace from signed invariant-independent-set enumeration.

    Intended for n divisible by six; the known concentration degree is n//3-1.
    """
    assert n % 6 == 0
    perm = [((j - i) if reflection else (j + i)) % n for i in range(n)]
    seen = set()
    orbits = []
    for i in range(n):
        if i in seen:
            continue
        o = set()
        a = i
        while a not in seen:
            seen.add(a)
            o.add(a)
            a = perm[a]
        orbits.append(o)
    allowed = [o for o in orbits if not any((i + 1) % n in o for i in o)]
    adj = []
    for i, o in enumerate(allowed):
        row = 0
        for h, p in enumerate(allowed):
            if h != i and any((v + 1) % n in p or (v - 1) % n in p for v in o):
                row |= 1 << h
        adj.append(row)

    @lru_cache(None)
    def at_minus_one(mask):
        if not mask:
            return 1
        bit = mask & -mask
        i = bit.bit_length() - 1
        return at_minus_one(mask ^ bit) - at_minus_one(mask & ~(bit | adj[i]))

    # Reduced Lefschetz number = -I(-1); homology only in degree n//3-1.
    return (-1) ** (n // 3) * at_minus_one((1 << len(allowed)) - 1)


def prism(n):
    """List edges b_i,c_i,a_i, and all perfect matchings by recursive pairing."""
    E = []
    for layer in (0, 1):
        for i in range(n):
            E.append(tuple(sorted(((layer, i), (layer, (i + 1) % n)))))
    for i in range(n):
        E.append(((0, i), (1, i)))
    inc = [[] for _ in range(2 * n)]
    for i, (a, b) in enumerate(E):
        inc[a[0] * n + a[1]].append(i)
        inc[b[0] * n + b[1]].append(i)
    PM = []

    def rec(rem, mask):
        if not rem:
            PM.append(mask)
            return
        v = min(rem)
        for i in inc[v]:
            a, b = E[i]
            u = a[0] * n + a[1]
            w = b[0] * n + b[1]
            mate = u ^ w ^ v
            if mate in rem:
                rec(rem - {v, mate}, mask | (1 << i))
    rec(set(range(2 * n)), 0)
    assert len(set(PM)) == len(PM)
    p1 = sum(1 << i for i in range(n) if i % 2 == 1) + sum(1 << (n + i) for i in range(n) if i % 2 == 0)
    p2 = sum(1 << i for i in range(n) if i % 2 == 0) + sum(1 << (n + i) for i in range(n) if i % 2 == 1)
    assert p1 in PM and p2 in PM and p1 & p2 == 0
    bad = []
    for i in range(n):
        bad += [(1 << i) | (1 << (n + (i + 1) % n)),
                (1 << (n + i)) | (1 << ((i + 1) % n))]
    def is_B(face):
        occupied = set()
        for i, (a, b) in enumerate(E):
            if face >> i & 1:
                if a in occupied or b in occupied:
                    return False
                occupied.add(a)
                occupied.add(b)
        return not any(face & pair == pair for pair in bad)
    def subs(mask):
        sub = mask
        while True:
            yield sub
            if sub == 0:
                break
            sub = (sub - 1) & mask
    return E, PM, p1, p2, is_B, subs


def face_lefschetz(faces, perm, edge_count):
    seen = set()
    orb = []
    for i in range(edge_count):
        if i in seen:
            continue
        bit = 0
        a = i
        while a not in seen:
            seen.add(a)
            bit |= 1 << a
            a = perm[a]
        orb.append(bit)
    # Reduced Lefschetz trace includes empty face in dimension -1.
    total = 0
    for face in faces:
        if all((face & b) in (0, b) for b in orb):
            total -= (-1) ** sum((face & b) != 0 for b in orb)
    return total


def small_prism_check(n):
    E, PM, p1, p2, is_B, subs = prism(n)
    allfaces = set()
    for pm in PM:
        allfaces.update(subs(pm))
    bfaces = {face for face in allfaces if is_B(face)}
    assert allfaces == bfaces | set(subs(p1)) | set(subs(p2))
    for p in (p1, p2):
        order = [i for i in range(2 * n) if p >> i & 1]
        assert len(order) == n
        for mask in range(1 << n):
            face = sum(1 << order[i] for i in range(n) if mask >> i & 1)
            # b/c edge indices ordered alternately by original cyclic coordinate.
            used = {(order[i] % n) for i in range(n) if mask >> i & 1}
            independent = all(((i + 1) % n) not in used for i in used)
            assert is_B(face) == independent
    # Test B group-invariance and the induced-character formula on the small n=6 case.
    if n == 6:
        edge_to_idx = {e: i for i, e in enumerate(E)}
        for swap, refl, rot in product((0, 1), (0, 1), range(n)):
            def vmap(v):
                a, i = v
                return (a ^ swap, (rot - i if refl else rot + i) % n)
            permutation = [edge_to_idx[tuple(sorted((vmap(a), vmap(b))))]
                           for a, b in E]
            trace_all = face_lefschetz(allfaces, permutation, len(E))
            trace_B = face_lefschetz(bfaces, permutation, len(E))
            # In degree 2, both X and B are homologically concentrated.
            trace_relative = trace_all - trace_B
            expected = ([4, 2, -2, -4, -2, 2][rot % 6]
                        if not refl and (swap - rot) % 2 == 0 else 0)
            assert trace_relative == expected, (swap, refl, rot, trace_relative, expected)
            assert {sum(1 << permutation[i] for i in range(len(E)) if f >> i & 1)
                    for f in bfaces} == bfaces
    return len(PM), len(allfaces), len(bfaces)


def main():
    for n in (6, 12, 18, 24, 30, 36, 42):
        count = 0
        for refl in (0, 1):
            for j in range(n):
                actual = cycle_homology_character(n, j, refl)
                expected = 0 if refl else [2, 1, -1, -2, -1, 1][j % 6]
                assert actual == expected, (n, refl, j, actual, expected)
                count += 1
        print('CYCLE_CHARACTER', n, count, 'PASS')
    for n in (4, 6, 8, 10):
        pm, faces, bfaces = small_prism_check(n)
        print('PRISM', n, 'perfect_matchings', pm,
              'faces_including_empty', faces, 'base_faces', bfaces, 'PASS')
    n = 12
    E, PM, p1, p2, is_B, subs = prism(n)
    assert all(is_B(pm) for pm in PM if pm not in (p1, p2))
    exceptional = set()
    for p in (p1, p2):
        for face in subs(p):
            used = {i % n for i in range(2 * n) if face >> i & 1}
            assert is_B(face) == all((i + 1) % n not in used for i in used)
            if not is_B(face):
                exceptional.add(face)
    edge_to_idx = {e: i for i, e in enumerate(E)}
    for swap, refl, rot in product((0, 1), (0, 1), range(n)):
        def vmap(v):
            a, i = v
            return (a ^ swap, (rot - i if refl else rot + i) % n)
        permutation = [edge_to_idx[tuple(sorted((vmap(a), vmap(b))))]
                       for a, b in E]
        # A genuinely separate chain-level character check, using only the
        # extra faces outside B, never the cycle-independence polynomial.
        actual = face_lefschetz(exceptional, permutation, len(E))
        expected = ([4, 2, -2, -4, -2, 2][rot % 6]
                    if not refl and (swap - rot) % 2 == 0 else 0)
        assert actual == expected, (swap, refl, rot, actual, expected)
    print('PRISM', n, 'perfect_matchings', len(PM),
          'exceptional_intersections', 2 ** n,
          'relative_chain_traces', 4 * n, 'PASS')
    print('CIRCULAR_LADDER_EQUIVARIANT_CHECKS_PASS')

if __name__ == '__main__':
    main()
