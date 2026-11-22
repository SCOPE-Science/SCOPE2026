#!/usr/bin/env python3
"""Numerical cross-checks of a circular von Mises / Poisson L2 limit.

Only the Python standard library is required. Diagnostics are NOT substitutes
for the analytic proof of the universal asymptotic theorem.
"""
import math

PI = math.pi

def erfcx(x):
    return math.exp(x*x)*math.erfc(x)

def h(x):
    return (1+2*x*x)*erfcx(x)-2*x/math.sqrt(PI)

def bisect(f,lo,hi,steps=120):
    assert f(lo)*f(hi)<0
    for _ in range(steps):
        md=(lo+hi)*0.5
        if f(lo)*f(md)<=0:hi=md
        else:lo=md
    return (lo+hi)*0.5

x=bisect(lambda t:h(t)-1/(2*math.sqrt(2)), 0, 3)
c=2*x*x
F=1+math.sqrt(2*PI)*x-4*math.sqrt(PI)*x*erfcx(x)
assert 0.50878<x<0.50879
assert 0.51771<c<0.51773
assert 0.07056<F<0.07058
assert abs(h(x)-1/(2*math.sqrt(2)))<1e-13

# Equivalent integral expression for h(x), by integration by parts.
def int_h(x, N=5000):
    L=20.0
    dx=L/N
    s=0.0
    for j in range(N+1):
        y=j*dx
        v=y*y*math.exp(-x*y-y*y/4)/(2*math.sqrt(PI))
        s+=(1 if j==0 or j==N else 4 if j%2 else 2)*v
    return s*dx/3
for z in (0,0.25,x,1,2):
    assert abs(h(z)-int_h(z))<1e-9
for j in range(50):
    assert h(j/20)>h((j+1)/20)

# Direct uniformly sampled circle integrals, no Bessel library. Return scaled squared error.
def loss(r,kappa,N=8192):
    d=1-r
    po=0.0; vs=0.0; pv=0.0; a=0.0
    for j in range(N):
        th=2*PI*j/N
        q=math.exp(-kappa*(1-math.cos(th)))
        p=(1-r*r)/(1+r*r-2*r*math.cos(th))
        a+=q;vs+=q*q;pv+=p*q;po+=p*p
    A=a/N
    return d*(po/N+vs/(N*A*A)-2*pv/(N*A))

def gold(f,lo,hi):
    inv=(math.sqrt(5)-1)/2
    a,b=hi-inv*(hi-lo),lo+inv*(hi-lo)
    fa,fb=f(a),f(b)
    for _ in range(100):
        if fa<fb:hi,b,fb= b,a,fa; a=hi-inv*(hi-lo);fa=f(a)
        else:lo,a,fa=a,b,fb;b=lo+inv*(hi-lo);fb=f(b)
    return (lo+hi)/2, f((lo+hi)/2)

print('critical x =',repr(x),'c =',repr(c),'F =',repr(F),'moment-loss ratio =',1/F)
for r in (0.9, 0.95, 0.98, 0.99):
    d=1-r
    z,loss_value=gold(lambda t:loss(r,math.exp(t)/d**2), math.log(0.2),math.log(1.2))
    fit_c=math.exp(z)
    print(f'r={r:.3f} scaled_kappa={fit_c:.9f} scaled_error={loss_value:.9f}')
    assert abs(fit_c-c)<0.06
    assert abs(loss_value-F)<0.005

print('All numerical checks passed. The analytic proof is separate.')
