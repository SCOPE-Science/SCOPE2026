#!/usr/bin/env python3
"""Exhaustive direct checks for 2-frugal independent-set polynomials on prisms."""
from math import comb
from itertools import product

def exact(n):
    out=[0]*(n+1);out[0]=1
    for k in range(1,2*n//3+1):
        for r in range((k+1)//2, min(k,n-k)+1):
            if k-r>r:continue
            u=n*comb(r,k-r)*comb(n-k-1,r-1)*2**r
            assert u%r==0
            out[k]+=u//r
    return out

def direct(n):
    edges=[]
    for i in range(n):
        for j in (0,1):
            edges.append((2*i+j,2*((i+1)%n)+j))
        edges.append((2*i,2*i+1))
    neighbors=[set() for _ in range(2*n)]
    for u,v in edges:
        neighbors[u].add(v);neighbors[v].add(u)
    assert all(len(z)==3 for z in neighbors)
    out=[0]*(n+1)
    for cfg in product((0,1,2),repeat=n):
        S={2*i+v-1 for i,v in enumerate(cfg) if v!=0}
        if all(not(u in S and v in S) for u,v in edges) and all(len(N&S)<=2 for N in neighbors):
            out[len(S)]+=1
    return out

def optimum(n):
    t,a=divmod(n,3)
    return [(3*2**t),((3*t+1)*(t+1)*2**t),((3*t+2)*2**(t+1))][a]

def main():
    for n in range(3,11):
        a=exact(n);b=direct(n)
        assert a==b,(n,a,b)
        best=max(i for i,v in enumerate(a) if v)
        assert best==2*n//3 and a[best]==optimum(n)
        print('DIRECT_GRAPH_DEFINITION_OK',n,best,a[best],sum(a))
    for n in range(11,81):
        a=exact(n)
        best=max(i for i,v in enumerate(a) if v)
        assert best==2*n//3 and a[best]==optimum(n)
    print('FORMULA_INTEGRALITY_AND_BOUNDARY_OK through n=80')
    print('VERIFY_OK')
if __name__=='__main__':main()
