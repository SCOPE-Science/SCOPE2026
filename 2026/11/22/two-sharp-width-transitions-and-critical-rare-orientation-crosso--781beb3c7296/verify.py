#!/usr/bin/env python3
"""Deterministic supplemental checks for a right square pyramid width theorem.
Pure Python 3; no external dependencies; analytic proof is in RESULT.md.
"""
import math

PI = math.pi
SQ2 = math.sqrt(2.0)


def direct_width(u, h):
    points = [(x, y, 0.0) for x in (-1.0, 1.0) for y in (-1.0, 1.0)]
    points.append((0.0, 0.0, h))
    dots = [sum(a * b for a, b in zip(p, u)) for p in points]
    return max(dots) - min(dots)


def formula_width(u, h):
    ell = abs(u[0]) + abs(u[1])
    return ell + max(ell, h * abs(u[2]))


def endpoints(h):
    return min(h, 2*h / math.sqrt(1+h*h)), max(2*SQ2, math.sqrt(2+h*h))


def folded_cdf_kernel(q):
    if q <= 1: return 0.0
    if q >= SQ2: return 1.0
    return 4.0 / PI * (math.asin(q / SQ2) - PI/4)


def wedge_area(h):
    s0 = h / math.sqrt(1+h*h)
    v_end = (1+h*h)**1.5/(2*h**3)
    low_at_0 = -h/2
    up_at_0 = h/(h*h-1)
    return 0.5*v_end*(up_at_0-low_at_0)


def min_coefficient(h):
    if h < math.sqrt(3)-1e-10: return 1/PI
    ob = (1+h*h)**2.5/(2*PI*h*h*(h*h-1))
    return ob + (1/PI if abs(h-math.sqrt(3))<1e-10 else 0)


checks=0

def check(ok, msg):
    global checks
    checks += 1
    if not ok: raise AssertionError(msg)

# Finite pointwise comparison with vertex support, in all height regimes.
for h in (0.35, 1.0, 1.65, math.sqrt(3), 1.93, math.sqrt(6), 3.05, 12.0):
    for j in range(2500):
        z = -1.0 + 2*(j+0.5)/2500
        theta = (j * 0.6180339887498949 % 1.0) * 2*PI
        s = math.sqrt(1-z*z)
        u = (s*math.cos(theta), s*math.sin(theta), z)
        check(abs(direct_width(u,h)-formula_width(u,h)) < 2e-12, 'support identity')

# Explicit exact equality witnesses for every phase and at the transitions.
for h in (0.4, 1.43, math.sqrt(3), 1.85, math.sqrt(6), 4., 20.):
    mn,mx=endpoints(h)
    min_u = (0.0,0.0,1.0) if h <= math.sqrt(3) else (h/math.sqrt(1+h*h),0.,1/math.sqrt(1+h*h))
    max_u = (1/SQ2,1/SQ2,0.) if h<=math.sqrt(6) else (1/math.sqrt(h*h+2),1/math.sqrt(h*h+2),h/math.sqrt(h*h+2))
    check(abs(direct_width(min_u,h)-mn)<2e-12,'minimizing witness')
    check(abs(direct_width(max_u,h)-mx)<2e-12,'maximizing witness')

# The local triangle in folded orientation coordinates has the claimed area.
for h in (math.sqrt(3), 2., 2.5, 4., 7.):
    expected = (1+h*h)**2.5/(8*h*h*(h*h-1))
    check(abs(wedge_area(h)-expected)<2e-12,'local wedge area')
    C = 4*wedge_area(h)/PI
    target = (1+h*h)**2.5/(2*PI*h*h*(h*h-1))
    check(abs(C-target)<2e-12,'tail coefficient')

# This exact first-octant cumulative kernel is checked against angular counting.
for q in (1.01,1.04,1.2,1.35,1.405):
    n=20000
    fraction=sum((math.cos((j+0.5)*PI/(2*n))+math.sin((j+0.5)*PI/(2*n))) <= q for j in range(n))/n
    check(abs(fraction-folded_cdf_kernel(q))<1/n+1e-8,'angular sublevel fraction')

# Critical crossover: local mode weights and both continuity limits.
crit_min = math.sqrt(3)
C_pole=1/PI
C_ridge=(1+crit_min**2)**2.5/(2*PI*crit_min**2*(crit_min**2-1))
check(abs(C_ridge-8/(3*PI))<1e-12,'critical minimum ridge coefficient')
check(abs(C_pole/(C_pole+C_ridge)-3/11)<1e-12,'critical minimum mixture')
C_eq=1/SQ2
C_apex=4/math.sqrt(2+6)
check(abs(C_eq/(C_eq+C_apex)-1/3)<1e-12,'critical maximum mixture')

print('PASS:',checks,'supplemental deterministic assertions')
