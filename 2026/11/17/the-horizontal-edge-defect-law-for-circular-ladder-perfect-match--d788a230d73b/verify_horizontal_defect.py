#!/usr/bin/env python3
"""Finite checks for horizontal-edge-defective cyclic-ladder perfect matching complexes.
Uses direct graph perfect-matching enumeration and independent GF(2) boundary elimination.
All instances and expected values below are finite corroboration, not an infinite proof.
"""
from itertools import combinations


def perfect_matchings(n, cut="top"):
    # Each vertex (row, column) has integer label 2*column+row.
    # cut='top' removes only T0; cut='both' removes T0 and B0.
    edges = {}
    for c in range(n):
        edges['R'+str(c)] = (2*c, 2*c+1)
        nxt = (c+1) % n
        if c or cut == 'none':
            edges['T'+str(c)] = (2*c, 2*nxt)
        if c or cut in ('top', 'none'):
            edges['B'+str(c)] = (2*c+1, 2*nxt+1)
    out = set()
    def recurse(available, selected):
        if not available:
            out.add(frozenset(selected))
            return
        v = min(available)
        for name, (u, w) in edges.items():
            if (v == u and w in available) or (v == w and u in available):
                recurse(available - {u, w}, selected + (name,))
    recurse(set(range(2*n)), ())
    return out


def faces(facets):
    ret = {frozenset()}
    for facet in facets:
        es = tuple(sorted(facet))
        for count in range(1, len(es)+1):
            for sub in combinations(es, count):
                ret.add(frozenset(sub))
    return ret


def path_independence_faces(names):
    # All independent subsets of a path, including the empty set.
    ans = {frozenset()}
    for i, v in enumerate(names):
        for s in tuple(ans):
            if i == 0 or names[i-1] not in s:
                ans.add(s | {v})
    return ans


def mod2_reduced_betti(complex_faces):
    ranks = {}
    bases = {}
    maxdim = max(map(len, complex_faces)) - 1
    for d in range(maxdim+1):
        bases[d] = {s: i for i, s in enumerate(sorted((f for f in complex_faces if len(f)==d+1), key=lambda x:tuple(sorted(x))))}
    for d in range(1, maxdim+1):
        pivots = {}
        for facet in bases[d]:
            column = 0
            for vertex in facet:
                column ^= 1 << bases[d-1][facet - {vertex}]
            while column:
                pivot = column.bit_length()-1
                if pivot in pivots:
                    column ^= pivots[pivot]
                else:
                    pivots[pivot] = column
                    break
        ranks[d] = len(pivots)
    result = {}
    for d in range(maxdim+1):
        dimension = len(bases[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d == 0 else 0)
        if dimension:
            result[d] = dimension
    return result


def expected(n):
    if n % 2:
        return {}
    k = n//2
    result = {k-1:1}
    if n % 6 == 0:
        result[n//3] = result.get(n//3,0)+1
    elif n % 6 == 4:
        d=(n-1)//3
        result[d] = result.get(d,0)+1
    return result


def run():
    total_facets=0
    total_simplices=0
    for n in range(3,11):
        cycle_pm=perfect_matchings(n,'top')
        path_pm=perfect_matchings(n,'both')
        extra=cycle_pm-path_pm
        assert not path_pm-cycle_pm
        cycle_faces=faces(cycle_pm)
        path_faces=faces(path_pm)
        total_facets+=len(cycle_pm)
        total_simplices+=len(cycle_faces)
        if n%2:
            assert not extra
            assert cycle_faces == path_faces
        else:
            unique=frozenset(['T'+str(i) for i in range(1,n,2)]+['B'+str(i) for i in range(0,n,2)])
            assert extra=={unique}
            extra_faces=faces(extra)
            assert cycle_faces == path_faces | extra_faces
            intersection=path_faces & extra_faces
            ordered=[]
            for i in range(1,n):
                if i%2: ordered.append('T'+str(i))
                else: ordered.append('B'+str(i))
            assert intersection == path_independence_faces(ordered)
            assert len(extra_faces) == 2**n
        result = mod2_reduced_betti(cycle_faces)
        assert result==expected(n), (n,result,expected(n))
        path_result = mod2_reduced_betti(path_faces)
        target={} if n%2 else {n//2-1:1}
        assert path_result==target, (n,path_result,target)
        print(f'n={n}: full_facets={len(cycle_pm)}; path_facets={len(path_pm)}; extra={len(extra)}; mod2={result}; decomposition=PASS')
    # Check larger n decomposition without big full boundary matrices.
    for n in (11,12,13,14):
        full=perfect_matchings(n,'top')
        path=perfect_matchings(n,'both')
        assert len(full-path)==(n%2==0)
        if n%2 == 0:
            unique=frozenset(['T'+str(i) for i in range(1,n,2)]+['B'+str(i) for i in range(0,n,2)])
            assert full-path=={unique}
        print(f'n={n}: exact_matching_partition=PASS; full_facets={len(full)}')
    print(f'finite_full_boundary_cases=8; total_full_facets={total_facets}; total_full_faces={total_simplices}')
    print('HORIZONTAL_EDGE_DEFECT_CLASSIFICATION_CHECK_PASS')


if __name__=='__main__':
    run()
