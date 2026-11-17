"""Finite checks for fixed-order Floater--Hormann variation asymptotics.

Requires Python 3.10+, NumPy and SciPy. This script corroborates algebra
and finite-n examples; the all-n theorem is proved separately.
"""
import math
from math import comb, pi, log
import numpy as np
from numpy.polynomial.legendre import leggauss
from fractions import Fraction


def coefficients(n, d):
    assert n >= 2*d and d >= 1
    return [sum(comb(d, k) for k in range(max(0, i-(n-d)), min(i, d)+1))
            for i in range(n+1)]


def weighted_coefficients(n, d):
    return [(-1)**i * b for i, b in enumerate(coefficients(n,d))]


def variation(n, d, q=48):
    w=np.array(weighted_coefficients(n,d),dtype=float)
    nodes, gauss=leggauss(q)
    x=(np.arange(n)[:,None]+(nodes[None,:]+1)/2).reshape(-1)
    area=np.tile(gauss/2,n)
    z=x[:,None]-np.arange(n+1)[None,:]
    a=w[None,:]/z
    ap=-a/z
    den=a.sum(axis=1)
    denp=ap.sum(axis=1)
    numerator=np.flip(np.cumsum(np.flip(a,axis=1),axis=1),axis=1)[:,1:]
    numeratorp=np.flip(np.cumsum(np.flip(ap,axis=1),axis=1),axis=1)[:,1:]
    deriv=(numeratorp*den[:,None]-numerator*denp[:,None])/den[:,None]**2
    return np.sum(abs(deriv)*area[:,None],axis=0)


def exact_checks():
    count=0
    for d in range(1,7):
        for n in range(2*d, 2*d+17):
            w=weighted_coefficients(n,d)
            assert sum(w)==0
            partial=0
            for j in range(1,n+1):
                partial+=w[j-1]
                assert abs(partial)<=2**(d-1)
                if d<=j<=n-d+1:
                    assert abs(partial)==2**(d-1)
                count+=1
            # Exact rational version of the nonvanishing-denominator bound.
            for m in range(n):
                for u in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
                    x=m+u
                    den=sum(Fraction(a,1)/(x-i) for i,a in enumerate(w))
                    assert abs(den)*u*(1-u)>=1
                    count+=1
    print('EXACT_WEIGHT_PREFIX_AND_DENOMINATOR_CHECKS_PASS',count)


def numerical_checks():
    count=0
    for d in (1,2,3,4):
        records=[]
        for n in (32,64,128,256):
            gains=variation(n,d,q=48)
            w=weighted_coefficients(n,d)
            prefix=np.cumsum(w)[:n]
            js=np.arange(1,n+1)
            profile=2*np.abs(prefix)/(pi*2**d)*(np.log(js)+np.log(n-js+1))
            residual=gains-profile
            assert np.isfinite(residual).all()
            assert np.max(np.abs(residual))<10
            records.append((n,gains.max(),gains[n//2-1],gains[0]))
            count+=n
        print('ORDER',d,'n,max,central,end',[(n,round(m,6),round(c,6),round(e,6)) for n,m,c,e in records])
        actual=records[-1][2]-records[-2][2]
        target=2/pi*log(2)
        assert abs(actual-target)<0.32
    print('FINITE_GAUSS_VARIATION_AND_LOG_SLOPE_CHECKS_PASS',count)


if __name__=='__main__':
    exact_checks()
    numerical_checks()
    print('ALL_FIXED_ORDER_FH_BV_CHECKS_PASS')
