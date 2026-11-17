#!/usr/bin/env python3
"""Standalone finite base certificate for a pentagonal bouquet robust clique theorem.

Python 3 standard library only.  All graph and face data are reconstructed here.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb

PIVOTS = (0, 6, 3, 2, 1, 7, 4, 5, 8)


def graph(m):
    assert m >= 1
    edges = set()
    for i in range(m):
        a, b, c, d = (1 + 4*i + j for j in range(4))
        for x, y in ((0,a), (a,b), (b,c), (c,d), (d,0)):
            edges.add(tuple(sorted((x,y))))
    return 1 + 4*m, edges


def robust_faces(m):
    n, edges = graph(m)
    nonedges3 = []
    for triple in combinations(range(n), 3):
        if not any(tuple(sorted(pair)) in edges for pair in combinations(triple, 2)):
            nonedges3.append(sum(1<<v for v in triple))
    accepted = []
    for mask in range(1, 1<<n):
        if not any(mask & tri == tri for tri in nonedges3):
            accepted.append(mask)
    return accepted


def morse_certificate(faces):
    universe = set(faces)
    remaining = set(faces)
    matched = set()
    pairs=[]
    for pivot in PIVOTS:
        bit=1<<pivot
        for lo in faces:
            hi=lo|bit
            if not lo&bit and lo in remaining and hi in remaining:
                assert hi in universe
                remaining.remove(lo);remaining.remove(hi)
                pairs.append((lo,hi))
                matched.add((lo,hi))
    # Hasse relation orientation: unmatched high->low, matched low->high.
    arcs = {f:[] for f in faces}
    indegree = dict.fromkeys(faces, 0)
    edge_count=0
    for hi in faces:
        for v in range(hi.bit_length()):
            if hi & (1<<v):
                lo=hi^(1<<v)
                if lo not in universe:
                    continue
                if (lo,hi) in matched:
                    u,w=lo,hi
                else:
                    u,w=hi,lo
                arcs[u].append(w)
                indegree[w]+=1
                edge_count+=1
    dq=deque([f for f in faces if indegree[f]==0])
    visited=0
    while dq:
        u=dq.popleft()
        visited+=1
        for w in arcs[u]:
            indegree[w]-=1
            if indegree[w]==0:
                dq.append(w)
    assert visited==len(faces), 'Morse Hasse matching is cyclic'
    assert remaining=={1, 390}, ('unexpected critical cells',remaining)
    assert len(pairs)==66
    assert sorted(Counter(f.bit_count()-1 for f in remaining).items())==[(0,1),(3,1)]
    return len(pairs), edge_count, visited


def trace_on_top(faces, permutation):
    # Reduced Lefschetz = alternating signed trace on nonempty chains - 1.
    reduced = -1
    for f in faces:
        vertices=[v for v in range(len(permutation)) if f&(1<<v)]
        image=[permutation[v] for v in vertices]
        if set(vertices)!=set(image):
            continue
        inversions=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
        reduced+= (-1)**(len(vertices)-1+inversions)
    return -reduced  # only degree-3 reduced homology, because of Morse matching


def main():
    for m in range(1,5):
        faces=robust_faces(m)
        c=Counter(f.bit_count()-1 for f in faces)
        expected=(4*m+1, 10*m+16*comb(m,2), 10*m+36*comb(m,2),
                  5*m+21*comb(m,2), m)
        got=tuple(c.get(j,0) for j in range(5))
        assert got==expected,(m,got,expected)
        assert max(c.keys())==4
        print('m=%d n=%d f=%s'%(m,4*m+1,got))
    faces=robust_faces(2)
    a,b,c=morse_certificate(faces)
    print('base_morse matched_pairs=%d hasse_edges=%d DAG_vertices=%d critical=(vertex,3-cell)'%(a,b,c))
    identity=tuple(range(9))
    petal_swap=(0,5,6,7,8,1,2,3,4)
    first_reflect=(0,4,3,2,1,5,6,7,8)
    second_reflect=(0,1,2,3,4,8,7,6,5)
    results=[trace_on_top(faces,perm) for perm in (identity,petal_swap,first_reflect,second_reflect)]
    assert results==[1,1,-1,-1],results
    print('H3_trace identity=%d swap=%d reflect_first=%d reflect_second=%d'%tuple(results))
    print('PENTAGON_BOUQUET_ROBUST_CERTIFICATE_PASS')

if __name__=='__main__':
    main()
