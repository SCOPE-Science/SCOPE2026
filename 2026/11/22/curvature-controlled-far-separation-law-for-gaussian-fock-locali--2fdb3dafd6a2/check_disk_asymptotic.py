"""Finite numerical checks for a disk mixed Gaussian Fock-localization trace.
These checks supplement an analytic asymptotic proof; they are not infinite proofs.
"""
from math import pi,sqrt,acos,exp,hypot
from scipy.integrate import quad
from scipy.special import i0e

def overlap_area(t,a,b):
    if t<=abs(a-b):return pi*min(a,b)**2
    if t>=a+b:return 0.
    x=max(-1.,min(1.,(t*t+a*a-b*b)/(2*t*a)))
    y=max(-1.,min(1.,(t*t+b*b-a*a)/(2*t*b)))
    q=max(0.,(-t+a+b)*(t+a-b)*(t-a+b)*(t+a+b))
    return a*a*acos(x)+b*b*acos(y)-sqrt(q)/2

def scaled_trace(d,a,b):
    L=d-a-b
    assert L>0
    def f(h):
        r=a+b-h
        return 2/pi*r*overlap_area(r,a,b)*exp(-2*L*h-h*h)*i0e(2*d*r)
    y,err=quad(f,0,a+b,epsabs=1e-14,epsrel=3e-11,limit=250)
    return y

for a,b in [(1.,1.),(.6,1.3)]:
    for L in [5,10,20,40,80]:
       d=L+a+b
       actual=scaled_trace(d,a,b)
       asym=sqrt(a*b)/(4*pi*L**3)
       ratio=actual/asym
       print(a,b,L,ratio)
       if L>=80: assert abs(ratio-1.)<0.025

# Crosswise 2.4 offset, comparison to claimed asymptotic (vertical residual)
a,b,c=.6,1.3,2.4
for L in [10,20,40,80,160]:
    d=L+a+b
    D=hypot(d,c)
    LD=D-a-b
    scaled=scaled_trace(D,a,b) * exp(L*L-LD*LD)
    predicted=sqrt(a*b)/(4*pi*L**3)*exp(-c*c)
    ratio=scaled/predicted
    print('shift',L,ratio)
    if L>=160: assert abs(ratio-1.)<0.07
