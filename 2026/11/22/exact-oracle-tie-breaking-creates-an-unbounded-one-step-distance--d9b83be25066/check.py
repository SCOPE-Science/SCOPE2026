#!/usr/bin/env python3
"""Finite consistency checks for an exact local-oracle one-step theorem.

The analytical statements for all real parameters are proved in RESULT.md;
this script checks representative rational examples and near-boundary regimes.
Run: python3 check.py
"""
from fractions import Fraction as F
from math import sqrt, isclose

checks = 0

def ok(condition, detail=""):
    global checks
    if not condition:
        raise AssertionError(detail)
    checks += 1

def tied_step(p, a, y):
    p, a, y = map(F, (p, a, y))
    gap = p*(p+a)
    dd = p*p+y*y
    alpha = min(F(1), gap/dd)
    new = (p*(1-alpha), alpha*y)
    return (new[0]*new[0]+new[1]*new[1])/(p*p), alpha

# Rational full algebraic determination of tied-oracle envelope.
for p in (F(1,2), F(1), F(2), F(5)):
    for a in (F(0), F(1,4), F(1,2), F(1), F(2), F(3), F(7), F(20)):
        r = a/p
        maximum = 2*r/(1+r) if r <= 1 else r
        radius_sq = a*a+2*a*p
        for numerator in range(-25,26):
            y = F(numerator,10)
            if y*y > radius_sq:
                continue
            ratio, alpha = tied_step(p,a,y)
            ok(ratio <= maximum, f"tied: {p,a,y,ratio,maximum}")
            ok(F(0) < alpha <= 1)
            # Exact short-step decrease for this isotropic quadratic.
            initial_obj = ((p+a)**2)/2
            # f(u,v) = 1/2((u+a)^2+v^2)
            xx = p*(1-alpha)
            yy = alpha*y
            new_obj = ((xx+a)**2+yy*yy)/2
            ok(new_obj < initial_obj)
        # y=0 always gives the exact minimizer.
        r0, alpha0 = tied_step(p,a,0)
        ok(r0 == 0)
        ok(alpha0 == 1)
        # Exact optimal y^2=pa when a>=p, and boundary when a<=p.
        if a >= p:
            y2 = p*a
            alpha = min(F(1),p*(p+a)/(p*p+y2))
            new2 = (p*(1-alpha))**2+alpha**2*y2
            ok(alpha==1 and new2/p**2==maximum)
        else:
            y2 = radius_sq
            alpha = min(F(1),p*(p+a)/(p*p+y2))
            new2 = (p*(1-alpha))**2+alpha**2*y2
            ok(new2/p**2 == maximum)

# Validate non-tied exact KKT conditions, one-step formula, and strict bound.
for p in (0.125,0.5,1.0,3.0):
    for a in (0.,.001,.1,.5,1.,5.,25.,150.):
        for q in (-10.,-2.,-.3,-1e-8,1e-8,.2,1.,10.):
            b=sqrt(a*a+2*a*p+q*q)
            t=sqrt((p+a)**2+q*q)
            sign=1 if q>0 else -1
            y=q-sign*b
            dx=-p
            dy=-sign*b
            # The first-coordinate KKT multiplier mu must be nonnegative.
            lam=abs(q)/b
            mu=p+a-p*lam
            ok(mu>=-1e-10)
            ok(isclose(dx*dx+dy*dy,t*t,rel_tol=1e-12,abs_tol=1e-11))
            gap=p*(p+a)+abs(q)*b
            alpha=min(1.,gap/(p*p+b*b))
            ok(0. < alpha <= 1.)
            x1=p*(1-alpha)
            q1=q-alpha*sign*b
            measured=x1*x1+q1*q1
            derived=p*p*((b-abs(q))**2+a*a)/(p*p+b*b)
            ok(isclose(measured,derived,rel_tol=1e-9,abs_tol=1e-9), str((p,a,q,measured,derived)))
            ok(measured<2*(p*p+q*q))
            before=((p+a)**2+q*q)/2
            after=((x1+a)**2+q1*q1)/2
            ok(after<before)
            # Check oracle objective against a well-spaced feasible slice grid.
            for k in range(101):
                x=k*p/100
                rem=t*t-(x-p)**2
                if rem<0:continue
                vy=q-sign*sqrt(rem)
                L=(p+a)*x+q*vy
                minval=q*y
                ok(L+1e-9 >= minval)

# A family of exact oracle ties produces unbounded point error inflation.
for a in (1,4,16,100,10000):
    p=1
    y=sqrt(a*p)
    ratio,alpha=tied_step(p,a,y)
    ok(alpha==1)
    ok(isclose(float(ratio),float(a/p)))
# For q!=0 the sharp 2-squared bound is approached by large normal offsets.
for a in (10.,100.,1000.,100000.):
    p,q=1.,1e-7
    b=sqrt(a*a+2*a*p+q*q)
    ratio=p*p*((b-q)**2+a*a)/((p*p+b*b)*(p*p+q*q))
    ok(0<2-ratio<3./a)
print(f"PASS: {checks} finite exact-rational and floating-point assertions")
