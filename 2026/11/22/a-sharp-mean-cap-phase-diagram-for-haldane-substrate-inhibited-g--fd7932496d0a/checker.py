#!/usr/bin/env python3
"""Deterministic diagnostic checks for the bounded-mean Haldane envelope theorem.
No external packages; the global theorem relies on the written analytic proof.
"""
from fractions import Fraction as Q
from math import sqrt, isclose
import random

checks = 0

def check(test, name):
    global checks
    checks += 1
    if not test:
        raise AssertionError(name)

def response(s, k, i, mu=1):
    return mu*s/(k+s+s*s/i)

def inflection(k, i):
    # unique positive root of s^3-3*k*i*s-k*i*i = 0
    lo, hi = sqrt(k*i), max(1., 4*sqrt(k*i)+i)
    while hi**3-3*k*i*hi-k*i*i < 0: hi *= 2
    for _ in range(100):
        mid=(lo+hi)/2
        if mid**3-3*k*i*mid-k*i*i > 0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def tangent(k, i, b):
    return (k+sqrt(k*k+k*b*(1+b/i)))*i/b

def upper(k,i,b,m):
    r=inflection(k,i)
    if b<=r: return response(m,k,i)
    a=tangent(k,i,b)
    if m<=a: return response(m,k,i)
    return ((b-m)*response(a,k,i)+(m-a)*response(b,k,i))/(b-a)

def lower(k,i,b,m):
    return (m/b)*response(b,k,i)

# Rational algebra: the line tangent at a is also a secant through the cap b.
for k,i,a in [(Q(1),Q(1),Q(4,3)),(Q(1),Q(1),Q(3,2)),(Q(2),Q(3),Q(3)),(Q(2),Q(3),Q(4))]:
    c=1/i
    b=k*(1+2*c*a)/(c*(c*a*a-k))
    check(a*a>k*i and b>a, 'valid rational tangency')
    D=lambda z:k+z+c*z*z
    fp=(k-c*a*a)/D(a)**2
    f=lambda z:z/D(z)
    for z in [Q(0),a/2,a,(a+b)/2,b,Q(2)*b/3]:
        ell=f(a)+fp*(z-a)
        rhs=-c*fp*(z-a)**2*(b-z)/D(z)
        check(ell-f(z)==rhs,'exact supporting-line identity')
        check(rhs>=0,'supporting line >= response')

# Full phase diagram and integration bound on arbitrary two-point laws.
for k,i in [(1.,1.),(2.,3.),(.4,4.),(5.,.3)]:
    peak=sqrt(k*i); r=inflection(k,i)
    check(r>peak,'inflection beyond response maximum')
    for scale in (.75,1.,1.001,1.3,2.,5.,10.):
        b=r*scale
        a=tangent(k,i,b)
        if b>r:
            check(peak<a<r<b,'location of tangent')
            b_from_a=k*i*(i+2*a)/(a*a-k*i)
            check(isclose(b,b_from_a,rel_tol=1e-12),'cap inverse')
        for j in range(1,20):
            m=b*j/20
            U,L=upper(k,i,b,m),lower(k,i,b,m)
            check(L-1e-12<=response(m,k,i)<=U+1e-12,'deterministic sandwiched')
            for u in range(0,11):
                x=m*u/10
                for v in range(1,11):
                    y=m+(b-m)*v/10
                    w=(m-x)/(y-x)
                    val=(1-w)*response(x,k,i)+w*response(y,k,i)
                    check(L-1e-11<=val<=U+1e-11,'all tested two-level laws bounded')

# Sharp transition and an asymptotic nonattainment signature.
k=i=1.
check(isclose(inflection(k,i),2*__import__('math').cos(__import__('math').pi/9),rel_tol=1e-12),'closed cubic root')
for m in (1.1,1.2,1.5,1.8):
    critical=k*i*(i+2*m)/(m*m-k*i)
    check(isclose(tangent(k,i,critical),m,rel_tol=1e-12),'sharp critical cap')
    check(isclose(upper(k,i,critical,m),response(m,k,i),rel_tol=1e-12),'transition equality')
    check(upper(k,i,critical*1.1,m)>response(m,k,i),'beneficial beyond threshold')
for b in (10,100,1000,10000):
    a=tangent(1,1,b)
    check(1<a<1+3/b,'tangency tends to kinetic peak')
    check(upper(1,1,b,3)<response(1,1,1),'strict unattained finite cap supremum')
check(upper(1,1,10000,3)>0.999*response(1,1,1),'limiting supremum')
print('PASS:', checks, 'deterministic assertions')
