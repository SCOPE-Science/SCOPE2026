#!/usr/bin/env python3
"""Separate arithmetic and grid checks for the three-observation two-decay design.
Only the Python standard library is required. These finite checks supplement the proof.
"""
from fractions import Fraction as F
from math import exp,log,sqrt,isfinite
from random import Random

checks=0

def check(cond, description):
    global checks
    checks+=1
    if not cond:
        raise AssertionError(description)

def obj(a,b,T,t):
    p=(exp(-a*t),exp(-b*t))
    q=(exp(-a*T),exp(-b*T))
    rows=((1.0,1.0),p,q)
    aa=sum(row[0]*row[0] for row in rows)
    bb=sum(row[1]*row[1] for row in rows)
    ab=sum(row[0]*row[1] for row in rows)
    return aa*bb-ab*ab

def minors(a,b,T,t):
    x=exp(-a*t); q=exp(-a*T); r=b/a; u=exp(-(b-a)*t); v=exp(-(b-a)*T)
    return x*x*(1-u)**2+q*q*(1-v)**2+q*q*x*x*(u-v)**2

def critical(a,b):
    return log(b/a)/(b-a)

def solve(a,b,T):
    r=b/a; q=exp(-a*T); v=exp(-(b-a)*T)
    if T <=critical(a,b):
        return None
    A=r*(1+q*q)
    B=-(r+1)*(1+q*q*v)
    C=1+q*q*v*v
    disc=B*B-4*A*C
    if disc<=0:
        raise AssertionError('unexpected nonpositive discriminant')
    # Stable small-root formula avoids cancellation at large horizons.
    small=2*C/(-B+sqrt(disc))
    big=(-B+sqrt(disc))/(2*A)
    if not (v<small<big<1):
        raise AssertionError(f'root ordering failure {a,b,T,v,small,big}')
    return -log(small)/(b-a)

# Exact rational Cauchy--Binet and derivative polynomials for integer rate ratios.
rng=Random(35858)
for r in range(2,10):
    for _ in range(240):
        q=F(rng.randrange(1,15),16)
        x=q+(1-q)*F(rng.randrange(0,17),16)
        rows=((F(1),F(1)),(x,x**r),(q,q**r))
        d00=sum(row[0]**2 for row in rows)
        d11=sum(row[1]**2 for row in rows)
        d01=sum(row[0]*row[1] for row in rows)
        gram=d00*d11-d01**2
        u=x**(r-1);v=q**(r-1)
        cb=x*x*(1-u)**2+q*q*(1-v)**2+q*q*x*x*(u-v)**2
        check(cb==gram,'Cauchy--Binet rational check')
        direct=2*x*(1-u)**2-2*(r-1)*x*u*(1-u)+2*q*q*x*(u-v)**2+2*(r-1)*q*q*x*u*(u-v)
        Q=r*(1+q*q)*u*u-(r+1)*(1+q*q*v)*u+1+q*q*v*v
        check(direct==2*x*Q,'exact derivative identity')
        check((x**r-x)**2+(q**r-q)**2+(x**r*q-x*q**r)**2==gram,'independent minors')

# Global optimality checked against dense grids for a range of real rate ratios.
for r in (1.03,1.1,1.5,2.0,2.7,3.0,7.0,20.0):
    a=1.0;b=r
    tc=critical(a,b)
    for scale in (.05,.3,.9,.999,1.001,1.01,1.2,1.5,3,6):
        T=tc*scale
        tstar=solve(a,b,T)
        endpoint= min(obj(a,b,T,0),obj(a,b,T,T))
        exact_end=2*exp(-2*a*T)*(1-exp(-(b-a)*T))**2
        # For r close to one and short T, near-cancellation affects plain Gram determinant.
        check(abs(endpoint-exact_end)<1e-11+1e-6*exact_end,'endpoint determinant')
        best=endpoint if tstar is None else minors(a,b,T,tstar)
        if tstar is None:
            check(T<=tc,'endpoint-side threshold')
        else:
            check(0<tstar<T,'interior location')
            check(best>exact_end,'strict interior advantage')
        for i in range(601):
            tt=T*i/600
            grid=minors(a,b,T,tt)
            check(best+1e-13>=grid,'global maximizer sampled grid')

# Explicit phase interface: at threshold the optimization is endpoint-only.
for r in (1.2,1.7,2,3,8):
    a=1.;b=r;tc=critical(a,b)
    T=tc
    eq=minors(a,b,T,0)
    for i in range(1,400):
        check(minors(a,b,T,T*i/400)<eq+1e-13,'critical-case strict interior gap')

# Near-threshold displacement and quadratic advantage, all from exact formula.
for r in (1.3,2.,4.):
    a=1.;b=r;tc=critical(a,b)
    q2=exp(-2*tc)
    for delta in (1e-3,3e-4):
        T=tc+delta
        ts=solve(a,b,T)
        predicted=tc-q2/(r-q2)*delta
        check(abs(ts-predicted)/delta<.04,'threshold expansion')
        extra=minors(a,b,T,ts)-minors(a,b,T,0)
        pred=q2*(b-a)**2/(r-q2)*delta**2
        check(abs(extra/pred-1)<.05,'quadratic gain expansion')

# Long-horizon limit and exponential gain.
for r in (1.5,2,3,7):
    a=1.;b=r;T=18.0
    ts=solve(a,b,T)
    check(abs(ts-critical(a,b))<.001,'large horizon time limit')
    optimum=minors(a,b,T,ts)
    norm=optimum/(2*exp(-2*T)*(1-exp(-(b-a)*T))**2)
    expected=(r-1)**2/(2*r**(2+2/(r-1)))*exp(2*T)
    check(abs(norm/expected-1)<.001,'asymptotic information gain')

print('VERIFICATION_OK',checks,'exact-rational and sampled-grid assertions')
