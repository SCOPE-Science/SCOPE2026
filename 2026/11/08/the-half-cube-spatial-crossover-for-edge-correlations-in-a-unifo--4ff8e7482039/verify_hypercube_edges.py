#!/usr/bin/env python3
"""Exact algebraic checks for two-edge inclusion in hypercube spanning trees.

Standalone. Requires Python >=3.10 and sympy.
"""
from sympy import Matrix, Rational
from math import comb

def pair_kernel_integral(d, i, j, v):
    # e=(0,2**i) and f=(v, v^2**j), with v_j=0
    assert d >= 2 and ((v >> j) & 1) == 0
    if i == j:
        r=v.bit_count()
        s=d-1-r
        assert 0<=r<=d-1
        return Rational(2,2**d)*sum(Rational((-1)**u*comb(r,u)*comb(s,w),u+w+1)
              for u in range(r+1) for w in range(s+1))
    r=(v & ~(1<<i)).bit_count()
    s=d-2-r
    sign=-1 if (v>>i)&1 else 1
    assert 0<=r<=d-2
    return sign*Rational(2,2**d)*sum(Rational((-1)**u*comb(r,u)*comb(s,w),u+w+2)
           for u in range(r+1) for w in range(s+1))

def laplacian(d):
    n=1<<d
    L=Matrix.zeros(n,n)
    edges=[]
    for v in range(n):
        for j in range(d):
            if not ((v>>j)&1):
                w=v^(1<<j); edges.append((v,w,j))
                L[v,v]+=1; L[w,w]+=1; L[v,w]-=1; L[w,v]-=1
    return L,edges

def edge_b(n,e):
    b=Matrix.zeros(n-1,1)
    u,v=e[:2]
    if u<n-1:b[u]+=1
    if v<n-1:b[v]-=1
    return b

def direct_weight_count(L,e,f,s,t):
    # Weighted matrix-tree determinant; s,t edge weights relative to base weight 1
    N=L.rows; C=L.copy()
    for x,edge in ((s-1,e),(t-1,f)):
        a,b=edge[:2]
        C[a,a]+=x;C[b,b]+=x;C[a,b]-=x;C[b,a]-=x
    return C[:N-1,:N-1].det(method='domain-ge')

def run():
    checks=0
    for d in range(2,6):
        L, edges=laplacian(d)
        n=1<<d
        source=(0,1,0)
        b=edge_b(n,source)
        x=L[:n-1,:n-1].inv()*b
        p=Rational(2*(n-1),d*n)
        assert (b.T*x)[0] == p
        checks+=1
        for e in edges:
            computed=(edge_b(n,e).T*x)[0]
            integral=pair_kernel_integral(d,0,e[2],e[0])
            assert computed==integral,(d,e,computed,integral)
            checks+=1
        # Test independent determinant counts for a selection of pairs d<=4
        if d<=4:
            representatives=[e for e in edges if e!=source]
            if d==4:
                representatives=[e for e in representatives if e[0] in (0,1,2,3,6,7,14)]
            for f in representatives:
                a=direct_weight_count(L,source,f,1,1)
                q=direct_weight_count(L,source,f,2,1)
                r=direct_weight_count(L,source,f,1,2)
                s=direct_weight_count(L,source,f,2,2)
                joint=(s-q-r+a)/a
                k=pair_kernel_integral(d,0,f[2],f[0])
                assert joint==p*p-k*k,(d,f,joint,p*p-k*k)
                checks+=1
        print('dimension',d,'evaluated_edges',len(edges),'checks_so_far',checks)
    # Exact integral positivity ordering checked via symbolic equivalence of integrands
    for d in range(3,15):
        for r in range(1,d-1):
            # Compare exact integral formulas for pairs at equal separation
            from sympy import symbols, integrate
            t=symbols('t')
            a=integrate((1-t)**r*(1+t)**(d-1-r),(t,0,1))*Rational(2,2**d)
            b_=integrate(t*(1-t)**r*(1+t)**(d-2-r),(t,0,1))*Rational(2,2**d)
            assert a>b_>0
            checks+=1
    print('VERIFY_OK',checks,'exact comparisons')
if __name__=='__main__':run()
