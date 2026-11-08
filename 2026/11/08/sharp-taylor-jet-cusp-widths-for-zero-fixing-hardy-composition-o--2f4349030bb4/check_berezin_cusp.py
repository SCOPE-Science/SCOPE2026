#!/usr/bin/env python3
"""Finite consistency checks for the analytic Hardy-composition Berezin formula.
All infinite-dimensional assertions require the separate written proof.
Uses only Python's standard library.
"""
import cmath
import math

checks = 0

def ok(test, label):
    global checks
    if not test:
        raise AssertionError(label)
    checks += 1

def val(w, a, c=0.0, m=2):
    phi = a*w + c*w**m
    return (1-abs(w)**2) / (1-w.conjugate()*phi)

def r_for_re(eps, theta, a, c, m):
    u = complex(math.cos(theta), math.sin(theta))
    left, right = 0.0, 0.75
    ok(val(right*u, a, c, m).real < 1-eps, 'section exists')
    for _ in range(58):
        mid = (left+right)/2
        if val(mid*u, a, c, m).real > 1-eps:
            left = mid
        else:
            right = mid
    r = (left+right)/2
    ok(abs(val(r*u, a, c, m).real - (1-eps)) < 3e-14, 'bisection section')
    return r

for a in (-1.0, -0.3, 0.0, 0.4, 0.9, 1.0):
    for r in (0.0, 0.03, 0.2, 0.55, 0.9):
        b = val(complex(r, 0), a)
        ok(abs(b.imag) < 1e-14, 'linear range is real')
        ok(abs(b.real - (1-r*r)/(1-a*r*r)) < 1e-14, 'linear exact formula')
        ok(0 < b.real <= 1, 'linear range bounds')

for m in (2, 3, 4):
    a, c = 0.25, 0.21
    for eps in (0.01, 0.003, 0.001):
        ims = []
        rs = []
        for j in range(1440):
            theta = 2*math.pi*j/1440
            r = r_for_re(eps, theta, a, c, m)
            rs.append(r)
            ims.append(val(r*complex(math.cos(theta), math.sin(theta)), a, c, m).imag)
        width = max(ims) - min(ims)
        limit = 2*abs(c)/(1-a)**((m+1)/2)
        ratio = width/eps**((m+1)/2)
        ok(abs(ratio/limit-1) < 0.09, 'finite small-epsilon cusp coefficient')
        ok(min(ims) < 0 < max(ims), 'non-real transverse sections')
        ok(all(abs(r*r/eps-1/(1-a)) < .12 for r in rs), 'section radius scaling')

# The operator symbol a*z+c*z^m maps the unit disk into itself in these examples:
for m in (2, 3, 4):
    a, c = 0.25, 0.21
    for j in range(1000):
        w = (j/1000) * cmath.exp(2j*math.pi/113)
        ok(abs(a*w+c*w**m) < 1, 'sample symbol remains in disk')

print(f'BEREZIN_JET_CUSP_FINITE_OK {checks}')
