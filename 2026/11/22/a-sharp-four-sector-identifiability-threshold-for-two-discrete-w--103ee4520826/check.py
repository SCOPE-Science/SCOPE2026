#!/usr/bin/env python3
"""Reproduce numerical checks of exact bin-marginalized and point-conditionalized wrapped Cauchy laws."""
import math
import random

TAU = 2 * math.pi

def md(m, rho):
    h = math.pi / m
    a = (1 + rho*rho)*math.cos(h)
    b = 2*rho
    c = (1-rho*rho)*math.sin(h)
    return [math.atan2(c, a-b*math.cos(TAU*j/m))/math.pi for j in range(m)]

def cd(m, eta, nu=0.0):
    weights = [1/(1+eta*eta-2*eta*math.cos(TAU*j/m-nu)) for j in range(m)]
    z = sum(weights)
    return [v/z for v in weights]

def integral_md(m, rho, j, steps=512):
    h = math.pi/m
    t = TAU*j/m
    left, right = t-h, t+h
    step = (right-left)/steps
    def f(x):
        return (1-rho*rho)/(TAU*(1+rho*rho-2*rho*math.cos(x)))
    return (step/3)*(f(left)+f(right)+sum((4 if k%2 else 2)*f(left+k*step) for k in range(1,steps)))

def curvature(p):
    m = len(p)
    x0, x1, x2 = 1, math.cos(TAU/m), math.cos(2*TAU/m)
    return (1/p[0]-1/p[1])/(x0-x1)-(1/p[1]-1/p[2])/(x1-x2)

def pzero_cd(m, eta):
    x = math.cos(TAU/m)
    return 1/(1+(m-1)*(1-eta)**2/(1+eta*eta-2*eta*x))

def match_low(m, v):
    low,high=0,1
    for _ in range(100):
        mid=(low+high)/2
        if pzero_cd(m,mid)<v: low=mid
        else: high=mid
    return (low+high)/2

rng = random.Random(1832)
assert_count=0
for m in [2,3,4,5,6,7,8,9,10,11,16,21,31]:
    for rho in [0., .001, .04, .13, .25, .4, .56, .71, .83, .93]:
        p = md(m,rho)
        assert abs(sum(p)-1)<1e-10; assert_count += 1
        assert min(p)>0; assert_count += 1
        assert all(abs(p[j]-p[-j])<1e-11 for j in range(1,m));assert_count+=1
        if rho <.94:
            for j in range(m):
                assert abs(p[j]-integral_md(m,rho,j))<2e-9; assert_count+=1
        if m in (2,3):
            eta=match_low(m,p[0])
            q=cd(m,eta)
            assert max(abs(a-b) for a,b in zip(p,q))<1e-12;assert_count+=1
        elif rho>0:
            assert curvature(p)>0;assert_count+=1
            for eta in [.001,.18,.42,.65,.89]:
                assert abs(curvature(cd(m,eta)))<2e-8;assert_count+=1

for i in range(120):
    m = rng.randint(4,50);rho=rng.uniform(.03,.95);eta=rng.uniform(.03,.95)
    p=md(m,rho);q=cd(m,eta)
    assert curvature(p)>0;assert_count+=1
    assert abs(curvature(q))<3e-8;assert_count+=1

# Analytic reciprocal curvature identity from the proof, checked with finite differences.
for i in range(120):
    y=rng.uniform(-10,10)
    t=math.atan2(1.0,y)
    analytic=2*math.pi*(1-y*t)/((1+y*y)**2*t**3)
    assert analytic>0;assert_count+=1
    eps=1e-3
    f=lambda z:math.pi/math.atan2(1.0,z)
    numerical=(f(y+eps)-2*f(y)+f(y-eps))/eps**2
    assert abs(numerical-analytic)<5e-5;assert_count+=1

p=md(4,.5)
print('assertions_passed',assert_count)
print('m4_rho_half_probabilities',p)
print('m4_curvature',curvature(p))
print('first_public_source_date','2020-09-11')
