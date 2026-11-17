#!/usr/bin/env python3
"""Finite diagnostic checks for the Hardy Hankel two-frequency kernel phase boundary.

Run: python3 checker.py. This is not a substitute for the all-degree proof.
Only Python 3 standard libraries are required.
"""
import math
import cmath
import random

checks = 0

def check(predicate, description):
    global checks
    if not predicate:
        raise AssertionError(description)
    checks += 1


def threshold(m):
    if m == 3:
        return 2.0, 0.0
    t = 2.0 / (m - 1)
    c = 2.0 ** (-(m - 1) / 2) * (1 - t) ** ((m - 3) / 2) * (1 + t) ** ((m + 1) / 2)
    r = math.sqrt((1 - t*t) / 2)
    return c, r


def f(m,c,r):
    return c*c*(1-r*r) + 1-r**(2*m) + 2*c*r**(m-1)*(1-r*r)


def ray(m,c,r):
    if r >= 1/math.sqrt(2):
        return None
    root=math.sqrt(1-2*r*r)
    return (r**(m-3)*(1-r*r-root),r**(m-3)*(1-r*r+root))

rng = random.Random(260933242)

# Unitary-equivalent 2x2 norm and Fourier variance for arbitrary phases.
for m in range(3,15):
    for j in range(12):
        a = (0.2 + 3*rng.random()) * cmath.exp(1j * rng.uniform(-math.pi,math.pi))
        b = (0.2 + 3*rng.random()) * cmath.exp(1j * rng.uniform(-math.pi,math.pi))
        c = abs(a)/abs(b)
        norm = (abs(a)+math.sqrt(abs(a)**2+4*abs(b)**2))/2
        gram = (abs(a)**2+2*abs(b)**2+abs(a)*math.sqrt(abs(a)**2+4*abs(b)**2))/2
        check(abs(norm*norm-gram)<1e-10*(gram+1),f'Gram {m} {j}')
        r=rng.uniform(0.05,0.96)
        theta=cmath.phase(a*b.conjugate())/(m-1)
        z=r*cmath.exp(1j*theta)
        # Poisson mean-square via analytic Fourier coefficients.
        poiss = abs(a)**2+abs(b)**2+2*(a.conjugate()*b*z**(m-1)).real
        vari = poiss-abs(a*z+b*z**m)**2
        check(abs(vari/abs(b)**2-f(m,c,r))<1e-10*(1+c*c),f'Variance {m} {j}')

# Every analytic critical point is an exact origin/off-center tie.
for m in range(3,20):
    C,R=threshold(m)
    check(C>0 and 0<=R<1/math.sqrt(2),f'domain {m}')
    check(abs(f(m,C,R)-f(m,C,0))<3e-11,f'tie {m}')
    if m>=4:
        small,big=ray(m,C,R)
        check(abs(big-C)<3e-11,f'upper root {m}')
        check(small<C,f'lower root {m}')
        # The threshold is uniquely attained on the sampled grid near the analytic point.
        v=max(ray(m,C,r)[1] for r in (k/2000/math.sqrt(2) for k in range(1,2000)))
        check(v<=C+5e-10,f'maximality {m}')

# Sharp phase separation for the origin. Dense meshes are diagnostic only.
for m in range(3,13):
    C,R=threshold(m)
    for k in (0.2,0.5,0.8,0.99):
        c=C*k
        delta=max(f(m,c,j/2000)-f(m,c,0) for j in range(1,2000))
        check(delta>1e-14,f'below-threshold improvement {m} {k} {delta}')
    for k in (1.01,1.2,2,5):
        c=C*k
        delta=max(f(m,c,j/2000)-f(m,c,0) for j in range(1,2000))
        check(delta<-1e-13, f'above-threshold strictness {m} {k} {delta}')
    if m==3:
        for k in (0.05,0.2,0.5,0.95):
            c=2*k
            x=(-2*c+math.sqrt(c*c+6*c))/3
            check(x>0 and x<1 and abs(3*x*x+4*c*x+c*c-2*c)<3e-12,f'cubic radius {k}')

print(f'PASS {checks} finite diagnostic assertions for degrees 3 through 19; no inference from finite tests to all degrees.')
