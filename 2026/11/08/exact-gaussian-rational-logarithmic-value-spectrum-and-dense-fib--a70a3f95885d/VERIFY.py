#!/usr/bin/env python3
"""Exact finite corroboration of the Gaussian-rational polar arithmetic-derivative spectrum."""
from fractions import Fraction as F
from math import gcd

def factor(n):
    n = abs(int(n)); d = {}; p=2
    while p*p <= n:
        while n % p == 0:
            d[p] = d.get(p,0) + 1; n//=p
        p=3 if p==2 else p+2
    if n>1: d[n]=d.get(n,0)+1
    return d

def logarithmic_rational(x):
    assert x > 0
    t = F(0)
    for p,e in factor(x.numerator).items(): t += F(e,p)
    for p,e in factor(x.denominator).items(): t -= F(e,p)
    return t

def gaussian_log(z):
    a,b=z; assert a!=0 or b!=0
    return logarithmic_rational(a*a+b*b)/2

def gaussian_mul(z,w):
    a,b=z; c,d=w
    return (a*c-b*d,a*d+b*c)

def gaussian_inv(z):
    a,b=z; s=a*a+b*b
    return (a/s,-b/s)

def gaussian_power(z,n):
    if n<0: return gaussian_power(gaussian_inv(z), -n)
    x=(F(1),F(0))
    while n:
        if n%2: x=gaussian_mul(x,z)
        z=gaussian_mul(z,z); n//=2
    return x

def egcd(a,b):
    if b==0: return (abs(a), 1 if a>0 else -1, 0)
    g,x,y=egcd(b,a%b); return g,y,x-(a//b)*y

def representation(r):
    assert r.denominator%8!=0
    b = r.denominator
    m=b
    while m%2==0: m//=2
    pf=factor(m)
    assert all(e==1 for e in pf.values())
    coeff=[m]+[4*m//p for p in pf]
    bez=[1]; g=coeff[0]
    for a in coeff[1:]:
        h,u,v=egcd(g,a)
        bez=[c*u for c in bez]+[v]; g=h
    assert g==1
    scale = int(r * (4*m))
    exps = [k*scale for k in bez]
    z=gaussian_power((F(1),F(1)),exps[0])
    for p,e in zip(pf,exps[1:]):
        z=gaussian_mul(z,gaussian_power((F(p),F(0)),e))
    assert gaussian_log(z)==r
    return z

def allowed(r):
    return all(e<= (2 if p==2 else 1) for p,e in factor(r.denominator).items())

def main():
    cases=0
    for d in range(1,13):
        for a in range(-10,11):
            for b in range(-10,11):
                if a==b==0: continue
                v=gaussian_log((F(a,d),F(b,d)))
                assert allowed(v)
                cases+=1
    spectra=0
    for den in range(1,81):
        for num in (-3,-2,-1,0,1,2,3):
            r=F(num,den)
            if allowed(r):
                representation(r)
                spectra+=1
    u=(F(4,27),F(0)); v=(F(4,3125),F(0)); circle=(F(3,5),F(4,5))
    assert gaussian_log(u)==0 and gaussian_log(v)==0 and gaussian_log(circle)==0
    assert gaussian_log((F(1),F(1)))==F(1,4)
    assert gaussian_log((F(3,2),-F(3,2)))==F(1,12)
    assert not allowed(F(1,8))
    print('VERIFY_OK gaussian_rational_cases=%s constructed_rational_levels=%s' %(cases,spectra))
    print('polar_arithmetic_log_(1+i)=1/4; log_(3/(1+i))=1/12; 1/8_excluded=PASS')
    print('independent_kernel_generators_4/27_4/3125=PASS rational_circle_3/5+4i/5=PASS')

if __name__=='__main__': main()
