#!/usr/bin/env python3
"""Deterministic numerical diagnostics for a circular lens area law.

All universal assertions and asymptotics require the companion analytic proof.
The computations use only the Python standard library.
"""
import math

PI=math.pi
COUNT=0

def approx(actual,expected,atol=1e-10,rtol=1e-8):
    global COUNT
    COUNT+=1
    assert math.isfinite(actual) and math.isfinite(expected)
    assert abs(actual-expected)<=atol+rtol*abs(expected),(actual,expected)

def rho(c,t):
    return math.sqrt(max(0.,1-c*c*math.sin(t)**2))-c*abs(math.cos(t))

def area(c,t,s):
    return 2*rho(c,t)*rho(c,s)*abs(math.sin(s-t))

def env(c):
    return 2*(1-c)*math.sqrt(1-c*c)

def G(lam,N=24000):
    h=PI/(2*N)
    return 4/PI**2*h*sum(math.sqrt(max(0.,1-2*lam*(math.sin((k+.5)*h)+math.cos((k+.5)*h)-1))) for k in range(N))

for c in [0.,.0002,.002,.02,.1,.25,.5,.8,.95,.995]:
    a=1-c; b=math.sqrt(1-c*c)
    approx(rho(c,0),a)
    approx(rho(c,PI/2),b)
    approx(area(c,0,PI/2),env(c))
    for j in range(1,100):
        t=PI*j/100
        r=rho(c,t)
        # The sampled boundary vector lies on the generating disk nearest its sign.
        approx((abs(r*math.cos(t))+c)**2+(r*math.sin(t))**2,1.,atol=3e-12)
        assert (r*math.cos(t)/a)**2+(r*math.sin(t)/b)**2<1+3e-12
        COUNT+=1
    for j in range(1,81):
        t=PI*(j+.25)/82
        for k in range(1,81):
            s=PI*(k+.75)/82
            assert area(c,t,s)<=env(c)+1e-11
            COUNT+=1

for c in [.1,.25,.5,.75]:
    a=1-c;b=math.sqrt(1-c*c)
    for eta in [.0004,.0002,.0001]:
        # Two directional perturbations isolate the quadratic and absolute contacts.
        dl=env(c)-area(c,eta,PI/2)
        dr=env(c)-area(c,0,PI/2+eta)
        approx(dl/(eta**2),a*a*b,atol=3e-3,rtol=2e-3)
        approx(dr/eta,2*a*c,atol=5e-4,rtol=2e-3)

# Exact disk CDF from uniform angle difference; use a quadrature count for a test.
for eps in [.001,.01,.1,.5,1.,1.8]:
    exact=2/PI*math.acos(1-eps/2)
    n=200000
    sample=sum(1 for j in range(n) if 2-2*abs(math.sin(PI*(j+.5)/n))<=eps)/n
    approx(sample,exact,atol=2e-5,rtol=1e-4)

# The mixed-parabolic limiting body has area 8/3.
n=20000
h=2/n
approx(sum(2*(1-(-1+(j+.5)*h)**2)*h for j in range(n)),8/3)

# The crossover coefficient includes both angular branches.
approx(G(0),2/PI)
for lam,val in [(.2,.60059247),(.5,.54080092),(1.,.41271686),(2.,.15463131),(5.,.05648558)]:
    approx(G(lam),val,atol=2e-5)
for lam in [100,1000]:
    approx(lam*G(lam),8/(3*PI**2),atol=1e-3,rtol=.005)

# Independent direct angular quadrature of the rare event for the fixed-lens theorem.
# The two near-maximizing patches are each parameterized by a rectangle in angular coordinates.
for c,eps in [(.25,1e-3),(.5,5e-4),(.8,2e-4)]:
    a=1-c;b=math.sqrt(1-c*c)
    Ralpha=1.08*math.sqrt(eps/(a*a*b))
    Rdelta=1.08*eps/(2*a*c)
    n1=n2=500
    hits=0
    for j in range(n1):
        alpha=-Ralpha+(j+.5)*(2*Ralpha/n1)
        for k in range(n2):
            delta=-Rdelta+(k+.5)*(2*Rdelta/n2)
            if area(c,alpha,PI/2+delta)>=env(c)-eps:
                hits+=1
    measured=(2*hits/n1/n2)*(2*Ralpha)*(2*Rdelta)/(PI**2)
    predicted=8/(3*PI**2*a*a*c*math.sqrt(b))*eps**1.5
    approx(measured,predicted,atol=0,rtol=.10)

print('VERIFY_OK deterministic_checks=%d; finite numerical diagnostics, analytic proof required' % COUNT)
