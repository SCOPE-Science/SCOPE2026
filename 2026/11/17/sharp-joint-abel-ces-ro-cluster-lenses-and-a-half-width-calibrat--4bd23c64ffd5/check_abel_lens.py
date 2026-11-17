"""Exact finite-envelope and numerical realization checks for Abel–Cesàro lenses.
Run: python check_abel_lens.py. Standard library only.
"""
from fractions import Fraction
from itertools import product
from math import exp, log, floor


def geometric_prefix(bits, p):
    q = 1-p
    return sum((p*q**j*bit for j, bit in enumerate(bits)), Fraction(0))


def exact_envelopes(n, k, p):
    q = 1-p
    return (q**(n-k)-q**n, 1-q**k+q**n)


cases = 0
for n in range(2, 12):
    for p in (Fraction(1, 4), Fraction(1, 3), Fraction(1, 2), Fraction(3, 4)):
        for k in range(n+1):
            values = [geometric_prefix(bits,p) for bits in product((0,1),repeat=n) if sum(bits)==k]
            lo, hi = exact_envelopes(n,k,p)
            assert min(values)==lo
            assert max(values) + (1-p)**n == hi
            cases += len(values)
print('EXACT_FINITE_ENVELOPES_ALL_BINARY_PREFIXES_PASS', cases)

for n in range(2, 40, 2):
    q = 2**(-2/n)
    w=1+2*q**n-2*q**(n//2)
    assert abs(w-0.5)<1e-12
print('FINITE_EVEN_LENGTH_HALF_WIDTH_CALIBRATION_PASS')

for lam in (0.2, 0.7, 1.0, 1.4, 2*log(2), 4.0):
    z=exp(-lam/2)
    assert abs((1+2*exp(-lam)-2*z) - (0.5+2*(z-0.5)**2)) < 1e-12
print('CONTINUUM_HALF_WIDTH_IDENTITY_PASS')


def construct(lam,u,theta,n=20000,T=12):
    def f(t):
        minimum = 1.0 if 1-u < t <= 1 else 0.0
        maximum = 1.0 if t <= u or 1 < t <= T else 0.0
        return (1-theta)*minimum+theta*maximum
    running=0.0
    last=0
    c=0
    b=0.0
    p=lam/n
    q=1-p
    weight=p
    for j in range(1, T*n+1):
        running+=f((j-0.5)/n)
        new=int(floor(running+1e-10))
        digit=new-last
        assert digit in (0,1)
        last=new
        if j<=n: c+=digit
        b+=weight*digit
        weight*=q
    return c/n,b

for lam,u,theta in ((0.7,0.25,0.3),(1.4,0.5,0.7),(2*log(2),0.5,0.4),(4.0,0.8,0.95)):
    lower=exp(-lam*(1-u))-exp(-lam)
    upper=1-exp(-lam*u)+exp(-lam)
    actual=construct(lam,u,theta)
    assert abs(actual[0]-u)<3e-4
    assert abs(actual[1]-(lower+theta*(upper-lower)))<7e-4, (actual,lower,upper)
print('MULTILEVEL_REALIZATION_CONSTRUCTION_PASS')
print('ALL_ABEL_CESARO_LENS_CHECKS_PASS')
