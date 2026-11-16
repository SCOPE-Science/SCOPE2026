#!/usr/bin/env python3
"""Reproduce the stated two-hop cyclic Fourier multiplier extremum.

All test cases are finite supplemental checks; the universal theorem is analytical.
"""
import math
import numpy as np


def analytic(n):
    if n == 3:
        return (0.0, math.sqrt(3.0))  # second optimum at b=1
    if n % 2 == 0:
        s=math.sin(math.pi/n)
        b=(math.sqrt(1+s*s)-s)**2
        return b,2*(1-b)
    d=math.cos(math.pi/n)
    c=math.cos(2*math.pi/n)
    h=1+d-c
    b=1/(h+math.sqrt(h*h-1)) # stable small root
    return b,2*math.sqrt(b*(1-c)*(1+d))


def direct(n,b):
    S=np.zeros((n,n))
    for j in range(n): S[(j+1)%n,j]=1
    L=np.eye(n)-(1-b)*S-b*(S@S)
    _, s, _=np.linalg.svd(L)
    return np.sort(s)[1]  # first nonzero singular


assert_count=0
for n in range(3,101):
    b,v=analytic(n)
    assert abs(direct(n,b)-v)<1e-10,(n,b,v,direct(n,b))
    assert_count+=1
    # Check the two endpoint-frequency formula over a dense b-grid.
    z=np.exp(2j*np.pi*np.arange(1,n)/n)
    xx=np.linspace(0,1,201)
    vals=np.abs((1-z)[None,:]*(1+xx[:,None]*z))
    got=vals.min(axis=1)
    if n%2==0:
        s=math.sin(math.pi/n)
        A=2*s*np.sqrt(1+xx**2+2*xx*math.cos(2*math.pi/n))
        B=2*(1-xx)
    else:
        d=math.cos(math.pi/n)
        A=2*math.sin(math.pi/n)*np.sqrt(1+xx**2+2*xx*math.cos(2*math.pi/n))
        B=np.sqrt(2*(1+d))*np.sqrt(1+xx**2-2*xx*d)
    assert np.allclose(got,np.minimum(A,B),atol=1e-12),(n,np.max(abs(got-np.minimum(A,B))))
    assert_count+=1
    assert np.max(got)<=v+1e-10,(n,got.max(),v)
    assert_count+=1
    if n>3:
        assert all(direct(n,t)<=v+1e-10 for t in [0,0.1,0.25,0.5,0.75,0.9,1]),n
        assert_count+=1
    else:
        assert abs(direct(3,1)-v)<1e-10
        assert_count+=1
print('PASS',assert_count,'independent finite assertions over n=3..100')
for n in [3,4,5,6,7,10,20,50,100]:
    b,v=analytic(n)
    print(f'n={n}: optimum_b={b:.12f}, gain={v/(2*math.sin(math.pi/n)):.12f}, gap={v:.12f}')
