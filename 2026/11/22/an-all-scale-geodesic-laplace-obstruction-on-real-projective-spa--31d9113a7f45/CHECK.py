#!/usr/bin/env python3
"""Supplementary exact identities and independent numerical quadrature."""
import math

def P(n,x):
    if n == 0: return 1.
    p,q=1.,x
    if n == 1: return q
    for j in range(1,n):
        p,q=q,((2*j+1)*x*q-j*p)/(j+1)
    return q

def simpson(f,steps=8192):
    assert steps%2 == 0
    b=math.pi/2
    s=f(0)+f(b)
    for j in range(1,steps):
        s+=(4 if j%2 else 2)*f(b*j/steps)
    return s*b/(3*steps)

def coeff(a,n):
    return 2*simpson(lambda th:math.exp(-a*th)*P(2*n,math.cos(th))*math.sin(th))

def residual(a,n):
    l=2*n
    p0=(-1)**n*math.comb(2*n,n)/4**n
    J=simpson(lambda th:a*math.exp(-a*th)*(a*math.sin(th)-math.cos(th))*P(l,math.cos(th)))
    return coeff(a,n)+2*(a*math.exp(-a*math.pi/2)*p0+J)/(l*(l+1))

checks=0
for a in (0.2,1.,3.):
    for n in (1,2,3,5,10,20):
        got=residual(a,n)
        assert abs(got)<2e-10,(a,n,got)
        checks+=1
# Negative eigenvalue examples, not used to prove universal sign.
for a,n in [(0.2,2),(1.,20),(0.1,4)]:
    value=coeff(a,n)
    print('example',a,n,value)
    if value < 0: checks+=1
# Positive Fourier coefficients of the projective line.
for a in (0.2,1.,3.):
    for k in range(0,30):
        exact=a*(1-(-1)**k*math.exp(-a*math.pi/2))/(a*a+4*k*k)
        numerical=simpson(lambda th:math.exp(-a*th)*math.cos(2*k*th))
        assert abs(exact-numerical)<2e-10 and exact>0,(a,k)
        checks+=1
print('VERIFY_OK',checks)
