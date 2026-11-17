#!/usr/bin/env python3
"""Finite diagnostics for normalized stretched-scale Laplace Gram determinants.
Requires Python 3, NumPy and mpmath; analytic proofs appear in RESULT.md.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps=85

def minus_log_product(alpha, c, n):
    x = np.arange(1, n+1, dtype=float)**alpha
    s = 0.0
    for i in range(n-1):
        u = (c/2) * (x[i+1:]-x[i])
        s -= 2.0*np.sum(np.log(-np.expm1(-2*u))-np.log1p(np.exp(-2*u)))
    return float(s)


def direct_det_log(alpha, c, n):
    a, cc = mp.mpf(str(alpha)), mp.mpf(str(c))
    z = [mp.power(j, a) for j in range(1,n+1)]
    g = mp.matrix([[mp.sech((cc/2)*abs(z[i]-z[j])) for j in range(n)] for i in range(n)])
    return float(-mp.log(mp.det(g)))


def critical_sum(c,n):
    return -2.0*sum((n-k)*math.log(math.tanh(c*k/2)) for k in range(1,n))


def run():
    count=0
    for a in (0.4,0.7,1.0,1.3,1.8):
        for c in (0.8,1.5,2.2):
            for n in (2,3,4,6,8,10,14):
                p=minus_log_product(a,c,n)
                d=direct_det_log(a,c,n)
                assert abs(p-d)<1e-6*(1+abs(d)), (a,c,n,p,d)
                count+=1
    for c in (0.8,1.2,2.2):
        for n in (2,3,4,5,8,12,30):
            assert abs(minus_log_product(1.0,c,n)-critical_sum(c,n))<1e-9
            count+=1
    for a in (0.4,0.7):
        for n in (500,1000,1800):
            ratio=minus_log_product(a,1.5,n)/n**(2-a)
            target=math.pi**2/(2*1.5*a*(2-a))
            assert 0<ratio<target
            count+=1
    for a in (1.25,1.5):
        d=[minus_log_product(a,1.5,n) for n in (50,100,250)]
        assert 0<d[0]<d[1]<d[2]
        assert d[2]-d[1]<d[1]-d[0]
        count+=1
    print(f'PASS: {count} finite assertions; not an infinite proof')

if __name__=='__main__':
    run()
