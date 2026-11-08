#!/usr/bin/env python3
"""Standalone finite consistency tests for the sparse Hardy-Hankel calculation.

This checks finite matrices, closed-form scalar identities, boundary cases and
sampled inequalities. The theorem's global quantified statements use the
algebraic proof in RESULT.md, not this finite computation.
"""
import cmath
import math

CHECKS = 0


def check(test, message):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(message)


def close(a, b, tol=3e-10):
    return abs(a-b) <= tol * max(1.0, abs(a), abs(b))


def critical(m):
    assert m >= 3
    if m == 3:
        return 0.5, 0.0
    s = 2.0/(m-1)
    x = (1.0-s*s)/2.0
    return (2.0/((1+s)**2))*x**(-(m-3)/2), x


def test_kernel(m, eps, w):
    # Matrix rows are the negative Fourier powers z^-1,...,z^-m.
    c = [0j]*m
    c[0] = math.sqrt(1-abs(w)**2)
    for j in range(1, m):
        c[j] = c[j-1]*w.conjugate()
    y = [c[0]*(1 if j == 0 else 0) + eps*c[m-j-1] for j in range(m)]
    return sum(abs(x)**2 for x in y)


def formula(m, eps, r):
    return 1-r*r+2*eps*(1-r*r)*r**(m-1)+eps*eps*(1-r**(2*m))


def max_hankel(eps):
    return (1+math.sqrt(1+4*eps*eps))/2


def run():
    for m in range(2, 17):
        for eps in (0.003, 0.2, 0.7, 1.3, 4.0):
            for r in (0.0, 0.19, 0.51, 0.76, 0.91):
                for theta in (0.0, 2*math.pi/(m-1)):
                    w = r*cmath.exp(1j*theta)
                    check(close(test_kernel(m, eps, w), formula(m, eps, r)),
                          f'kernel formula mismatch m={m} eps={eps} r={r}')
            # Top singular value of a 2x2 invariant block.
            h = max_hankel(eps)
            check(close(h*h-h-eps*eps, 0), 'spectral quadratic')
            check(h >= eps, 'operator eigenvalue dominates remaining block')
    for m in range(3, 18):
        threshold, x_star = critical(m)
        for fraction in (0.05, 0.35, 0.85, 0.999):
            eps = fraction*threshold
            base = 1+eps*eps
            for j in range(1, 301):
                r = j/301
                check(formula(m,eps,r) <= base+1e-8*max(1,base),
                      f'origin should dominate m={m}, eps={eps}, r={r}')
        if m>=4:
            r=math.sqrt(x_star)
            check(close(formula(m,threshold,r), 1+threshold**2),
                  'critical positive-radius tie')
            eps=1.06*threshold
            check(max(formula(m,eps,j/1600) for j in range(1,1600)) >
                  1+eps*eps+1e-9, 'transition should open a positive-radius winner')
        else:
            for eps in (0.51,0.8,1.0,3.0):
                x=(math.sqrt(1+6*eps)-2)/(3*eps)
                check(0<x<1, 'cubic maximizer range')
                check(formula(3,eps,math.sqrt(x)) > 1+eps*eps,
                      'cubic transition')
    for eps in (0.002,0.003,0.004,0.005,0.007):
        # m=2: unique critical point of a strictly concave radial profile.
        left,right=0.0,1.0
        for _ in range(80):
            mid=(left+right)/2
            grad=eps-mid-3*eps*mid**2-2*eps**2*mid**3
            if grad>0: left=mid
            else:right=mid
        r=(left+right)/2
        g=math.sqrt(formula(2,eps,r))
        gap=max_hankel(eps)-g
        check(close(r,eps-3*eps**3,tol=4e-7),'quadratic radial expansion')
        check(abs(gap/(eps**4)-0.5) < 0.002,'quartic norm gap')
    for m in (3,4,5,6,9,20,50,100):
        t,x=critical(m)
        check(t>=0.5, 'critical threshold at least one half')
        if m>=4:
            s=2/(m-1)
            check(close(x,(1-s*s)/2), 'critical radius')
            check(close(t, 2/(1+s)**2*x**(-(m-3)/2)), 'critical amplitude')
    print(f'PASSED {CHECKS} finite consistency assertions')


if __name__=='__main__':
    run()
