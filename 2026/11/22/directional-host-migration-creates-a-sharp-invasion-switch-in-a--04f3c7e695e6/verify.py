#!/usr/bin/env python3
"""Reproduce exact two-patch next-generation identities with rational arithmetic.

This finite checker supplements, and does not replace, the analytic proof.
"""
from fractions import Fraction as F
from math import sqrt
from itertools import product


def mm(X, Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def inv(X):
    d = X[0][0]*X[1][1] - X[0][1]*X[1][0]
    assert d != 0
    return [[X[1][1]/d, -X[0][1]/d],[-X[1][0]/d, X[0][0]/d]]


def tr(X):
    return X[0][0]+X[1][1]


def det(X):
    return X[0][0]*X[1][1]-X[0][1]*X[1][0]


def calc(c, xi, n, p, q, m):
    h = [[1+m*p,-m*q],[-m*p,1+m*q]]
    v = [[1+n,-n],[-n,1+n]]
    A = [[c*xi,F(0)],[F(0),c/xi]]
    B = [[c/xi,F(0)],[F(0),c*xi]]
    K = mm(mm(mm(inv(h),A),inv(v)),B)
    P = p+q
    a = (1+n)/(1+2*n)
    b = n/(1+2*n)
    T = (q/xi**2+p*xi**2)/P
    target_trace = c**2*(2*a+m*P*(a+b*T))/(1+m*P)
    target_det = c**4/((1+2*n)*(1+m*P))
    assert tr(K) == target_trace
    assert det(K) == target_det
    discr = float(tr(K)**2-4*det(K))
    assert discr >= -1e-12
    rho = (float(tr(K)) + sqrt(max(0.0,discr)))/2
    return K,rho,P,T,a,b


def main():
    cases = 0
    cs = [F(1,3),F(1,2),F(4,5),F(3,2)]
    xis = [F(3,2),F(2),F(4)]
    ps = [F(1),F(2),F(9)]
    qs = [F(1),F(5)]
    ns = [F(1,10),F(1),F(3)]
    ms = [F(0),F(1,10),F(1,3),F(1),F(10)]
    for c,xi,p,q,n in product(cs,xis,ps,qs,ns):
        rhos=[]
        for m in ms:
            _,rho,P,T,a,b=calc(c,xi,n,p,q,m)
            rhos.append(rho)
            cases+=1
        if T>1:
            assert all(rhos[i+1]>rhos[i]+1e-12 for i in range(len(ms)-1))
        elif T<1:
            assert all(rhos[i+1]<rhos[i]-1e-12 for i in range(len(ms)-1))
        else:
            assert max(rhos)-min(rhos)<1e-12
        assert abs(rhos[0]-float(c**2)) < 1e-12
        for m in ms:
            # Check the second route is essential: with immobile vectors,
            # rho(K) is exactly the constant square of local reproduction.
            _,r0,_,_,_,_=calc(c,xi,F(0),p,q,m)
            assert abs(r0-float(c*c))<1e-12
    c,xi,n,p,q=F(1,2),F(4),F(1),F(9),F(1)
    mstar=F(44,235)
    assert calc(c,xi,n,p,q,F(0))[1] == 0.25
    assert calc(c,xi,n,p,q,mstar)[1] == 1.0
    assert calc(c,xi,n,p,q,F(1))[1] > 1
    for m in [F(0),mstar,F(1,2),F(5)]:
        K,_,P,T,a,b=calc(c,xi,n,p,q,m)
        assert (1-tr(K)+det(K)) == (F(44)-F(235)*m)/(F(64)*(1+F(10)*m))
    assert F(1,4)*(F(2,3)+F(1,3)*F(461,32)) == F(175,128)
    # Check the exact switch location: p/q=xi^-2 makes T=1.
    assert calc(F(1,2),F(2),F(1),F(1),F(4),F(1))[3]==1
    print(f'PASS: {cases} exact trace/determinant certificates, monotonicity samples, boundary and rational threshold.')


if __name__=='__main__':
    main()
