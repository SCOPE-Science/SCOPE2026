"""Exact finite checks for a weighted balanced double-star coherence formula.

This program supplements, but does not replace, the all-order analytical proof.
Requires only the Python standard library. Run: python verify_double_star.py
"""
from fractions import Fraction as Q
from math import isclose, sqrt


def inv(A):
    n = len(A)
    T = [[Q(A[i][j]) for j in range(n)] + [Q(int(i == j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        k = next(i for i in range(j, n) if T[i][j])
        T[j], T[k] = T[k], T[j]
        q = T[j][j]
        T[j] = [v / q for v in T[j]]
        for i in range(n):
            if i != j:
                q = T[i][j]
                T[i] = [u-q*v for u, v in zip(T[i], T[j])]
    return [t[n:] for t in T]


def observed(m, a, b):
    n = 2*m+2
    L = [[Q(0) for _ in range(n)] for _ in range(n)]
    for hub in (0, 1):
        for j in range(m):
            v = 2 + hub*m+j
            w = a
            L[hub][hub] += w
            L[v][v] += w
            L[hub][v] -= w
            L[v][hub] -= w
    L[0][0] += b
    L[1][1] += b
    L[0][1] -= b
    L[1][0] -= b
    B = inv([[u+Q(1, n) for u in row] for row in L])
    P = [[u-Q(1, n) for u in row] for row in B]
    f1 = sum(P[i][i] for i in range(n))
    f2 = sum(P[i][j]*P[j][i] for i in range(n) for j in range(n))
    return f1, f2


def formula(m, a, b):
    A1 = Q(2*m-1) + Q(1, m+1)
    A2 = Q(2*m-1) + Q(1, (m+1)**2)
    return A1/a + Q(m+1, 2)/b, A2/a**2 + Q(m)/(a*b) + Q((m+1)**2, 4)/b**2


def root(m):
    A2=2*m-1+1/(m+1)**2
    def cubic(r):
        return 2*A2*r**3+m*r*r-2*m*m*r-m*(m+1)**2
    lo, hi = 0., float(2*m+1)
    assert cubic(lo) < 0 < cubic(hi)
    for i in range(90):
        md=(lo+hi)/2
        if cubic(md)<0: lo=md
        else: hi=md
    return (lo+hi)/2


def f2(m,r):
    A2=2*m-1+1/(m+1)**2
    return (2*m+r)**2*(A2+m/r+(m+1)**2/(4*r*r))


def verify():
    count=0
    for m in range(2,7):
        for a,b in [(Q(1,7),Q(2,5)),(Q(3,5),Q(2,5)),(Q(5,17),Q(7,19))]:
            assert observed(m,a,b)==formula(m,a,b)
            count+=2
    for m in (2,3,4,5,8,16,64,512,4096):
        A1=2*m-1+1/(m+1)
        r1=sqrt(m*(m+1)/A1)
        r2=root(m)
        assert r2>0 and f2(m,r2)<f2(m,r1)
        eps = 1e-4
        assert f2(m,r2)<f2(m,r2*(1+eps))
        assert f2(m,r2)<f2(m,r2*(1-eps))
        count+=3
    for m in (10**5,10**6,10**7):
        r2=root(m)
        assert isclose(r2 / m**(2/3),4**(-1/3),rel_tol=0.05)
        count+=1
    print(f'PASS: {count} exact rational and numerical checks; numerical tests are not a proof of infinite claims')

if __name__=='__main__':
    verify()
