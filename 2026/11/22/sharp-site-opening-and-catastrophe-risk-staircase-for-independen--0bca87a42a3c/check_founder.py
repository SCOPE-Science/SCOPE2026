#!/usr/bin/env python3
"""Reproducible numerical diagnostics for a fixed-cost founding-site theorem.

The exact theorem depends on analytic inequalities, not floating-point tests.
Run: python3 check_founder.py
"""
import math

TESTS = 0


def verify(condition, message):
    global TESTS
    TESTS += 1
    if not condition:
        raise AssertionError(message)


def ell(c, p, x):
    return -math.log(c + (1-c)*math.exp(-p*x))


def derivative(c, p, x):
    q = (1-c)*math.exp(-p*x)
    return p*q/(c+q)


def curvature(c, p, x):
    q = (1-c)*math.exp(-p*x)
    return -p*p*c*q/(c+q)**2


def effort_star(c, p, h):
    def H(x):
        return (x+h)*derivative(c,p,x)-ell(c,p,x)
    lo, hi = 0.0, 1.0
    while H(hi) > 0:
        hi *= 2
        if hi > 1.e12:
            raise AssertionError('bracket failed')
    for _ in range(150):
        mid = (lo+hi)/2
        if H(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def feasible_count(B,h):
    return [m for m in range(1,math.ceil(B/h)) if m*h < B]


def site_score(B,h,p,c,m):
    return m*ell(c,p,B/m-h)


def optimum(B,h,p,c):
    vals = [(m,site_score(B,h,p,c,m)) for m in feasible_count(B,h)]
    best = max(v for _,v in vals)
    return [m for m,v in vals if best-v < 5e-11]


def main():
    for c in (.001,.01,.1,.2,.4,.65,.85,.95,.995):
        for p,h in ((.3,.5),(1.,1.),(2.,.1),(1.3,4.)):
            x=effort_star(c,p,h)
            verify(x>0,'positive root')
            verify(abs((x+h)*derivative(c,p,x)-ell(c,p,x)) < 2e-12,'stationarity')
            for z in (0.1,1.,x,2*x,8*x):
                verify(curvature(c,p,z)<0,'concavity')
            for B in (1.25*h,2.8*h,5.4*h,12*h,21*h):
                counts=feasible_count(B,h)
                possible=optimum(B,h,p,c)
                pivot=B/(h+x)
                nearest={k for k in (math.floor(pivot),math.ceil(pivot)) if k in counts}
                if not nearest:
                    nearest={min(counts) if pivot<min(counts) else max(counts)}
                verify(set(possible).issubset(nearest),'integer candidates')
                for i in range(len(counts)-2):
                    v0,v1,v2=(site_score(B,h,p,c,counts[i+j]) for j in range(3))
                    verify(v1-v0>=v2-v1-1e-10,'strictly concave score')
    for B,h,p in ((10,1,1),(13,2,.3),(20,3,2)):
        prev=0
        for i in range(1,1000):
            c=i/1000
            m=optimum(B,h,p,c)[0]
            verify(m>=prev,'site number monotonic catastrophe risk')
            prev=m
    for c,m in ((.1,3),(.9,5)):
        B,h,p=10,1,1
        verify(optimum(B,h,p,c)==[m],'explicit example')
    verify(abs((1-(.1+.9*math.exp(-7/3))**3)-.9934319292147585)<1e-13,'first probability')
    verify(abs((1-(.9+.1*math.exp(-1))**5)-.2785496225050095)<1e-13,'second probability')
    print(f'PASS: {TESTS} diagnostic assertions; analytic proof required for universal claims')


if __name__=='__main__': main()
