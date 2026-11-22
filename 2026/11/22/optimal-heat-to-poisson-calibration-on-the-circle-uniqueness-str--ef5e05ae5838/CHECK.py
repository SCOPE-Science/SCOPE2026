#!/usr/bin/env python3
"""Finite diagnostics for heat-to-Poisson circle-kernel projection.

These checks test formulas and finite numerical truncations; they are not a
substitute for the analytic uniqueness and asymptotic arguments in RESULT.md.
Requires Python 3 standard library only.
"""
import math


def g(t, a, cutoff=45.0):
    nmax = max(12, int(math.sqrt(cutoff / t)) + 6)
    s = math.fsum(n * math.exp(-t*n*n-a*n) for n in range(1, nmax+1))
    return 4.0 * math.sinh(a)**2 * s


def root_a(t):
    lo, hi = 0.0, max(1.0, t + 1.0)
    while g(t, hi) <= 1:
        hi *= 2
    for _ in range(90):
        mid = (lo+hi)/2
        if g(t, mid) < 1: lo = mid
        else: hi = mid
    return (lo+hi)/2


def loss(t, a):
    nmax = max(20, int(math.sqrt(48/t))+6, int(48/a)+6)
    return 2.0 * math.fsum((math.exp(-n*a)-math.exp(-t*n*n))**2 for n in range(1,nmax+1))


def simp(f, a, b, n=20000):
    h=(b-a)/n
    s=f(a)+f(b)
    s+=4*math.fsum(f(a+j*h) for j in range(1,n,2))
    s+=2*math.fsum(f(a+j*h) for j in range(2,n,2))
    return h*s/3


def H(c):
    return 4.0*simp(lambda y:y*math.exp(-y-y*y/(c*c)),0.0,45.0,10000)


def find_c():
    lo,hi=0.4,2.0
    for _ in range(65):
        mid=(lo+hi)/2
        if H(mid)<1:lo=mid
        else:hi=mid
    return (lo+hi)/2


def J(c):
    return 2*simp(lambda x:(math.exp(-c*x)-math.exp(-x*x))**2,0.0,45.0,10000)


def H_prime(c):
    return 8/c**3*simp(lambda y:y**3*math.exp(-y-y*y/c**2),0.0,45.0,10000)


def main():
    checks=0
    for t in (0.003,0.01,0.05,0.1,0.25,0.5,1.0,2.0,3.0,5.0):
        a=root_a(t)
        assert a>t and abs(g(t,a)-1)<3e-11
        checks+=2
        assert g(t,a*0.99)<1 and g(t,a*1.01)>1
        checks+=2
        assert loss(t,a)<loss(t,a*0.95) and loss(t,a)<loss(t,a*1.05)
        checks+=2
        xs=[0.1*a,a,2*a,4*a]
        assert all(g(t,xs[j])<g(t,xs[j+1]) for j in range(3))
        checks+=1
    c=find_c(); j=J(c)
    assert abs(c-1.0777422543051748)<1e-8; checks+=1
    assert abs(j-0.06738055658082554)<1e-8; checks+=1
    b=(c**4/20+c*c/30)/H_prime(c)
    assert abs(b-0.0909824498025251)<1e-8; checks+=1
    for t in (0.003, 0.01, 0.03):
        a=root_a(t)
        observed=(a/math.sqrt(t)-c)/t**2
        assert abs(observed-b)<0.003; checks+=1
        E=loss(t,a)
        error_prediction=j/math.sqrt(t)-c*(2+c*c)/60*t**1.5
        assert abs(E-error_prediction)<0.0005*t**1.5; checks+=1
    for t in (3.0,4.0,5.0):
        q=math.exp(-t); r=math.exp(-root_a(t))
        approx=q-2*q**3+11*q**5
        assert abs(r-approx) < 70*q**7
        checks+=1
    print(f'PASS {checks} finite diagnostics; c={c:.15f}; J={j:.15f}; b={b:.15f}')


if __name__=='__main__':main()
