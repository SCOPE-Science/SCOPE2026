#!/usr/bin/env python3
"""Reproduce exact and floating-point checks for an additive inverse-power decay law.
No external packages are required. This supplements, but does not replace, the proof.
"""
from fractions import Fraction as F
from math import isfinite, log

assertions = 0

def check(x):
    global assertions
    assertions += 1
    if not x:
        raise AssertionError('check '+str(assertions))

def critical(p, d):
    a = p/d**2
    b = (p+d)/d**2
    h = 1+(2*p+d)/d**2
    if d <= 1:
        raise ValueError('requires exponent gap > 1')
    u = (h+(h*h+4*a*b*(d*d-1))**0.5)/(2*a*(d-1))
    g = h+a*u+b/u
    return u, u/g**d, g

def gfun(u,p,d):
    return 1+(2*p+d)/d**2 + p*u/d**2 + (p+d)/(d*d*u)

def kval(u,p,d):
    return u/gfun(u,p,d)**d

def efunc(t,p,d,k,c=1):
    y=1+t/c
    u=k*y**d
    return (1-1/y)*(p+d/(1+u))

def deriv_sign_scaled(t,p,d,k,c=1):
    y=1+t/c
    u=k*y**d
    return p*(1+u)**2 + d*(1+u) - (y-1)*d*d*u

def root_k(k,p,d,lo,hi):
    # Valid for brackets that contain exactly one crossing.
    f0=kval(lo,p,d)-k
    f1=kval(hi,p,d)-k
    check(f0*f1 < 0)
    for _ in range(90):
        mid=(lo+hi)/2
        fm=kval(mid,p,d)-k
        if fm==0: return mid
        if f0*fm<0:
            hi=mid
        else:
            lo=mid; f0=fm
    return (lo+hi)/2

# Exact rational calibration and factor certificate, no float approximations.
u=F(9); p=F(1); d=F(2)
g=F(2)+u/F(4)+F(3)/(F(4)*u)
check(g==F(13,3))
check(u/g**2==F(81,169))
check((F(1,4)-F(3,4)/u**2)==F(13,54))
for v in range(1,100):
    h=F(v**4-12*v**3+24*v*v+27,9)
    term=F(v*v,3)
    expected=(1+term)**2+2*(1+term)-4*(v-1)*term
    check(expected==h)
    check((v**4-12*v**3+24*v*v+27)==(v-3)*(v**3-9*v*v-3*v-9))
check(efunc(2,1,2,1/3)==1.0)
check(deriv_sign_scaled(2,1,2,1/3)==0)
check(deriv_sign_scaled(3,1,2,1/3)<0)
check(deriv_sign_scaled(10,1,2,1/3)>0)

# Reconstruct exact phase classification for broad positive parameters.
for p in (0.4,0.7,1.0,2.0,4.0):
    for d in (0.35,0.8,1.0,1.15,1.4,2.0,3.0):
        if d>1:
            us,ks,ys=critical(p,d)
            check(us>0 and ys>1 and ks>0)
            for ratio in (0.16,0.4,0.7,0.95):
                k=ks*ratio
                lo=us*1e-12
                while kval(lo,p,d)>=k: lo*=0.1
                ul=root_k(k,p,d,lo,us)
                hi=us*2
                while kval(hi,p,d)>=k: hi*=2
                ur=root_k(k,p,d,us,hi)
                tl=gfun(ul,p,d)-1; tr=gfun(ur,p,d)-1
                check(0<tl<tr)
                for frac in (0.1,0.25,0.5,0.8):
                    check(deriv_sign_scaled(tl*frac,p,d,k)>0)
                check(deriv_sign_scaled((tl+tr)/2,p,d,k)<0)
                for fac in (1.2,1.5,2):
                    check(deriv_sign_scaled(tr*fac,p,d,k)>0)
                for t in (tl,tr):
                    check(abs(deriv_sign_scaled(t,p,d,k))<1e-7*max(1,(1+k*(1+t)**d)**2))
            for ratio in (1.1,2.0,10.0):
                k=ks*ratio
                for t in (0.01,0.1,0.25,1,3,10,100,1000):
                    check(deriv_sign_scaled(t,p,d,k)>0)
        elif d<1:
            for k in (0.03,0.1,0.3,1.0,3.0):
                lo=1e-14
                hi=1.0
                while kval(hi,p,d)<k: hi*=10
                ur=root_k(k,p,d,lo,hi)
                tr=gfun(ur,p,d)-1
                check(tr>0)
                check(deriv_sign_scaled(0,p,d,k)>0)
                check(deriv_sign_scaled(tr*.5,p,d,k)>0)
                check(deriv_sign_scaled(tr*2,p,d,k)<0)
                check(deriv_sign_scaled(tr*10,p,d,k)<0)
        else:
            for ratio in (.2,.5,.9):
                k=ratio/p
                lo=1e-14; hi=1
                while kval(hi,p,d)<k: hi*=10
                ur=root_k(k,p,d,lo,hi)
                tr=gfun(ur,p,d)-1
                check(tr>0)
                check(deriv_sign_scaled(tr*.5,p,d,k)>0)
                check(deriv_sign_scaled(tr*2,p,d,k)<0)
            for ratio in (1.,1.2,4.):
                k=ratio/p
                for t in (0,0.01,0.1,1,3,10,100,1000):
                    check(deriv_sign_scaled(t,p,d,k)>0)

# Numerical derivative identity compared to independent central differences.
for p in (0.55,1.0,1.8,3):
  for d in (0.4,0.9,1,1.5,2.5):
    for k in (0.04,0.17,0.7,2.1):
      for c in (0.3,1.0,3.0):
        for t in (0.2,0.75,2,4,10,25):
          h=1e-5*(1+t)
          direct=(efunc(t+h,p,d,k,c)-efunc(t-h,p,d,k,c))/(2*h)
          y=1+t/c; u=k*y**d
          expr=deriv_sign_scaled(t,p,d,k,c)/(c*y*y*(1+u)**2)
          check(isfinite(direct) and abs(direct-expr)<2e-8*max(1,abs(expr)))

# Independent exact second stationary time certificate (one rational stationary time).
def poly(v): return v**3-9*v*v-3*v-9
l=9.; r=10.
check(poly(l)<0 and poly(r)>0)
for _ in range(85):
    mid=(l+r)/2
    if poly(mid)>0:r=mid
    else:l=mid
v=(l+r)/2
check(9.4199008193 < v < 9.4199008194)
check(0.9523044940<efunc(v-1,1,2,1/3)<0.9523044941)

print('PASS', assertions, 'assertions')
print('p=1, gap=2, c=1, A/B=1/3; max at t=2, E=1; min at t=%.12f, E=%.12f'%(v-1,efunc(v-1,1,2,1/3)))
print('critical A/B=81/169; merged stationary t=10/3')
