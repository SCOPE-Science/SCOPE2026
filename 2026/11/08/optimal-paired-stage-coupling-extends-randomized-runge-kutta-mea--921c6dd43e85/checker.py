#!/usr/bin/env python3
"""Exact-rational and independently discretized checks of two-step randomized RK stability.
No external packages. The continuum proof is given in RESULT.md, not replaced by tests.
"""
from fractions import Fraction as F
from math import isclose

def g(z):
    c=1-z+z*z/F(2)
    return c*c+z**4/F(12)

def anti(z):
    c=1-z+z*z/F(2)
    return c**4-c*c*z**4/F(6)+z**8/F(80)

def moment_poly(a):
    return (72*a**5-10*a**4-60*a**3+40*a*a-10*a+1)/F(30)

def opt(z):
    if z<=1:return anti(z)
    a=(z-1)/(z*z)
    return z**8*moment_poly(a)

def rootpoly(z):
    return (z**10-10*z**9+50*z**8-140*z**7+210*z**6-68*z**5-360*z**4+760*z**3-760*z*z+360*z-72)

def quantile(z,t):
    if z<=1:
        # R positive and increasing, q_{|R|}=1-z+z^2*t
        return 1-z+z*z*t
    a=(z-1)/(z*z)
    return z*z*t/F(2) if t<=2*a else z*z*t-z+1

checks=0
for z in [F(k,20) for k in range(1,101)]+[F(101,50),F(20563,10000),F(20564,10000)]:
    hz=opt(z);az=anti(z);iz=g(z)**2
    assert hz>=0 and hz<=az and az<iz,(z,hz,az,iz)
    checks+=4
    if z>1:
        assert 30*z*z*(hz-1)==rootpoly(z),(z,hz)
        checks+=1
    for t in [F(k,50) for k in range(51)]:
        assert quantile(z,t)>=0
        checks+=1
assert opt(F(2))==F(4,5)
assert anti(F(2))==F(23,15)
assert g(F(2))**2==F(49,9)
assert g(F(4,3))==F(139,243)
assert opt(F(20563,10000))<1<opt(F(20564,10000))
checks+=5
# midpoint quantile quadrature validates separate derivation of the continuous formula
for zz in [0.25,0.5,1.0,1.25,1.6,2.0,2.05,2.1,3.0]:
    z=F(str(zz)); n=16384
    average=sum(float(quantile(z,F(2*k+1,2*n))*quantile(z,F(2*n-2*k-1,2*n)))**2 for k in range(n))/n
    assert isclose(average,float(opt(z)),rel_tol=0,abs_tol=5e-7),(zz,average,float(opt(z)))
    checks+=1
# bisection over exact fraction values for the unique upper crossing
lo=F(2);hi=F(21,10)
for _ in range(90):
    mid=(lo+hi)/2
    if opt(mid)<1:lo=mid
    else:hi=mid
    checks+=1
assert hi-lo<F(1,10**27)
assert F(2)<lo<hi<F(21,10)
print('PASS exact_rational_and_quantile_checks=',checks)
print('P2=',opt(F(2)),'antithetic2=',anti(F(2)),'iid2=',g(F(2))**2)
print('root bracket 2.0563 < z* < 2.0564: ',opt(F(20563,10000))<1<opt(F(20564,10000)))
print('z* approximately:',format(float((lo+hi)/2),'.14f'))
