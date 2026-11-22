#!/usr/bin/env python3
"""Exact-rational consistency tests for a perturbed three-stage TDRK rule."""
from fractions import Fraction as F
from itertools import product

CHECKS = 0

def check(cond):
    global CHECKS
    assert cond
    CHECKS += 1


def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def sc(a, v):
    return a[0]*v, a[1]*v

def rot(a, w):
    return -w*a[1], w*a[0]

def second(a, w, q):
    return sc(a, -q*w*w)

def step(a, w, h, q0, q1):
    y1 = add(add(a, sc(rot(a, w), h/2)), sc(second(a, w, q0), h*h/8))
    y2 = add(add(a, sc(rot(a, w), h)), sc(second(y1, w, q1), h*h/2))
    fsum = add(add(rot(a, w), sc(rot(y1, w), F(4))), rot(y2, w))
    return add(a, sc(fsum, h/6))

def norm2(a):
    return a[0]*a[0]+a[1]*a[1]

def parts(w,h,q0,q1):
    v=w*h; x=v*v
    aa=1-x/2+q1*x*x/24
    bb=v*(1-(q0+q1)*x/12+q0*q1*x*x/96)
    return aa,bb

def scalar_mult(a, aa, bb):
    return aa*a[0]-bb*a[1], bb*a[0]+aa*a[1]

def joint(eps,p):
    return [(1+eps,1+eps,p/2),
            (1-eps,1-eps,p/2),
            (1+eps,1-eps,(1-p)/2),
            (1-eps,1+eps,(1-p)/2)]

def mean_step(w,h,eps,p):
    return sum(prob*norm2(parts(w,h,q0,q1)) for q0,q1,prob in joint(eps,p))

def Q(s,p,x):
    return (1-s)**2*x*x+16*(3*s-1)*(x-4)+8*s*p*((x-8)**2+16)

def form(w,h,eps,p):
    x=(w*h)**2
    return 1+x**3*Q(eps**2,p,x)/9216

for w in [F(1),F(3,2),F(7,5)]:
    for h in [F(1,10),F(1,3),F(1),F(5,2)]:
        for eps in [F(0),F(1,4),F(3,5),F(3,4),F(1)]:
            for s0,s1 in product([-1,1],repeat=2):
                q0,q1=1+s0*eps,1+s1*eps
                u=(F(2,3),F(-7,5))
                exact=step(u,w,h,q0,q1)
                aa,bb=parts(w,h,q0,q1)
                check(exact==scalar_mult(u,aa,bb))
                check(norm2(exact)==norm2(u)*(aa*aa+bb*bb))
            for p in [F(0),F(1,20),F(1,10),F(1,4),F(1,2),F(3,4),F(1)]:
                check(mean_step(w,h,eps,p)==form(w,h,eps,p))
                if eps:
                    x=(w*h)**2; s=eps*eps
                    difference=mean_step(w,h,eps,p)-mean_step(w,h,eps,F(0))
                    check(difference==p*8*s*x**3*((x-8)**2+16)/9216)

# Exact cross-coupling example: antithetic stabilizes, independent grows.
eps=F(3,4); w=h=F(1)
ma=mean_step(w,h,eps,F(0)); mi=mean_step(w,h,eps,F(1,2))
check(ma==1-F(8399,2359296))
check(mi==1+F(29041,2359296))
check(ma<1<mi)

# Explicit multi-step averaging of all stage-sign histories.
for p in [F(0),F(1,16),F(1,2),F(1)]:
    for eps in [F(1,4),F(3,4)]:
        for n in range(1,5):
            configurations=[(q0,q1,prob) for q0,q1,prob in joint(eps,p) if prob]
            accum=F(0)
            for history in product(configurations,repeat=n):
                u=(F(1),F(2)); prob=F(1)
                for q0,q1,weight in history:
                    u=step(u,F(1),F(1),q0,q1)
                    prob*=weight
                accum+=prob*norm2(u)
            check(accum==F(5)*mean_step(F(1),F(1),eps,p)**n)

# Rational stress tests of the sharp phase criterion.  The theorem itself
# follows from the quadratic-sign proof, not these finite tests.
for eps in [F(1,8),F(1,2),F(3,5),F(2,3),F(3,4),F(1)]:
    s=eps*eps
    for p in [F(0),F(1,100),F(1,20),F(1,10),F(1,5),F(1,2),F(1)]:
        pc=(3*s-1)/(10*s)
        expected_small_stable=bool(s>F(1,3) and p<pc)
        x=F(1,10**8)
        check((Q(s,p,x)<0)==expected_small_stable)
        for x in [F(1,10),F(1),F(4),F(8),F(16)]:
            check((1+x**3*Q(s,p,x)/9216<1)==(Q(s,p,x)<0))

print('VERIFY_OK', CHECKS, 'exact-rational assertions')
