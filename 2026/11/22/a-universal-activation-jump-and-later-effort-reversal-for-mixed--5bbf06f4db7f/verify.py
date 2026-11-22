#!/usr/bin/env python3
"""Independent numerical diagnostics for a mixed Poisson fruit-set allocation law.

This program is supplementary only. The proofs of global uniqueness and
threshold ordering are analytic, not conclusions drawn from finite tests.
"""
import math
import random

def H(t):
    q = math.exp(-t)
    return 1.0-(1.0+2.0*t)*q+t*q*q

def bisect(f,a,b,steps=85):
    fa=f(a)
    assert fa*f(b)<0
    for _ in range(steps):
        c=(a+b)/2.0
        if fa*f(c)<=0:b=c
        else:a,fa=c,f(c)
    return (a+b)/2.0

U=bisect(H,0.5,1.0)

def Bcrit(v):return 2*U-math.log(v*U)

def hard_active(B,v):
    # The increasing stationary branch y > 1/2; the bisection bracket
    # [U,B] is valid only for B >= Bcrit(v).
    return bisect(lambda y:2*y-math.log(v*y)-B,U,B)

def fruit(B,v,y):
    x=B-y
    return -math.expm1(-x)+v*(-math.expm1(-y)-y*math.exp(-y))

def optimum(B,v):
    c=Bcrit(v)
    if B<c-1e-12: return 0.0
    if B>c+1e-12: return hard_active(B,v)
    return U

rng=random.Random(20260827)
checks=0
assert 0.8425689<U<0.8425691;checks+=1
for v in [1.0,0.9,0.5,0.1,0.005,1e-5]:
    c=Bcrit(v)
    assert 0<U<c<2/v;checks+=1
    assert abs(fruit(c,v,0.0)-fruit(c,v,U))<3e-13;checks+=1
    assert abs(H(U))<1e-14;checks+=1
    for B in [c-1e-3,c-1e-6,c+1e-6,c+1e-3,2/v,2/v+1.0]:
        y=optimum(B,v)
        assert 0<=y<=B;checks+=1
        for i in range(501):
            yy=B*i/500.0
            assert fruit(B,v,y)>=fruit(B,v,yy)-6e-10,(v,B,y,yy)
            checks+=1
        if B>c+1e-9:
            assert abs(math.exp(-(B-y))-v*y*math.exp(-y))<1e-10;checks+=1
            if B<2/v-1e-9:assert y<B/2;checks+=1
            if B>2/v+1e-9:assert y>B/2;checks+=1

for k in range(700):
    v=math.exp(rng.uniform(math.log(1e-4),0.0))
    c=Bcrit(v)
    B=c*math.exp(rng.uniform(-2.5,1.5))
    y=optimum(B,v)
    for i in range(81):
        yy=B*i/80
        assert fruit(B,v,y)>=fruit(B,v,yy)-1.5e-9,(v,B,y,yy)
        checks+=1
    if B>c+1e-9:
        assert y>U;checks+=1
        if B<2/v:assert y<B/2;checks+=1
        else:assert y>B/2;checks+=1

# Critical jump is independent of the relative fruit value, and the
# active stationary branch is strictly increasing in total effort.
for j in range(101):
    v=math.exp(-j/15)
    c=Bcrit(v)
    y1=hard_active(c+0.01,v)
    y2=hard_active(c+0.2,v)
    assert U<y1<y2;checks+=1
    assert abs(hard_active(2/v,v)-(1/v))<1e-8;checks+=1

print('PASS numerical diagnostic assertions:',checks)
print('Universal activation dose:',format(U,'.15f'))
print('Unit-weight budget threshold:',format(Bcrit(1.0),'.15f'))
