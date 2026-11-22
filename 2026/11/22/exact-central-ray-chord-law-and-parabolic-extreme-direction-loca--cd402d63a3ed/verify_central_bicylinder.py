#!/usr/bin/env python3
"""Independent quadrature and deterministic sampling for a bicylinder's central-ray law.
Only the Python standard library is required. Finite tests do not establish the theorem.
"""
from math import acos, asin, atan, cos, pi, sin, sqrt, isclose
import random

ROOT2 = sqrt(2.0)
TESTS = 0

def check(test, message):
    global TESTS
    TESTS += 1
    if not test:
        raise AssertionError(message)

def survival_t(t):
    if not 0 <= t <= 1/ROOT2:
        raise ValueError('t out of range')
    s = sqrt(max(0.0, 1.0-2*t*t))
    return 4/pi*(atan(s)-t*atan(s/t)) if t > 0 else 1.0

def survival_l(l):
    if l <= 2:
        return 1.0
    if l >= 2*ROOT2:
        return 0.0
    return survival_t(sqrt(1-4/l**2))

def radial_chord(u):
    x,y,z = u
    return 2/sqrt(max(x*x+z*z,y*y+z*z))

def independent_integral(t, steps=16000):
    start = asin(t)
    end = pi/4
    if start >= end: return 0.0
    step = (end-start)/steps
    def fun(ph):
        return sqrt(max(0.0, 1.0-(t/sin(ph))**2))
    # Simpson quadrature, with independently obtained geometric integrand.
    res = fun(start)+fun(end)
    for j in range(1,steps):
        res += (4 if j%2 else 2)*fun(start+j*step)
    return (4/pi)*(res*step/3)

check(survival_l(2)==1 and survival_l(2*ROOT2)==0, 'endpoints')
for t in (0.01,0.03,0.07,0.1,0.2,0.3,0.4,0.5,0.6,0.68,0.705):
    check(abs(survival_t(t)-independent_integral(t))<6e-7, 'spherical integral mismatch '+str(t))
for t in (0.01,0.06,0.12,0.25,0.42,0.59,0.69):
    h = 1e-5
    numerical = -(survival_t(t+h)-survival_t(t-h))/(2*h)
    predicted = (4/pi)*atan(sqrt(1-2*t*t)/t)
    check(abs(numerical-predicted)<2e-7, 'density mismatch '+str(t))
for eps in (1e-2,1e-3,1e-4):
    low = 1-survival_l(2+eps)
    low_two_term = 2*sqrt(eps)-(2/pi)*eps
    check(abs(low-low_two_term)<1.0*eps**1.5, 'lower-tail expansion '+str(eps))
    high = survival_l(2*ROOT2-eps)
    high_lead = (4/(3*pi*2**.75))*eps**1.5
    check(abs(high/high_lead-1)<1.1*eps, 'upper-tail expansion '+str(eps))

rng=random.Random(7061461)
N=220000
values=[]
for _ in range(N):
    z=rng.uniform(-1,1)
    phi=rng.uniform(0,2*pi)
    r=sqrt(1-z*z)
    u=(r*cos(phi),r*sin(phi),z)
    length=radial_chord(u)
    check(2-1e-12<=length<=2*ROOT2+1e-12,'radial range')
    t=min(abs(u[0]),abs(u[1]))
    check(abs(length-2/sqrt(1-t*t))<2e-12,'radial representation')
    values.append(length)
for l in (2.02,2.05,2.11,2.25,2.50,2.65,2.75,2.80):
    observed=sum(x>l for x in values)/N
    predicted=survival_l(l)
    check(abs(observed-predicted)<0.0045, 'MC CDF mismatch '+str(l))

# Independent area quadrature of the shrinking four parabolic neighborhoods.
def local_area(h,steps=30000):
    dz=2*sqrt(h)/steps
    ans=0.0
    for j in range(steps+1):
        z=-sqrt(h)+j*dz
        # z^2+(1-z^2)|sin(2q)| < h, with |q|<pi/4
        ratio=max(0.0,min(1.0,(h-z*z)/(1-z*z)))
        angular_width=asin(ratio)  # full width in q about one maximum
        ans+=(1 if j in (0,steps) else (4 if j%2 else 2))*angular_width
    return dz*ans/3
for h in (0.1,0.04,0.01,0.003):
    ar=local_area(h)
    check(abs(ar/((4/3)*h**1.5)-1)<0.40*h, 'marked-domain area '+str(h))
    # Exactly four disjoint angular lobes on sphere with area element dphi dz.
    check(abs(4*ar/(4*pi)-survival_t(sqrt((1-h)/2)))<2e-8, 'local area CDF '+str(h))
print('PASS:',TESTS,'deterministic assertions; 220000 seeded isotropic directions,')
print('independent spherical quadrature, analytic density, endpoint tails, local angular area.')
