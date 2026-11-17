"""Exact-rational checks for two-stage Radau IIA graph diffusion on balanced bicliques.

Run with Python 3: python verify.py
No nonstandard libraries are needed. These checks complement a general proof.
"""
from fractions import Fraction as F


def stability(z):
    return (F(6)-2*z)/(z*z+4*z+6)


def zeros(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def mm(A, B):
    n = len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def laplacian(m):
    n = 2*m
    L = zeros(n)
    for i in range(n):
        L[i][i] = m
        for j in range(n):
            if (i < m) != (j < m):
                L[i][j] = -1
    return L


def entry(m, i, j, x):
    a, b = stability(x), stability(2*x)
    si, sj = (1 if i < m else -1), (1 if j < m else -1)
    return (F(1, 2*m) + b*si*sj/F(2*m)
            + a*((1 if i == j else 0) - (F(1,m) if si==sj else 0)))


def ppoly(m, x):
    return 4*x**4+(36-16*m)*x**3+(16*m+36)*x*x+72*m*x+72*m


def polydiag(m, x):
    d1 = x*x+4*x+6
    d2 = 4*x*x+8*x+6
    return ppoly(m, x)/(2*m*d1*d2)


def verify():
    checked = 0
    checked_entries = 0
    for m in (2,3,4,5,6,7,9):
        n = 2*m
        L = laplacian(m)
        L2 = mm(L,L)
        for x in (F(0),F(1,2),F(1),F(3),F(4),F(6),F(8),F(11),F(12),F(16),F(40)):
            h = x/m
            A = [[entry(m,i,j,x) for j in range(n)] for i in range(n)]
            for i in range(n):
                assert sum(A[i],F(0)) == 1, ('row sum',m,x,i)
                for j in range(n):
                    assert A[i][j]==A[j][i], ('symmetry',m,x,i,j)
                    if i==j:
                        assert A[i][j]==polydiag(m,x), ('diag identity',m,x,i)
                    elif x>0:
                        assert A[i][j]>0, ('offdiagonal positivity',m,x,i,j)
                    checked_entries+=1
            D = [[(F(1) if i==j else F(0)) + F(2,3)*h*L[i][j]
                 + h*h*L2[i][j]/6 for j in range(n)] for i in range(n)]
            N = [[(F(1) if i==j else F(0)) - h*L[i][j]/3
                 for j in range(n)] for i in range(n)]
            assert mm(D,A)==N, ('rational map identity',m,x)
            checked+=1
    assert ppoly(6,F(6))==0
    assert ppoly(6,F(8))<0
    assert ppoly(5,F(8))>0
    # Elementary SOS: P_5(x)/4 = (x^2-6x-4)^2+x^3+x^2+42x+74.
    for x in (F(0),F(1,7),F(3),F(6),F(8),F(100)):
        assert ppoly(5,x)==4*((x*x-6*x-4)**2+x**3+x*x+42*x+74)
    print(f'PASS: {checked} exact-rational matrix cases; {checked_entries} checked entries; polynomial and sign witnesses verified')

if __name__ == '__main__':
    verify()
