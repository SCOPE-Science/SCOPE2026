#!/usr/bin/env python3
"""Numerical diagnostics for unequal Steinmetz bicylinder radial chord geometry.
All mathematics and assertions are independent of any external package files.
"""
import math
import numpy as np
from scipy.integrate import quad

def pair(s,t):
    assert s>=0 and t>=0 and s*s+t*t<=1+1e-13
    if s==0 or t==0:return 0.
    z=max(0.,1-s*s-t*t)
    return (2/math.pi)*(s*math.asin(min(1.,t/math.sqrt(1-s*s)))+t*math.asin(min(1.,s/math.sqrt(1-t*t)))-math.atan2(s*t,math.sqrt(z)))

def cdf(L,a,b):
    assert 0<a<b
    if L<=2*a:return 0.
    if L>=2*math.hypot(a,b):return 1.
    s=math.sqrt(1-(2*a/L)**2)
    if L<=2*b:return s
    t=math.sqrt(1-(2*b/L)**2)
    return s+t-pair(s,t)

def density_parts(L,a,b):
    if L<=2*a or L>=2*math.hypot(a,b):return 0.,0.
    s=math.sqrt(1-(2*a/L)**2)
    sa=4*a*a/(L**3*s)
    if L<=2*b:return sa,0.
    t=math.sqrt(1-(2*b/L)**2)
    tb=4*b*b/(L**3*t)
    da=sa*(1-2/math.pi*math.asin(min(1.,t/math.sqrt(1-s*s))))
    db=tb*(1-2/math.pi*math.asin(min(1.,s/math.sqrt(1-t*t))))
    return da,db

nassert=0
for a,b in [(0.5,1.),(1.,1.3),(1.,2.),(2.,5.)]:
    hi=2*math.hypot(a,b)
    assert cdf(2*a,a,b)==0 and cdf(hi,a,b)==1; nassert+=2
    for k in range(1,40):
        L=2*a+(hi-2*a)*k/40
        assert 0<cdf(L,a,b)<1; nassert+=1
    for k in range(1,30):
        L=2*b+(hi-2*b)*k/30
        s=math.sqrt(1-(2*a/L)**2); t=math.sqrt(1-(2*b/L)**2)
        num=2/math.pi*quad(lambda x:math.asin(t/math.sqrt(1-x*x)),0,s,epsabs=2e-12)[0]
        assert abs(pair(s,t)-num)<1e-10; nassert+=1
        fa,fb=density_parts(L,a,b)
        h=min(1e-5*a,(hi-L)/100,(L-2*b)/100)
        der=(cdf(L+h,a,b)-cdf(L-h,a,b))/(2*h)
        assert abs((fa+fb)-der)<2e-5; nassert+=1
    for e in [1e-2,1e-3,1e-4,1e-5]:
        L=hi-e*a
        da,db=density_parts(L,a,b)
        assert abs(da/(da+db)-a*a/(a*a+b*b)) < 0.04; nassert+=1

# Monte Carlo using uniform directions as a check on the distribution and label branches
rng=np.random.default_rng(211126)
N=800000
U=rng.normal(size=(N,3));U/=np.linalg.norm(U,axis=1)[:,None]
a,b=1.,2.
Ca=2*a/np.sqrt(1-U[:,2]**2)
Cb=2*b/np.sqrt(1-U[:,0]**2)
V=np.minimum(Ca,Cb)
for L in [2.1,2.5,3,3.6,4,4.1,4.3,4.45]:
    emp=np.mean(V<=L); exact=cdf(L,a,b)
    sigma=math.sqrt(max(1e-8,exact*(1-exact))/N)
    print('CDF',L,round(emp,6),round(exact,6),'z=',round((emp-exact)/sigma,3))
    assert abs(emp-exact)<6*sigma+0.0005; nassert+=1
# Endpoint and contact asymptotics (dimensionful scaling)
for a,b in [(1.,2.),(1.,1.3),(2.,5.)]:
    hi=2*math.hypot(a,b); R=math.hypot(a,b)
    C=2*math.sqrt(R)/(3*math.pi*a*b)
    for e in [1e-3,1e-4]:
        fa,fb=density_parts(hi-e,a,b)
        # integrated upper survival is accurately computed using 2-point numerical quadrature
        tail=quad(lambda L:sum(density_parts(L,a,b)),hi-e,hi,epsabs=1e-12,limit=300)[0]
        print('tail',a,b,e,tail/(C*e**1.5), 'label',fa/(fa+fb))
        assert abs(tail/(C*e**1.5)-1)<0.015
        nassert+=1
print('PASS',nassert,'diagnostics')
