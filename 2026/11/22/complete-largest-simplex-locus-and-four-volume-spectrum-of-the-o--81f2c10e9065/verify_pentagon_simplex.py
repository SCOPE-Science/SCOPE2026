#!/usr/bin/env python3
"""Exact finite combinatorial certificate for the orthogonal double pentagon.
All comparisons use integer indices and signs; no floating comparison decides a level or equality.
"""
from itertools import combinations,product
from collections import Counter
from math import comb

BIG={tuple(x) for x in [(0,1,3),(0,2,3),(0,2,4),(1,2,4),(1,3,4)]}
TRIS=set(combinations(range(5),3))
SMALL=TRIS-BIG
EDGES={tuple(sorted((i,(i+1)%5))) for i in range(5)}
DIAGS=set(combinations(range(5),2))-EDGES

def classify(S):
    A=tuple(v for v in S if v<5)
    B=tuple(v-5 for v in S if v>=5)
    if len(A)==3 and len(B)==2:
        tri,edge=A,B
    elif len(A)==2 and len(B)==3:
        tri,edge=B,A
    else:return 'zero'
    if tri in BIG and edge in EDGES:return 'high'
    if tri in SMALL and edge in DIAGS:return 'low'
    return 'middle'

def sign_sorted(S):
    A=tuple(v for v in S if v<5)
    B=tuple(v-5 for v in S if v>=5)
    if len(A)==3 and len(B)==2:
        return 1 if B[1]-B[0] in (1,2) else -1
    if len(A)==2 and len(B)==3:
        return 1 if A[1]-A[0] in (1,2) else -1
    return 0

def ordered_sign(X):
    S=tuple(sorted(X))
    c=classify(S)
    if c!='high':return 0
    inversions=sum(X[i]>X[j] for i in range(5) for j in range(i+1,5))
    return sign_sorted(S)*(-1 if inversions%2 else 1)

def run():
    S_all=list(combinations(range(10),5))
    counts=Counter(classify(S) for S in S_all)
    assert counts=={'zero':52,'low':50,'middle':100,'high':50},counts
    opt=[S for S in S_all if classify(S)=='high']
    assert len(opt)==50
    # A family is maximal when every simultaneously occurring vertex tuple has
    # equal magnitude and the SAME oriented sign in the fixed five-position ordering.
    edges=set(); degree=Counter(); cross=0
    for S in opt:
        orig=sign_sorted(S)
        successors=[]
        for k in range(5):
            choices=[]
            for v in range(10):
                if v in S:continue
                X=list(S);X[k]=v
                if ordered_sign(X)==orig:
                    choices.append(v)
                    T=tuple(sorted(X))
                    pair=tuple(sorted((S,T)))
                    edges.add(pair)
                    degree[S]+=1
                    successors.append((k,v,T))
            assert len(choices)<=1,('larger support face',S,k,choices)
        assert len(successors)==3,(S,successors)
        for (ka,va,_),(kb,vb,_) in combinations(successors,2):
            assert ka!=kb,(S,successors)
            X=list(S);X[ka]=va;X[kb]=vb
            assert ordered_sign(X)!=orig,(S,successors,'2D maximizer')
    assert len(edges)==75,len(edges)
    assert set(degree.values())=={3},degree
    cross=sum((len(set(a)&set(b))==4 and len([v for v in a if v<5])!=len([v for v in b if v<5])) for a,b in edges)
    assert cross==25,cross
    # Each permitted replacement is a genuine polytope edge:
    # either an adjacent pair in one pentagonal factor or a cross-factor pair.
    for S,T in edges:
        v=next(iter(set(S)-set(T)))
        w=next(iter(set(T)-set(S)))
        assert (v<5)!=(w<5) or tuple(sorted((v%5,w%5))) in EDGES
    # The quotient optimizer graph is connected, not just a union of cycles.
    adjacency={S:set() for S in opt}
    for S,T in edges:
        adjacency[S].add(T)
        adjacency[T].add(S)
    reached={opt[0]}
    frontier=[opt[0]]
    while frontier:
        v=frontier.pop()
        for w in adjacency[v]-reached:
            reached.add(w)
            frontier.append(w)
    assert len(reached)==50,len(reached)
    # The 25 same-composition edges on each side, plus 25 cross-composition edges.
    print('PASS: 252 vertex quintuples, levels zero=52, low=50, middle=100, high=50')
    print('PASS: 50 high-volume vertex simplices; exactly 75 one-parameter moving-vertex segments')
    print('PASS: every maximum vertex simplex has exactly three same-sign adjacent endpoints; no pairs of simultaneous moves')
    print('PASS: 25 cross-composition and 50 within-composition genuine polytope-edge segments; optimizer graph connected')

if __name__=='__main__':run()
