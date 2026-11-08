#!/usr/bin/env python3
"""Exact finite checks accompanying the induced eight-cycle cut-complex theorem.

No dependencies beyond the Python standard library.
"""
from itertools import combinations
from math import ceil


def adjacency(n, p, x, y):
    d = abs(x-y)
    return x != y and min(d, n-d) <= p


def rank_mod2(columns):
    pivots = {}
    for col in columns:
        v = col
        while v:
            pivot = v.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = v
                break
            v ^= pivots[pivot]
    return len(pivots)


def boundary_rank(lower_faces, upper_faces):
    dictionary = {s:i for i, s in enumerate(lower_faces)}
    columns = []
    for s in upper_faces:
        vector = 0
        for t in combinations(s, len(s)-1):
            vector ^= 1 << dictionary[t]
        columns.append(vector)
    return rank_mod2(columns)


def validate_seed():
    n, p = 8, 2
    all_faces = [list(combinations(range(n), k)) for k in range(n+1)]
    disconnected = {t for t in all_faces[3]
                    if sum(adjacency(n, p, a, b) for a, b in combinations(t,2)) < 2}
    # Alexander dual of the ordinary three-cut complex:
    dual = [[] for _ in range(n+1)]
    for k in range(n+1):
        dual[k] = [s for s in all_faces[k] if not any(set(t).issubset(s) for t in disconnected)]
    counts = [len(c) for c in dual]
    assert counts == [1,8,28,32,10,0,0,0,0], counts
    dual_ranks = [boundary_rank(dual[k-1], dual[k]) for k in range(1,5)]
    assert dual_ranks == [1,7,21,10], dual_ranks
    # Every one of the 10 tetrahedra has a triangle in no other tetrahedron.
    for four in dual[4]:
        assert any(sum(set(t).issubset(s) for s in dual[4]) == 1
                   for t in combinations(four,3))
    dual_h2 = len(dual[3]) - dual_ranks[2] - dual_ranks[3]
    assert dual_h2 == 1
    # Direct, independent homology computation of the actual cut complex.
    cut = [[] for _ in range(n-2)]
    for k in range(n-2):
        cut[k] = [s for s in all_faces[k]
                  if any(set(t).isdisjoint(s) for t in disconnected)]
    cut_counts = [len(c) for c in cut]
    cut_ranks = [boundary_rank(cut[k-1], cut[k]) for k in range(1,len(cut))]
    cut_betti = [len(cut[k]) - (cut_ranks[k-1] if k else 0)
                 - (cut_ranks[k] if k < len(cut_ranks) else 0)
                 for k in range(len(cut))]
    assert cut_counts == [1,8,28,56,60,24],cut_counts
    assert cut_ranks == [1,7,21,35,24],cut_ranks
    assert cut_betti == [0,0,0,0,1,0], cut_betti
    print('SEED_OK dual_faces='+str(counts[:5])+
          ' dual_boundary_ranks='+str(dual_ranks)+
          ' cut_faces='+str(cut_counts)+
          ' cut_boundary_ranks='+str(cut_ranks)+
          ' reduced_cut_betti_dimension_3=1')


def validate_band():
    cases=0
    for p in range(2,81):
        low=ceil(8*(p+1)/3)
        for n in range(low,4*p+1):
            verts=[(j*n)//8 for j in range(8)]
            assert len(set(verts))==8
            for i,j in combinations(range(8),2):
                should=min(j-i,8-(j-i))<=2
                got=adjacency(n,p,verts[i],verts[j])
                assert got == should, ('embedding',p,n,verts,i,j,got,should)
            # Verify the gap inequalities used in the infinite proof.
            cyc=verts+[v+n for v in verts]
            assert all(cyc[i+2]-cyc[i]<=p for i in range(8))
            assert all(cyc[i+3]-cyc[i]>=p+1 for i in range(8))
            cases+=1
    # Explicitly check the link construction for modest parameters without
    # enumerating the exponentially large ambient complex.
    for p in range(2,7):
        for n in range(ceil(8*(p+1)/3),4*p+1):
            S=[j*n//8 for j in range(8)]
            for mask in range(1<<8):
                sigma={S[j] for j in range(8) if mask>>j&1}
                rest=[v for v in S if v not in sigma]
                ambient_link_member=any(
                    sum(adjacency(n,p,a,b) for a,b in combinations(t,2))<2
                    for t in combinations(rest,3))
                local_cut_member=any(
                    sum(min(abs(i-j),8-abs(i-j))<=2 for i,j in combinations(t,2))<2
                    for t in combinations([j for j in range(8) if not mask>>j&1],3))
                assert ambient_link_member==local_cut_member
    print('BAND_OK embedding_cases='+str(cases)+
          ' p_range=2..80 exact_adjacency_and_gap_checks; link_checks_p=2..6')


if __name__=='__main__':
    validate_seed()
    validate_band()
    print('ALL_VERIFY_OK')
