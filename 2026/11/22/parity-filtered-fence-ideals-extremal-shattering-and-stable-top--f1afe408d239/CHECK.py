#!/usr/bin/env python3
"""Finite independent checks for odd-fence parity-ideal shattering.

The direct trace oracle enumerates order ideals without using the theorem's
interval or rigid-label characterization. All finite assertions are exhaustive
within the stated m range, not proofs of the infinite statements.
"""
from itertools import combinations
from math import comb


def ideals(m):
    n = 2 * m + 1
    ans = []
    # A v_i bit may be set only when both neighboring u-bits are set.
    for mask in range(1 << n):
        if all(not (mask & (1 << (2*i-1))) or
               ((mask & (1 << (2*i-2))) and (mask & (1 << (2*i))))
               for i in range(1, m + 1)):
            ans.append(mask)
    return ans


def shatters(support, family):
    positions = [j for j in range(support.bit_length()) if (support >> j) & 1]
    target = 1 << len(positions)
    if len(family) < target:
        return False
    seen = set()
    for mask in family:
        trace = sum(1 << k for k, pos in enumerate(positions) if mask & (1 << pos))
        seen.add(trace)
        if len(seen) == target:
            return True
    return False


def top_candidates(m):
    n = 2*m+1
    return [sum(1 << j for j in subset)
            for subset in combinations(range(n), m)
            if all(b-a > 1 for a,b in zip(subset,subset[1:]))]


def predicted(m, parity):
    n = 2*m + 1
    mins = [2*i for i in range(m+1)]
    out = {sum(1 << x for x in mins if x != 2*j) for j in range(m+1)}
    if parity == 1:
        for r in (1,2):
            for a in range(m-r+1):
                if a <= 1 and m-a-r <= 1:
                    s = sum(1 << (2*i-1) for i in range(a+1,a+r+1))
                    s += sum(1 << (2*i) for i in range(m+1) if i<a or i>a+r)
                    out.add(s)
    return out


def rank_mod(rows, prime=1000003):
    rank = 0
    cols = len(rows[0]) if rows else 0
    for j in range(cols):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][j] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][j] % prime, -1, prime)
        rows[rank] = [(x*inv) % prime for x in rows[rank]]
        for i in range(rank+1, len(rows)):
            factor = rows[i][j] % prime
            if factor:
                rows[i] = [(a-factor*b) % prime for a,b in zip(rows[i],rows[rank])]
        rank += 1
    return rank


def top_homology_rank(facets):
    codim = sorted({s & ~(1 << x) for s in facets for x in range(s.bit_length())
                    if s & (1 << x)})
    face_index = {s:i for i,s in enumerate(codim)}
    matrix = [[0]*len(facets) for _ in codim]
    for j,facet in enumerate(facets):
        vertices = [x for x in range(facet.bit_length()) if facet & (1 << x)]
        for k,v in enumerate(vertices):
            matrix[face_index[facet & ~(1 << v)]][j] = (-1)**k
    return len(facets) - rank_mod(matrix)


def verify():
    comparisons = 0
    for m in range(1,9):
        candidates = top_candidates(m)
        fs = ideals(m)
        for parity in (0,1):
            family = [x for x in fs if x.bit_count()%2 == parity]
            actual = {s for s in candidates if shatters(s, family)}
            comparisons += len(candidates)
            expected = predicted(m, parity)
            assert actual == expected, (m, parity, actual^expected)
            assert len(actual) == m+1+(comb(3,m-1) if parity and m-1<=3 else 0)
            if m <= 5:
                expected_betti = (2 if parity and m <= 2 else 1)
                assert top_homology_rank(sorted(actual)) == expected_betti
            # Unique (m+1)-antichain, all minimal elements, is unshattered.
            all_minima = sum(1 << (2*i) for i in range(m+1))
            assert not shatters(all_minima, family)
            # All smaller supports of some predicted top support are shattered.
            for s in expected:
                assert shatters(s, family)
        print(f'm={m}, ideals={len(fs)}, top-supports even={m+1}, '
              f'odd={m+1+(comb(3,m-1) if m-1<=3 else 0)}, verified')
    print(f'PASS: {comparisons} top-antichain/parity comparisons; m=1,...,8; top boundary ranks m<=5')


if __name__ == '__main__':
    verify()
