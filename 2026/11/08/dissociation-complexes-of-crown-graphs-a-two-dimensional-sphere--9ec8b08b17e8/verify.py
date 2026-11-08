#!/usr/bin/env python3
"""Independent finite checker for the crown-graph dissociation complex."""
from collections import Counter
from itertools import combinations
from math import comb


def actual(n):
    edges = [[False] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                edges[i][n+j] = edges[n+j][i] = True
    faces = [0]*(1 << (2*n))
    counts = Counter()
    max_counts = Counter()
    by_size = {}
    for mask in range(1 << (2*n)):
        selected = [i for i in range(2*n) if mask >> i & 1]
        okay = all(sum(edges[i][j] for j in selected if j != i) <= 1 for i in selected)
        faces[mask] = okay
        if okay:
            counts[len(selected)] += 1
            by_size.setdefault(len(selected), []).append(mask)
    for mask in range(1 << (2*n)):
        if not faces[mask]:
            continue
        ismax = not any(faces[mask | (1 << i)] for i in range(2*n) if not (mask >> i & 1))
        a = mask & ((1 << n) - 1)
        b = (mask >> n) & ((1 << n) - 1)
        criterion = (not a) or (not b) or (a.bit_count() <= 2 and b.bit_count() <= 2 and ((a | b).bit_count() <= 2))
        assert criterion, ('classification false positive', n, mask)
        if ismax:
            max_counts[mask.bit_count()] += 1
            assert (a == (1 << n)-1 and b == 0) or (b == (1 << n)-1 and a == 0) or (a == b and a.bit_count() == 2), (n, mask)
    for mask in range(1 << (2*n)):
        a = mask & ((1 << n) - 1)
        b = (mask >> n) & ((1 << n) - 1)
        predicted = (not a) or (not b) or ((a | b).bit_count() <= 2 and a.bit_count() <= 2 and b.bit_count() <= 2)
        assert faces[mask] == predicted, ('classification mismatch', n, mask)
    expected = Counter({0:1})
    for k in range(1, n+1):
        expected[k] += 2 * comb(n,k)
    expected[2] += n*n
    expected[3] += 2*n*(n-1)
    expected[4] += comb(n,2)
    expected_facets = Counter()
    expected_facets[n] += 2
    expected_facets[4] += comb(n,2)
    assert counts == expected, ('polynomial mismatch', n, counts, expected)
    assert max_counts == expected_facets, ('max facet mismatch', n, max_counts, expected_facets)
    return counts,max_counts,by_size


def rank_mod2(vectors):
    basis = {}
    for v in vectors:
        while v:
            i = v.bit_length()-1
            if i not in basis:
                basis[i] = v
                break
            v ^= basis[i]
    return len(basis)


def betti(n, by_size):
    ranks = {}
    for k in range(2,max(by_size)+1):
        previous = {mask:i for i,mask in enumerate(by_size.get(k-1, []))}
        cols=[]
        for face in by_size.get(k, []):
            col=0
            for j in range(2*n):
                if face>>j&1:
                    col |= 1 << previous[face^(1<<j)]
            cols.append(col)
        ranks[k-1] = rank_mod2(cols)
    result={}
    for k in range(1,max(by_size)+1):
        dim=k-1
        result[dim] = len(by_size.get(k,[])) - ranks.get(k-1,0) - ranks.get(k,0)
        if dim==0:
            result[dim] -= 1  # reduced H_0 for connected complexes
    result={k:v for k,v in result.items() if v}
    assert result == {2:comb(n-1,2)}, (n,result)
    return result

if __name__ == '__main__':
    total=0
    for n in range(3,9):
        counts,facets,faces=actual(n)
        total += 1<<(2*n)
        betti(n,faces)
        print(f'n={n} subsets={1<<(2*n)} faces={sum(counts.values())} facets={sum(facets.values())}')
    print(f'VERIFY_OK orders=3..8 subsets={total} face_enumerator=PASS facet_enumerator=PASS all_feasible_sets=PASS homology_mod2_n3..8=PASS')
