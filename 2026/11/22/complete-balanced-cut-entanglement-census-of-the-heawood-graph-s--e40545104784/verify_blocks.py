#!/usr/bin/env python3
"""Independent exact Fano design and block-rank verifier.
Constructs cyclic Fano lines rather than vector-dot lines, then computes
ranks of two independent square matrices instead of the 14x14 cross-cut.
"""
from itertools import combinations
from collections import defaultdict

N = 7
LINES = [frozenset({i, (i+1)%N, (i+3)%N}) for i in range(N)]
assert len(set(LINES)) == N
assert all(sum(p in L for L in LINES) == 3 for p in range(N))
assert all(sum(p in L and q in L for L in LINES) == 1 for p,q in combinations(range(N), 2))

# Standard modular Gaussian elimination using list-of-list arrays.
def rank_mod2(entries):
    rows = [list(map(int, row)) for row in entries]
    if not rows:
        return 0
    col_count = len(rows[0]);row_count=len(rows)
    where = 0
    for col in range(col_count):
        j = next((j for j in range(where,row_count) if rows[j][col]),None)
        if j is None:continue
        rows[where],rows[j]=rows[j],rows[where]
        for k in range(row_count):
            if k != where and rows[k][col]:
                for t in range(col,col_count):rows[k][t] ^= rows[where][t]
        where+=1
        if where==row_count:break
    return where

counts = defaultdict(int)
by_count = defaultdict(int)
for a in range(8):
    for points_a in combinations(range(N), a):
        points_b = sorted(set(range(N))-set(points_a))
        for lines_a in combinations(range(N), N-a):
            lines_b = sorted(set(range(N))-set(lines_a))
            # Cut matrix is permutation-equivalent to diag(A,B).
            block1 = [[int(p in LINES[l]) for l in lines_b] for p in points_a]
            block2 = [[int(p in LINES[l]) for l in lines_a] for p in points_b]
            entropy = rank_mod2(block1)+rank_mod2(block2)
            counts[entropy]+=1
            by_count[(a,entropy)]+=1
assert dict(counts) == {4:100,5:980,6:1680,7:672},counts
EXPECTED={
 0:{4:1},1:{4:28,5:21},2:{4:21,5:252,6:168},
 3:{5:217,6:672,7:336},4:{5:217,6:672,7:336},
 5:{4:21,5:252,6:168},6:{4:28,5:21},7:{4:1}}
for a, vals in EXPECTED.items():
    assert {r:v for (aa,r),v in by_count.items() if aa==a}==vals, (a,by_count)
assert sum(counts.values()) == 3432
print('BLOCKS_OK histogram='+str(sorted(counts.items())))
print('BLOCKS_BY_POINTS='+str(sorted(by_count.items())))
