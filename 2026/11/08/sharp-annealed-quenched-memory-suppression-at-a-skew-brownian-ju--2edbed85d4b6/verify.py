#!/usr/bin/env python3
"""Independent exact and high-precision checks of a skew Brownian flux-variance theorem."""
from fractions import Fraction as F
from math import isclose
import mpmath as mp

mp.mp.dps = 55

def g(x,t,D=1):
    return mp.exp(-x*x/(4*D*t))/mp.sqrt(4*mp.pi*D*t)

def Phi(z):
    return mp.erfc(-z/mp.sqrt(2))/2

def A(x,t,L=1,D=1):
    h=mp.sqrt(2*D*t)
    return Phi((L-x)/h)-Phi(-x/h)

def B(x,t,L=1,D=1):
    h=mp.sqrt(2*D*t)
    return Phi((L+x)/h)-Phi(x/h)

def avg(f,L=1):
    return mp.quad(f,[0,L/2,L])/L

def mv(t,L=1,D=1):
    aa=avg(lambda x:A(x,t,L,D),L)
    bb=avg(lambda x:B(x,t,L,D),L)
    va=avg(lambda x:A(x,t,L,D)**2,L)-aa*aa
    vb=avg(lambda x:B(x,t,L,D)**2,L)-bb*bb
    cov=avg(lambda x:A(x,t,L,D)*B(x,t,L,D),L)-aa*bb
    return va,vb,cov

def beta0(t):
    va,vb,cov=mv(t)
    return -cov/vb

checks=0
# Fraction arithmetic, independent from the symbolic covariance derivation.
def variance_monomials(i,j):
    return F(1,i+j+1)-F(1,i+1)*F(1,j+1)
for b in [F(-1),F(0),F(1),F(1,3),F(-1,61),F(7,8)]:
    h=1+b;k=b-1
    covpoly=h*h*variance_monomials(2,2)+2*h*k*variance_monomials(1,2)+k*k*variance_monomials(1,1)
    assert covpoly == (61*b*b+2*b+1)/180
    assert covpoly>0
    checks+=2
assert (61*F(-1,61)**2+2*F(-1,61)+1)==F(60,61)
checks+=1
# Test propagator against independently quadrature-integrated probability.
for t in [mp.mpf('0.01'),mp.mpf('0.37'),mp.mpf('3.5')]:
    for x in [mp.mpf('0.13'),mp.mpf('0.6'),mp.mpf('0.98')]:
        for b in [mp.mpf('-0.7'),mp.mpf('0'),mp.mpf('0.43'),mp.mpf('1')]:
            via_kernel=mp.quad(lambda y:g(y-x,t)+b*g(y+x,t),[0,mp.mpf('0.5'),1])
            via_cdf=A(x,t)+b*B(x,t)
            assert abs(via_kernel-via_cdf)<mp.mpf('1e-40')
            checks+=1
# Compare direct Bernoulli variance difference to quadratic covariance.
for t in [mp.mpf('0.005'),mp.mpf('0.03'),mp.mpf('0.2'),mp.mpf('1'),mp.mpf('3')]:
    va,vb,cov=mv(t)
    assert vb>0
    for b in [mp.mpf('-1'),mp.mpf('0'),mp.mpf('0.71'),mp.mpf('1')]:
        S=lambda x: A(x,t)+b*B(x,t)
        m=avg(S)
        diff=avg(lambda x:S(x)**2)-m*m
        quad=va+2*b*cov+b*b*vb
        assert abs(diff-quad)<mp.mpf('1e-40')
        assert diff>0
        checks+=2
# The optimum moves from near reflecting to slightly transmitting.
for t,lo,hi in [('0.01','0.70','0.82'),('0.1','0.10','0.18'),('1','-0.02','0'),('10','-0.02','-0.01'),('1000','-0.01640','-0.01638')]:
    value=beta0(mp.mpf(t))
    assert mp.mpf(lo)<value<mp.mpf(hi), (t,value)
    checks+=1
# Check the dimensionful uniform t^-3 polynomial for three interface biases.
for b in [mp.mpf('-1')/61,mp.mpf('0'),mp.mpf('1')]:
    va,vb,cov=mv(mp.mpf(1000))
    direct=(va+2*b*cov+b*b*vb)*mp.pi*(1000)**3
    target=(61*b*b+2*b+1)/11520
    assert abs(direct/target-1)<mp.mpf('0.001'), (b,direct,target)
    checks+=1
print('PASS',checks,'exact/numeric assertions; beta0(0.01), beta0(1), beta0(1000)=',*[mp.nstr(beta0(mp.mpf(t)),15) for t in ['0.01','1','1000']])
