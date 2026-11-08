"""Finite checks using direct graph definitions for forest complexes of bipartite graphs.

Run with python3 forest_bipartite_verify.py. Requires Python standard library only.
"""
from itertools import combinations
from math import comb
from random import Random


def forest_complex(a,b,mask):
    n=a+b
    edge_list=[(i,a+j) for i in range(a) for j in range(b)]
    edges=[e for k,e in enumerate(edge_list) if mask&(1<<k)]
    faces={-1:[0]}
    for s in range(1,1<<n):
        parent=list(range(n))
        def root(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        acyclic=True
        for i,j in edges:
            if s>>i&1 and s>>j&1:
                x,y=root(i),root(j)
                if x==y:
                    acyclic=False
                    break
                parent[x]=y
        if acyclic:
            faces.setdefault(s.bit_count()-1,[]).append(s)
    return faces


def gf2_rank(vectors):
    basis={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p in basis:
                v^=basis[p]
            else:
                basis[p]=v
                break
    return len(basis)


def betti_reduced(faces,n):
    ranks={}
    for k in range(1,max(faces)+1):
        preceding={m:i for i,m in enumerate(faces.get(k-1,[]))}
        columns=[]
        for m in faces.get(k,[]):
            v=0
            for j in range(n):
                if m&(1<<j):
                    v^=1<<preceding[m^(1<<j)]
            columns.append(v)
        ranks[k]=gf2_rank(columns)
    bettis={k:len(faces.get(k,[]))-ranks.get(k,0)-ranks.get(k+1,0) for k in range(max(faces)+1)}
    bettis[0]-=1
    return bettis,ranks


def verify():
    profiles=0
    graph_subset_cases=0
    acyclic_subsets=0
    # All bipartite edge sets on the indicated bipartitions; no use of the theorem in construction.
    for a,b in [(2,2),(2,3),(2,4),(3,3)]:
        for mask in range(1<<(a*b)):
            profiles+=1
            faces=forest_complex(a,b,mask)
            graph_subset_cases+=1<<(a+b)
            acyclic_subsets+=sum(len(v) for k,v in faces.items() if k>=0)
            assert len(faces[0])==a+b
            assert len(faces[1])==comb(a+b,2)
            assert len(faces[2])==comb(a+b,3)
            bet,_=betti_reduced(faces,a+b)
            assert bet.get(0,0)==bet.get(1,0)==0,(a,b,mask,bet)
            expected=(a-1)*(b-1) if mask==(1<<(a*b))-1 else 0
            assert bet.get(2,0)==expected,(a,b,mask,bet)
    # Additional profiles for larger sizes with deterministic random edge subsets.
    rng=Random(2023)
    extra=0
    for a,b in [(3,4),(4,4),(3,5)]:
        full=(1<<(a*b))-1
        cases={0,full}
        while len(cases)<40:
            cases.add(rng.randrange(full+1))
        for mask in sorted(cases):
            faces=forest_complex(a,b,mask)
            bet,_=betti_reduced(faces,a+b)
            expected=(a-1)*(b-1) if mask==full else 0
            assert bet.get(0,0)==bet.get(1,0)==0 and bet.get(2,0)==expected,(a,b,mask,bet)
            extra+=1
    # All individual edge deletions, checking full homological acyclicity over F2.
    single=0
    for a,b in [(2,2),(2,5),(3,3),(3,5),(4,4),(5,5)]:
        full=(1<<(a*b))-1
        for j in range(a*b):
            faces=forest_complex(a,b,full^(1<<j))
            bet,_=betti_reduced(faces,a+b)
            assert all(v==0 for v in bet.values()),(a,b,j,bet)
            single+=1
    # Sharp two-deletion example, plus its f-vector and mod2 homology.
    a=b=3
    full=(1<<9)-1
    witness=forest_complex(3,3,full^(1<<0)^(1<<4))
    bet,ranks=betti_reduced(witness,6)
    assert {k:len(witness.get(k,[])) for k in range(5)}=={0:6,1:15,2:20,3:13,4:2}
    assert bet=={0:0,1:0,2:0,3:1,4:0},bet
    # Integral primitivity of the top boundary follows from these distinct unique boundary faces.
    fours=witness[4]
    assert len(fours)==2
    for x in fours:
        assert any(sum(int((y & x)==y) for y in fours)==1 for y in witness[3] if (y&x)==y)
    print('VERIFY_OK exhaustive_graph_profiles=%d vertex_subsets=%d induced_acyclic_subsets=%d larger_profiles=%d single_missing_edge_profiles=%d all_fields_mod2=PASS sharp_witness_fvector=PASS sharp_witness_H3_mod2=PASS'%(
        profiles,graph_subset_cases,acyclic_subsets,extra,single))

if __name__=='__main__':
    verify()
