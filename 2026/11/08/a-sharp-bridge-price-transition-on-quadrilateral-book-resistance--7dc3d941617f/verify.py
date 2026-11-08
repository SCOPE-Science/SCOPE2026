"""Exact-arithmetic supplementary checks for the parallel-three-edge-route theorem.

Requires Python 3.10+ standard library only. Run: python verify.py
The general proof is given in RESULT.md; finite checks are not proof.
"""
from fractions import Fraction as F
from random import Random
from math import sqrt


def invert(A):
    n = len(A)
    M = [[F(x) for x in row] + [F(int(i == j)) for j in range(n)]
         for i, row in enumerate(A)]
    for j in range(n):
        pivot = next((k for k in range(j, n) if M[k][j]), None)
        if pivot is None:
            raise ValueError("singular")
        M[j], M[pivot] = M[pivot], M[j]
        v = M[j][j]
        M[j] = [z/v for z in M[j]]
        for k in range(n):
            if k != j:
                c = M[k][j]
                if c:
                    M[k] = [u - c*v for u, v in zip(M[k], M[j])]
    return [row[n:] for row in M]


def kirchhoff(m, weights):
    n = 2*m + 2
    assert len(weights) == 3*m + 1
    edges = []
    for j in range(m):
        edges += [(0, 2+2*j), (2+2*j, 3+2*j), (3+2*j, 1)]
    edges += [(0, 1)]
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for (u, v), c in zip(edges, weights):
        L[u][u] += c
        L[v][v] += c
        L[u][v] -= c
        L[v][u] -= c
    M = [[L[i][j] + F(1,n) for j in range(n)] for i in range(n)]
    Inv = invert(M)
    return n*(sum(Inv[i][i] for i in range(n))-1)


def spectral_formula(m, a, b, q):
    n = 2*m + 2
    return n*(F(m-1,a) + F(m-1,a+2*b) + F(1,(m+1)*a)
        + ((m+1)*a+2*b+2*q)/(2*m*a*b+2*q*a+4*b*q))


def g(m,r,t):
    return m-1+1/(m+1)+(m-1)/(1+2*r)+(m+1+2*r+2*t)/(2*m*r+2*t+4*r*t)


def g0(m,r):
    return g(m,r,0)


def g0p(m,r):
    return -2*(m-1)/(1+2*r)**2-(m+1)/(2*m*r*r)


def root_r(m):
    def f(r): return g0(m,r)+(r+2)*g0p(m,r)
    lo,hi = 1e-8,8.0
    assert f(lo)<0<f(hi)
    for _ in range(90):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2


def dcrit(m,r):
    return (r+2)*(m+1+4*r+4*r*r)/(2*m*r*r*g0(m,r))


def main():
    cnt = 0
    rng = Random(20261107)
    for m in range(2,7):
        for a,b,q in ((F(1),F(1),F(0)), (F(1),F(0),F(1)),
                      (F(2,3),F(3,2),F(1,5)), (F(5,4),F(2,5),F(2,3))):
            weights = [x for _ in range(m) for x in (a,b,a)]+[q]
            actual=kirchhoff(m,weights)
            expected=spectral_formula(m,a,b,q)
            assert actual == expected,(m,a,b,q,actual,expected)
            cnt+=1
    # The b=0 boundary is never optimal at unit path-edge prices:
    # direct finite-difference derivatives of the exact spectral expression.
    for m in range(2,8):
        for a,q in ((F(1),F(1)),(F(3,2),F(2,5)),(F(2,3),F(7,2))):
            z=(F(m-1,a)+F(m-1,a)+F(1,(m+1)*a)
                + ((m+1)*a+2*q)/(2*q*a))
            h=F(1,10**10)
            def tr(a,b,q): return spectral_formula(m,a,b,q)/F(2*m+2)
            left=(tr(a-h/2,h,q)-z)/h
            expected=-F(m*((m+1)**2*a*a+4*(m+1)*a*q+(2*m+3)*q*q),2*a*a*q*q*(m+1))
            assert left<0 and abs(float(left-expected))<1e-5,(m,a,q,left,expected)
            cnt+=1
    assert abs(root_r(2)-1)<1e-10
    assert abs(dcrit(2,1)-99/35)<1e-10
    cnt+=2
    for m in [2,3,4,5,6,8,10,20,50,100,1000]:
        r=root_r(m)
        dc=dcrit(m,r)
        assert 0<r<2 and dc>0
        assert abs(g0(m,r)+(r+2)*g0p(m,r))<1e-8
        assert abs((dc*g0(m,r)-(2+r)*(m+1+4*r+4*r*r)/(2*m*r*r)))<1e-8
        cnt+=2
    limit=3+3*sqrt(3)/2
    assert abs(root_r(10000)-(sqrt(3)-1)/2)<.001
    assert abs(10000*dcrit(10000,root_r(10000))-limit)<.015
    cnt+=2
    # Independent nonsymmetric competitors, exact fractions. An illustration
    # only; global optimality follows instead from strict convexity and KKT.
    m=2; d=F(4); budget=F(6)
    optimum=kirchhoff(2,[F(1)]*6+[F(0)])
    for _ in range(60):
        w=[F(rng.randint(1,12),rng.randint(1,7)) for _ in range(7)]
        C=sum(w[:6])+d*w[6]
        w=[z*budget/C for z in w]
        assert kirchhoff(m,w) >= optimum
        cnt+=1
    print("VERIFY_OK",cnt)
    print("M2 dcrit",F(99,35),"; limiting m*dcrit",limit)

if __name__ == '__main__':
    main()
