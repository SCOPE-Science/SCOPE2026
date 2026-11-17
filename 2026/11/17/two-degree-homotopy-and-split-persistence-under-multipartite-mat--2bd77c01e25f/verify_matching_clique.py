#!/usr/bin/env python3
"""Finite, independent checks for higher clique-free matching-fault complexes.

Standard-library only. Exact combinatorial face enumeration and GF(2) chain ranks;
finite checks corroborate rather than prove the unrestricted integral theorem.
"""
import itertools
from math import comb


def gf2_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            p = col.bit_length() - 1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p] = col
                break
    return len(pivots)


def all_faces(a, b, s, t, q):
    n = a + b + s
    E = set()
    for i in range(n):
        for j in range(i + 1, n):
            group_i = 0 if i < a else (1 if i < a + b else 2 + i - a - b)
            group_j = 0 if j < a else (1 if j < a + b else 2 + j - a - b)
            if group_i != group_j and not (i < t and j == a + i):
                E.add((i, j))
    faces = [[] for _ in range(n)]
    for mask in range(1, 1 << n):
        vertices = [u for u in range(n) if (mask >> u) & 1]
        direct = not any(all((u, v) in E for u, v in itertools.combinations(Q, 2))
                         for Q in itertools.combinations(vertices, q))
        A = [v for v in vertices if v < a]
        B = [v - a for v in vertices if a <= v < a + b]
        singleton_count = sum(v >= a + b for v in vertices)
        shore_count = bool(A) + bool(B) + singleton_count
        special = (shore_count == q and len(A) == len(B) == 1
                   and A[0] == B[0] and A[0] < t)
        structural = shore_count <= q - 1 or special
        assert direct == structural, (a, b, s, t, q, mask)
        if direct:
            faces[len(vertices) - 1].append(mask)
    return faces


def reduced_betti(faces):
    ranks = []
    for d in range(1, len(faces)):
        if not faces[d]:
            ranks.append(0)
            continue
        lower = {face: ix for ix, face in enumerate(faces[d - 1])}
        columns = []
        for face in faces[d]:
            column = 0
            for v in range(len(faces)):
                if (face >> v) & 1:
                    column ^= 1 << lower[face ^ (1 << v)]
            columns.append(column)
        ranks.append(gf2_rank(columns))
    result = {}
    for d, level in enumerate(faces):
        if not level:
            break
        rank_down = ranks[d - 1] if d else 1  # augmentation
        rank_up = ranks[d] if d < len(ranks) else 0
        beta = len(level) - rank_down - rank_up
        assert beta >= 0
        if beta:
            result[d] = beta
    return result


def run_case(a, b, s, c, q):
    old_faces = None
    d = comb(s, q - 2)
    h = comb(s, q - 1)
    for t in range(c + 1):
        faces = all_faces(a, b, s, t, q)
        betti = reduced_betti(faces)
        expected = ({q - 2: h + d} if t == 0 else
                    {q - 2: h, q - 1: (t - 1) * d})
        expected = {degree: rank for degree, rank in expected.items() if rank}
        assert betti == expected, (a, b, s, c, q, t, betti, expected)
        if old_faces is not None:
            old = set().union(*map(set, old_faces))
            new = set().union(*map(set, faces))
            additions = new - old
            expected_added = set()
            for chosen in itertools.combinations(range(a + b, a + b + s), q - 2):
                mask = sum(1 << u for u in chosen)
                expected_added.add(mask | (1 << (t - 1)) | (1 << (a + t - 1)))
            assert additions == expected_added
        old_faces = faces
        print(f"a={a} b={b} s={s} c={c} q={q} t={t} nonempty_faces={sum(map(len,faces))} reduced_F2_betti={betti}")


if __name__ == '__main__':
    for case in [(2, 2, 3, 2, 4), (3, 3, 3, 3, 4),
                 (3, 3, 4, 2, 4), (2, 2, 4, 2, 5)]:
        run_case(*case)
    print('MATCHING_DEFECT_CLIQUE_FREE_FINITE_PASS')
