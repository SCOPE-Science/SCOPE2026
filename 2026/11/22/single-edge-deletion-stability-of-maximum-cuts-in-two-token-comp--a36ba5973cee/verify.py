#!/usr/bin/env python3
"""Reproducible finite checks for a sharp token-graph cut formula."""
from itertools import combinations


def construct(n):
    assert n >= 3
    # Vertices 0 and 1 will be the endpoints of the missing base edge.
    # red pairs represent one side of the cut of F_2.
    if n == 3:
        return {(0, 1)}
    if n == 4:
        return {(0, 1), (2, 3)}
    if n == 5:
        return {tuple(sorted(e)) for e in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]}
    q, r = divmod(n,4)
    if r == 0:
        ss=2*q-1; tt=2*q-1; defect='path'; cross='matching'
    elif r == 1:
        ss=2*q-1; tt=2*q; defect='path'; cross='double-first'
    elif r == 2:
        ss=2*q; tt=2*q; defect='perfect'; cross='matching'
    else:
        ss=2*q; tt=2*q+1; defect='perfect'; cross='matching-except-last'
    assert ss+tt == n-2
    S=list(range(2,2+ss)); T=list(range(2+ss,n))
    red={(0,1)}
    for v in S:
        red.add((0,v)); red.add((1,v))
    for x,y in combinations(T,2): red.add((x,y))
    removed=set()
    if defect=='perfect':
        assert len(S)%2==0
        for j in range(0,len(S),2): removed.add((S[j],S[j+1]))
    else:
        assert len(S)>=3 and len(S)%2==1
        removed.add((S[0],S[1]));removed.add((S[0],S[2]))
        for j in range(3,len(S),2): removed.add((S[j],S[j+1]))
    for x,y in combinations(S,2):
        if (x,y) not in removed: red.add((x,y))
    if cross=='double-first':
        for j,t in enumerate(T): red.add((S[0] if j<2 else S[j-1],t))
    else:
        for s,t in zip(S,T): red.add((s,t))
    return red


def cut_score(n, red, missing=False):
    R=set(red)
    deg=[sum((min(v,w),max(v,w)) in R for w in range(n) if w!=v) for v in range(n)]
    full=sum(d*(n-1-d) for d in deg)
    penalty=sum(((0,w) in R)!=((1,w) in R) for w in range(2,n))
    return full-penalty if missing else full


def theorem_value(n):
    return n * ((n-1)**2//4) - (n%4==3) - (2 if n==5 else 0)


def verify():
    for n in range(3,101):
        red=construct(n)
        deg=[sum((min(v,w),max(v,w)) in red for w in range(n) if w!=v) for v in range(n)]
        assert all(((0,w) in red)==((1,w) in red) for w in range(2,n)) if n!=5 else True
        assert cut_score(n,red,True)==theorem_value(n),(n,cut_score(n,red,True),theorem_value(n),deg)
        if n!=5:
            assert cut_score(n,red,False)==theorem_value(n)
    print('EXPLICIT_ALL_RESIDUE_CONSTRUCTIONS_PASS n=3..100')
    for n in range(3,7):
        pairs=list(combinations(range(n),2))
        token_edges=[]
        for i,(u,v) in enumerate(pairs):
            for j,(x,y) in enumerate(pairs[:i]):
                if len({u,v,x,y})==3 and tuple(sorted(set((u,v))^set((x,y))))!=(0,1):
                    token_edges.append((i,j))
        scores=[]
        for mask in range(1<<len(pairs)):
            red={e for i,e in enumerate(pairs) if mask>>i &1}
            actual=sum(((mask>>i)^(mask>>j))&1 for i,j in token_edges)
            assert actual==cut_score(n,red,True)
            scores.append(actual)
        assert max(scores)==theorem_value(n)
        print('INDEPENDENT_TOKEN_EDGE_EXHAUSTIVE_PASS',n,len(scores),max(scores),scores.count(max(scores)))
    assert sum(cut_score(5,construct(5),True) for _ in range(1))==18
    print('EXCEPTIONAL_FIVE_VERTEX_CYCLE_PASS')
    print('VERIFY_OK')
if __name__=='__main__': verify()
