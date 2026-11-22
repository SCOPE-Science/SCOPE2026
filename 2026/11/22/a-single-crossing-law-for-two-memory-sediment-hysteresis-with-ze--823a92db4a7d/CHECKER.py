#!/usr/bin/env python3
"""Finite diagnostics for the two-memory hydrograph theorem; not a continuum proof."""
import math

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(f"diagnostic {checks}: {message}")

def f(rate, q):
    return math.exp(-rate*q)-math.exp(-rate*(2.0-q))

def R(k,h,q):
    # This form is well-conditioned for the checks away from q=1.
    return math.exp(h-k)*math.sinh(k*(1-q))/math.sinh(h*(1-q))

def J(r):
    return (1-2*r*math.exp(-r)-math.exp(-2*r))/(r*r)

def simpson(fun, count=4096):
    assert count%2==0
    step=1.0/count
    s=fun(0.0)+fun(1.0)
    for i in range(1,count):
        s+=(4 if i%2 else 2)*fun(i*step)
    return s*step/3

pairs=[(.3,.1),(.8,.4),(1.2,.3),(2.0,1.0),(3.0,.7),(4.0,1.5),(8.0,3.0)]
for k,h in pairs:
    rpeak=math.exp(h-k)*k/h
    rfoot=math.exp(h-k)*math.sinh(k)/math.sinh(h)
    check(rfoot>rpeak>0,'strict boundary ordering')
    previous=rfoot
    for j in range(1,500):
        q=j/500
        current=R(k,h,q)
        check(current<previous,'strict ratio monotonicity')
        check(abs(current-f(k,q)/f(h,q))<4e-11*max(current,1.0),'ratio identity')
        previous=current
    for frac in [0.0,.1,.3,.5,.7,.9,1.0]:
        b=rpeak+(rfoot-rpeak)*frac
        def sign(q):
            return f(k,q)-b*f(h,q)
        if frac==0.0:
            for j in range(1,300): check(sign(j/300)>0,'clockwise boundary')
        elif frac==1.0:
            for j in range(1,300): check(sign(j/300)<0,'counterclockwise boundary')
        else:
            lo=0.0;hi=1.0
            for _ in range(80):
                mid=(lo+hi)/2
                if R(k,h,mid)>b:lo=mid
                else:hi=mid
            root=(lo+hi)/2
            check(0<root<1,'interior root')
            check(sign(max(.000001,root/2))>0,'first lobe')
            check(sign((root+1)/2)<0,'second lobe')
    check(J(k)>0 and J(h)>0,'positive integral')
    check(abs(simpson(lambda q:q*f(k,q))-J(k))<1e-11,'area primitive k')
    check(abs(simpson(lambda q:q*f(h,q))-J(h))<1e-11,'area primitive h')
    bg=J(k)/J(h)
    check(rpeak<bg<rfoot,'zero-area ratio interior')
    check(abs(simpson(lambda q:q*(f(k,q)-bg*f(h,q))))<1e-11,'zero signed area')
    # For every q, directly compare opposite time branches of C.
    a=15.0;A=1.0;B=bg
    def C(t):
        q=t if t<=1 else 2-t
        return q*(a+A*math.exp(-k*t)+B*(1-math.exp(-h*t)))
    check(a>A*k+B*h,'synchronized-peak sufficient condition')
    prev=C(0.0)
    for j in range(1,501):
        cur=C(j/500)
        check(cur>prev,'unique rising time peak');prev=cur
    for j in range(501,1001):
        cur=C(j/500)
        check(cur<prev,'unique falling time peak');prev=cur
    for j in range(1,500):
        q=j/500
        gap=C(q)-C(2-q)
        target=q*(f(k,q)-bg*f(h,q))
        check(abs(gap-target)<1e-12*max(1.0,abs(gap)),'time-branch matching')

k=2.0;h=1.0;A=1.0;a=4.0;bg=J(k)/J(h)
lo=0.0;hi=1.0
for _ in range(90):
    mid=(lo+hi)/2
    if R(k,h,mid)>bg:lo=mid
    else:hi=mid
root=(lo+hi)/2
check(abs(bg-0.8540017411631948)<1e-14,'benchmark b')
check(abs(root-0.4403936786577955)<1e-13,'benchmark crossover')
check(a>k+bg*h,'benchmark synchronized peaks')
print(f'PASS {checks} finite diagnostics; benchmark B/A={bg:.12f}; crossing q={root:.12f}')
