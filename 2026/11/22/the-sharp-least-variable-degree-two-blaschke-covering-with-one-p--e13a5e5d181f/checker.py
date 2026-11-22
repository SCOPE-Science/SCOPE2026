#!/usr/bin/env python3
"""Finite diagnostics for a sharp constrained Blaschke angular-speed variance formula."""
import math, cmath

def sroot(r):
    lo,hi=0.0,r
    for _ in range(100):
        m=(lo+hi)*0.5
        h=m*(1+r*m)**2/(1-m*m)**2
        if h<r: lo=m
        else: hi=m
    return (lo+hi)*0.5

def v_formula(r,t,angle):
    q=r*t
    z=q*complex(math.cos(angle),math.sin(angle))
    return 2*(r*r/(1-r*r)+t*t/(1-t*t)+2*(z/(1-z)).real)

def v_series(r,t,angle,n=250):
    a=complex(r,0);b=t*complex(math.cos(angle),math.sin(angle))
    ans=0.0
    for k in range(1,n+1): ans+=2*abs(a**k+b**k)**2
    return ans

def v_grid(r,t,angle,n=8192):
    a=complex(r,0);b=t*complex(math.cos(angle),math.sin(angle))
    total=0.0
    for j in range(n):
        u=2*math.pi*j/n
        z=complex(math.cos(u),math.sin(u))
        speed=(1-r*r)/(abs(z-a)**2)+(1-t*t)/(abs(z-b)**2)
        total+=(speed-2)**2
    return total/n

count=0
for r in (0.05,0.1,0.3,0.5,0.8,0.9):
    t=sroot(r); assert 0<t<r;count+=1
    assert abs(t*(1+r*t)**2-r*(1-t*t)**2)<2e-13;count+=1
    assert v_formula(r,t,math.pi)<v_formula(r,0.0,0.0);count+=1
    assert v_formula(r,t,math.pi)<v_formula(r,r,math.pi);count+=1
    for f in (0.,0.27,0.65,1.):
        tt=r*f
        for phase in (0.,0.7,1.6,2.4,math.pi):
            assert v_formula(r,tt,phase)>v_formula(r,t,math.pi)-1e-11;count+=1
    for phase in (0.,math.pi/3,math.pi):
        assert abs(v_formula(r,t,phase)-v_series(r,t,phase))<3e-12;count+=1
        assert abs(v_formula(r,t,phase)-v_grid(r,t,phase))<4e-10;count+=1
for r in (0.01,0.02):
    s=sroot(r)
    assert abs(s-(r-4*r**3+32*r**5))<400*r**7;count+=1
assert abs(sroot(0.999999)-(3-math.sqrt(5))/2)<2e-5;count+=1
print('PASS',count,'finite diagnostic assertions')
