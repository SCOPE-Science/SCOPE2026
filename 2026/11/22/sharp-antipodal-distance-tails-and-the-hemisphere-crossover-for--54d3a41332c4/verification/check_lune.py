#!/usr/bin/env python3
"""Independent integral and finite-distance checks for spherical-lune tail formulas.

Uses Python 3 standard library only. Finite experiments support, not replace,
the proof of limits and strict monotonicity.
"""
import math

PI = math.pi


def simpson(f, lo, hi, n=4000):
    assert n > 0 and n % 2 == 0
    h = (hi - lo) / n
    acc = f(lo) + f(hi)
    for i in range(1, n):
        acc += (4 if i % 2 else 2) * f(lo + h * i)
    return acc * h / 3


def coefficient(alpha):
    return (1 - alpha / math.tan(alpha)) / (16 * alpha * alpha)


def radial_integral_coefficient(alpha):
    c = math.cos(alpha)
    def f(x):
        d = (1 - x)**2 + 2 * c * x * (1 - x) + x*x
        return x * (1-x) / (d*d)
    return (math.sin(alpha)**2 / (8*alpha**2)) * simpson(f, 0, 1, 12000)


def J(a):
    if a >= 1:
        return 0.0
    if a <= 0:
        return 2.0/3
    v = math.sqrt(1-a*a)
    return 2*((v**3)/3 - a*(PI/4 - (a*v + math.asin(a))/2))


def crossover(lam):
    assert lam >= 0
    return simpson(lambda t:J(lam*math.sin(t)), 0, PI, 16000)/(2*PI*PI)


def halton(i, base):
    x = 0.0
    d = 1.0
    while i:
        i, r = divmod(i, base)
        d /= base
        x += r * d
    return x


def fixed_exact_sample(alpha, eps, N=130000):
    B = 1.2*eps/math.cos(alpha/2)
    assert 0 < B < 1
    sq = 0.0
    for i in range(1,N+1):
        a,b,c,d = (halton(i,base) for base in (2,3,5,7))
        ru, rv = B*math.sqrt(a), B*math.sqrt(c)
        dot = math.sqrt(1-ru*ru)*math.sqrt(1-rv*rv) - ru*rv*math.cos(alpha*(b-d))
        if dot > math.cos(eps):
            sq += 1/math.sqrt((1-ru*ru)*(1-rv*rv))
    return B**4*sq/(8*eps**4*N)


def crossover_exact_sample(lam, eps, N=130000):
    delta = lam*eps
    alpha = PI - delta
    tot=0.0
    for i in range(1,N+1):
        a,b,c,d = (halton(i,base) for base in (2,3,5,7))
        t, h, u, v = PI*a, 2*b-1, eps*c, eps*d
        s = t + eps*h
        if s < 0 or s > PI:
            continue
        A=math.sin(t)*math.sin(s)*math.cos(delta)+math.cos(t)*math.cos(s)
        dot=(math.cos(u)*math.cos(v)*A
          - math.cos(u)*math.sin(v)*math.sin(t)*math.sin(delta)
          - math.sin(u)*math.cos(v)*math.sin(s)*math.sin(delta)
          - math.sin(u)*math.sin(v)*math.cos(delta))
        if dot>math.cos(eps):
            tot+=math.cos(u)*math.cos(v)
    return PI*tot/(alpha**2*N)


def check():
    count=0
    for a in (0.3,0.6,1.0,PI/2,2.4,2.8):
        exact=coefficient(a)
        computed=radial_integral_coefficient(a)
        assert abs(computed/exact-1)<3e-8, (a,computed,exact)
        count += 1
    assert abs(coefficient(PI/2)-1/(4*PI**2))<1e-14
    assert abs(crossover(0)-1/(3*PI))<1e-10
    count+=2
    for a in (0.6,PI/2,2.4):
        est=fixed_exact_sample(a,0.02)
        assert abs(est/coefficient(a)-1)<0.045,(a,est,coefficient(a))
        count+=1
    for lam in (0,0.5,1,2):
        est=crossover_exact_sample(lam,0.02)
        ref=crossover(lam)
        assert abs(est/ref-1)<0.06,(lam,est,ref)
        count+=1
    for lam in (5,10,20,50):
        asympt=1/(16*PI*lam)
        assert abs(crossover(lam)/asympt-1)<0.025,(lam,crossover(lam),asympt)
        count+=1
    assert all(coefficient(a)<coefficient(b) for a,b in zip((.3,.6,1.,1.5,2.,2.5),(.6,1.,1.5,2.,2.5,3.)))
    count+=1
    print('LUNE_ANTIPODAL_TAIL_CHECKS_OK',count)

if __name__=='__main__':
    check()
