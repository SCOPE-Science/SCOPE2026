#!/usr/bin/env python3
"""Exact finite checks of the two cyclic forbidden subposets for cycle-plus-tail Morse complexes.

The all-n statement is proved separately by a fixed three-incidence link analysis;
finite checks here do not establish the unbounded claim.
"""
from collections import defaultdict


def enumerate_fields(n, tail):
    assert n >= 3 and tail in (1, 2)
    edges = [(i, (i+1) % n) for i in range(n)]
    edges += [(0, n)]
    if tail == 2:
        edges += [(n, n+1)]
    incidences = [(v, j) for j, (a,b) in enumerate(edges) for v in (a,b)]
    positives = [(i, i) for i in range(n)]
    negatives = [((i+1)%n, i) for i in range(n)]
    cyc = [frozenset(positives), frozenset(negatives)]
    result = {frozenset()}
    def extend(face, options):
        for k, (v,e) in enumerate(options):
            if any(v == u or e == f for u,f in face):
                continue
            new = face | {(v,e)}
            result.add(frozenset(new))
            extend(new, options[k+1:])
    extend(set(), incidences)
    return result, cyc, incidences


def boundary_matrix(faces_d, faces_prev):
    lookup = {f:i for i,f in enumerate(faces_prev)}
    out = [[0]*len(faces_d) for _ in faces_prev]
    for j, face in enumerate(faces_d):
        for k, atom in enumerate(sorted(face)):
            sub = frozenset(set(face)-{atom})
            if sub in lookup:
                out[lookup[sub]][j] = (-1)**k
    return out


def matmul(A,B):
    if not A or not B:
        return []
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def main():
    total = 0
    for n in range(3, 11):
        for tail in (1, 2):
            K, cycles, incidences = enumerate_fields(n, tail)
            forbidden = {f for f in K if any(set(c)<=f for c in cycles)}
            part = []
            assert not any(set(cycles[0])<=f and set(cycles[1])<=f for f in K)
            for cycle in cycles:
                cofaces = {f for f in forbidden if set(cycle)<=f}
                part.append(cofaces)
            assert part[0].isdisjoint(part[1])
            assert part[0]|part[1] == forbidden
            expected = {n: (1 if tail==1 else 1), n+1:(0 if tail==1 else 3), n+2:(0 if tail==1 else 1)}
            if tail==1:
                expected = {n:1,n+1:1}
            for orient, block in enumerate(part):
                counts = {k:sum(len(f)==k for f in block) for k in expected}
                assert counts == expected, (n,tail,orient,counts)
                faces_by_size = {k:sorted((f for f in block if len(f)==k), key=lambda z: sorted(z)) for k in expected}
                if tail==1:
                    d = boundary_matrix(faces_by_size[n+1],faces_by_size[n])
                    assert d == [[1]] or d == [[-1]]
                else:
                    d_lo = boundary_matrix(faces_by_size[n+1],faces_by_size[n])
                    d_hi = boundary_matrix(faces_by_size[n+2],faces_by_size[n+1])
                    assert len(d_lo)==1 and len(d_lo[0])==3 and len(d_hi)==3 and len(d_hi[0])==1
                    assert matmul(d_lo,d_hi)==[[0]]
                    assert sorted(abs(k) for k in d_lo[0]) == [1,1,1]
                    assert sorted(abs(k[0]) for k in d_hi) == [0,1,1]
                    # First differential has primitive image Z and second has primitive image
                    # inside kernel Z^2, leaving H_n = Z and no torsion.
                total += len(block)
            print(f'n={n:2d} tail={tail}: generalized={len(K)} excluded={len(forbidden)} relative cells per orientation={counts} verified')
    print(f'PASS: 16 exhaustive finite configurations, {total} forbidden faces, exact integral relative differentials.')

if __name__ == '__main__':
    main()
