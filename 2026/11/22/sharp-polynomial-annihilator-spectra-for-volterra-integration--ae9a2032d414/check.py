#!/usr/bin/env python3
"""Exact finite checks and constructive near-extremizers for Legendre-tail integration.
All infinite limits are proved in RESULT.md rather than inferred from these tests.
"""
from fractions import Fraction as F
from math import sqrt, gamma, pi

def col2(n):
    assert n>=1
    return F(1,4*(2*n+1)*(2*n+3))+F(1,4*(2*n+1)*(2*n-1))

def off2(n):
    return F(1,16*(2*n+1)*(2*n+3)**2*(2*n+5))

def moment1(m,N):
    return sum((col2(n) for n in range(m,N+1)),F())

def moment2(m,N):
    return sum((col2(n)**2 for n in range(m,N+1)),F())+2*sum((off2(n) for n in range(m,N-1)),F())

def finite_upper(m):
    return 1/(2*sqrt((2*m+1)*(2*m+3))) + 1/(2*sqrt((2*m+1)*(2*m-1)))

def explicit_witness(m,L):
    # Alternating Legendre coefficients in every other degree.
    out={}
    for j in range(L):
        n=m+2*j
        c=(-1)**j
        a=1/(2*sqrt((2*n+1)*(2*n+3)))
        b=1/(2*sqrt((2*n+1)*(2*n-1)))
        out[n+1]=out.get(n+1,0)+c*a
        out[n-1]=out.get(n-1,0)-c*b
    return sqrt(sum(v*v for v in out.values())/L)

def run():
    checks=0
    for m in range(1,45):
        assert F(m,2*(4*m*m-1))==F(1,8)*(F(1,2*m-1)+F(1,2*m+1))
        checks+=1
        for N in range(m,m+34):
            assert col2(N)==F(1,2*(2*N-1)*(2*N+3))
            assert moment1(m,N)==F(1,8)*(F(1,2*m-1)+F(1,2*m+1)-F(1,2*N+1)-F(1,2*N+3))
            checks+=2
    for m in (60,120,300,700):
        N=2*m
        # Use end N=floor(2m), so the limit is for R=2.
        k2=float(m*moment1(m,N))
        k4=float(m**3*moment2(m,N))
        target2=(1-1/2)/8
        target4=(1-1/8)/128
        assert abs(k2-target2)<0.0025
        assert abs(k4-target4)<0.0015
        lower=m*explicit_witness(m,max(6,int(m**.4)))
        upper=m*finite_upper(m)
        assert 0.42<lower<upper and upper<0.51
        checks+=4
        print('m',m,'finite_block_2nd',round(k2,7),'limit',round(target2,7),
              'finite_block_4th',round(k4,7),'limit',round(target4,7),
              'norm_witness',round(lower,7),'norm_bound',round(upper,7))
    assert abs(gamma(1.5)/(4*sqrt(pi)*gamma(2))-1/8)<1e-13
    assert abs(gamma(2.5)/(16*3*sqrt(pi)*gamma(3))-1/128)<1e-13
    checks+=2
    print('PASS',checks,'exact/witness assertions')

if __name__=='__main__': run()
