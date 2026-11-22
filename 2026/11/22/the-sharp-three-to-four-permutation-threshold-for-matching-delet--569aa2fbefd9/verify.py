#!/usr/bin/env python3
"""Finite cross-checks for permutation 1-11 representations and matching-deleted bicliques."""
from itertools import combinations, permutations

def graph_edges(a,b,s):
    A=tuple('a'+str(i) for i in range(1,a+1))
    B=tuple('b'+str(i) for i in range(1,b+1))
    E={frozenset((x,y)) for x in A for y in B if not (int(x[1:])==int(y[1:])<=s)}
    return A,B,E

def represented_edges(blocks):
    vertices=tuple(blocks[0])
    pos=[{v:i for i,v in enumerate(row)} for row in blocks]
    assert all(set(block)==set(vertices) and len(block)==len(vertices) for block in blocks)
    E=set()
    for u,v in combinations(vertices,2):
        seq=[p[u]<p[v] for p in pos]
        defects=sum(seq[i]!=seq[i+1] for i in range(len(seq)-1))
        if defects<=1:E.add(frozenset((u,v)))
    return E

def two_realizer(a,b,s):
    assert 0<=s<=2 and s<=a and s<=b
    A,B,E=graph_edges(a,b,s)
    if s==0:
        L1=A+B;L2=B+A
    elif s==1:
        x=A[0];y=B[0];AA=A[1:];BB=B[1:]
        L1=(x,)+AA+BB+(y,)
        L2=BB+(x,y)+AA
    else:
        x,y=A[:2];u,v=B[1],B[0];AA=A[2:];BB=B[2:]
        L1=(x,)+AA+(u,y)+BB+(v,)
        L2=(u,)+BB+(x,v)+AA+(y,)
    return L1,L2

def short_blocks(a,b,s):
    L1,L2=two_realizer(a,b,s)
    return tuple(reversed(L1)),L1,tuple(reversed(L2))

def crown_blocks(a,b,s):
    A,B,E=graph_edges(a,b,s)
    N=a+b-s
    ids_a=list(range(1,a+1));ids_b=list(range(1,s+1))+list(range(a+1,N+1))
    c1=['a'+str(i) for i in range(1,N+1)]+['b'+str(i) for i in range(1,N+1)]
    c2=['a'+str(i) for i in range(N,0,-1)]+['b'+str(i) for i in range(N,0,-1)]
    c3=[v for i in range(1,N+1) for v in ('b'+str(i),'a'+str(i))]
    c4=[v for i in range(1,N+1) for v in ('a'+str(i),'b'+str(i))]
    selected=set('a'+str(i) for i in ids_a)|set('b'+str(i) for i in ids_b)
    relabel={'a'+str(i):'a'+str(j) for j,i in enumerate(ids_a,1)}
    relabel.update({'b'+str(i):'b'+str(j) for j,i in enumerate(ids_b,1)})
    return [tuple(relabel[v] for v in block if v in selected) for block in (c1,c2,c3,c4)]

def test():
    small=large=0
    for a in range(1,10):
        for b in range(1,10):
            for s in range(min(a,b)+1):
                A,B,E=graph_edges(a,b,s)
                blocks=crown_blocks(a,b,s)
                assert represented_edges(blocks)==E,(a,b,s,'four')
                large+=1
                if s<=2:
                    assert represented_edges(short_blocks(a,b,s))==E,(a,b,s,'three',short_blocks(a,b,s))
                    small+=1
    print('FOUR_PERMUTATION_FAMILY',large,'PASS')
    print('THREE_PERMUTATION_FAMILY',small,'PASS')
    for n in range(2,7):
        checked=0
        first=tuple(range(n))
        for mid in permutations(first):
            for last in permutations(first):
                blocks=(first,mid,last)
                E=represented_edges(blocks)
                P2={v:i for i,v in enumerate(mid)}
                P1={v:i for i,v in enumerate(first)}
                P3={v:i for i,v in enumerate(last)}
                relation={(u,v) for u in first for v in first if u!=v and P2[u]<P2[v] and P1[u]>P1[v] and P3[u]>P3[v]}
                assert all((u,w) in relation for u,v in relation for z,w in relation if v==z)
                assert {frozenset((u,v)) for u,v in relation}=={frozenset((u,v)) for u,v in combinations(first,2)}-E
                checked+=1
        print('TRIPLE_ORDER_POSET_CHECK',n,checked,'PASS')
    print('VERIFY_OK')
if __name__=='__main__':test()
