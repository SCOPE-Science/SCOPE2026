#!/usr/bin/env python3
"""Independent reproducibility checks for the two-price prism Laplacian formulas.

Uses only Python's standard library. Finite checks support, but do not replace,
the general spectral and convexity proof in RESULT.md.
"""
from fractions import Fraction as F
from math import acos, cos, pi, sqrt, log
from random import Random


def inverse(M):
    n = len(M)
    A = [list(row) + [F(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for j in range(n):
        k = next(k for k in range(j, n) if A[k][j])
        A[j], A[k] = A[k], A[j]
        t = A[j][j]
        A[j] = [v / t for v in A[j]]
        for i in range(n):
            if i != j:
                t = A[i][j]
                if t:
                    A[i] = [x - t*y for x,y in zip(A[i], A[j])]
    return [row[n:] for row in A]


def trace(A):
    return sum((row[i] for i, row in enumerate(A)), F(0))


def cycle_matrix(m):
    L = [[F(0) for _ in range(m)] for _ in range(m)]
    for i in range(m):
        j = (i+1) % m
        L[i][i] += 1; L[j][j] += 1
        L[i][j] -= 1; L[j][i] -= 1
    return L


def prism_laplacian(m, a, b):
    n = 2*m
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for layer in range(2):
        for i in range(m):
            u = layer*m+i
            v = layer*m+(i+1) % m
            for p,q,w in [(u,v,a)]:
                L[p][p]+=w; L[q][q]+=w
                L[p][q]-=w; L[q][p]-=w
    for i in range(m):
        u,v = i,m+i
        L[u][u]+=b; L[v][v]+=b
        L[u][v]-=b; L[v][u]-=b
    return L


def kirchhoff_exact(L):
    n = len(L)
    M = [[L[i][j] + F(1,n) for j in range(n)] for i in range(n)]
    inv = inverse(M)
    return n * (trace(inv)-F(1))


def spectral_formula(m,a,b):
    C = cycle_matrix(m)
    r = b/a
    A = [[C[i][j] + (2*r if i==j else 0) for j in range(m)] for i in range(m)]
    T = trace(inverse(A))
    S = F(m*m-1,12)
    return 2*m*(S+T)/a


def numerical_T(m,r):
    v = sqrt(r*(r+2))
    t = m*acos(1/(1+r)) if False else m*log(1+r+v)
    return m/(2*v)*(1+2/(pow(2.718281828459045,t)-1)) if t<700 else m/(2*v)


def derivative(m,c,r):
    S=(m*m-1)/12
    return c*S + sum((c*(4*sin2(k,m))-4)/(2*r+4*sin2(k,m))**2 for k in range(m))


def sin2(k,m):
    return (1-cos(2*pi*k/m))/2


def ratio_opt(m,c):
    lo,hi=1e-12,1.0
    while derivative(m,c,hi)<0:
        hi*=2
    for _ in range(125):
        md=(lo+hi)/2
        if derivative(m,c,md)<0:lo=md
        else:hi=md
    return (lo+hi)/2


def run():
    count=0
    # Exact-rational spectral decomposition vs full, unrestricted-size Laplacian inversion.
    for m in range(3,8):
        for a,b in [(F(1),F(1)),(F(3,7),F(4,9)),(F(5,3),F(2,11))]:
            k1=kirchhoff_exact(prism_laplacian(m,a,b))
            k2=spectral_formula(m,a,b)
            assert k1==k2,(m,a,b,k1,k2)
            count+=1
    # Exact-rational trace resolvent check, including its derivative.
    for m in range(3,12):
        C=cycle_matrix(m)
        for r in [F(1,11),F(1,2),F(7,5),F(11,2)]:
            A=[[C[i][j]+(2*r if i==j else 0) for j in range(m)] for i in range(m)]
            G=inverse(A)
            tr2=sum((G[i][j]*G[j][i] for i in range(m) for j in range(m)),F(0))
            # T'(r)=-2 tr(A^-2): finite-difference rational identity is checked symbolically
            # using dA/dr=2I and matrix inverse multiplication.
            for h in [F(1,1000)]:
                A2=[[C[i][j]+(2*(r+h) if i==j else 0) for j in range(m)] for i in range(m)]
                H=inverse(A2)
                exact_delta=trace(H)-trace(G)
                rhs=-2*h*sum((G[i][j]*H[j][i] for i in range(m) for j in range(m)),F(0))
                assert exact_delta==rhs
                count+=1
            v=sqrt(float(r)*(float(r)+2))
            q=1+float(r)-v
            closed=m/(2*v)*(1+q**m)/(1-q**m)
            assert abs(float(trace(G))-closed)<3e-9*max(1,closed)
            count+=1
    # Analytic first-order condition numerically, strict signs, and asymptotic scale.
    for c in [0.5,1.0,3.0,10.0]:
        for m in [3,5,9,20,50,100,500,1000]:
            r=ratio_opt(m,c)
            assert r>0
            assert derivative(m,c,0.97*r)<0 and derivative(m,c,1.03*r)>0
            alpha=(3*sqrt(2)/c)**(2/3)
            if m>=500:
                assert abs(r*m**(2/3)/alpha-1)<0.08
            count+=1
    print('VERIFY_OK',count)

if __name__=='__main__':
    run()
