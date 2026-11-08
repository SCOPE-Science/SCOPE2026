#!/usr/bin/env python3
"""Reproduce the identifying-set calculation for the three-letter directed de Bruijn graph.
No external dependencies. Exact sets, independently generated radius-two in-balls.
"""
from itertools import product

def inballs(q):
    A=range(q); V=set(product(A,repeat=3))
    pred=lambda v:{(a,v[0],v[1]) for a in A}
    return {v:({v}|pred(v)|set().union(*(pred(x) for x in pred(v)))) for v in V}

def test(q):
    B=inballs(q)
    S={v for v in B if v[0]!=v[2]}
    T=[frozenset(S&B[v]) for v in B]
    assert len(S)==q*q*(q-1)
    assert all(T)
    assert len(set(T))==q**3, ('invalid q',q)
    # Test the closed-form in-ball decomposition, independent from the graph BFS.
    A=range(q)
    for a,b,c in B:
        direct=({(x,y,a) for x in A if x!=a for y in A}
                |{(x,a,b) for x in A if x!=b}
                |({(a,b,c)} if a!=c else set()))
        assert direct==S&B[(a,b,c)],(q,a,b,c)
    return len(S)

def binary_exception():
    q=2;B=inballs(q);V=sorted(B)
    valid=[]
    for bitmask in range(1<<len(V)):
        S={v for i,v in enumerate(V) if bitmask>>i&1}
        T=[frozenset(S&B[v]) for v in V]
        if all(T) and len(set(T))==len(V):valid.append(S)
    assert min(map(len,valid))==7
    opt=[S for S in valid if len(S)==7]
    assert len(opt)==2
    assert {next(iter(set(V)-S)) for S in opt}=={(0,0,0),(1,1,1)}
    return len(opt)

if __name__=='__main__':
    assert binary_exception()==2
    for q in range(3,9):
        k=test(q)
        print('alphabet',q,'minimum_code_size',k,'identified',q**3)
    print('VERIFY_OK')
