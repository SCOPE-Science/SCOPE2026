#!/usr/bin/env python3
"""Independent numerical and rational diagnostics for a two-stage renewal-succession theorem.
Run: python3 check.py. Uses Python's standard library only.
"""
from fractions import Fraction as Q
from math import exp, expm1, isclose
from random import Random

checks=0

def check(p, detail):
    global checks
    assert p, detail
    checks += 1

def g(x):
    # Stable near zero, avoiding the subtraction of nearly equal quantities.
    if x<1e-4:
        B=sum(((-1.)**k)*(k-1)*x**k/__import__('math').factorial(k) for k in range(2,9))
    else:
        B=-expm1(-x)-x*exp(-x)
    return B/(x*(1+x))

def p_suitable(t,a,b):
    if a==b: return a*t*exp(-a*t)
    return a*exp(-b*t)*(-expm1(-(a-b)*t))/(a-b)

def ud(m,a,b):
    if abs(a-b)<1e-12:
        x=a*m
        return (-expm1(-x)-x*exp(-x))/x
    return a/(a-b)*((-expm1(-b*m))/(b*m)-(-expm1(-a*m))/(a*m))

def ue(m,a,b):
    return a*m/((1+a*m)*(1+b*m))

def simpson(f,low,high,n=1000):
    h=(high-low)/n
    return (f(low)+f(high)+4*sum(f(low+(2*j-1)*h) for j in range(1,n//2+1))+2*sum(f(low+2*j*h) for j in range(1,n//2)))*h/3

def r_elastic(x):
    B=-expm1(-x)-x*exp(-x)
    return x*x*exp(-x)/B-1-x/(1+x)

def root_rate(a,b):
    zlow,zhigh=.1,3.
    for _ in range(100):
        mid=(zlow+zhigh)/2
        if r_elastic(mid)>0:zlow=mid
        else:zhigh=mid
    z=(zlow+zhigh)/2
    if a==b:return z/a,z
    low,high=z/max(a,b),z/min(a,b)
    # D is positive at the lower endpoint, negative at the upper endpoint.
    for _ in range(75):
        mid=(low+high)/2
        d=a/(a-b)*(g(a*mid)-g(b*mid))
        if d>0:low=mid
        else:high=mid
    return (low+high)/2,z

# Exact stationary CTMC equations with exponential reset rate rho=1/m.
for na in range(1,19):
    for nb in range(1,17):
        for nm in range(1,8):
            a,b,m=Q(na,3),Q(nb,4),Q(nm,5)
            rho=1/m
            p0=rho/(a+rho)
            p1=a*rho/((a+rho)*(b+rho))
            p2=1-p0-p1
            check(p0+p1+p2==1 and min(p0,p1,p2)>0,'stationary normalization')
            check(a*p0==(b+rho)*p1,'suitable-stage balance')
            check(b*p1==rho*p2,'post-senescence balance')
            check(p1==a*m/((1+a*m)*(1+b*m)),'closed rational formula')

# Direct integration checks independent of the renewal formula.
for a,b in [(1.,1.),(1.,2.),(2.,1.),(.5,3.),(3.,.5),(2.,5.)]:
    for m in [.15,.4,1.2,2.5,5.]:
        v=simpson(lambda t:p_suitable(t,a,b),0,m)/m
        check(abs(v-ud(m,a,b))<2.e-8,('fixed-period integral',a,b,m,v,ud(m,a,b)))
        # Exponential-reset renewal occupancy integral on finite interval.
        T=40/(1/m+min(a,b))
        w=simpson(lambda t:exp(-t/m)*p_suitable(t,a,b)/m,0,T,n=4000)
        check(abs(w-ue(m,a,b))<2.e-8,('exponential integral',a,b,m,w,ue(m,a,b)))

rng=Random(20261118)
for j in range(700):
    a=10**rng.uniform(-1,1)
    b=a if j%7==0 else 10**rng.uniform(-1,1)
    if abs(a-b)<1e-7 and a!=b: b*=1.01
    crit,z=root_rate(a,b)
    check(.8<z<.95,'peak root bracket')
    if a!=b:
        check(z/max(a,b)<crit<z/min(a,b),'strict crossover bounds')
    check(abs(ue(crit,a,b)-ud(crit,a,b))<3e-9,('crossover equality',a,b,crit))
    for factor,sign in [(.5,1.),(.8,1.),(1.25,-1.),(2.,-1.)]:
        m=crit*factor
        D=ue(m,a,b)-ud(m,a,b)
        check(sign*D>1e-12,('crossing sign',a,b,m,D))
print(f'PASS: {checks} assertions, including exact-rational Markov balances and direct quadrature')
print('Equal-rate crossover z =',root_rate(1.,1.)[0])
print('Rate (a,b)=(1,2) crossover m =',root_rate(1.,2.)[0])
