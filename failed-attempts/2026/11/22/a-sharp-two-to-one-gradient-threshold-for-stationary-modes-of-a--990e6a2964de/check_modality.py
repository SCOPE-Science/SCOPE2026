#!/usr/bin/env python3
"""Independent arithmetic diagnostics for a stationary velocity-jump mode threshold.
The continuum proof is in RESULT.md; these finite checks are not its replacement.
"""
import math
import random
from fractions import Fraction

count = 0

def check(ok, label):
    global count
    count += 1
    if not ok:
        raise AssertionError(f"{label}, assertion {count}")


def kappa(rho, t):
    if rho == 0:
        return 0.0
    return math.cosh(t)**2 * math.tanh(rho*t)/math.tanh(t)


def logderiv_kappa(rho, t):
    return 2 * (math.tanh(t) + rho/math.sinh(2*rho*t) - 1/math.sinh(2*t))


def actual_derivative(rho, t, A, B, C):
    return A/math.cosh(t)**2 - B-C*math.tanh(rho*t)/math.tanh(t)


def log_stationary_ratio(t, rho, v0, v1, gamma0, gamma1, u):
    # Direct quadrature of the source's exact zero-current stationary formula.
    # Simpson's rule, independent from the threshold formula.
    x = t/u
    def kernel(s):
        y = math.tanh(u*s)
        z = math.tanh(rho*u*s)
        return -2*(gamma0*v1*y+gamma1*v0*z)/(v0*v0-v1*v1*y*y)
    n=200
    h=x/n
    integ=h/3*(kernel(0)+kernel(x)+4*sum(kernel((2*j-1)*h) for j in range(1,n//2+1)) +2*sum(kernel((2*j)*h) for j in range(1,n//2)))
    den = v0*v0-v1*v1*math.tanh(t)**2
    return math.log(v0*v0/den)+integ

# Hyperbolic derivative identity, elementary comparison lemma, ratio monotonicity.
for rho in (0.1,0.3,0.8,1.0,1.3,1.6,1.9,2.0):
    for t in (0.03,0.1,0.3,0.7,1.2,2.0):
        h=1e-5
        numeric=(math.log(kappa(rho,t+h))-math.log(kappa(rho,t-h)))/(2*h)
        analytic=logderiv_kappa(rho,t)
        check(abs(numeric-analytic)<2e-7, "logarithmic derivative")
        check(analytic>0, "strict positive gradient")
        check(kappa(rho,t+h)>kappa(rho,t-h), "positive increment")
        bound=2*math.tanh(t)*(1-1/math.cosh(2*t))
        check(analytic+1e-12>=bound, "sharp comparison with rho=2")

# F is strictly increasing, and the derivative of stationary density changes sign once at most.
rng=random.Random(410051)
for n in range(160):
    rho=2*rng.random()
    A=10**rng.uniform(-1,2)
    B=10**rng.uniform(-2,1)
    C=10**rng.uniform(-2,1)
    ts=[0.002 + j*0.03 for j in range(100)]
    vals=[B*math.cosh(t)**2+C*kappa(rho,t) for t in ts]
    check(all(vals[i+1]>vals[i] for i in range(len(vals)-1)), "stationary threshold monotonic")
    signs=[1 if A>v else -1 for v in vals]
    check(all(not (signs[j]==-1 and signs[j+1]==1) for j in range(len(signs)-1)), "no return to positive derivative")
    sign_actual = actual_derivative(rho,0.3,A,B,C)
    sign_criterion = A - (B*math.cosh(0.3)**2 + C*kappa(rho,0.3))
    check((sign_actual > 0) == (sign_criterion > 0), "derivative threshold equivalence")

# A worked rational witness at gradient ratio 3, which is a known special regime.
# rho=3, v0=1, v1=1/10, gamma0=gamma1=1, u=300, g=900.
# In squared tanh coordinate y, the derivative sign is the quadratic
# -1 + 47y -90y^2. Its roots are exactly 1/45 and 1/2.
y1,y2=Fraction(1,45),Fraction(1,2)
Q=lambda y: -Fraction(1)+47*y-90*y*y
check(Q(y1)==0 and Q(y2)==0,'exact rational stationary extrema')
for y,sgn in ((Fraction(0),-1), (Fraction(1,5),1), (Fraction(9,10),-1)):
    check(Q(y)*sgn>0, 'exact three-phase derivative signs')

# Independent numerical differentiation of stationary probability from quadrature.
for rho in (.5,1.5,2.0,3.0):
    for t in (.15,.5,1.1):
        v0,v1=2.0,1.0
        gamma0,gamma1=1.0,.8
        u=3.5
        A=u*v1*v1
        B=gamma0*v1
        C=gamma1*v0
        h=0.0004
        measured=(log_stationary_ratio(t+h,rho,v0,v1,gamma0,gamma1,u)-log_stationary_ratio(t-h,rho,v0,v1,gamma0,gamma1,u))/(2*h)
        exact=2*math.tanh(t)/(v0*v0-v1*v1*math.tanh(t)**2)*actual_derivative(rho,t,A,B,C)/u
        check(abs(measured-exact)<1e-5, 'stationary density independent quadrature')

print(f'PASS: {count} deterministic assertions; analytic proof remains necessary.')
