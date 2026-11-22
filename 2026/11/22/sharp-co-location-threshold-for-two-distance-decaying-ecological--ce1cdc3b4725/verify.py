"""Finite numerical diagnostics for two independent distance-decaying ecological detectors.

Requires Python 3 standard library only. The theorem's proof is analytical;
these checks test algebra, constraints and numerical examples independently.
"""
import json
import math
import random

rng = random.Random(20261119)
checks = 0

def verify(test, description):
    global checks
    checks += 1
    if not test:
        raise AssertionError(description)

def h(d):
    if d == 0:
        return 1.0
    return math.exp(d) * math.sinh(d / 2) / (d / 2)

def optimum(ell, p):
    if p <= math.exp(-ell / 2):
        return 0.0
    lo, hi = 0.0, ell
    threshold = p * math.exp(ell / 2)
    for _ in range(65):
        mid = (lo + hi) / 2
        if h(mid) < threshold:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def formula(ell, p, a, b):
    if a > b:
        a, b = b, a
    d = b - a
    center = (a + b) / 2
    return (4*p - 2*p*math.cosh(d/2)*(math.exp(-center) + math.exp(center-ell))
            - p*p*math.exp(-d)*(1+d)
            + p*p/2*(math.exp(-2*center) + math.exp(2*center-2*ell))) / ell

def midpoint_integral(ell, p, a, b, n=3600):
    # Independent midpoint quadrature of the original conditional detection law.
    step = ell / n
    acc = 0.0
    for j in range(n):
        x = (j + 0.5)*step
        v1 = p * math.exp(-abs(x-a))
        v2 = p * math.exp(-abs(x-b))
        acc += v1+v2-v1*v2
    return acc/n

# Check analytical integration against independent direct quadrature.
for j in range(110):
    ell = rng.uniform(.15, 9)
    p = rng.uniform(.03, 1)
    a = rng.uniform(0, ell)
    b = rng.uniform(0, ell)
    verify(abs(formula(ell,p,a,b)-midpoint_integral(ell,p,a,b)) < 5e-7,
           'integral mismatch at sample %d' % j)

# Global comparison: random freely placed detector pairs in each tested landscape.
for j in range(125):
    ell = rng.uniform(.1, 9)
    p = rng.uniform(.01, 1)
    d = optimum(ell,p)
    best = formula(ell,p,(ell-d)/2,(ell+d)/2)
    verify(0 <= d < ell, 'optimal separation out of range')
    for k in range(90):
        a,b = rng.random()*ell,rng.random()*ell
        verify(formula(ell,p,a,b) <= best + 2e-12,
               'random freely placed pair improves on the claimed global maximum')

# Check exact centering comparison for pairs having prescribed separations.
for j in range(280):
    ell = rng.uniform(.1,10)
    p = rng.uniform(.01,1)
    d = rng.uniform(0,ell)
    a = rng.uniform(0,ell-d)
    centered = formula(ell,p,(ell-d)/2,(ell+d)/2)
    verify(formula(ell,p,a,a+d)<=centered+2e-12,
           'off-center improvement')

# Threshold ties, transition and monotonicity of optimizing separation.
for j in range(250):
    ell = rng.uniform(.15,10)
    pcrit = math.exp(-ell/2)
    p0 = max(.00001, pcrit*0.95)
    verify(optimum(ell,p0)==0,'co-location phase mismatch')
    verify(optimum(ell,pcrit)==0,'critical co-location mismatch')
    if pcrit < .9:
        p1 = (1+pcrit)/2
        d=optimum(ell,p1)
        verify(0 < d < ell,'separated phase mismatch')
        verify(abs(h(d)-p1*math.exp(ell/2))<5e-12,'root equation mismatch')
        verify(optimum(ell,1)>=d,'larger p shrank optimal separation')

# Full limiting positions, including the singular p=1 boundary.
for ell in [1e-3, 5e-4, 2e-4, 1e-4]:
    d=optimum(ell,1)
    verify(abs(d/ell-0.5)<0.0002,'quarter-geometry limit')
    verify(optimum(ell,0.99)==0.0,'imperfect long-range co-location')

# Fixed-decay short-sensor range / large landscape thirds regime.
for ell in [30.0,45.0,60.0]:
    for p in [.2,.5,1.0]:
        d=optimum(ell,p)
        approx=ell/3+2*math.log(ell)/3+2*math.log(p/3)/3
        verify(abs((d-approx)/ell)<0.045,'large-transect regime')

# Publication-style benchmark and an alternative baseline.
ell,p=2.0,.7
d=optimum(ell,p)
a,b=(ell-d)/2,(ell+d)/2
optimal=formula(ell,p,a,b)
center=formula(ell,p,ell/2,ell/2)
verify(abs(d-0.6269981100871)<2e-10,'benchmark gap')
verify(abs(optimal-0.6796718115204)<2e-10,'benchmark coverage')
verify(abs(center-0.67312592675295)<2e-10,'benchmark co-located coverage')
verify(optimal>center,'separation improvement')

print(json.dumps({
    'status':'passed','finite_assertions':checks,
    'benchmark':{'lambda_L':ell,'p':p,'optimal_dimensionless_gap':d,
                 'sensor_locations_dimensionless':[a,b],
                 'optimal_detection_probability':optimal,
                 'midpoint_colocation_detection_probability':center},
    'scope':'Numerical diagnostic checks only; general theorem requires analytical proof.'
},sort_keys=True,indent=2))
