#!/usr/bin/env python3
"""Numerical cross-checks of the exact cubic-range cycle mixing theorem.

The all-size assertion is proved algebraically in RESULT.md; these finite checks
are diagnostic corroboration only, not exhaustive verification.
"""
import cmath
import math


def parameters(n):
    assert n >= 12 and n % 6 == 0
    theta = 2 * math.pi / n
    c = math.cos(theta)
    A = (1 - c) * (1 + 2 * c)
    H = 2 * c + 5 * A
    a, b = A / H, c / H
    t = (2 * c - A) / H
    return c, a, b, t


def eigenvalue(x, a, b):
    return a * (4 * x*x + 2*x - 1) + 2*b * (4*x*x*x - 3*x)


def check():
    spectral = factor = 0
    for n in range(12, 1207, 6):
        c, a, b, t = parameters(n)
        assert a > 0 and b > 0 and 0 < t < 1
        assert abs(5*a + 2*b - 1) < 5e-13
        assert abs(t - (2*b - a)) < 5e-13
        critical = (1, n//6, n//3, n//2)
        for j,sign in zip(critical,(1,-1,1,-1)):
            x = math.cos(2*math.pi*j/n)
            assert abs(eigenvalue(x,a,b)-sign*t) < 1e-11, (n,j)
        for j in range(1,n):
            x = math.cos(2*math.pi*j/n)
            lam = eigenvalue(x,a,b)
            assert -t-2e-11 <= lam <= t+2e-11, (n,j,lam,t)
            fp = 4*b*(x+1)*(2*x-1)*(x-c+1/(2*c))
            fm = 4*b*(2*x+1)*(x-c)*(x+1/(2*c))
            assert abs(lam+t-fp) < 2e-11
            assert abs(lam-t-fm) < 2e-11
            spectral += 1
            factor += 2
    vectors = 0
    for n in (12,18,24,30,36,48,60):
        c,a,b,t = parameters(n)
        P=[[0.] *n for _ in range(n)]
        for i in range(n):
            P[i][i]=a
            for k,v in [(1,a),(2,a),(3,b)]:
                P[i][(i+k)%n]=v
                P[i][(i-k)%n]=v
        for row in P:
            assert abs(sum(row)-1)<1e-12
            assert min(row)>=0
        for j in range(n):
            vec=[cmath.exp(2j*math.pi*j*i/n) for i in range(n)]
            lam=1 if j==0 else eigenvalue(math.cos(2*math.pi*j/n),a,b)
            for i in range(n):
                pvec=sum(P[i][k]*vec[k] for k in range(n))
                assert abs(pvec-lam*vec[i])<3e-12,(n,j,i)
                vectors+=1
    print('VERIFY_OK', 'spectral_checks='+str(spectral), 'factor_checks='+str(factor), 'matrix_fourier_checks='+str(vectors))


if __name__=='__main__':
    check()
