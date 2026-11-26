#!/usr/bin/env python3
"""Reproducible finite checks for symmetric mixing on prism graphs.

Requires Python 3; NumPy and SciPy are optional for additional numerical
matrix-spectrum and linear-program checks. Exact rational tests use stdlib.
This is a finite verification supplement, not an all-n proof.
"""
from fractions import Fraction as Q
from math import cos, pi, isclose


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def charpoly_coefficients(A):
    n=len(A)
    B=[[Q(int(i==j)) for j in range(n)] for i in range(n)]
    coeffs=[]
    for k in range(1,n+1):
        AB=matmul(A,B)
        c=-sum(AB[i][i] for i in range(n))/k
        coeffs.append(c)
        B=[[AB[i][j]+(c if i==j else Q(0)) for j in range(n)] for i in range(n)]
    return coeffs


def roots_poly(roots):
    p=[Q(1)]
    for r in roots:
        q=[Q(0)]*(len(p)+1)
        for i,coef in enumerate(p):
            q[i]+=coef
            q[i+1]-=coef*r
        p=q
    return p[1:]


def prism_matrix(n,a,b):
    M=[[Q(0) for _ in range(2*n)] for _ in range(2*n)]
    for layer in range(2):
        for i in range(n):
            v=layer*n+i
            M[v][v]+=1-2*a-b
            M[v][layer*n+(i-1)%n]+=a
            M[v][layer*n+(i+1)%n]+=a
            M[v][(1-layer)*n+i]+=b
    return M


def rational_case(n):
    dmin={3:Q(3),4:Q(2),6:Q(1)}[n]
    dmax={3:Q(3),4:Q(4),6:Q(4)}[n]
    D=dmax+2*dmin
    a=Q(2)/D
    b=dmin/D
    mu=dmax/D
    M=prism_matrix(n,a,b)
    assert all(sum(row)==1 and all(x>=0 for x in row) for row in M)
    assert all(M[i][j]==M[j][i] for i in range(2*n) for j in range(2*n))
    dk={3:[0,3,3],4:[0,2,4,2],6:[0,1,3,4,3,1]}[n]
    roots=[Q(1)-a*d for d in dk]+[Q(1)-a*d-2*b for d in dk]
    assert charpoly_coefficients(M)==roots_poly(roots)
    assert abs(max(abs(r) for r in roots if r != 1)-mu) == 0
    return n,a,b,mu


def numeric_case(n):
    import numpy as np
    from scipy.optimize import linprog
    u=2*(1-cos(2*pi/n))
    v=2*(1-cos(2*pi*(n//2)/n))
    den=v+2*u
    a,b,mu=2/den,u/den,v/den
    assert a>=0 and b>=0 and 2*a+b<=1+1e-13
    # Full real matrix, independent of Fourier block calculation.
    M=np.array(prism_matrix(n,a,b),dtype=float)
    eig=np.linalg.eigvalsh(M)
    assert abs(eig[-1]-1)<2e-12
    observed=max(abs(eig[:-1]))
    assert abs(observed-mu)<2e-10,(n,observed,mu)
    # Independently optimize all orbit-averaged probabilities by linear programming.
    rows=[]; bounds=[]
    for d,c in [(u,0),(v,0),(0,2),(v,2)]:
        rows.extend([[-d,-c,-1],[d,c,-1]])
        bounds.extend([-1,1])
    rows.append([2,1,0]); bounds.append(1)
    r=linprog([0,0,1],A_ub=rows,b_ub=bounds,bounds=[(0,None)]*3,method='highs')
    assert r.success
    assert abs(r.fun-mu)<5e-8
    assert abs(r.x[0]-a)<5e-8
    assert abs(r.x[1]-b)<5e-8
    return n,a,b,mu

if __name__ == '__main__':
    for n in (3,4,6):
        rational_case(n)
    print('EXACT_RATIONAL_CHARPOLY: 3 cases (6, 8, 12 vertices) passed')
    try:
        import numpy
        import scipy
    except ImportError:
        print('NUMERICAL_OPTIONAL_SKIPPED: install NumPy and SciPy for numerical checks')
    else:
        for n in range(3,61):
            numeric_case(n)
        print('MATRIX_SPECTRA_AND_LP: 58 sizes, 6 to 120 vertices, passed')
    print('PRISM_VERIFICATION_OK')
