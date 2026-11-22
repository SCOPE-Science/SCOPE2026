"""Standalone arithmetic and grid checks for weighted two-point Neumann trace design.

These checks are finite sanity tests; the all-weight theorem uses the analytical
semidefinite certificate in RESULT.md.
"""
import math
import random

root3 = math.sqrt(3.0)
d0 = (1.0-math.sqrt(2.0/3.0))/2.0
b0 = (1.0-1.0/root3)/2.0
rc = 5.0-2.0*root3


def K(x, y):
    return 1.0/3.0-max(x, y)+(x*x+y*y)/2.0


def eigmax(r, x, y):
    a = r*K(x,x)
    d = K(y,y)
    c = math.sqrt(r)*K(x,y)
    return (a+d+math.hypot(a-d,2.0*c))/2.0


def b_of_a(a):
    return (1.0-math.sqrt(1.0/3.0+4.0*a-4.0*a*a))/2.0


def R(a):
    b = b_of_a(a)
    return (b*b+1.0/12.0)/(a*a+1.0/12.0)


def optimum(r):
    assert r >= 1
    if r >= rc:
        return 0.5, 0.5+b0, r/12.0, None
    lo, hi = 0.0, d0
    for _ in range(70):
        mid=(lo+hi)/2
        if R(mid)>r:
            lo=mid
        else:
            hi=mid
    a=(lo+hi)/2
    b=b_of_a(a)
    x=0.5-a
    y=0.5+b
    L=math.sqrt(r)*a/x
    U=b/(math.sqrt(r)*(1-y))
    u=U/(L+U)
    v=L*U/(L+U)
    return x,y,r*K(x,x),(u,v)


num=0
assert abs(R(0.0)-rc)<1.e-13; num+=1
assert abs(R(d0)-1)<1.e-13; num+=1
assert abs(K(0.5-d0,0.5+d0))<1.e-13;num+=1
for r in [1.0,1.0001,1.01,1.1,1.2,1.3,1.4,1.5,1.535,rc,1.54,2.0,4.0,10.0,100.0]:
    x,y,bound,cert=optimum(r)
    assert abs(eigmax(r,x,y)-bound)<1.e-11;num+=1
    assert abs(K(x,y))<1.e-11;num+=1
    if cert is not None:
        u,v=cert
        assert 0<u<1 and 0<v and v*v<u*(1-u);num+=1
        assert abs(r*K(x,x)-K(y,y))<1.e-11;num+=1
        assert abs(u*r*(2*x-1)+2*v*math.sqrt(r)*x)<1.e-11;num+=1
        assert abs((1-u)*(2*y-1)+2*v*math.sqrt(r)*(y-1))<1.e-11;num+=1
        assert (u*r+v*math.sqrt(r))>0 and ((1-u)+v*math.sqrt(r))>0;num+=1
    rng=random.Random(int(r*100000))
    for _ in range(10000):
        a=rng.random();b=rng.random()
        assert eigmax(r,a,b)>=bound-2.e-11,(r,a,b,bound)
        num+=1
print(f'PASS {num} numerical / algebraic assertions')
