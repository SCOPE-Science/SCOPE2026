#!/usr/bin/env python3
"""Finite checks for one-node Rademacher Lanczos logdet risk.

Mathematical conclusions for all parameters are proved in RESULT.md; this
script performs exact finite sign enumeration and separate numerical tests.
"""
import itertools
import math

checks=0

def close(x,y,tol=2e-11):
    global checks
    checks+=1
    if not math.isclose(x,y,rel_tol=tol,abs_tol=tol):
        raise AssertionError((x,y))

def risk_formula(a,b,t,N):
    r=(a-b)/(a+b)
    B=math.log1p(-r*r*t*t)-math.log1p(-r*r)
    U=math.log((1+r*t)/(1-r*t))
    return B*B+U*U/N

def sample_values(a,b,theta):
    mid=(a+b)/2
    off=(a-b)*math.sin(2*theta)/2
    return [2*math.log(mid+off*z1*z2) for z1,z2 in itertools.product((-1,1),repeat=2)]

def unique_minimizer(a,b,N):
    r=(a-b)/(a+b)
    B0=-math.log1p(-r*r)
    Nb=2/B0
    if N<=Nb: return 0.
    def H(t):
        return math.log((1+r*t)/(1-r*t))/(r*t*(math.log1p(-r*r*t*t)-math.log1p(-r*r)))
    low,high=1e-13,1-1e-13
    for _ in range(110):
        mid=(low+high)/2
        if H(mid)>N: high=mid
        else: low=mid
    return (low+high)/2

for a,b in ((2.,1.),(3.,1.),(9.,1.),(11.,4.),(100.,1.)):
    r=(a-b)/(a+b)
    B0=-math.log1p(-r*r)
    close((math.log(a/b)/B0)**2>2/B0, True)
    for theta in (0.,0.031,0.17,0.27,math.pi/8,0.56,math.pi/4):
        t=abs(math.sin(2*theta))
        vals=sample_values(a,b,theta)
        mean=sum(vals)/4
        var=sum((v-mean)**2 for v in vals)/4
        B=math.log1p(-r*r*t*t)-math.log1p(-r*r)
        U=math.log((1+r*t)/(1-r*t))
        close(mean-math.log(a*b),B)
        close(var,U*U)
        for N in (1,2,3,5,10,100):
            close((mean-math.log(a*b))**2+var/N,risk_formula(a,b,t,N))
        # Explicit enumeration of all randomized probe sequences for N<=4.
        for N in (1,2,3,4):
            outcomes=[]
            for seq in itertools.product(vals,repeat=N):
                outcomes.append((sum(seq)/N-math.log(a*b))**2)
            close(sum(outcomes)/len(outcomes),risk_formula(a,b,t,N))
    for N in (1,2,3,5,10,30,100,500):
        endpoint=max(B0*B0,math.log(a/b)**2/N)
        tstar=unique_minimizer(a,b,N)
        for i in range(1001):
            t=i/1000
            close(risk_formula(a,b,t,N)<=endpoint+5e-12,True)
            close(risk_formula(a,b,t,N)+2e-8>=risk_formula(a,b,tstar,N),True)
        if tstar>0:
            delta=1e-5
            if tstar>delta and tstar<1-delta:
                approx=(risk_formula(a,b,tstar+delta,N)-risk_formula(a,b,tstar-delta,N))/(2*delta)
                close(approx,0.,5e-5)

# Boundary check: a=b gives exact deterministic zero error and the limiting
# threshold formulas are not asserted there (our theorem requires a>b).
for a in (0.25,1.,4.):
    for theta in (0.0,0.2,0.7):
        close(risk_formula(a,a,abs(math.sin(2*theta)),10),0.)

print(f"PASS: {checks} finite direct-enumeration, endpoint/minimum, and derivative comparisons")
print("Analytic assertions for continuous intervals are established in RESULT.md, not by this grid.")
