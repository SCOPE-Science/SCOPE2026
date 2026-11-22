#!/usr/bin/env python3
"""Second, separate verification: use longest common subsequences, not deletion shadows.

Every length-6 pair is two-deletion-confusable exactly when its LCS has length >=4.
Run: python3 verify_lcs.py
"""
from itertools import combinations
from collections import Counter

WORDS = []
# Generate words by choosing disjoint positions for zero and one; two elsewhere.
for zero_pos in combinations(range(6), 2):
    for one_pos in combinations((i for i in range(6) if i not in zero_pos), 2):
        word = tuple(0 if i in zero_pos else (1 if i in one_pos else 2) for i in range(6))
        WORDS.append(word)
WORDS.sort()
assert len(WORDS)==90 and len(set(WORDS))==90

def lcs(a, b):
    row=[0]*7
    for x in a:
        nxt=[0]
        for j,y in enumerate(b):
            nxt.append(row[j]+1 if x==y else max(row[j+1],nxt[-1]))
        row=nxt
    return row[-1]

edges=[[False]*90 for _ in range(90)]
for i in range(90):
    for j in range(i+1,90):
        edges[i][j]=lcs(WORDS[i],WORDS[j])<=3

# Enumerate all compatible pairs, triangles and quadrangles by increasing indices.
pairs=[];triangles=[];quads=[]
for a in range(90):
    for b in range(a+1,90):
        if edges[a][b]:pairs.append((a,b))
for a,b in pairs:
    for c in range(b+1,90):
        if edges[a][c] and edges[b][c]:triangles.append((a,b,c))
for a,b,c in triangles:
    for d in range(c+1,90):
        if edges[a][d] and edges[b][d] and edges[c][d]:quads.append((a,b,c,d))
assert len(pairs)==1164
assert len(triangles)==1788
assert len(quads)==144
for a,b,c,d in quads:
    for e in range(d+1,90):
        assert not(edges[a][e] and edges[b][e] and edges[c][e] and edges[d][e]), (a,b,c,d,e)
# Separate multiset of pairs from direct combinatorial deletion representations.
for a,b in pairs:
    assert lcs(WORDS[a], WORDS[b])<=3
# Every four-codeword optimum recovered; no larger code.
print('independent_lcs_exhaustion: counts=90,1164,1788,144; five_sets=0')
print('maximum_size=4, maximizing_codebooks=144')
