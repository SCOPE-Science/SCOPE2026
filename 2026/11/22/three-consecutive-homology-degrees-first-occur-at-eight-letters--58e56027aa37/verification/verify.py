#!/usr/bin/env python3
"""Exact finite F_2 homology of perfect-matching involution word complexes.

Requires Python 3.9+, no external libraries. Every permutation and every face is
exhaustively enumerated; elimination is over integer bit vectors in F_2.
"""
from itertools import combinations
from math import prod

EXPECTED = {
    2: ([2, 1], [1, 1], [0, 0]),
    4: ([4, 12, 12, 3], [1, 3, 8, 3], [0, 1, 1, 0]),
    6: ([6, 30, 120, 186, 90, 15], [1, 5, 25, 92, 75, 15], [0, 0, 3, 19, 0, 0]),
    8: ([8, 56, 336, 1680, 3612, 2677, 840, 105],
        [1, 7, 49, 287, 1385, 1933, 735, 105],
        [0, 0, 0, 8, 294, 9, 0, 0]),
}

def all_fixed_point_free_involutions(n):
    # Invariant: partner is a symmetric partial matching on [0,n).
    def visit(rem, partner):
        if not rem:
            yield tuple(partner[x] for x in range(n))
            return
        x, rest = rem[0], rem[1:]
        for y in rest:
            partner[x] = y
            partner[y] = x
            yield from visit([z for z in rest if z != y], partner)
            del partner[x]
            del partner[y]
    yield from visit(list(range(n)), {})

def all_cells(n):
    by_len = [set() for _ in range(n)]
    permutations = list(all_fixed_point_free_involutions(n))
    assert len(permutations) == prod(range(n-1,0,-2))
    for perm in permutations:
        assert sorted(perm) == list(range(n))
        assert all(perm[perm[x]] == x and perm[x] != x for x in range(n))
        for k in range(1,n+1):
            for subs in combinations(range(n),k):
                by_len[k-1].add(tuple(perm[i] for i in subs))
    return [sorted(level) for level in by_len]

def gf2_rank(vectors, low=False):
    pivots = {}
    for vector in vectors:
        v = vector
        while v:
            p = (v & -v).bit_length() - 1 if low else v.bit_length()-1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return len(pivots)

def compute(n):
    cells=all_cells(n)
    dims=list(map(len,cells))
    # The augmented differential d_0 sends every vertex to the empty word.
    ranks=[1]
    prior_columns=[1]*len(cells[0])
    assert gf2_rank(prior_columns) == 1
    assert gf2_rank(prior_columns,low=True) == 1
    for degree in range(1,n):
        face_index={face:i for i,face in enumerate(cells[degree-1])}
        columns=[]
        for word in cells[degree]:
            v=0
            for i in range(len(word)):
                face=word[:i]+word[i+1:]
                assert face in face_index
                v ^= 1 << face_index[face]
            columns.append(v)
        # Direct chain-square verification: each twice-deleted face cancels.
        if degree == 1:
            assert all(v.bit_count() == 2 for v in columns)
        else:
            earlier_index = {w:i for i,w in enumerate(cells[degree-2])}
            for word in cells[degree]:
                twice = 0
                for i in range(len(word)):
                    once = word[:i] + word[i+1:]
                    for j in range(len(once)):
                        twice ^= 1 << earlier_index[once[:j]+once[j+1:]]
                assert twice == 0, (n, degree, word)
        hi=gf2_rank(columns)
        lo=gf2_rank(columns,low=True)
        assert hi==lo,(n,degree,hi,lo)
        ranks.append(hi)
    betti=[dims[d]-ranks[d]-(ranks[d+1] if d+1<n else 0) for d in range(n)]
    assert min(betti)>=0
    assert sum((-1)**d*dims[d] for d in range(n))-1 == sum((-1)**d*betti[d] for d in range(n))
    assert (dims,ranks,betti)==EXPECTED[n],(n,dims,ranks,betti)
    print(f'n={n} generators={prod(range(n-1,0,-2))}')
    print('  chain ranks        :',dims)
    print('  augmented d ranks  :',ranks)
    print('  reduced F2 Betti   :',betti)
    print('  pivot schemes      : high-bit and low-bit agree in every degree')
    print('  d^2                : zero by explicit two-deletion parity and augmentation')
    print('  Euler and expected : verified')

if __name__=='__main__':
    for n in (2,4,6,8):
        compute(n)
    print('PASS: exhaustive finite classification and sharp first three-degree occurrence at n=8.')
