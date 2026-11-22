#!/usr/bin/env python3
"""Recompute the integral graph Jacobian of the degree-one del Pezzo intersection-one graph.
No external packages or data files required. All arithmetic is exact.
"""
from itertools import combinations, product
from collections import Counter
from math import prod


def e8_doubled_roots():
    roots=[]
    for i,j in combinations(range(8),2):
        for a,b in product((-2,2),repeat=2):
            v=[0]*8;v[i]=a;v[j]=b;roots.append(tuple(v))
    for a in product((-1,1),repeat=8):
        if sum(z==-1 for z in a)%2==0:
            roots.append(tuple(a))
    assert len(roots)==240 and len(set(roots))==240
    assert all(sum(x*x for x in a)==8 for a in roots)
    return roots


def orthogonality_graph(roots):
    n=len(roots)
    A=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if sum(a*b for a,b in zip(roots[i],roots[j]))==0:
                A[i][j]=A[j][i]=1
    assert all(sum(row)==126 for row in A)
    assert sum(sum(row) for row in A)==30240
    return A


def local_smith(L,p,exp):
    """Counts valuations of SNF of a nonsingular integral matrix.
    Exact over Z/p^exp; all pivots at a level are units and are eliminated
    using invertible row/column operations; a block divisible by p is
    divided by p and valuation level increments. exp must exceed max valuation.
    """
    n=len(L); mod=p**exp
    B=[[x%mod for x in row] for row in L]
    counts=Counter(); k=0; v=0
    while k<n:
        ij=next(((i,j) for i in range(k,n) for j in range(k,n) if B[i][j]%p), None)
        if ij is None:
            assert mod>p, 'insufficient modulus for the claimed Smith valuations'
            for i in range(k,n):
                B[i][k:]=[x//p for x in B[i][k:]]
            mod//=p;v+=1
            continue
        i,j=ij
        B[k],B[i]=B[i],B[k]
        for row in B:
            row[k],row[j]=row[j],row[k]
        pivot=B[k][k]
        inv=pow(pivot,-1,mod)
        pivrow=B[k]
        for i in range(k+1,n):
            fac=B[i][k]*inv%mod
            if fac:
                row=B[i]
                for j in range(k+1,n):
                    row[j]=(row[j]-fac*pivrow[j])%mod
        counts[v]+=1; k+=1
    assert sum(counts.values())==n
    return dict(sorted(counts.items()))


def exact_spectral_certificate(A):
    n=len(A)
    # Check exact monic polynomial x(x-126)(x-6)(x+18) annihilates A.
    # A^2 and A^3 are computed using integer arithmetic, not floating eigenvalues.
    def multiply(B,C):
        R=[[0]*n for _ in range(n)]
        for i in range(n):
            row=R[i]
            for k,b in enumerate(B[i]):
                if b:
                    c=C[k]
                    for j in range(n):
                        row[j]+=b*c[j]
        return R
    A2=multiply(A,A)
    A3=multiply(A2,A)
    A4=multiply(A3,A)
    for i in range(n):
        for j in range(n):
            assert A4[i][j]-114*A3[i][j]-1620*A2[i][j]+13608*A[i][j]==0
    assert sum(A2[i][i] for i in range(n))==30240
    seen={0};todo=[0]
    while todo:
        i=todo.pop()
        for j,b in enumerate(A[i]):
            if b and j not in seen:
                seen.add(j);todo.append(j)
    assert len(seen)==n
    # Connectedness makes the 126-eigenspace one-dimensional.
    # The remaining multiplicities follow from total dimension, trace A=0,
    # and trace A^2=30240; the polynomial identity restricts eigenvalues
    # to 126,6,-18,0. (A is real symmetric.)
    return {126:1,6:84,-18:35,0:120}


def main():
    roots=e8_doubled_roots()
    A=orthogonality_graph(roots)
    assert exact_spectral_certificate(A)=={126:1,6:84,-18:35,0:120}
    L=[[126*(i==j)-A[i][j] for j in range(240)] for i in range(240)]
    expected={2:{0:120,2:9,3:26,4:50,6:26,7:8},
              3:{0:36,1:48,2:120,3:35},
              5:{0:156,1:83},
              7:{0:119,1:120}}
    for sink in (0,112):
        R=[[L[i][j] for j in range(240) if j!=sink]
           for i in range(240) if i!=sink]
        for p,precision in ((2,9),(3,5),(5,3),(7,3)):
            actual=local_smith(R,p,precision)
            assert actual==expected[p],(sink,p,actual,expected[p])
    tree=126**120*120**84*144**35//240
    assert 126**120*120**84*144**35 % 240==0
    assert tree == 2**508*3**393*5**83*7**120
    factors={p:sum(([p**v]*n for v,n in sorted(count.items())),[])
             for p,count in expected.items()}
    inv=[prod(factors[p][i] for p in factors) for i in range(239)]
    assert all(inv[i+1]%inv[i]==0 for i in range(238))
    expected_inv={1:36,3:48,9:35,63:1,252:9,504:26,1008:1,
                  5040:48,15120:1,60480:26,120960:8}
    assert dict(Counter(inv))==expected_inv
    assert prod(inv)==tree
    print('E8_DEL_PEZZO_240_CRITICAL_GROUP_OK', 'factors',len(inv),'tree_valuations',{p:sum(v*n for v,n in c.items()) for p,c in expected.items()})

if __name__=='__main__':main()
