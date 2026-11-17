#!/usr/bin/env python3
"""Reproduce numerical and exact checks for the regular-polygon spherical-depth formula.
Only the Python standard library is needed. The proof for all n is in RESULT.md.
"""
from math import pi, tan, cos, log, isclose
from fractions import Fraction as Q

checks=0
def assert_close(a,b,tol=2.e-11):
    global checks
    assert abs(a-b) < tol, (a,b,abs(a-b))
    checks+=1

def simpson(f,a,b,N=2048):
    assert N%2==0
    h=(b-a)/N
    out=f(a)+f(b)
    for i in range(1,N):
        out+=(4 if i%2 else 2)*f(a+i*h)
    return out*h/3

def B_closed(n):
    z=tan(pi/(2*n))**2
    return (z*z-1)/(z*(z-3)) + ((z-1)**3*(z+1)/(z*z*(z-3)**2))*log((1+z)/(1-z)**2)

def B_integral(n):
    a=pi/n; t=tan(a)
    s1=simpson(lambda x: (tan(x-a/2)+t)/cos(x)**2,-a/2,a/2)
    s2=simpson(lambda x: (tan(x-a/2)-tan(x-3*a/2))/cos(x)**2,a/2,a)
    return (s1+s2)/(2*t*t)

def probability(n):
    if n%2==0: return .5
    return .5+(-1)**((n+1)//2)*(.5-B_closed(n))/n

# Independent integration of the band probability, and the known triangle case.
for n in (3,5,7,9,11,13,15,17,19,21):
    assert_close(B_closed(n), B_integral(n),2.e-10)
    b=B_closed(n)
    assert b<.5 and b>0
    checks+=1
    assert (probability(n)-.5)*(-1)**((n+1)//2)>0
    checks+=1
assert_close(probability(3),1/3+log(3)/6)
for n in range(4,50,2):
    assert_close(probability(n),.5,1.e-15)

# Direct sector-pair count verifies the geometric step independently of integrals.
for n in (3,5,7,9,11,13,15):
    a=pi/n; r=(n-1)//2
    for i in range(39):
        x=a*(-1+2*(i+.314159)/39)
        for j in range(39):
            y=a*(-1+2*(j+.271828)/39)
            u=x-y
            if min(abs(abs(u)-a/2),abs(abs(u)-3*a/2))<1.e-10: continue
            count=sum(cos(2*k*a+u)<0 for k in range(n))
            in_band=a/2<abs(u)<3*a/2
            expect = (r+1 if not in_band else r) if n%4==3 else (r if not in_band else r+1)
            assert count==expect,(n,x,y,count,expect)
            checks+=1

# Exact rational value of the quartic-convolution coefficient.
# K(u) = int_{u-1}^1(t^2-1/3)((t-u)^2-1/3)dt
#      = -(u-2)(3u^4+6u^3-8u^2-16u+8)/90.
# Expand and integrate on [1/2, 3/2] using exact fractions.
p1=[Q(2),Q(-1)]
p2=[Q(8),Q(-16),Q(-8),Q(6),Q(3)]
coeff=[Q(0)]*6
for i,x in enumerate(p1):
    for j,y in enumerate(p2): coeff[i+j]+=x*y/Q(90)
a,b=Q(1,2),Q(3,2)
J=Q(1,2)*sum(c*(b**(i+1)-a**(i+1))/Q(i+1) for i,c in enumerate(coeff))
assert J == -Q(5,192), J
checks+=1

# Local asymptotic coefficient: far enough n for stable double-precision subtraction.
const=5*pi**4/192
for n in (31,41,51,61):
    signed=(probability(n)-.5)*(-1)**((n+1)//2)*n**5
    assert abs(signed-const) < 18/n**2,(n,signed,const)
    checks+=1
print(f'PASS: {checks} checks; n=3 probability={probability(3):.12f}; n=5={probability(5):.12f}; limiting coefficient={const:.12f}')
