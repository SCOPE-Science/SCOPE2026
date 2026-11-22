#!/usr/bin/env python3
"""Independent exhaustive checks for Ising one-spin dynamics on the triangular-book graph."""
from itertools import product
from math import comb

def classify(n):
    edges=[(0,1)]+[(h,i) for h in (0,1) for i in range(2,n+2)]
    states=list(product((-1,1),repeat=n+2))
    E={s:sum(s[i]*s[j] for i,j in edges) for s in states}
    weak=[]; strict=[]; ground=[]; neutral_escape=0
    minimum=min(E.values())
    for s in states:
        moves=[]
        for i in range(n+2):
            t=s[:i]+(-s[i],)+s[i+1:]
            moves.append((E[t]-E[s],t))
        if E[s]==minimum: ground.append(s)
        if all(d>=0 for d,_ in moves):
            weak.append(s)
            if all(d>0 for d,_ in moves): strict.append(s)
            elif E[s]>minimum:
                found=any(d==0 and any(E[u[:j]+(-u[j],)+u[j+1:]]<E[u] for j in range(n+2)) for d,u in moves)
                assert found,(n,s)
                neutral_escape+=1
        else:
            assert any(d<0 for d,_ in moves)
    predicted=2+(2*comb(n,n//2) if n%2==0 else 4*comb(n,(n-1)//2))
    assert len(weak)==predicted,(n,len(weak),predicted)
    assert len(strict)==2 and len(ground)==2
    assert {E[s] for s in weak}=={1-2*n,-1}
    assert all(s[0]==s[1] and all(v==-s[0] for v in s[2:]) for s in strict)
    assert neutral_escape==predicted-2
    return n,len(states),len(weak),len(strict),neutral_escape

if __name__=='__main__':
    for n in range(2,13):
        print(*classify(n))
    print('PASS: all exhaustive tests for n=2..12')
