#!/usr/bin/env python3
"""Finite-order-type verifier for triples on three-row clique paths."""
from itertools import combinations, product
from collections import defaultdict

def mv(nodes, cols):
    n=max(cols)+1
    S=set(nodes)
    def dist(a,b):return abs(a[0]-b[0])+(a[1]!=b[1])
    def has_short_path(a,b):
        # independent BFS, avoids every selected internal vertex
        q=[a];seen={a};idx=0
        while idx<len(q):
            p=q[idx];idx+=1
            if p==b:return True
            i,r=p
            nbr=[(i,s) for s in range(3) if s!=r]
            if i>0:nbr.append((i-1,r))
            if i+1<n:nbr.append((i+1,r))
            for z in nbr:
                if z in seen or (z in S and z!=b) or dist(a,z)>dist(a,b):continue
                # force a shortest path, improving distance to b by exactly one
                if dist(z,b)!=dist(p,b)-1:continue
                seen.add(z);q.append(z)
        return False
    return all(has_short_path(a,b) for a,b in combinations(nodes,2))

def check(cols):
    all_nodes=[(i,r) for i in cols for r in range(3)]
    valid=aug=exception=0
    for X in combinations(all_nodes,3):
        if set(i for i,r in X)!=set(cols):continue
        if not mv(X,cols):continue
        valid+=1
        if any(mv(X+(v,),cols) for v in all_nodes if v not in X):aug+=1
        else:
            exception+=1
            assert len(cols)==1 and len(set(r for i,r in X))==3,(cols,X)
    return valid,aug,exception

if __name__=='__main__':
    canonical=[(0,), (0,1),(0,2),(0,1,2),(0,1,3),(0,2,3),(0,2,4)]
    total=[0,0,0]
    for cols in canonical:
        a=check(cols)
        total=[x+y for x,y in zip(total,a)]
        print('occupied_columns=',cols,'valid=',a[0],'extend_in_occupied_columns=',a[1],'exceptions=',a[2])
    print('TOTAL',total)
    assert total[2]==1
