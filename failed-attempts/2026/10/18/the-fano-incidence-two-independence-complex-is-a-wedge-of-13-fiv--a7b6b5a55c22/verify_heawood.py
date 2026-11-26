#!/usr/bin/env python3
"""Complete finite simplicial discrete-Morse certificate for the Fano incidence graph.

Only Python's standard library is used. Vertex bits 0..6 are Fano points,
vertex bits 7..13 are Fano lines. Incidence: p = l,l+1,l+3 modulo 7.
"""
from collections import defaultdict, deque

N = 14
ORDER = (11, 2, 10, 9, 7, 1, 12, 13, 8, 0, 4, 3, 6, 5)
EXPECT_F = (14,91,322,651,728,392,58)
EXPECT_CRITICAL = (2048,363,377,627,4697,5057,8314,8664,9058,12345,12593,12712,13065,13842)


def construct():
    adj = [0]*N
    for line in range(7):
        for offset in (0,1,3):
            point = (line+offset)%7
            adj[point] |= 1 << (7+line)
            adj[7+line] |= 1 << point
    # Form the entire simplicial complex by independently examining all
    # nonempty vertex subsets; max induced degree <=1 is equivalent to
    # all induced connected components having cardinality <=2.
    faces = []
    for mask in range(1,1 << N):
        if all(not(mask & (1 << v)) or (adj[v]&mask).bit_count() <= 1
               for v in range(N)):
            faces.append(mask)
    return faces


def verify():
    faces = construct()
    fs = set(faces)
    vector = tuple(sum(x.bit_count() == d+1 for x in faces) for d in range(7))
    assert vector == EXPECT_F, vector
    for upper in faces:
        for v in range(N):
            if upper & (1 << v):
                lower = upper ^ (1 << v)
                assert lower == 0 or lower in fs
    remaining = set(faces)
    paired = []
    for v in ORDER:
        bit = 1 << v
        for low in sorted(x for x in remaining if not x & bit):
            high = low | bit
            if high in remaining:
                paired.append((low, high))
                remaining.remove(low)
                remaining.remove(high)
    assert len(paired) == 1121, len(paired)
    assert len(remaining) == 14
    assert sorted(remaining, key=lambda x:(x.bit_count(), x)) == list(EXPECT_CRITICAL)
    c = defaultdict(int)
    for x in remaining:c[x.bit_count()-1]+=1
    assert dict(c) == {0:1,5:13}, c
    # Independent complete DAG reconstruction. Every cover upper>lower is
    # downwards, except the 1121 matched covers, which point upwards.
    reverse = set(paired)
    indeg = {face:0 for face in faces}
    edges = {face: [] for face in faces}
    covers = 0
    for upper in faces:
        for bitno in range(N):
            bit = 1 << bitno
            if not upper & bit:continue
            low = upper ^ bit
            if low == 0:continue
            covers += 1
            if (low,upper) in reverse:src,dst=low,upper
            else:src,dst=upper,low
            edges[src].append(dst)
            indeg[dst]+=1
    assert covers == 10150,covers
    q=deque(f for f in faces if indeg[f]==0)
    visited=0
    while q:
        x=q.popleft();visited+=1
        for y in edges[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    assert visited == len(faces), (visited,len(faces))
    # Separate exact boundary rank computation over GF(2).
    layers={d:[f for f in faces if f.bit_count()==d+1] for d in range(7)}
    ranks={0:0,7:0}
    for d in range(1,7):
        rows={m:i for i,m in enumerate(layers[d-1])}
        pivots={}
        for m in layers[d]:
            x=0
            for j in range(N):
                if m & (1<<j):x^=1<<rows[m ^ (1<<j)]
            while x:
                i=x.bit_length()-1
                if i in pivots:x^=pivots[i]
                else:pivots[i]=x;break
        ranks[d]=len(pivots)
    assert tuple(ranks[d] for d in range(1,7))==(13,78,244,407,321,58)
    betti={d:len(layers[d])-ranks[d]-ranks[d+1]-(d==0)
           for d in range(7)}
    assert betti=={0:0,1:0,2:0,3:0,4:0,5:13,6:0}
    print('INCIDENCE FANO: 14 vertices / 21 graph edges / all 16383 nonempty subsets tested')
    print('SIMPLICIAL F-VECTOR:',vector, 'total',len(faces))
    print('MATCHING PAIRS:',len(paired),'UNMATCHED:',len(remaining),
          'critical by dimension:',dict(c))
    print('COVER RELATIONS:',covers,'ACYCLICITY TOPOLOGICAL SORT:',visited,'/',len(faces))
    print('MOD2 BOUNDARY RANKS:',[ranks[d] for d in range(1,7)])
    print('MOD2 REDUCED BETTI NUMBERS:',tuple(betti[d] for d in range(7)))
    print('INTEGRAL HOMOTOPY TYPE: wedge of 13 five-spheres (discrete-Morse CW)')
    print('VERIFY_OK')

if __name__=='__main__':verify()
