#!/usr/bin/env python3
"""Numerical and exact-arithmetic checks of the finite-star temporal BV formula.
Run with Python 3 standard library: python check_star_heat_derivative.py.
Finite computations complement, rather than prove, the all-degree theorem.
"""
import math
import random
from fractions import Fraction


def norm(k, t):
    u = math.exp(-k*t)
    b = (1-(k+1)*u)/k
    return math.exp(-t)*(abs(1-b)+(k-1)*abs(b))


def piece(k, t):
    z=math.exp(-t)
    if t <= math.log(k+1)/k:
        return (k+1)*z**(k+1)
    return z*(2*(k-1)/k-(k-2)*(k+1)/k*z**k)


def derivative_leaf_differences(x, t):
    k=len(x)-1
    u0=x[0]
    leafavg=sum(x[1:])/k
    d0=u0-leafavg
    central_rate=-k*d0*math.exp(-(k+1)*t)
    return [-(x[i]-leafavg)*math.exp(-t) + d0*math.exp(-(k+1)*t)-central_rate for i in range(1,k+1)]


def heat_vertices(x,t):
    k=len(x)-1
    v=sum(x[1:])/k
    m=sum(x)/(k+1)
    c=(x[0]-v)*math.exp(-(k+1)*t)/(k+1)
    return [m+k*c]+[m-c+(x[i]-v)*math.exp(-t) for i in range(1,k+1)]


def check():
    rng=random.Random(173207)
    for k in range(2,81):
        t0=math.log(k+1)/k
        for t in [0.,t0*.25,t0,t0*1.1,t0*2,0.5,1.,2.]:
            if abs(norm(k,t)-piece(k,t))>1e-12:raise AssertionError(('piece',k,t))
            for j in (1,k//2+1,k):
                x=[0.]+[1. if i==j else 0. for i in range(1,k+1)]
                deriv=derivative_leaf_differences(x,t)
                if abs(sum(map(abs,deriv))-norm(k,t))>2e-12:raise AssertionError(('attain',k,t,j))
    print('CLOSED_FORM_AND_ONE_EDGE_SHARPNESS_PASS k=2..80')
    for k in range(2,31):
        for _ in range(60):
            x=[rng.uniform(-3,3) for _ in range(k+1)]
            t=rng.uniform(0,1.8)
            y=derivative_leaf_differences(x,t)
            var=sum(abs(x[i]-x[0]) for i in range(1,k+1))
            if sum(map(abs,y))>norm(k,t)*var+2e-11:raise AssertionError(('induced',k,t))
            eps=3e-6
            pp=heat_vertices(x,t+eps)
            pm=heat_vertices(x,t-eps)
            z=[((pp[i]-pm[i])-(pp[0]-pm[0]))/(2*eps) for i in range(1,k+1)]
            if max(abs(a-b) for a,b in zip(y,z))>3e-7:raise AssertionError(('independent',k,t))
    print('INDEPENDENT_VERTEX_HEAT_FINITE_DIFFERENCES_AND_INPUT_STRESS_PASS cases=1740')
    for k in range(4,151):
        t0=math.log(k+1)/k
        t1=math.log((k-2)*(k+1)**2/(2*(k-1)))/k
        if not t1>t0:raise AssertionError(('torder',k))
        vals=[norm(k,t) for t in (t0+1e-7,t1,t1+1e-7)]
        if not(vals[1]>vals[0] and vals[1]>vals[2]):raise AssertionError(('uniquepeak',k,vals))
    print('SECONDARY_TURNING_TIME_AND_PEAK_SAMPLED_PASS k=4..150')
    def exact_Mpower(k):
        return Fraction(2*(k-1),k+1)**k*Fraction(2*(k-1),(k-2)*(k+1)**2)
    assert exact_Mpower(8)<1 and exact_Mpower(9)>1
    print('EXACT_DEGREE_EIGHT_NINE_UNIT_GAIN_TRANSITION_PASS',str(exact_Mpower(8)),str(exact_Mpower(9)))
    print('ALL_STAR_HEAT_TEMPORAL_BV_CHECKS_PASS')

if __name__=='__main__': check()
