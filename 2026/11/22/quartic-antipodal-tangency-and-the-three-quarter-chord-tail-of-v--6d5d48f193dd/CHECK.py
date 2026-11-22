#!/usr/bin/env python3
"""Deterministic, standard-library numerical diagnostics for a Viviani chord-tail theorem.
The proof of the infinite asymptotic is in RESULT.md; finite checks do not prove it.
"""
from math import sin, cos, sqrt, acos, pi, gamma, isclose

def simpson(fun, lo, hi, n):
    assert n > 0 and n % 2 == 0
    h = (hi-lo)/n
    return h/3 * (fun(lo)+fun(hi)+4*sum(fun(lo+h*i) for i in range(1,n,2))+2*sum(fun(lo+h*i) for i in range(2,n,2)))

def point(t):
    return (1+cos(t), sin(t), 2*sin(t/2))

def norm2(v):
    return sum(z*z for z in v)

def beta(a,b):
    return gamma(a)*gamma(b)/gamma(a+b)

def Eminus1():
    return simpson(lambda z:sqrt(1+sin(z)**2),0,pi/2,4096)

E=Eminus1()
L=8*E
B=beta(.25,1.5)
C=2*8**.75*B/L**2
assert abs(C-0.14244157343155045)<1e-11
checks=0
for i in range(1,109):
    u=((17*i)%223-111)/110
    v=((31*i)%241-120)/115
    a=point(pi+u); b=point(3*pi+v)
    S=tuple(a[j]+b[j] for j in range(3))
    m=(u+v)/2; d=(u-v)/2
    expr=4*((1-cos(d))**2+(1+cos(d))*(1-cos(m)))
    assert abs(norm2(S)-expr)<2e-13
    checks+=1

# Integrate the exact small-deficit event, without fitting parameters.  The
# variable d is mapped through sin(theta) to resolve its endpoint cusp.
def exact_small_tail(eps):
    thresh=8*eps-eps*eps
    dmax=acos(1-sqrt(thresh)/2)
    def outer(theta):
        d=dmax*sin(theta)
        cd=cos(d)
        b=(thresh/4-(1-cd)**2)/(1+cd)
        if b<=0: return 0.
        mmax=acos(max(-1., min(1., 1-b)))
        def weight(m):
            u=m+d; v=m-d
            return sqrt(1+sin(u/2)**2)*sqrt(1+sin(v/2)**2)
        return simpson(weight,-mmax,mmax,48)*dmax*cos(theta)
    return 4*simpson(outer,-pi/2,pi/2,512)/L**2

for eps,max_error in ((1e-2,.06),(1e-3,.025),(1e-4,.012),(1e-5,.006)):
    p=exact_small_tail(eps)
    assert p>0
    ratio=p/(C*eps**.75)
    assert abs(ratio-1)<max_error,(eps,ratio)
    checks+=2

# Parametric speed and both antipodal curvature vectors.
for t in (pi,3*pi):
    p=point(t)
    assert abs(norm2(p)-4)<1e-12
    speed=sqrt(1+cos(t/2)**2)
    assert abs(speed-1)<1e-12
    checks+=2
assert isclose(norm2((1,0,0)),1)
print('PASS',checks,'deterministic diagnostic assertions')
print('arc length',format(L,'.15f'))
print('sharp coefficient',format(C,'.15f'))
for eps in (1e-2,1e-3,1e-4,1e-5):
    print('eps',eps,'relative coefficient',format(exact_small_tail(eps)/(C*eps**.75),'.12f'))
