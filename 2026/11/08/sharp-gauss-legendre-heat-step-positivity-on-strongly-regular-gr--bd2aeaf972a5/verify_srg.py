#!/usr/bin/env python3
"""Reproducible exact-arithmetic checks for the Gauss endpoint heat step on strongly regular graphs."""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt


def cycle(n):
    return n, {(i, (i+1) % n) for i in range(n)}


def petersen():
    edges = []
    for i in range(5):
        edges.extend(((i,(i+1)%5),(i,5+i),(5+i,5+(i+2)%5)))
    return 10, edges


def complete_bipartite(a,b):
    return a+b, ((i,a+j) for i in range(a) for j in range(b))


def paley(q):
    squares = {(i*i)%q for i in range(1,q)}
    assert -1 % q in squares
    return q, ((i,j) for i in range(q) for j in range(i+1,q) if (j-i)%q in squares)


def triangular(m):
    vertices=list(combinations(range(m),2))
    return len(vertices), ((i,j) for i in range(len(vertices)) for j in range(i+1,len(vertices)) if set(vertices[i]) & set(vertices[j]))


def adjacency(graph):
    n,edges=graph
    A=[[0]*n for _ in range(n)]
    for u,v in edges:
        assert 0<=u<n and 0<=v<n and u!=v
        A[u][v]=A[v][u]=1
    return A


def srg_parameters(A):
    v=len(A)
    degrees=[sum(row) for row in A]
    assert len(set(degrees))==1
    k=degrees[0]
    assert 0<k<v-1
    lam=set();mu=set()
    for i in range(v):
        for j in range(i+1,v):
            common=sum(A[i][l]*A[l][j] for l in range(v))
            (lam if A[i][j] else mu).add(common)
    assert len(lam)==len(mu)==1
    lam,mu=next(iter(lam)),next(iter(mu))
    assert mu>0
    return v,k,lam,mu


def predicted(A,h):
    v,k,lam,mu=srg_parameters(A)
    s=2*k-lam+mu
    p=mu*v
    # The product of the two scalar Pade denominator factors.
    D=F(144)+72*s*h+12*(s*s+p)*h*h+6*p*s*h**3+p*p*h**4
    adjacent=12*h*(12+6*mu*h+mu*(s-v)*h*h)/D
    nonadjacent=12*mu*h*h*(6+s*h)/D
    diag=1-k*adjacent-(v-k-1)*nonadjacent
    B=[[F(diag if i==j else adjacent if A[i][j] else nonadjacent) for j in range(v)] for i in range(v)]
    return B,adjacent,nonadjacent,diag


def matmul(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]


def verify_matrix(A,h):
    v,k,lam,mu=srg_parameters(A)
    L=[[F((k if i==j else 0)-A[i][j]) for j in range(v)] for i in range(v)]
    L2=matmul(L,L)
    B,adj,nonadj,diag=predicted(A,h)
    left=[[F(int(i==j))+h*L[i][j]/2+h*h*L2[i][j]/12 for j in range(v)] for i in range(v)]
    right=[[F(int(i==j))-h*L[i][j]/2+h*h*L2[i][j]/12 for j in range(v)] for i in range(v)]
    assert matmul(left,B)==right
    assert all(sum(row,F(0))==1 for row in B)
    assert all(B[i][j]==B[j][i] for i in range(v) for j in range(v))
    assert all(B[i][i]>0 for i in range(v))
    assert nonadj>0
    delta=v-2*k+lam-mu
    poly=12+6*mu*h-mu*delta*h*h
    assert (adj>0)==(poly>0)
    assert (adj==0)==(poly==0)
    assert (adj<0)==(poly<0)
    return 1


def main():
    examples=[('cycle5',cycle(5)),('Petersen',petersen()),('bipartite_4_4',complete_bipartite(4,4)),
              ('Paley13',paley(13)),('triangular6',triangular(6)),('triangular7',triangular(7))]
    checked=0
    for name,graph in examples:
        A=adjacency(graph)
        v,k,lam,mu=srg_parameters(A)
        delta=v-2*k+lam-mu
        for h in [F(1,4),F(1,1),F(2,1),F(4,1),F(10,1)]:
            checked+=verify_matrix(A,h)
        if delta>0:
            hstar=(3+sqrt(9+12*delta/mu))/delta
            assert hstar>0
            assert 12+6*mu*F(1,100)-mu*delta*F(1,100)**2>0
            assert 12+6*mu*F(100)-mu*delta*F(100)**2<0
            print(name,(v,k,lam,mu),'finite cutoff',repr(hstar))
        else:
            print(name,(v,k,lam,mu),'all-step positive')
    # Particular exact witness: the Petersen graph at h=4 has a negative edge entry.
    B,edge,nonedge,diag=predicted(adjacency(petersen()),F(4))
    assert edge<0 and nonedge>0 and diag>0
    print('Petersen h=4 edge:',edge,'nonedge:',nonedge,'diagonal:',diag)
    assert srg_parameters(adjacency(triangular(6)))==(15,8,4,4)
    assert srg_parameters(adjacency(triangular(7)))==(21,10,5,4)
    assert srg_parameters(adjacency(paley(13)))==(13,6,2,3)
    print('PASS:',checked,'exact rational matrix identities plus entrywise sign, symmetry, row-sum and parameter assertions')

if __name__=='__main__':
    main()
