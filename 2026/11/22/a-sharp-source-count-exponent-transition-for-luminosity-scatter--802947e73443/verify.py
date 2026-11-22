#!/usr/bin/env python3
"""Numerical cross-checks for the finite-horizon flux-selection identity.

All analytic claims require the proof in RESULT.md; numerical tests are diagnostic.
This script uses only the Python standard library.
"""
import math

TESTS = 0

def check(ok, note=''):
    global TESTS
    TESTS += 1
    if not ok:
        raise AssertionError(f'{TESTS}: {note}')

def phi(z):
    return math.erfc(-z / math.sqrt(2.0)) / 2.0

def selected(q, x, t):
    a = q / 2.0
    if t == 0.0:
        return min(1.0, x**a)
    d = math.log(x)
    s = math.sqrt(t)
    return (x**a * math.exp(a*(a-1.0)*t/2.0)
            *phi((-d-(a-0.5)*t)/s)
            + phi((d-t/2.0)/s))

def density_at_zero(x, t):
    d = math.log(x)
    return math.exp(-(d-t/2.0)**2/(2.0*t))/math.sqrt(2*math.pi*t)

def truncated_power(q, x, t):
    a=q/2.0
    d=math.log(x)
    return x**a*math.exp(a*(a-1)*t/2)*phi((-d-(a-0.5)*t)/math.sqrt(t))

def derivative(q, x, t):
    a=q/2.0
    return a/2.0*((a-1)*truncated_power(q,x,t)-density_at_zero(x,t))

def ratio(q,x,t):
    p=density_at_zero(x,t)
    return truncated_power(q,x,t)/p if p>0 else float("inf")

def solve(q,x):
    a=q/2.0
    check(a>1 and x<1)
    lo=1e-6
    hi=max(3.0, 4*abs(math.log(x)))
    while ratio(q,x,hi) > 1/(a-1):
        hi *=2
    # Starting point is small enough for the chosen examples.
    check(ratio(q,x,lo)>1/(a-1),'lower bracket')
    for _ in range(95):
        m=(lo+hi)/2
        if ratio(q,x,m)>1/(a-1):lo=m
        else:hi=m
    return (lo+hi)/2

def radial(q,x,t,n=4096):
    # Independent radial-space integration, using the survival probability.
    s=math.sqrt(t)
    d=math.log(x)
    def fn(y):
        if y==0:
            return 1.0 if q==1 else 0.0
        return q*y**(q-1)*phi((d-t/2-2*math.log(y))/s)
    sm=fn(0.0)+fn(1.0)
    for i in range(1,n):
        sm+=(4 if i%2 else 2)*fn(i/n)
    return sm/(3*n)

for q in (1,2,3,4,5):
    for x in (.1,.5,.9,1.0,1.5,3.0):
        for t in (.07,.4,1.7,4.0):
            v=selected(q,x,t)
            check(0<v<1,'fraction bounds')
            if q<=4:
                check(abs(v-radial(q,x,t))<2.0e-6,'direct radial integral')
            # Independent symmetric time difference.
            h=2e-5*min(1,t)
            fd=(selected(q,x,t+h)-selected(q,x,t-h))/(2*h)
            check(abs(fd-derivative(q,x,t))<2.0e-7,'derivative identity')
            if q<=2 or x>=1:
                check(derivative(q,x,t)<0,'negative selection derivative')

for q in (2.5,3,4,6):
    for x in (.01,.1,.2,.5,.8):
        t=solve(q,x)
        check(abs(ratio(q,x,t)-1/(q/2-1))<1.0e-8,'root equation')
        check(derivative(q,x,t*.85)>0,'rise before optimum')
        check(derivative(q,x,t*1.15)<0,'fall after optimum')
        check(selected(q,x,t)>selected(q,x,0),'strict interior advantage')
        for t2 in (t/2, .8*t,1.3*t,2*t):
            check(selected(q,x,t)>selected(q,x,t2)-2.0e-14,'global examples')

# The three-dimensional example and its deep-census asymptotics.
t=solve(3,.1)
check(abs(t-2.151163193212655)<2e-10,'numerical 3D optimum')
check(abs(selected(3,.1,t)-.04896978900936576)<2e-10,'3D maximum')
h=20.0
x=math.exp(-h)
t=solve(3,x)
check(abs(t-(2*h-4))<.5,'asymptotic optimizing variance')
asym=3*x/math.sqrt(4*math.pi*h)
check(abs(selected(3,x,t)/asym-1)<.1,'asymptotic yield')

print(f'PASS: {TESTS} numerical assertions; analytic theorem in RESULT.md.')
