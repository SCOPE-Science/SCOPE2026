#!/usr/bin/env python3
"""Numerical diagnostics for the finite-reactivity Péclet crossover theorem.

All universal claims are proved analytically in RESULT.md; finite diagnostics
below test formulas and asymptotic normalization at sampled parameters.
Run with: python3 verify.py
Only Python's standard library is required.
"""
import math

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def base(b, a, y):
    """Dimensionless mean time for drift toward the reactive site."""
    return (math.expm1(y) + math.exp(y) * (b+y)/a) / (y*(2*b+y))

def c(n,b,a):
    if n == 0:
        return b/a
    return (1.0+(b+n)/a)/math.factorial(n)

def C(n,b,a):
    return 2*b*(n-1)*c(n,b,a)+(n-3)*c(n-1,b,a)

def H(y,b,a):
    """The exact derivative numerator divided by y^2; stable at small y."""
    c0=b/a
    value=-2*b*c0/y**2-2*c0/y+C(2,b,a)
    for n in range(3,90):
        term=C(n,b,a)*y**(n-2)
        value+=term
        if n>35 and abs(term)<1e-15*max(1.0,abs(value)):
            break
    return value

def stationary_numerator(y,b,a):
    e=math.exp(y)
    g=math.expm1(y)+e*(b+y)/a
    gp=e*(1+(b+y+1)/a)
    return y*(2*b+y)*gp-(2*b+2*y)*g

def root(b,a):
    left=1e-16
    right=1.0
    while H(right,b,a)<0:
        right*=2
        if right>20:
            raise RuntimeError('Unbounded bracket')
    for _ in range(100):
        mid=(left+right)/2
        if H(mid,b,a)<0:
            left=mid
        else:
            right=mid
    return (left+right)/2

def limit_subcritical(b):
    left=1e-14
    right=1.0
    def q(y):
        # perfect-reactivity H, with the vanishing constant coefficient
        value=b-1
        for n in range(3,90):
            value+=(2*b*(n-1)/math.factorial(n)
                    +(n-3)/math.factorial(n-1))*y**(n-2)
        return value
    while q(right)<0:
        right*=2
    for _ in range(90):
        mid=(left+right)/2
        if q(mid)<0: left=mid
        else: right=mid
    return (left+right)/2

def critical_Y(lam):
    lo=0.0
    hi=10.0+3*abs(lam)
    def q(y): return (2/3)*y**3+lam*y*y-2
    for _ in range(100):
        mid=(lo+hi)/2
        if q(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def main():
    for b in (0.2,0.5,0.8,1.0,1.2,1.5,2.0,4.0):
        for a in (0.1,0.5,1.0,3.0,10.0,1e2,1e4):
            y=root(b,a)
            check(y>0, 'positive root')
            check(abs(H(y,b,a))<2e-7*(1+abs(C(2,b,a))),f'H root residual {b},{a},{y}')
            for factor in (0.5,0.8,0.95):
                check(H(y*factor,b,a)<0,'negative before optimum')
                check(base(b,a,y*factor)>base(b,a,y),'time larger to left')
            for factor in (1.05,1.2,2.0):
                check(H(y*factor,b,a)>0,'positive after optimum')
                check(base(b,a,y*factor)>base(b,a,y),'time larger to right')
            sample=(0.05,0.1,0.2,0.4,0.8,1.5,2.5,4.0)
            for x,z in zip(sample,sample[1:]):
                check(H(z,b,a)>H(x,b,a),'H monotonic')
            for v in (0.05,0.1,0.25,0.5,1.0,1.5,2.0):
                n=stationary_numerator(v,b,a)
                check(abs(H(v,b,a)*v*v-n)<2e-9*(1+abs(n)), 'series identity')
    for b in (0.25,0.5,0.8):
        y_inf=limit_subcritical(b)
        check(abs(root(b,1e8)/y_inf-1)<2e-6,'subcritical limiting optimum')
    for b in (1.1,1.5,2.0,4.0):
        for a in (1e6,1e8):
            z=root(b,a)/(b*math.sqrt(2/(a*(b-1))))
            check(abs(z-1)<0.03,'supercritical square-root asymptotic')
    for a in (1e5,1e6,1e8):
        check(abs(root(1,a)/(3/a)**(1/3)-1)<0.006,
              'critical cube-root asymptotic')
    for lam in (-4,-3,-2,-1,0,1,2,3,4):
        a=1e8
        b=1+lam*a**(-1/3)
        y=root(b,a)
        check(abs(y*a**(1/3)/critical_Y(lam)-1)<0.018,
              'critical window scaling')
    print(f'PASS: {CHECKS} deterministic bounded checks')
    print('Diagnostics do not replace infinite-dimensional or asymptotic proofs.')

if __name__=='__main__': main()
