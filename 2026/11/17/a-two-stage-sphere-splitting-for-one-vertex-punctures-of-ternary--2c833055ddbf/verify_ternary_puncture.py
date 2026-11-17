#!/usr/bin/env python3
"""Independent finite checks for a ternary Hamming neighborhood-complex splitting.

Only finite enumerations are performed; the all-dimension theorem uses the
separate combinatorial null-attachment proof.
"""
from itertools import product, combinations
from collections import defaultdict


def dist(x, y):
    return sum(a != b for a, b in zip(x, y))


def complex_faces(d, puncture):
    points = list(product(range(3), repeat=d))
    if puncture:
        points.remove((0,) * d)
    near = {w: set(z for z in points if dist(w, z) == 1) for w in points}
    faces = defaultdict(set)
    for S in near.values():
        for length in range(1, len(S) + 1):
            faces[length - 1].update(frozenset(c) for c in combinations(S, length))
    return points, near, faces


def binary_rank(columns):
    pivots = {}
    for column in columns:
        while column:
            lead = column.bit_length() - 1
            if lead in pivots:
                column ^= pivots[lead]
            else:
                pivots[lead] = column
                break
    return len(pivots)


def mod2_betti(faces):
    ff = {k: tuple(sorted(v, key=lambda f: tuple(sorted(f)))) for k, v in faces.items()}
    ranks = {}
    for k in sorted(ff):
        if k == 0:
            continue
        labels = {s: i for i, s in enumerate(ff[k - 1])}
        cols = []
        for s in ff[k]:
            mask = 0
            for x in s:
                mask ^= 1 << labels[s - {x}]
            cols.append(mask)
        ranks[k] = binary_rank(cols)
    betti = {k: len(ff[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0) for k in ff}
    betti[0] -= 1
    return [len(ff[k]) for k in sorted(ff)], [betti[k] for k in sorted(ff)]


def local_certificates(d):
    zero = (0,) * d
    words = list(product(range(3), repeat=d))
    N = {w: set(z for z in words if dist(w, z) == 1) for w in words}
    S = tuple(w for w in words if dist(w, zero) == 1)
    index = {w: next(i for i, x in enumerate(w) if x) for w in S}
    edges = {(a, b) for a, b in combinations(S, 2) if index[a] != index[b]}
    g = len(edges) - len(S) + 1
    assert g == 2*d*(d-2)+1
    link_pieces = {a: N[a] - {zero} for a in S}
    for a, b in combinations(S, 2):
        J = link_pieces[a] & link_pieces[b]
        assert len(J) == (1 if index[a] != index[b] else 0)
    for a,b,c in combinations(S,3):
        assert not (link_pieces[a] & link_pieces[b] & link_pieces[c])
        if len({index[a],index[b],index[c]}) != 3:
            continue
        # Attach a triangle across three distinct coordinate directions.
        T = tuple((a[i] or b[i] or c[i]) for i in range(d))
        assert T != zero
        for x,y in ((a,b),(b,c),(c,a)):
            U = tuple(x[i] or y[i] for i in range(d))
            assert U != zero and {x,y,T} <= N[U]
        # The dual link triangle has vertices at three pairwise joins.
        p_ab = tuple(a[i] or b[i] for i in range(d))
        p_bc = tuple(b[i] or c[i] for i in range(d))
        p_ca = tuple(c[i] or a[i] for i in range(d))
        assert {p_ab,p_bc,p_ca} <= N[T]
    return g, len(edges)


def main():
    for d in range(3,7):
        g, e = local_certificates(d)
        print(f'local d={d}: 2d={2*d} edges={e} cycle_rank={g} sphere_loss={2*g} PASS')
    for d in (2,3,4):
        full, _, A = complex_faces(d, False)
        punct, _, B = complex_faces(d, True)
        fv, bh = mod2_betti(A)
        pv, bp = mod2_betti(B)
        print(f'global d={d}: full_f={fv} punct_f={pv} full_reduced_beta={bh} punct_reduced_beta={bp}')
        if d >= 3:
            g = 2*d*(d-2)+1
            assert bh[1] == bp[1] == d
            assert bh[2] - bp[2] == 2*g
            assert all(x == 0 for x in bh[3:]+bp[3:])
            print(f'homology d={d}: first_homology_unchanged={d}, second_homology_loss={2*g} PASS')
        else:
            assert (bh[1], bp[1], bh[2], bp[2]) == (2,3,1,0)
            print('boundary d=2: distinct behavior PASS')
    print('TERNARY_PUNCTURE_FINITE_CHECK_PASS')

if __name__ == '__main__':
    main()
