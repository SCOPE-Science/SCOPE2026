#!/usr/bin/env python3
"""Reproduce exact rational identities and finite checks for the three-stage response theorem.

Python standard library only. Numerical tests are diagnostics, not proof of
infinite-time, all-parameter, or uniqueness assertions.
"""
from fractions import Fraction as Q
import math


def matmul(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]


def det3(M):
    return M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0]) + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])


def solve3(A, b):
    # Exact rational Cramer's rule.
    d = det3(A)
    assert d
    return [det3([[b[i] if j == k else A[i][j] for j in range(3)] for i in range(3)]) / d for k in range(3)]


def exact_checks():
    cases = [(Q(1), Q(1), Q(1)), (Q(3, 2), Q(2, 3), Q(5, 2)), (Q(4, 5), Q(7, 3), Q(2))]
    count = 0
    for c, m, kappa in cases:
        P = (m + c) / kappa
        Z = P / m
        # Equilibrium check.
        assert -P-kappa*P*Z+P+(c+m)*Z == 0
        assert P-P == 0 and P-m*Z == 0
        J = [[-(2+c/m), Q(1), Q(0)], [Q(1), Q(-1), Q(0)], [Q(0), Q(1), -m]]
        w = [Z, Q(0), -Z]
        for s in [Q(1,2), Q(2), Q(7,3), Q(5)]:
            A = [[(s if i == j else Q(0)) - J[i][j] for j in range(3)] for i in range(3)]
            u = solve3(A, w)
            lhs = sum(u)
            det = (s+m)*(s*s+(3+c/m)*s+(1+c/m))
            rhs = Z/m*((m*m-m-c)*s+(2*m*m-c))/det
            assert lhs == rhs, (c,m,s,lhs,rhs)
            count += 1
        a = m*m-m-c
        assert sum(sum(J[i][j]*w[j] for j in range(3)) for i in range(3)) == Z*a/m
        Nstar = lambda mm: (mm+c)*(2+1/mm)/kappa
        derivative = (2-c/m**2)/kappa
        assert (Nstar(m+Q(1,13))-Nstar(m))*13 == (2-c/(m*(m+Q(1,13))))/kappa
        assert derivative == (2-c/m**2)/kappa
    return count


def vecf(X, m, c=1.0, kap=1.0):
    x,y,z=X
    return (-x-kap*x*z+y+(c+m)*z, x-y, y-m*z)


def integrate(m=1.0, c=1.0, kap=1.0, delta=0.02, h=0.001, Tmax=35.0):
    P=(m+c)/kap
    X=(P,P,P/m)
    old=sum(X)
    n=int(Tmax/h)
    roots=[]
    prev_t=0.0; prev_f=0.0
    neg=pos=False
    for i in range(1,n+1):
        f1=vecf(X,m+delta,c,kap)
        X2=tuple(x+.5*h*v for x,v in zip(X,f1))
        f2=vecf(X2,m+delta,c,kap)
        X3=tuple(x+.5*h*v for x,v in zip(X,f2))
        f3=vecf(X3,m+delta,c,kap)
        X4=tuple(x+h*v for x,v in zip(X,f3))
        f4=vecf(X4,m+delta,c,kap)
        X=tuple(x+h*(a+2*b+2*d+e)/6 for x,a,b,d,e in zip(X,f1,f2,f3,f4))
        f=sum(X)-old
        t=i*h
        assert min(X)>0
        neg |= f < -1e-9
        pos |= f > 1e-9
        if prev_f < 0 and f >= 0:
            roots.append(prev_t + h*(-prev_f)/(f-prev_f))
        prev_f=f; prev_t=t
    target=(2+1/(m+delta))*(m+delta+c)/kap-old
    assert abs((sum(X)-old)-target) < 1e-8
    return roots,neg,pos


def h_reference(t):
    r=math.sqrt(2.0)
    return ((2+r)/4)*math.exp(-(2-r)*t)-math.exp(-t)+((2-r)/4)*math.exp(-(2+r)*t)


def H_reference(t):
    r=math.sqrt(2.0)
    p,q=2-r,2+r
    return ((2+r)/4)*(-math.expm1(-p*t))/p - (-math.expm1(-t)) + ((2-r)/4)*(-math.expm1(-q*t))/q


def limit_crossing():
    # For c=m=kappa=1, A=-1 and B=1, so H(t_*)=h(t_*).
    left,right=1.2,2.2
    assert H_reference(left)-h_reference(left)<0
    assert H_reference(right)-h_reference(right)>0
    for _ in range(64):
        mid=(left+right)/2
        if H_reference(mid)-h_reference(mid)<0: left=mid
        else: right=mid
    return (left+right)/2


if __name__=='__main__':
    n=exact_checks()
    tstar=limit_crossing()
    assert abs(tstar-1.6161502178)<1e-6
    for d in (.001,.01,.02,.1):
        roots,neg,pos=integrate(delta=d)
        assert neg and pos and len(roots)==1
        if d<=.01: assert abs(roots[0]-tstar)<.04
        print('shock',d,'crossing',format(roots[0],'.9f'))
    print('exact rational resolvent tests:',n)
    print('small-shock limiting crossing:',format(tstar,'.11f'))
    print('finite checks passed; analytic proof needed for universal conclusions')
