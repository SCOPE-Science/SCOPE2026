#!/usr/bin/env python3
"""Exact checks for the canonical queens lattice gas high-temperature variance.

Only Python's standard library is needed. Finite checks corroborate, but do
not replace, the all-size parity and covariance identities proved in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def n_edges(n):
    return n * (n - 1) * (5 * n - 1) // 3


def n_wedges(n):
    if n % 2 == 0:
        return n * (67*n**3 - 180*n**2 + 146*n - 36) // 12
    return (n-1) * (67*n**3 - 113*n**2 + 33*n - 3) // 12


def var_formula(n):
    den = 18*(n+1)**2*(n*n-3)*(n*n-2)
    if n % 2 == 0:
        num = (n-2)*(n-1)*(31*n**5-75*n**4+32*n**3+24*n*n-24*n-6)
    else:
        num = (n-2)*(n-1)**2*(31*n**4-44*n**3-12*n*n+12*n-3)
    return F(num, den)


def hypergeom(n, j):
    if j > n:
        return F(0)
    p=F(1)
    for a in range(j):
        p *= F(n-a, n*n-a)
    return p


def graph_edges(n):
    squares = [(i,j) for i in range(n) for j in range(n)]
    return [(u,v) for u in range(n*n) for v in range(u+1,n*n)
            if squares[u][0]==squares[v][0]
            or squares[u][1]==squares[v][1]
            or abs(squares[u][0]-squares[v][0]) == abs(squares[u][1]-squares[v][1])]


def test():
    count=0
    for n in range(2, 81):
        degree=[]
        ab=0
        for i in range(n):
            for j in range(n):
                a=abs(i-j)
                b=abs(i+j-(n-1))
                degree.append(4*(n-1)-a-b)
                ab+=a*b
        wed=sum(d*(d-1)//2 for d in degree)
        edge=sum(degree)//2
        assert edge==n_edges(n)
        assert wed==n_wedges(n)
        ab_expected=(n*n*(n*n-4) if n%2==0 else (n*n-1)*(n*n-3))//12
        assert ab==ab_expected
        e=edge; w=wed; z=comb(e,2)-w
        p2,p3,p4=(hypergeom(n, j) for j in [2,3,4])
        mu=e*p2
        var=e*p2+2*w*p3+2*z*p4-mu*mu
        assert mu==F((5*n-1)*(n-1),3*(n+1))
        assert var==var_formula(n)
        count+=6
    # This uses direct edge construction, unlike the degree calculations above.
    for n in range(2,6):
        edges=graph_edges(n)
        M=n*n
        assert len(edges)==n_edges(n)
        deg=[sum(u==v or w==v for u,w in edges) for v in range(M)]
        assert sum(comb(d,2) for d in deg)==n_wedges(n)
        total=comb(M,n)
        h1=h2=0
        for chosen in combinations(range(M),n):
            occupied=set(chosen)
            h=sum(u in occupied and v in occupied for u,v in edges)
            h1+=h
            h2+=h*h
        mean=F(h1,total)
        var=F(h2,total)-mean*mean
        assert mean==F((5*n-1)*(n-1),3*(n+1))
        assert var==var_formula(n)
        count+=4
    assert F(5,3)+F(67,6)-F(100,9)==F(31,18)
    count+=1
    print(f'PASS: {count} exact equalities; full uniform-subset enumeration for n=2,3,4,5.')

if __name__=='__main__':test()
