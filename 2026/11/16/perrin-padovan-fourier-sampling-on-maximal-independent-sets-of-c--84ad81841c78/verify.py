"""Finite, reproducible tests for maximal-independent-set cyclic Fourier covariance.
Python 3 standard library only; the general theorem is proved separately.
"""
from fractions import Fraction
from itertools import product
from math import acos, cos, pi, sqrt


def coefficients(n):
    a = [0] * (n+1)
    a[0] = 1
    for d in range(1, n+1):
        a[d] = (a[d-2] if d>=2 else 0)+(a[d-3] if d>=3 else 0)
    P=[0]*(n+1)
    P[0:3]=[3,0,2]
    for d in range(3,n+1): P[d]=P[d-2]+P[d-3]
    return a,P[n]


def model(n):
    a,P=coefficients(n)
    p=Fraction(a[n],P)
    row=[Fraction(a[d]*a[n-d],P)-p*p for d in range(n)]
    return P,p,row


def configurations(n):
    return [x for x in product((0,1),repeat=n)
            if all(not (x[i] and x[(i+1)%n]) and
                   (x[(i-1)%n] or x[i] or x[(i+1)%n]) for i in range(n))]


def fourier_eigenvalues(row):
    n=len(row)
    return [sum(float(row[d])*cos(2*pi*k*d/n) for d in range(n)) for k in range(n)]


def rational_rank(matrix):
    A=[list(row) for row in matrix]
    n=len(A);rank=0
    for j in range(n):
        i=next((i for i in range(rank,n) if A[i][j]),None)
        if i is None: continue
        A[rank],A[i]=A[i],A[rank]
        q=A[rank][j]
        for c in range(j,n): A[rank][c]/=q
        for i in range(rank+1,n):
            q=A[i][j]
            if q:
                for c in range(j,n): A[i][c]-=q*A[rank][c]
        rank+=1
    return rank


def run():
    count=0
    for n in range(3,16):
        configurations_n=configurations(n)
        P,p,row=model(n)
        assert P==len(configurations_n)
        assert p==Fraction(sum(x[0] for x in configurations_n),P)
        for d in range(n):
            direct=Fraction(sum(x[0]*x[d] for x in configurations_n),P)-p*p
            assert direct==row[d],(n,d,direct,row[d]);count+=1
        eigen=fourier_eigenvalues(row)
        rank_pred={3:2,4:1,5:4,6:4,7:6}.get(n,n)
        actual=rational_rank([[row[(j-i)%n] for j in range(n)] for i in range(n)])
        assert actual==rank_pred,(n,actual,rank_pred)
        assert sum(v>1e-8 for v in eigen)==rank_pred,(n,eigen)
        if n>=8:
            assert min(eigen)>0
        count+=2
    alpha=1.324717957244746
    A=alpha**-2; B=alpha**-3; p=1/(2*A+3*B)
    assert abs(A+B-1)<1e-13
    Q=lambda x: 1+A*A+(4-2*A)*x+4*B*x*x
    xstar=-(2-A)/(4*B)
    assert -1<xstar<1
    cond=Q(1)/Q(xstar)
    assert abs(cond-43.42455574592406)<1e-9
    for n in (30,40,60,100,180):
        _,_,row=model(n)
        eig=fourier_eigenvalues(row)
        for k in range(n):
            limiting=p*A*B/Q(cos(2*pi*k/n))
            assert abs(eig[k]-limiting)<1e-4 if n==30 else abs(eig[k]-limiting)<1e-6
            count+=1
    print('PASS:', count, 'exact and numerical assertions;')
    print('theorem asymptotic squared condition ratio:', format(cond,'.14f'))

if __name__=='__main__':
    run()
