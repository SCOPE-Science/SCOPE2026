#!/usr/bin/env python3
"""Reproducible checks for alphabet-permutation symmetries of de Bruijn cycles."""
from math import factorial
from itertools import permutations

def count_n1(q,sigma):
    fixed=[]
    for w in permutations(range(q)):
        transformed=tuple(sigma[a] for a in w)
        if any(transformed==w[k:]+w[:k] for k in range(q)):
            fixed.append(w)
    return len(fixed)//q

def all_db2(q):
    N=q*q
    seq=[0,0]
    used={0}
    def dfs():
        if len(seq)==N+1:
            if seq[-1]==0:
                yield tuple(seq[:-1])
            return
        for b in range(q):
            e=seq[-1]*q+b
            if e not in used:
                used.add(e);seq.append(b)
                yield from dfs()
                seq.pop();used.remove(e)
    yield from dfs()

def n2_sym_count(q,sigma):
    count=0
    for w in all_db2(q):
        trans=tuple(sigma[a] for a in w)
        if any(trans==w[k:]+w[:k] for k in range(q*q)):
            count+=1
    return count

def construct_n2_m_odd(m):
    assert m%2 and m>=1
    # Edges are (source orbit, destination orbit, target phase) for each
    # of the two choices in each of m destination orbits.
    E=[(i,j,p) for i in range(m) for j in range(m) for p in range(2)]
    out=[[] for _ in range(m)]
    for e,(i,_,_) in enumerate(E):out[i].append(e)
    stack=[(0,None)]
    rev=[]
    while stack:
        v,_=stack[-1]
        if out[v]:
            e=out[v].pop(0)
            stack.append((E[e][1],e))
        else:
            _,e=stack.pop()
            if e is not None:rev.append(e)
    walk=list(reversed(rev))
    assert len(walk)==len(E)
    assert E[walk[0]][0] ==0
    assert E[walk[-1]][1]==0
    v=0;phase=0;symbols=[]
    for _ in range(2):
        for eid in walk:
            i,j,p=E[eid]
            assert v==i
            symbols.append(2*i+phase)
            v=j;phase^=p
    assert phase==0 and v==0
    q=2*m
    assert len(symbols)==q*q and len({(symbols[k],symbols[(k+1)%(q*q)]) for k in range(q*q)})==q*q
    assert all(symbols[k+q*q//2]==(symbols[k]^1) for k in range(q*q//2))
    return symbols

if __name__=='__main__':
    cases=[(2,[1,0],1,1),(3,[1,2,0],2,0),(4,[1,0,3,2],2,0),(4,[1,2,3,0],2,0)]
    for q,sigma,n1_expected,n2_expected in cases:
        a=count_n1(q,sigma);b=n2_sym_count(q,sigma)
        assert (a,b)==(n1_expected,n2_expected),(q,sigma,a,b)
        print('small',q,sigma,'n1',a,'n2',b)
    for m in [1,3,5]:
        w=construct_n2_m_odd(m)
        print('construction',2*m,'length',len(w),'prefix',w[:min(24,len(w))])
    print('VERIFY_OK')
