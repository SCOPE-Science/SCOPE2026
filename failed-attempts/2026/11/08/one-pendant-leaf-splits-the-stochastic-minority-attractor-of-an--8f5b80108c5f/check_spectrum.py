#!/usr/bin/env python3
"""Independent exact spectral checker for each recurrent class.
Uses SymPy to compute direct characteristic polynomials of inclusion graph Laplacians.
"""
from itertools import combinations
from math import comb
import sympy as sp

def graph(m):
    n=2*m
    low=list(combinations(range(n),m-1))
    high=list(combinations(range(n),m))
    all_states=low+high
    ix={a:i for i,a in enumerate(all_states)}
    L=sp.zeros(len(all_states))
    for j,u in enumerate(high):
        for v in combinations(u,m-1):
            k=ix[v]; i=len(low)+j
            L[i,i]+=1;L[k,k]+=1;L[i,k]-=1;L[k,i]-=1
    return L

def main():
    for m in (1,2,3):
        L=graph(m)
        x=sp.Symbol('x')
        p=sp.Poly(L.charpoly(x).as_expr(),x)
        eigen={}
        for j in range(m):
            d=comb(2*m,j)-(comb(2*m,j-1) if j else 0)
            for z in (j,2*m+1-j):eigen[z]=eigen.get(z,0)+d
        extra=comb(2*m,m)-comb(2*m,m-1)
        eigen[m]=eigen.get(m,0)+extra
        predicted=sp.prod((x-z)**v for z,v in eigen.items())
        assert sp.expand(predicted-p.as_expr())==0
        assert sorted(eigen)[1]==1
        print(f'm={m}: matrix {L.rows}x{L.cols}; eigenvalue multiplicities {dict(sorted(eigen.items()))}; gap=1/{2*m+2}')
    print('PASS: exact characteristic polynomials and gaps for m=1,2,3')

if __name__=='__main__':main()
