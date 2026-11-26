"""Exact finite cross-checks for the rational equivariant homology character of graph Morse complexes.

Usage: python3 verify_equivariant_k2n.py
Uses the Python standard library only. This tests bounded instances; the arbitrary-n theorem
relies on the signed-orbit proof in RESULT.md and published sphere-wedge theorem.
"""
from collections import Counter
from itertools import combinations


def forest_faces(n):
    """Exhaustively choose none/tail/head for each undirected edge, disallow directed cycles."""
    edges = [(0, i + 2) for i in range(n)] + [(1, i + 2) for i in range(n)]
    tokens = [(k, v) for k, (v, w) in enumerate(edges) for v in (v, w)]
    ti = {v: i for i, v in enumerate(tokens)}
    faces = []

    def rec(k, occupied, arrows, mask):
        if k == len(edges):
            faces.append(mask)
            return
        rec(k + 1, occupied, arrows, mask)
        u, v = edges[k]
        for src, dest in ((u, v), (v, u)):
            if src in occupied:
                continue
            z = dest
            while z in arrows and z != src:
                z = arrows[z]
            if z == src:
                continue
            arrows[src] = dest
            rec(k + 1, occupied | {src}, arrows, mask | (1 << ti[k, src]))
            del arrows[src]

    rec(0, set(), {}, 0)
    assert len(set(faces)) == len(faces)
    return edges, tokens, faces


def permutations_by_partition(n):
    def partitions(total, lo=1):
        if total == 0:
            yield ()
        for p in range(lo, total + 1):
            for rest in partitions(total - p, p):
                yield (p,) + rest
    for lengths in partitions(n):
        sigma = list(range(n))
        lo = 0
        for length in lengths:
            for j in range(length):
                sigma[lo + j] = lo + (j + 1) % length
            lo += length
        yield lengths, sigma


def formula(n, lengths, swap):
    fixed = lengths.count(1)
    two_cycles = lengths.count(2)
    sign = (-1) ** (n - len(lengths))
    return sign * ((fixed * fixed - 1) if not swap
                   else (-1) ** n * (fixed - 2 * two_cycles - 1))


def signed_lefschetz_trace(n, edges, tokens, faces, perm, swap):
    transform = lambda v: (1 - v if swap else v) if v < 2 else 2 + perm[v - 2]
    edge_lookup = {tuple(sorted(e)): i for i, e in enumerate(edges)}
    token_lookup = {t: i for i, t in enumerate(tokens)}
    vertex_map = []
    for eid, tail in tokens:
        new_edge = tuple(sorted(transform(u) for u in edges[eid]))
        vertex_map.append(token_lookup[edge_lookup[new_edge], transform(tail)])
    z = 0
    for mask in faces:
        original = [i for i in range(4 * n) if mask >> i & 1]
        image = [vertex_map[i] for i in original]
        if sorted(image) != original:
            continue
        inversions = sum(image[i] > image[j]
                         for i in range(len(image)) for j in range(i + 1, len(image)))
        z += -1 if (len(image) + inversions) % 2 else 1
    return (-1) ** (n + 1) * z


def rank_mod_two(columns):
    basis = {}
    for v in columns:
        while v:
            k = v.bit_length() - 1
            if k in basis:
                v ^= basis[k]
            else:
                basis[k] = v
                break
    return len(basis)


def reduced_betti(faces):
    by_size = {}
    for m in faces:
        by_size.setdefault(m.bit_count(), []).append(m)
    ranks = {}
    for size in range(1, max(by_size) + 1):
        smaller = {m: i for i, m in enumerate(by_size[size - 1])}
        cols = []
        for m in by_size[size]:
            vec = 0
            w = m
            while w:
                one = w & -w
                vec ^= 1 << smaller[m ^ one]
                w ^= one
            cols.append(vec)
        ranks[size] = rank_mod_two(cols)
    return {size - 1: len(group) - ranks.get(size, 0) - ranks.get(size + 1, 0)
            for size, group in sorted(by_size.items()) if size > 0}


def run():
    counts = []
    for n in range(2, 7):
        edges, tokens, faces = forest_faces(n)
        cases = 0
        for lengths, perm in permutations_by_partition(n):
            for swap in (False, True):
                actual = signed_lefschetz_trace(n, edges, tokens, faces, perm, swap)
                expected = formula(n, lengths, swap)
                assert actual == expected, (n, lengths, swap, actual, expected)
                cases += 1
        # Euler independently from face counts; identity is the predicted top homology trace.
        chi = -sum((-1) ** m.bit_count() for m in faces)
        assert chi == (-1) ** n * (n * n - 1), (n, chi)
        if n <= 5:
            betti = reduced_betti(faces)
            assert betti[n] == n * n - 1, (n, betti)
            assert all(v == 0 for k, v in betti.items() if k != n), (n, betti)
        counts.append(f'{n}:{len(faces)}faces/{cases}characters')
    print('VERIFY_OK ' + ', '.join(counts) + ', integral face enumeration and mod-2 boundaries (n<=5)')


if __name__ == '__main__':
    run()
