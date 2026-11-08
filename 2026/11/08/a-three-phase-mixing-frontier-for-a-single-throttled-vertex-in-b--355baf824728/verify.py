#!/usr/bin/env python3
"""Reproducibility checks for the one-vertex-throttled bipartite mixing frontier.
Run with Python 3 standard library only: python verify.py
The finite calculations support, but do not replace, the all-size proof.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def parameters(m, b):
    assert m >= 3 and 0 <= b <= 1
    if b <= 1 / (m + 1):
        a = 1 / m
        r = (1 - (m + 1) * b + sqrt((1 - (m + 1) * b)**2 + 4 * m * (m - 1) * (1 - b))) / (2 * m)
        regime = 1
    elif b <= 2 / 3:
        a = (2*m - (m+1)*b) / (m * (2*m-1))
        r = sqrt((2*(m+1)*b*b - 4*m*b + 2*m-1) / (2*m-1))
        regime = 2
    else:
        A = m * (3*m - 1)
        B = (3*m + 1) * b - 8*m + 2
        C = 4 - 2 * (m + 1)*b/m
        disc = B*B - 4*A*C
        assert disc > -1.e-10
        a = (-B - sqrt(max(0, disc))) / (2*A)
        r = 1 - m*a
        regime = 3
    return a, r, regime


def eigenvalues(m, b, a):
    # Orbit quotient has two nonstationary roots of x^2-Tx+D.
    T = 2 - (m+1)*b/m - (2*m-1)*a
    D = 1 - (m+1)*b/m + a*(2*b*m-2*m+1)
    det = T*T - 4*D
    assert det > -1.e-9, (m, b, a, det)
    tplus, tminus = (T+sqrt(max(0,det)))/2, (T-sqrt(max(0,det)))/2
    alpha = 1-m*a
    beta = 1-b/m-(m-1)*a
    return tplus, tminus, alpha, beta


def rho(m, b, a):
    tplus, tminus, alpha, beta = eigenvalues(m,b,a)
    return max(abs(tplus), abs(tminus), abs(alpha), abs(beta))


def exact_checks():
    n = 0
    for m in range(3, 16):
        for j in range(0, 101):
            b = F(j, 100)
            # Rational identities for the characteristic polynomial and regime 2.
            a = (2*m - (m+1)*b) / (m * (2*m-1))
            T = 2 - F(m+1,m)*b - (2*m-1)*a
            D = 1 - F(m+1,m)*b + a*(2*b*m-2*m+1)
            assert T == 0
            r2 = (2*(m+1)*b*b - 4*m*b + 2*m-1) / (2*m-1)
            assert -D == r2
            alpha = 1-m*a
            beta = 1-b/m - (m-1)*a
            assert r2-alpha*alpha == F((m-1), (2*m-1)**2)*(3*b-2)*((m+1)*b-2*m)
            assert r2-beta*beta == (3*b-2)*(b*(m*m+2*m-2)-2*m*(m-1)) / (2*m-1)**2
            # polynomial evaluating at alpha, as used for the high-b constraint.
            A = m*(3*m-1)
            B = (3*m+1)*b - 8*m+2
            C = 4-F(2*(m+1),m)*b
            qminus = (-alpha)**2-T*(-alpha)+D
            assert qminus == A*a*a+B*a+C
            n += 1
    return n


def full_matrix_check(m, b, a):
    # Build 2m x 2m symmetric stochastic matrix using exact rational values.
    P = [[F(0) for _ in range(2*m)] for _ in range(2*m)]
    for i in range(m):
        for j in range(m, 2*m):
            w = b/m if i == 0 else a
            P[i][j] = P[j][i] = w
    for i in range(2*m):
        P[i][i] = 1 - sum(P[i])
        assert P[i][i] >= 0
        assert sum(P[i]) == 1
    assert all(P[i][j] == P[j][i] for i in range(2*m) for j in range(2*m))
    # Internal A' and V differences are eigenvectors with expected eigenvalues.
    alpha = 1-m*a
    beta = 1-b/m-(m-1)*a
    for i,j,z in ((1,2,alpha),(m,m+1,beta)):
        v = [F(0)]*(2*m)
        v[i],v[j] = F(1),F(-1)
        assert [sum(P[k][l]*v[l] for l in range(2*m)) for k in range(2*m)] == [z*v[k] for k in range(2*m)]


def jacobi_spectral_norm(mat):
    # Symmetric Jacobi eigenvalue algorithm used only for small finite cross-checks.
    n=len(mat)
    a=[row[:] for row in mat]
    for _ in range(70*n*n):
        best=0.0; p=q=0
        for i in range(n):
            for j in range(i+1,n):
                if abs(a[i][j])>best:
                    best=abs(a[i][j]);p=i;q=j
        if best<1.e-12: break
        tau=(a[q][q]-a[p][p])/(2*a[p][q])
        t=(1 if tau>=0 else -1)/(abs(tau)+sqrt(1+tau*tau))
        c=1/sqrt(1+t*t); si=t*c
        apq=a[p][q];app=a[p][p];aqq=a[q][q]
        a[p][p]=app-t*apq
        a[q][q]=aqq+t*apq
        a[p][q]=a[q][p]=0.0
        for k in range(n):
            if k==p or k==q:continue
            akp,akq=a[k][p],a[k][q]
            a[k][p]=a[p][k]=c*akp-si*akq
            a[k][q]=a[q][k]=si*akp+c*akq
    else:
        raise AssertionError('Jacobi did not converge')
    return max(abs(a[i][i]) for i in range(n))


def extensive_checks():
    count, numerical_comparisons = 0, 0
    rnd=Random(173)
    for m in [3,4,5,6,7,8,10,13,16,25,50]:
        for j in range(0, 101):
            b=j/100
            a,r,regime=parameters(m,b)
            assert 0 <= a <= 1/m+1e-12
            assert b/m+(m-1)*a <= 1+1e-12
            assert abs(rho(m,b,a)-r)<1e-8,(m,b,regime,a,r,rho(m,b,a))
            for k in range(301):
                aq=k/(300*m)
                assert rho(m,b,aq) >= r-1e-8, (m,b,regime,aq,rho(m,b,aq),r)
                numerical_comparisons+=1
            count+=1
    for m in range(3,8):
        for b in [F(0),F(1,10),F(1,m+1),F(1,2),F(2,3),F(4,5),F(1)]:
            aa=[F(1,m), F(2*m-(m+1)*b, m*(2*m-1))]
            # Other legal values, including middle and end.
            aa.extend([F(1,2*m), F(1,3*m)])
            for a in aa:
                if a>=0 and a<=F(1,m):
                    full_matrix_check(m,b,a)
    # Random unsymmetrized feasible matrices; no false stronger optimization claims.
    # A random weighted bipartite matrix is feasible if each column and row sum <= 1.
    for m in range(3,7):
        for _ in range(60):
            b=rnd.random()
            aopt,ropt,_=parameters(m,b)
            weights=[[0.0]*m for i in range(m)]
            # Random nonuniform entries from distinguished row summing to b.
            raw=[rnd.random() for _ in range(m)]; s=sum(raw)
            weights[0]=[b*x/s for x in raw]
            for i in range(1,m):
                for j in range(m):
                    weights[i][j]=rnd.random()/(2*m)
            # Symmetry averaging gives a feasible orbit representative with the same b.
            a=sum(weights[i][j] for i in range(1,m) for j in range(m))/(m*(m-1))
            assert rho(m,b,a)>=ropt-1e-9
            P=[[0.0]*(2*m) for _ in range(2*m)]
            for i in range(m):
                for j in range(m):
                    P[i][m+j]=P[m+j][i]=weights[i][j]
            for i in range(2*m):
                P[i][i]=1-sum(P[i]); assert P[i][i]>=-1e-12
            centered=[[P[i][j]-1/(2*m) for j in range(2*m)] for i in range(2*m)]
            brute=jacobi_spectral_norm(centered)
            assert brute>=rho(m,b,a)-1.e-9,(m,b,brute,rho(m,b,a))
            assert brute>=ropt-1.e-9
    return count,numerical_comparisons

if __name__ == '__main__':
    count = exact_checks()
    n,comparisons=extensive_checks()
    print('VERIFY_OK: rational algebra instances:',count,'parameter instances:',n,'one-dimensional comparisons:',comparisons)
