#!/usr/bin/env python3
"""Standalone diagnostics for the nested field-capture/PCR efficiency theorem."""
import math

checks = 0

def verify(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def exponent(m, p, q):
    return -math.log1p(-p * (1.0 - (1.0-q)**m))

def efficiency(m, p, q, a, b):
    return exponent(m, p, q) / (a + b * m)

def root_p(m, q=0.5, a=1.0, b=1.0):
    def diff(p):
        return efficiency(m, p, q, a, b)-efficiency(m+1, p, q, a, b)
    lo, hi = 1.0e-9, 1.0 - 1.0e-12
    verify(diff(lo) > 0.0, 'low-p sign')
    verify(diff(hi) < 0.0, 'high-p sign')
    for _ in range(70):
        mid = (lo+hi)/2
        if diff(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def relaxed_root(p, q=0.5, a=1.0, b=1.0):
    c=-math.log1p(-q)
    alpha=c*a/b
    def f(y):
        e=math.exp(-y)
        den=1-p+p*e
        psi=-math.log(den)
        der=p*e/den
        return (alpha+y)*der-psi
    lo,hi=0., 200.
    for _ in range(90):
        mid=(lo+hi)/2
        if f(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/(2*c)

# Correct two-level probability by exhaustive sample-state mixture.
for p in (0.02, 0.4, 0.8, 0.98):
    for q in (0.15, 0.5, 0.9):
        for m in range(1, 26):
            failure = (1-p)+p*(1-q)**m
            verify(abs(math.exp(-exponent(m,p,q))-failure)<5e-15,'sample probability')

# Global integer maximum by direct search for multiple nondegenerate calibrations.
for a,b in ((1.,1.), (0.2,1.), (3.,0.7)):
    for q in (0.2,0.5,0.8):
        for p in (0.02,0.1,0.4,0.8,0.92,0.97,0.995,0.999):
            mc=relaxed_root(p,q,a,b)
            best=max(range(1,101),key=lambda m: efficiency(m,p,q,a,b))
            candidates={max(1,math.floor(mc)),max(1,math.ceil(mc))}
            verify(best in candidates, 'continuous peak brackets integer winner')
            verify(all(efficiency(best,p,q,a,b)>=efficiency(m,p,q,a,b)-2e-15 for m in range(1,101)), 'global finite comparison')

thresholds=[root_p(m) for m in range(2,12)]
for i in range(len(thresholds)-1):
    verify(thresholds[i]<thresholds[i+1],'strict threshold ordering')
for m,p in enumerate(thresholds,start=2):
    verify(abs(efficiency(m,p,0.5,1,1)-efficiency(m+1,p,0.5,1,1))<3e-14,'tie')

verify(abs(thresholds[0] - 0.8359967364464)<1e-10, 'first switch')
verify(abs(thresholds[1] - 0.9551000827929)<1e-10, 'second switch')
verify(abs(thresholds[2] - 0.9849530658494)<1e-10, 'third switch')

# Finite-index asymptotic consistency, without claiming that finite checks prove limits.
r=0.5
c=-math.log(r)
for m in (8,10,12):
    p=root_p(m)
    approx=c*r**(m+1)/((1-r)*m)
    verify(0.7 < (1-p)/approx < 1.25, 'threshold asymptotic check')

for p in (0.1,0.4,0.8,0.95,0.99,0.999):
    m=relaxed_root(p)
    verify(m>0.,'positive relaxed optimum')
for p1,p2 in ((0.3,0.8),(0.8,0.95),(0.95,0.999)):
    verify(relaxed_root(p1)<relaxed_root(p2),'monotonic relaxed optimum')

print(f'PASS: {checks} standalone diagnostic assertions')
print('p_2,p_3,p_4 = ',*(f'{x:.12f}' for x in thresholds[:3]))
print('relaxed m at p=0.8, q=0.5, a=b=1:', f'{relaxed_root(0.8):.12f}')
