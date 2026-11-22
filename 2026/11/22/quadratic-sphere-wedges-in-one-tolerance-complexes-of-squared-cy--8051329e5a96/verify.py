#!/usr/bin/env python3
"""Exact finite checks of a three-stage simplicial collapse for squared cycles.

All faces are represented as tuples of sorted vertex labels. No external packages.
"""
from itertools import combinations
from math import comb


def faces(n):
    edge_set = {tuple(sorted((i, (i+d)%n))) for i in range(n) for d in (1,2)}
    triangles = {tuple(sorted((i, (i+1)%n, (i+2)%n))) for i in range(n)}
    f2 = {t for t in combinations(range(n), 3)
          if any(tuple(sorted(e)) in edge_set for e in combinations(t, 2))}
    f3 = {tuple(sorted((*t, j))) for t in triangles
          for j in range(n) if j not in t}
    return f2, f3


def test_collapse(n):
    f2, f3 = faces(n)
    assert len(f2) == n*(2*n-9), (n, len(f2))
    assert len(f3) == n*(n-4), (n, len(f3))
    remaining_2 = set(f2)
    remaining_3 = set(f3)
    stage_counts = [0, 0, 0]

    def remove(tet, triangle, stage):
        tet = tuple(sorted(set(tet)))
        triangle = tuple(sorted(set(triangle)))
        assert len(tet) == 4 and len(triangle) == 3 and set(triangle).issubset(tet)
        assert tet in remaining_3 and triangle in remaining_2, (n, stage, tet, triangle)
        incidents = [f for f in remaining_3 if set(triangle).issubset(f)]
        assert incidents == [tet], (n, stage, tet, triangle, incidents)
        remaining_3.remove(tet)
        remaining_2.remove(triangle)
        stage_counts[stage] += 1

    for i in range(n):
        excluded = {(i+d)%n for d in (-2,-1,0,1,2,3,4)}
        for j in range(n):
            if j not in excluded:
                remove(((i)%n, (i+1)%n, (i+2)%n, j),
                       (i%n, (i+2)%n, j), 0)
    for i in range(n):
        remove(((i-2)%n, i%n, (i+1)%n, (i+2)%n),
               ((i-2)%n, (i+1)%n, (i+2)%n), 1)
    for i in range(n):
        remove((i%n, (i+1)%n, (i+2)%n, (i+4)%n),
               (i%n, (i+1)%n, (i+4)%n), 1)
    for i in range(n):
        remove((i%n, (i+1)%n, (i+2)%n, (i+3)%n),
               (i%n, (i+1)%n, (i+3)%n), 2)
    assert not remaining_3
    assert stage_counts == [n*(n-7), 2*n, n], (n, stage_counts)
    assert len(remaining_2) == len(f2)-len(f3)
    rank = len(remaining_2)-comb(n-1,2)
    assert rank == (n*n-7*n-2)//2
    return rank, stage_counts, len(f2), len(f3)


def independent_boundary_rank_mod_two(n):
    f2, f3 = faces(n)
    ordered_f2 = sorted(f2)
    ids = {t: i for i,t in enumerate(ordered_f2)}
    pivots = {}
    for tet in sorted(f3):
        v = 0
        for t in combinations(tet, 3):
            v ^= 1 << ids[t]
        while v:
            p = v.bit_length()-1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    assert len(pivots) == len(f3), (n, len(pivots), len(f3))
    return len(pivots)


def main():
    for n in range(9, 31):
        rank, stage_counts, f2, f3 = test_collapse(n)
        if n <= 16:
            boundary_rank = independent_boundary_rank_mod_two(n)
            assert boundary_rank == f3
        print('n=%d f2=%d f3=%d stage_counts=%s beta2=%d%s' %
              (n, f2, f3, stage_counts, rank,
               ' F2_boundary_rank=%d' % boundary_rank if n<=16 else ''))
    print('PASS: 22 full exact simplicial-collapse checks and eight independent mod-2 boundary ranks.')


if __name__ == '__main__':
    main()
