#!/usr/bin/env python3
"""Deterministic, independent numerical checks for ideal-hyperbolic-polygon radial laws."""
from math import acos, asin, atan, atanh, cos, cosh, exp, pi, sin, sinh, sqrt, tanh

def simpson(f, a, b, m=24000):
    assert m % 2 == 0
    h=(b-a)/m
    z=f(a)+f(b)
    for i in range(1,m):
        z+=(4 if i%2 else 2)*f(a+i*h)
    return z*h/3

def exact_survival(n,t):
    alpha=pi/n; r=atanh(cos(alpha)); A=(n-2)*pi
    if t<=0:return 1.
    if t<=r:return 1-2*pi*(cosh(t)-1)/A
    theta=acos(cos(alpha)/tanh(t))
    return 2*n/A*(acos(sin(theta)/sin(alpha))-cosh(t)*(alpha-theta))

def independent_survival(n,t):
    alpha=pi/n; r=atanh(cos(alpha)); A=(n-2)*pi
    if t<=r: return 1-2*pi*(cosh(t)-1)/A
    theta=acos(cos(alpha)/tanh(t))
    Delta=alpha-theta; c=cos(alpha); b=sin(alpha)
    endpoint=sqrt(2*Delta*c/b)
    def g(v):
        if v==0:return endpoint
        phi=alpha-Delta*v*v
        # avoid catastrophic cancellation at tiny v
        den=(b-sin(phi))*(b+sin(phi))
        return 2*Delta*v*(cos(phi)/sqrt(den)-cosh(t))
    return 2*n/A*simpson(g,0,1,3000)

def lim(y):
    if y<=0:return 1-(2/pi)*exp(y)
    x=exp(-y)
    return (2/pi)*(asin(x)-exp(y)*x*x/(1+sqrt(1-x*x)))

def checks():
    worst=0.
    for n in (3,4,7,11):
        r=atanh(cos(pi/n))
        for t in (r+0.13,r+0.6,r+1.8):
            e=exact_survival(n,t);q=independent_survival(n,t)
            err=abs(q-e)
            worst=max(worst,err)
            assert err<2e-8,(n,t,err)
        c=2*n*cos(pi/n)/(sin(pi/n)*(n-2)*pi)
        # Moderate tail avoids cancellation. No infinity inference from this check.
        ratio=exact_survival(n,8.0)/exp(-8.0)
        assert abs(ratio/c-1)<2e-5,(n,ratio,c)
        assert abs(exact_survival(n,r)-(1-2*(1/sin(pi/n)-1)/(n-2)))<1e-12
        h=1e-7
        theta=acos(cos(pi/n)/tanh(r+h))
        A=(n-2)*pi
        tangent_cusp=(-2*n/A)*sinh(r+h)*theta/sqrt(h)
        predicted=(-2*n/A)*sqrt(2*cos(pi/n))
        assert abs(tangent_cusp/predicted-1)<3e-6,(n,tangent_cusp,predicted)
        assert abs(exact_survival(n,8.5)/exact_survival(n,8)-exp(-.5))<1e-6
    for n in (500,4000):
        alpha=pi/n; v=0.5
        U_inside=(2*n/((n-2)*pi))*(asin(sin(alpha*v)/sin(alpha))-alpha*v)
        assert abs(U_inside-1/3)<2/n,(n,U_inside)
        r=atanh(cos(pi/n))
        for y in (-1.,0.,0.4,1.2):
            x=exact_survival(n,r+y)
            assert abs(x-lim(y))<4/n,(n,y,x,lim(y))
    # Exact normalization of the finite-dimensional marked density and its marginals.
    # (z,s) density exp(s) on 0<z<exp(-2s); therefore integrate exp(-s).
    z=simpson(lambda s:exp(-s),0.,24.,20000)
    assert abs(z-(1-exp(-24)))<1e-9
    # Arcsine marginal and its independent exponential radial-depth marginal.
    # Coordinate substitution u=sin(phi) removes the endpoint singularity.
    norm=simpson(lambda phi: 1/pi,-pi/2,pi/2,20000)
    assert abs(norm-1)<1e-12
    print('ALL_CHECKS_PASSED; max_direct_quadrature_error=%.3g'%worst)
if __name__=='__main__': checks()
