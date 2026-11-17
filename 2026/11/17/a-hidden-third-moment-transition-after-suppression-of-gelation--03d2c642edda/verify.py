#!/usr/bin/env python3
"""Finite checks for the stationary coagulation--shattering moment threshold."""
from fractions import Fraction
from math import sqrt, log

def exact_prefix(lam, nmax=32):
    a = [Fraction(0)]*(nmax+1)
    a[1] = lam/(1+lam)
    for k in range(2,nmax+1):
        conv = sum(a[i]*a[k-i] for i in range(1,k))
        a[k] = Fraction(k, 2*(k+lam))*conv
        assert 2*(k+lam)*a[k] == k*conv
    assert all(x > 0 for x in a[1:])
    return a

def float_prefix(lam, nmax=3500):
    import numpy as np
    a=np.zeros(nmax+1, dtype=float)
    a[1]=lam/(1+lam)
    vals={}
    for k in range(2,nmax+1):
        a[k] = (k/(2*(k+lam)))*float(np.dot(a[1:k],a[k-1:0:-1]))
        if k in (500,1000,2000,3500):
            j=np.arange(1,k+1, dtype=float)
            vals[k] = float(np.dot(j*j,a[1:k+1]))
    return vals

def main():
    exact_prefix(Fraction(9,2))
    for lam in (4.2,4.5,5.0):
        m=(lam-sqrt(lam*(lam-4)))/2
        nums=float_prefix(lam)
        assert all(nums[b]>nums[a] for a,b in zip((500,1000,2000),(1000,2000,3500)))
        if lam == 5.0:
            theoretical=lam/(lam-3*m)
            assert nums[3500]<theoretical and nums[3500]>5
            print('finite_side',lam,'partial_M3',round(nums[3500],9),'limit_M3',round(theoretical,9))
        elif lam == 4.5:
            assert 0.9 < (nums[3500]-nums[1000])/(3*log(3500/1000)) < 1.1
            print('critical_side',lam,'partial_M3',round(nums[3500],9),'log_increment_ratio',round((nums[3500]-nums[1000])/(3*log(3.5)),6))
        else:
            print('divergent_side',lam,'partial_M3',round(nums[3500],9))
    print('VERIFY_OK exact_rational_coefficients=32 numeric_rates=3; FINITE_TEST_ONLY')

if __name__=='__main__':main()
