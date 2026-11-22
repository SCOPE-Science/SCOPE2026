"""Independent deterministic diagnostics for an exact Gaussian two-detector law.

Run with Python 3.10+: python checker.py
The global theorem is analytical; finite checks do not certify all real inputs.
"""
from math import exp, log, log1p, sqrt, isfinite
from random import Random


def log_qcritical(d, s):
    assert isinstance(d, int) and d >= 1 and s > 0
    return (d / 2) * log1p(2*s) - (d / 2 + 1) * log1p(s)


def coverage(d, s, q, a, ell=1.0):
    assert d >= 1 and s > 0 and 0 < q <= 1 and a >= 0 and ell > 0
    t = (a/ell)**2
    return (2*q*(1+s)**(-d/2)*exp(-t/(2*(1+s)))
            - q*q*(1+2*s)**(-d/2)*exp(-t))


def coverage_t_derivative(d, s, q, t):
    return (-q*(1+s)**(-d/2-1)*exp(-t/(2*(1+s)))
            +q*q*(1+2*s)**(-d/2)*exp(-t))


def optimum(d, s, q, ell=1.0):
    z = log(q) - log_qcritical(d, s)
    return ell*sqrt(max(0.0, 2*(1+s)/(1+2*s)*z))


def critical_spread(d):
    assert d >= 3
    def f(x): return log_qcritical(d, x)
    lo = (d-2)/4
    hi = max(1.0, 2**(d/2))
    while f(hi) > 0:
        hi *= 2
    for _ in range(100):
        mid = (lo+hi)/2
        if f(mid) > 0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def main():
    n=0
    def check(test, note):
        nonlocal n
        n += 1
        if not test: raise AssertionError(f'assertion {n}: {note}')
    rng=Random(490111)
    phi=(1+sqrt(5))/2
    for d in range(3,22):
        root=critical_spread(d)
        check(root > 0, ('positive root',d))
        check(abs(log_qcritical(d,root)) < 4e-12, ('root residual',d,root))
        check(log_qcritical(d,root*0.5) > 0, ('pre-root',d))
        check(log_qcritical(d,root*1.2) < 0, ('post-root',d))
        for s in [root*.1, root*.85, root, root*1.15, root*2]:
            q=1.0
            a=optimum(d,s,q)
            check((a<1e-9)==(s<=root*(1+1e-13)), ('phase',d,s,root,a))
    check(abs(critical_spread(3)-0.63770838850224)<1e-10,'3D root')
    check(abs(critical_spread(4)-phi)<1e-11,'golden-ratio root')
    for d in (16,20,24,28,32):
        root=critical_spread(d)
        S=2**(d/2)
        approx=S-d/4-1
        check(abs(root-approx) < 2*d*d/S, ('dimension asymptotics', d, root,approx))
    # Independent Gaussian one-dimensional midpoint-rule integral:
    # z is a standard normal; tensor Gaussian convolution is proved in text.
    for d,s,q,a in [(1,0.25,0.8,0.3),(1,1.5,0.7,1.1),(1,3,1,1.5)]:
        half=12
        steps=24000
        dz=2*half/steps
        total=0.0
        for j in range(steps+1):
            z=-half+j*dz
            e1=q*exp(-(sqrt(s)*z-a)**2/2)
            e2=q*exp(-(sqrt(s)*z+a)**2/2)
            w=1 if j in (0,steps) else (4 if j%2 else 2)
            total += w*exp(-z*z/2)/sqrt(2*3.141592653589793)*(e1+e2-e1*e2)
        integ=total*dz/3
        check(abs(integ-coverage(d,s,q,a))<1.3e-12,('independent quadrature',s,q,a,integ))
    for d in range(1,21):
        for s in [0.0001,0.08,0.3,0.75,1.1,2.3,6.0,20.0]:
            for q in [0.05,0.2,0.5,0.9,1.0]:
                a=optimum(d,s,q)
                ref=coverage(d,s,q,a)
                check(ref>=0 and ref<=1+1e-12, ('probability',d,s,q,ref))
                for j in range(101):
                    b=j*max(0.05,1.5*a+0.5)/100
                    check(ref >= coverage(d,s,q,b)-8e-14,('grid global',d,s,q,a,b))
                if a>0.00001:
                    t=a*a
                    der0=coverage_t_derivative(d,s,q,0)
                    der1=coverage_t_derivative(d,s,q,t*0.5)
                    der2=coverage_t_derivative(d,s,q,t*1.5)
                    check(der0>0 and der1>0 and der2<0,('derivative signs',d,s,q))
                else:
                    check(coverage_t_derivative(d,s,q,0) <= 1e-10,('zero derivative',d,s,q))
    # Additional seeded coverage checks stress boundaries and scales.
    for j in range(4000):
        d = rng.randrange(1,22)
        s = exp(rng.uniform(-7,8))
        q = exp(rng.uniform(-9,0))
        a = optimum(d,s,q)
        value = coverage(d,s,q,a)
        b = max(0,a+rng.uniform(-2,2))
        check(value >= coverage(d,s,q,b)-1e-13 and isfinite(value),('random',j,d,s,q,a,b))
    print(f'PASS: {n} deterministic assertions; independent 1-D quadrature and exhaustive parameter grids checked.')
    print(f'3D critical spread: {critical_spread(3):.15f}')
    print(f'4D critical spread: {critical_spread(4):.15f}; golden ratio {phi:.15f}')

if __name__ == '__main__': main()
