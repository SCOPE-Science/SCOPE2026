#!/usr/bin/env python3
"""Numerical consistency checks for a stochastic two-level eigenvalue crossing benchmark.
Standard-library only. These checks supplement an analytic proof.
"""
import math

checks = 0

def near(a, b, atol=1e-9, rtol=3e-6):
    global checks
    checks += 1
    assert abs(a-b) <= atol + rtol*max(abs(a), abs(b)), (a,b)

def simpson(f, a, b, tol=1e-11, depth=30):
    fa,fb=f(a),f(b)
    c=(a+b)/2;fc=f(c)
    s=(b-a)*(fa+4*fc+fb)/6
    def rec(a,b,fa,fb,fc,s,tol,depth):
        c=(a+b)/2; l=(a+c)/2; r=(c+b)/2
        fl,fr=f(l),f(r)
        sl=(c-a)*(fa+4*fl+fc)/6
        sr=(b-c)*(fc+4*fr+fb)/6
        if depth==0 or abs(sl+sr-s)<15*tol:
            return sl+sr+(sl+sr-s)/15
        return rec(a,c,fa,fc,fl,sl,tol/2,depth-1)+rec(c,b,fc,fb,fr,sr,tol/2,depth-1)
    return rec(a,b,fa,fb,fc,s,tol,depth)

def quad(f,eps, power=0):
    # Splitting near the avoided crossing prevents underresolution.
    cuts=sorted(set([0.,min(eps,1.),min(math.sqrt(eps),1.),1.]))
    return sum(simpson(f,a,b,tol=1e-9*eps**power) for a,b in zip(cuts,cuts[1:]))

def ev_diff(t,e,theta=0):
    return (1-theta*theta)*e*e/(math.hypot(t,e)+math.hypot(t,theta*e))

def proj_diff_sq(t,e,theta=0):
    r1=math.hypot(t,e)
    r0=math.hypot(t,theta*e)
    if r0==0: return 0.0
    return ((t/r1-t/r0)**2+(e/r1-theta*e/r0)**2)/2

for e in [0.25,0.1,0.02,0.003]:
    pn=quad(lambda t:proj_diff_sq(t,e),e)
    pe=1+e-math.hypot(1,e)
    near(pn,pe)
    en=quad(lambda t:ev_diff(t,e)**2,e,power=3)
    ee=2/3+e*e-(2/3)*(1+e*e)**1.5+(2/3)*e**3
    near(en,ee)
for theta in [0.0,0.25,0.5,0.8]:
    for e in [0.2,0.03,0.003]:
        a=quad(lambda t:proj_diff_sq(t,e,theta),e)
        b=quad(lambda t: ev_diff(t,e,theta)**2,e,power=3)
        near(a>0,True)
        near(b>0,True)
        if theta==0:
            near(a,1+e-math.hypot(1,e))
for p in [0.25,0.75,1,1.5,2,3]:
    for e in [0.004,0.0008]:
        v=quad(lambda t:ev_diff(t,e)**p,e,power=min(2*p,p+1))
        if p<1:
            limit= e**(2*p)/(2**p*(1-p))
        elif p==1:
            limit=(e*e/2)*math.log(1/e)
        else:
            limit=e**(p+1)*p/(p*p-1)
        # The critical and subcritical rates converge slowly; test direction and near-order.
        near(0.4 < v/limit < 1.5, True)
for q in [0.25,0.5,1,2]:
    for e in [0.004,0.0008]:
        v=quad(lambda t:proj_diff_sq(t,e)**q,e,power=min(2*q,1))
        if q<0.5:
            limit=e**(2*q)/(2**q*(1-2*q))
            near(0.4 < v/limit < 1.5, True)
        elif q==0.5:
            limit=e*math.log(1/e)/math.sqrt(2)
            near(0.4 < v/limit < 1.5, True)
        elif q==1:
            near(v,1+e-math.hypot(1,e))
        else:
            near(v>0,True)
print(f'PASS: {checks} deterministic quadrature and algebra checks.')
