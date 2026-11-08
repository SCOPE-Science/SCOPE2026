#!/usr/bin/env python3
"""Standalone scientific checks for symmetric two-state migration observation design."""
import itertools
import math
from fractions import Fraction

checks = 0

def check(test, label):
    global checks
    checks += 1
    if not test:
        raise AssertionError(label)

def f(u):
    return (u * u / math.expm1(u)) if u else 0.0

def fp(u):
    if not u:
        return 1.0
    if u > 700:
        return 0.0
    e = math.exp(u)
    return u * (2 * math.expm1(u) - u * e) / math.expm1(u)**2

def f2_at_peak(a):
    return 2 * (1-a) * (2-a) / a

def g(u):
    return 2 * (-math.expm1(-u)) - u

lo, hi = 1., 2.
for _ in range(80):
    mid = (lo + hi) / 2
    if g(mid)>0:lo=mid
    else:hi=mid
a = (lo+hi)/2
check(1.5<a<1.7, 'root localization')
check(abs(g(a))<1e-14,'root residual')
check(f2_at_peak(a)<0,'strict local maximum')
for j in range(1,1000):
    u = 0.001+j*0.025
    check(fp(u)<1,'zero-gap exclusion')
    if u<a-0.01:
        check(fp(u)>0,'one-gap increasing')
    if u>a+0.01:
        check(fp(u)<0,'one-gap decreasing')

# Independent log-likelihood enumeration for Bernoulli flip observations.
for q in (Fraction(1,8),Fraction(1,4),Fraction(1,2),Fraction(3,4)):
    for d in (Fraction(1,5),Fraction(1,2),Fraction(2),Fraction(4)):
        probs=((1+q)/2,(1-q)/2)
        # d/dk of same-state probability = -d q; flip probability = +d q.
        score=(-d*q,d*q)
        information=sum(score[i]*score[i]/probs[i] for i in range(2))
        expected=4*d*d*q*q/(1-q*q)
        check(information==expected,'one-gap rational Fisher identity')
        for m in (2,3,4):
            path_information=Fraction(0)
            for path in itertools.product((0,1),repeat=m):
                pr=Fraction(1)
                s=Fraction(0)
                for x in path:
                    pr*=probs[x]
                    s+=score[x]/probs[x]
                path_information+=pr*s*s
            check(path_information==m*expected,'independent exact path information')

# Exact rational polynomial identity for the strict two-gap witness.
for z in range(2,100):
    z=Fraction(z)
    lhs=1/(z-1)+9/(z**3-1)-8/(z**2-1)
    rhs=(z*z-5*z-2)/((z+1)*(z*z+z+1))
    check(lhs==rhs,'rational finite witness factorization')
    if z>=7:
        check(lhs>0,'strict finite witness at rational z')

# One-gap analytic information formula against direct transition probabilities.
for k in (0.4,1.0,2.3):
    for d in (0.03,0.2,0.5,1.2,3.0):
        q=math.exp(-2*k*d)
        pplus=(1+q)/2
        pminus=(1-q)/2
        direct=d*d*q*q*(1/pplus+1/pminus)
        formula=f(4*k*d)/(4*k*k)
        check(math.isclose(direct,formula,rel_tol=1e-12,abs_tol=1e-13),'two-state Fisher formula')

# Strict concavity over sufficiently short intervals; central second differences.
for u in [0.03*i for i in range(1,15)]:
    h=1e-4
    second=(f(u+h)-2*f(u)+f(u-h))/(h*h)
    check(second<-0.3,'small gap concavity')

# Equation for the unique long-horizon branch, independently root-solved.
def short_branch(m,H):
    low=a
    high=a+0.01
    def residual(s):
        return fp(s)-fp(H-(m-1)*s)
    check(residual(low)>0 and residual(high)<0,'root bracket')
    for _ in range(90):
        mid=(low+high)/2
        if residual(mid)>0:low=mid
        else:high=mid
    return (low+high)/2

for m in (2,3,4,5):
    for H in (30.0,34.0,38.0):
        s=short_branch(m,H)
        B=H-(m-1)*s
        R=H-(m-1)*a
        J=(m-1)*f(s)+f(B)
        Jeq=m*f(H/m)
        check(a<=s<a+0.01 and B>s,'one macroscopic gap')
        check(J>Jeq,'strict relative-information improvement')
        check(abs(fp(s)-fp(B))<1e-12,'equal-slope optimality')
        leading=R*R*math.exp(-R)/(-f2_at_peak(a))
        if leading>1e-10:
            check(abs((s-a)/leading-1)<0.12,'short-gap first asymptotic')
        check(abs((J-(m-1)*f(a))/(R*R*math.exp(-R))-1)<0.15,'value first correction')
        ratio_prediction=m*(m-1)*f(a)*math.exp(H/m)/H**2
        check(abs(J/Jeq/ratio_prediction-1)<0.7,'relative efficiency growth')

# Independent finite grid for m=2 and m=3, with coarse grid covering interior.
for H in (0.25,0.5,1.0):
    for m in (2,3):
        equal=m*f(H/m)
        if m==2:
            for i in range(1,100):
                x=H*i/100
                check(equal>=f(x)+f(H-x)-1e-12,'strict small-T equal spacing grid')
        else:
            for i in range(1,30):
                for j in range(1,30-i):
                    x=H*i/30
                    y=H*j/30
                    check(equal>=f(x)+f(y)+f(H-x-y)-1e-12,'3-gap equal spacing grid')

# Exact witness also compared numerically as a separate independent check.
uniform=8/math.expm1(4)
unequal=1/math.expm1(2)+9/math.expm1(6)
check(unequal>uniform and unequal/uniform>1.19,'finite witness')
print(f'PASS: {checks} mathematical checks; a={a:.12f}; witness ratio={unequal/uniform:.9f}')
