#!/usr/bin/env python3
"""Exact small-rank and numerical-semigroup checks for rank-block dimensionalities.
No external packages required; finite checks support, rather than replace, the proof.
"""
from itertools import product


def rank_integer_binary(matrix, n):
    rows = [sum(((matrix >> (n*i+j)) & 1) << j for j in range(n)) for i in range(n)]
    piv = 0
    for j in range(n):
        ix = next((i for i in range(piv, n) if (rows[i] >> j) & 1), None)
        if ix is None:
            continue
        rows[piv], rows[ix] = rows[ix], rows[piv]
        for i in range(n):
            if i != piv and ((rows[i] >> j) & 1):
                rows[i] ^= rows[piv]
        piv += 1
        if piv == n:
            break
    return piv


def mat_mul(x, y, n):
    result = 0
    for i in range(n):
        for j in range(n):
            v = 0
            for k in range(n):
                v ^= ((x >> (n*i+k)) & 1) & ((y >> (n*k+j)) & 1)
            result |= (v << (n*i+j))
    return result


def all_partitions(n):
    parts = []
    def recur(k):
        if k == n:
            yield tuple(tuple(b) for b in parts)
            return
        for i in range(len(parts)):
            parts[i].append(k)
            yield from recur(k+1)
            parts[i].pop()
        parts.append([k])
        yield from recur(k+1)
        parts.pop()
    yield from recur(0)


def is_saturated(P, n):
    idx = {r:i for i,b in enumerate(P) for r in b}
    for A in P:
        for B in P:
            product_ranks = set()
            for a in A:
                for b in B:
                    product_ranks.update(range(max(0,a+b-n), min(a,b)+1))
            if any(set(P[idx[r]]) - product_ranks for r in product_ranks):
                return False
    return True


def is_interval_semigroup(P, n):
    if any(tuple(range(b[0],b[-1]+1)) != b for b in P):
        return False
    ends = {b[0] for b in P}
    return all(max(0,a+b-n) in ends for a in ends for b in ends)


def main():
    # Product ranks over the smallest finite field, including the full 3x3 monoid.
    for n in (2,3):
        matrices = range(2**(n*n))
        by_rank = [[] for _ in range(n+1)]
        for matrix in matrices:
            by_rank[rank_integer_binary(matrix,n)].append(matrix)
        for r in range(n+1):
            for s in range(n+1):
                seen = {rank_integer_binary(mat_mul(a,b,n),n) for a in by_rank[r] for b in by_rank[s]}
                expected = set(range(max(0,r+s-n),min(r,s)+1))
                assert seen == expected, (n,r,s,seen,expected)
        print('GF2_MATRIX_PRODUCTS_OK', n, [len(x) for x in by_rank])
    expected_counts = {2:2,3:3,4:5,5:7,6:12,7:16,8:27,9:37}
    for n, expected in expected_counts.items():
        good = [P for P in all_partitions(n) if is_saturated(P,n)]
        correct = [P for P in all_partitions(n) if is_interval_semigroup(P,n)]
        assert set(good) == set(correct), (n, set(good)^set(correct))
        assert len(good) == expected, (n,len(good),expected)
        print('PARTITION_CLASSIFICATION_OK',n,len(good))
    print('MATRIX_RANK_NUMERICAL_SEMIGROUP_CHECKS_OK')


if __name__ == '__main__':
    main()
