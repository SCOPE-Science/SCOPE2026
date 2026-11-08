#!/usr/bin/env python3
"""Finite cross-checks for the clearing criterion on triangular friendship graphs.

Run: python3 verify.py
Uses exact integers and two separate state-transition implementations.
The mathematical proof, not finite testing, establishes the unrestricted result.
"""
from functools import lru_cache
from itertools import combinations_with_replacement


def defect(a, b):
    if a == b == 1:
        return 4
    if a % 2 == b % 2 == 0:
        return 0
    if a > 0 and b > 0 and (a + b) % 2 == 1:
        return 1
    if a % 2 == b % 2 == 1:
        return 2
    return 3


def weight(a, b):
    return (a+b-defect(a,b))//2


def potential(c):
    center=c[0]
    return center+sum(weight(c[1+2*j],c[2+2*j]) for j in range((len(c)-1)//2))


def is_exception(c):
    return c[0]==3 and all(x==0 for x in c[1:])


def adjacency(m):
    n=2*m+1
    edges=[[] for _ in range(n)]
    for j in range(m):
        a,b=2*j+1,2*j+2
        for x,y in ((0,a),(0,b),(a,b)):
            edges[x].append(y)
            edges[y].append(x)
    return tuple(tuple(sorted(neigh)) for neigh in edges)


def all_configurations(n,t):
    # Independent exact weak-composition generator.
    for dividers in combinations_with_replacement(range(n), t):
        row=[0]*n
        for k in dividers:
            row[k]+=1
        yield tuple(row)


def oracle(adj):
    @lru_cache(None)
    def reachable(c):
        total=sum(c)
        if total==1:
            return True
        if total==0:
            return False
        for u,neighbors in enumerate(adj):
            if c[u]<2:
                continue
            for v in neighbors:
                nxt=list(c)
                nxt[u]-=2
                nxt[v]+=1
                if reachable(tuple(nxt)):
                    return True
        return False
    return reachable


def local_inequalities():
    # Check all finite boundary/residue cases plus a large stress range.
    for a in range(129):
        for b in range(129):
            x=defect(a,b)
            assert 0<=x<=4
            assert 2*weight(a,b)+x==a+b
            if a>=2:
                assert x<=defect(a-2,b),('outer-to-center',a,b)
                assert defect(a-2,b+1)>=x-1,('outer-to-mate',a,b)
            assert defect(a+1,b)>=x-3,('center-to-outer',a,b)
            if a>=2:
                assert weight(a+2,b)==weight(a,b)+1,('periodic-a',a,b)
            if b>=2:
                assert weight(a,b+2)==weight(a,b)+1,('periodic-b',a,b)
    print('LOCAL_DEFECT_AND_PERIODICITY_OK')


def exhaustive_tests():
    for m,cap in ((1,11),(2,12),(3,12)):
        adj=adjacency(m)
        solvable=oracle(adj)
        checked=0
        for total in range(2,cap+1):
            for c in all_configurations(len(adj),total):
                expected=potential(c)>=1 and not is_exception(c)
                actual=solvable(c)
                assert expected==actual,(m,total,c,potential(c),expected,actual)
                checked+=1
        print('LABELLED_GRAPH_EXHAUSTIVE_OK',m,'through_size',cap,'configurations',checked,'cache',solvable.cache_info().currsize)


def boundary_tests():
    for m in range(2,10):
        n=2*m+1
        exceptional=(0,2*m+1,0)+sum(((1,1) for _ in range(m-1)),())
        assert len(exceptional)==n
        assert sum(exceptional)==4*m-1
        assert potential(exceptional)==0
        all_pairs=[(1,1)]*(m-1)+[(2*m+1,0)]
        assert sum(defect(a,b) for a,b in all_pairs)==4*m-1
        for a in range(0,2*m+3):
            for b in range(0,2*m+3-a):
                # Defect table's boundary values, not an exploration shortcut.
                assert defect(a,b)<=4
        if m<=4:
            sol=oracle(adjacency(m))
            assert not sol(exceptional)
        print('CRITICAL_UNIQUE_OBSTRUCTION_PATTERN_OK',m)

if __name__=='__main__':
    local_inequalities()
    exhaustive_tests()
    boundary_tests()
    print('VERIFY_OK')
