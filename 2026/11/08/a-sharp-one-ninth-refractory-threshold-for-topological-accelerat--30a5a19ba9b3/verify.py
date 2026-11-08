"""Reproduce the sharp refractory threshold for Brownian winding completion.
All quantities are dimensionless with absorbing boundaries ±1 and generator d²/dx².
Independent backward-generator finite differences validate renewal results.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.sparse import diags, lil_matrix
from scipy.sparse.linalg import spsolve


def exact_mean(r, delay):
    if r == 0:
        return 0.5
    x = math.sqrt(r)/2
    c = math.cosh(x)
    c2 = math.cosh(2*x)
    return (c2-1)/(r*c) + delay*(c2/c - 1)


def bvp_mean(r, delay, n=4001):
    # Grid on [-1, 1], absorbing endpoints, state at index (n-1)//2.
    assert n % 2 == 1
    h = 2/(n-1)
    k = n-2
    main=np.full(k,-2/h**2-r)
    near=np.full(k-1,1/h**2)
    A=diags((near,main,near),(-1,0,1),shape=(k,k),format='lil')
    rhs=np.full(k,-1.0)
    mid=(n-1)//2 - 1
    for j in range(k):
        pos=(j+1)*h-1
        if abs(pos)<0.5 - h/10:
            weight=1.0
        elif abs(abs(pos)-0.5) <= h/10:
            weight=0.5
        else:
            weight=0.0
        A[j,mid]+=r*weight
        rhs[j]-=r*delay*weight
    ans=spsolve(A.tocsr(),rhs)
    return float(ans[mid])


def coeff(n):
    # (2n)! times coefficient of x^(2n) in
    # G=(1+2x^2/9)cosh(2x) -(20x^2/9)cosh(x)-1.
    return Fraction(4**n)+Fraction(2*n*(2*n-1),9)*(Fraction(2*4**(n-1)-20))


def run():
    assert coeff(1)==0 and coeff(2)==0
    assert coeff(3)==104
    assert all(coeff(n)>0 for n in range(3,80))
    cases=0
    for r in [0.0,0.02,0.1,0.5,1.,2.,5.,12.]:
        for delay in [0.0,1/18,0.06,0.1,0.4]:
            calc=exact_mean(r,delay)
            disc=bvp_mean(r,delay,n=4001)
            assert abs(disc-calc)<0.0001, (r,delay,calc,disc)
            cases+=1
    baseline=.5
    assert exact_mean(.02,0.02)<baseline
    assert exact_mean(.02,1/18)>baseline
    assert all(exact_mean(r,1/18)>baseline for r in [0.02,0.1,0.5,1.,2.,5.,12.])
    assert all(exact_mean(r,0.1)>baseline for r in [0.02,0.1,0.5,1.,2.,5.,12.])
    # Check local derivative in r: mean(r,d)=.5+(-1/48+3d/8)*r+O(r²)
    for d in [0,0.02,.1]:
        h=.001
        slope=(exact_mean(h,d)-.5)/h
        expected=-1/48+3*d/8
        assert abs(slope-expected)<.00005,(d,slope,expected)
    print('VERIFY_OK: coefficients, small-rate expansion, 40 independent finite-difference means (absolute error < 1e-4), threshold checks')

if __name__ == '__main__':run()
