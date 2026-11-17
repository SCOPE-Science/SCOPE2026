#!/usr/bin/env python3
"""Exact finite checks for the three-column total three-cut theorem.

This is an independent finite test of the general proof, not a substitute for it.
Uses the ordinary graph adjacency definition to enumerate every independent
triple and every face; verifies the first-available-coordinate matching and
its full oriented face-incidence graph.
"""
from collections import Counter, deque
from itertools import combinations


def graph_independent_triples(m):
    n = 3*m
    def adjacent(u, v):
        ru, cu = u % m, u // m
        rv, cv = v % m, v // m
        return (cu == cv and ru != rv) or (ru == rv and abs(cu-cv) == 1)
    out=[]
    for tr in combinations(range(n),3):
        if not any(adjacent(u,v) for u,v in combinations(tr,2)):
            out.append(sum(1<<i for i in tr))
    return out


def complex_faces(m, triples):
    full=(1<<(3*m))-1
    facets=[full^t for t in triples]
    return {mask for mask in range(full+1) if any(mask & ~facet == 0 for facet in facets)}


def coordinate_matching(faces, m):
    remaining=set(faces)
    matched=set()
    counts=[]
    for i in range(3*m):
        b=1<<i
        pairs=[(lo,lo|b) for lo in remaining if not lo&b and (lo|b) in remaining]
        for lo,hi in pairs:
            assert lo in remaining and hi in remaining
            remaining.remove(lo)
            remaining.remove(hi)
            matched.add((lo,hi))
        counts.append(len(pairs))
    return remaining,matched,counts


def acyclic(faces, matched):
    # Reversed matched edges and unreversed nonmatched edges.
    # A directed cycle here is exactly a forbidden closed gradient path.
    forward={mask: [] for mask in faces}
    indegree={mask: 0 for mask in faces}
    incidences=0
    for hi in faces:
        x=hi
        while x:
            b=x&-x
            lo=hi^b
            assert lo in faces
            a,z=(hi,lo) if (lo,hi) in matched else (lo,hi)
            forward[a].append(z)
            indegree[z]+=1
            incidences+=1
            x-=b
    q=deque(s for s,d in indegree.items() if d==0)
    visited=0
    while q:
        v=q.popleft();visited+=1
        for w in forward[v]:
            indegree[w]-=1
            if indegree[w]==0:q.append(w)
    assert visited==len(faces), f'directed gradient cycle: visited {visited}/{len(faces)}'
    return incidences


def expected_critical(m):
    a=sum(1<<i for i in range(1,m))
    tails=list(range(1,m))
    out=set()
    for b_missing in tails:
        for c_missing in tails:
            b=sum(1<<(m+i) for i in tails if i!=b_missing)
            c=sum(1<<(2*m+i) for i in tails if i!=c_missing)
            out.add(a|b|c)
    return out


def run():
    for m in range(2,6):
        triples=graph_independent_triples(m)
        assert len(triples)==m*(m-1)**2
        faces=complex_faces(m, triples)
        rem,matched,stage=coordinate_matching(faces,m)
        expect=expected_critical(m)
        assert rem==expect,(m,rem^expect)
        assert all(s.bit_count()==3*m-5 for s in rem)
        assert len(matched)*2+len(rem)==len(faces)
        incidences=acyclic(faces,matched)
        # The empty face is in a matched pair, yielding the standard base point.
        assert any(lo==0 for lo,_ in matched)
        print(f'm={m}: independent_triples={len(triples)}, faces_including_empty={len(faces)}, '
              f'matched_pairs={len(matched)}, incidences={incidences}, '
              f'critical_{3*m-6}_cells={len(rem)}, all_checks=PASS')
    print('THREE_COLUMN_TOTAL_THREE_CUT_MORSE_PASS')

if __name__=='__main__':run()
