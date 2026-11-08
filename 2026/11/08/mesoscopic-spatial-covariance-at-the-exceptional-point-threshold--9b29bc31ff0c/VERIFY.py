#!/usr/bin/env python3
"""Standalone checks for a stationary directed Gaussian cascade.
Uses only Python's standard library.  Numerical tests support, not replace, proof.
"""
from fractions import Fraction
from math import comb, exp, erfc, lgamma, log, pi, sqrt


def covariance_exact(n, i, j, k, d):
    """Exact rational closed formula, sites indexed 1..n."""
    if i > j:
        i, j = j, i
    gap = j-i
    val = Fraction(0)
    for q in range(n-j+1):
        val += Fraction(comb(2*q+gap, q), 1) / (2*k)**(2*q+gap)
    return (d/k)*val


def covariance_recursion(n, k, d):
    arr = [[Fraction(0) for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            arr[i][j] = (arr[i+1][j]+arr[i][j+1]+2*d*(i==j))/(2*k)
    return arr


def covariance_float(n, i, j, k=1.0, d=1.0):
    if i > j:
        i,j = j,i
    gap = j-i
    logtwo = log(2.0)
    s = 0.0
    for q in range(n-j+1):
        t = 2*q+gap
        lp = lgamma(t+1)-lgamma(q+1)-lgamma(q+gap+1)-t*logtwo
        s += exp(lp-(t+1)*log(k))
    return d*s  # factor k**(-1) already included in exponent


def kernel(zeta, sep, d=1.0, intervals=4000):
    # u=v^2 cancels the square-root endpoint singularity.
    if intervals % 2: intervals += 1
    h = 1.0/intervals
    sm = 0.0
    for j in range(intervals+1):
        v=j*h
        f=exp(-2*zeta*v*v - sep*sep/(4*v*v)) if v>0 else (1.0 if sep==0 else 0.0)
        sm += (1 if j in (0,intervals) else (4 if j%2 else 2))*f
    return 2*d/sqrt(pi)*sm*h/3


def main():
    tests=0
    for n in range(1,12):
        for k in (Fraction(1,2),Fraction(1),Fraction(5,4),Fraction(2),Fraction(3)):
            for d in (Fraction(1,3),Fraction(1),Fraction(5,2)):
                a=covariance_recursion(n,k,d)
                for i in range(1,n+1):
                    for j in range(1,n+1):
                        assert a[i][j] == covariance_exact(n,i,j,k,d)
                        assert a[i][j]==a[j][i]
                        tests+=2
    # Finite size critical covariance at two scales, including negative detunings.
    for zeta in (-1.0,0.0,0.75):
        for sep in (0.0,0.7,1.5):
            predicted = kernel(zeta,sep)
            errors=[]
            for n in (500,2000,8000):
                i=1
                j=1+round(sep*sqrt(n))
                value=covariance_float(n,i,j,1+zeta/n)/sqrt(n)
                errors.append(abs(value-predicted))
                tests+=1
            assert errors[-1]<0.055, (zeta,sep,errors,predicted)
            assert errors[-1] <= errors[0]+0.005, (zeta,sep,errors)
    # Closed-form critical kernel for zeta=0.
    for sep in (0.0,0.15,0.7,1.5,3.0):
        ratio = kernel(0,sep)/kernel(0,0)
        claimed = exp(-sep**2/4)-sqrt(pi)*sep/2*erfc(sep/2)
        assert abs(ratio-claimed)<2e-8,(sep,ratio,claimed)
        tests+=1
    for k in (1.1,1.3,1.8):
        val=covariance_float(1000,1,1,k)
        asserted=1/sqrt(k*k-1)
        assert abs(val-asserted)<1e-10,(k,val,asserted)
        tests+=1
    print(f'PASS: {tests} exact-rational and bounded asymptotic/integral checks')

if __name__=='__main__':
    main()
