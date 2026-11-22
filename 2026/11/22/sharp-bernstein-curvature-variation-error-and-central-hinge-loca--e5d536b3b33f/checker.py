"""Numerical and exact-arithmetic consistency checks for Bernstein hinge smoothing.

Run: python checker.py   (requires Python 3, NumPy, SciPy)
The analytic infinite-degree proof is in RESULT.md; this finite checker is not a proof.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.integrate import simpson, quad
from scipy.special import ndtr
from scipy.stats import binom

checks = 0

def validate(ok, msg):
    global checks
    if not bool(ok):
        raise AssertionError(msg)
    checks += 1

def kernel(n, t, x):
    x = np.asarray(x, dtype=float)
    q = math.floor(n*t)
    ans = x*binom.sf(q-1, n-1, x) - t*binom.sf(q, n, x) - np.maximum(x-t, 0.0)
    return ans

def norm_sq(n, t, count=12001):
    xs = np.linspace(0, 1, count)
    return float(simpson(kernel(n,t,xs)**2, x=xs))

def exact_kernel(n, t, x):
    assert isinstance(t, Fraction) and isinstance(x, Fraction)
    from math import comb
    return sum(Fraction(comb(n,k),1)*x**k*(1-x)**(n-k)*max(Fraction(k,n)-t,0)
               for k in range(n+1)) - max(x-t,0)

for n in range(1,7):
    for i in range(1,11):
        t=Fraction(i,13)
        for j in range(1,11):
            x=Fraction(j,12)
            exact=exact_kernel(n,t,x)
            validate(exact>=0, 'Jensen positivity')
            approx=float(kernel(n,float(t),np.array([float(x)]))[0])
            validate(abs(float(exact)-approx)<2e-12, 'binomial tail formula')

for i in range(1,13):
    t=Fraction(i,14)
    validate(Fraction(1,3)*t*t*(1-t)*(1-t)>=0, 'degree-one shape')
    validate(abs(norm_sq(1,float(t))-float(t*t*(1-t)*(1-t)/3))<5e-10,'degree-one integral')
validate(Fraction(1,3)*Fraction(1,4)**2==Fraction(1,48),'degree-one exact sharp constant')

for n in [2,3,4,5,10,25,60]:
    for t in [.13,.21,.4,.5,.7,.87]:
        a=norm_sq(n,t)
        b=norm_sq(n,1-t)
        validate(abs(a-b)<4e-9, 'reflection symmetry')
        validate(a>=0,'nonnegative squared norm')

phi=lambda z:math.exp(-z*z/2)/math.sqrt(2*math.pi)
G=lambda z:phi(z)-abs(z)*ndtr(-abs(z))
I=2/(3*math.sqrt(math.pi))*(1-1/math.sqrt(2))
Iquad=2*quad(lambda z:G(z)**2,0,12,epsabs=1e-13)[0]
validate(abs(Iquad-I)<1e-12,'closed Gaussian squared profile')
lim=I/8
validate(abs(lim-0.013770608595526972)<1e-15,'asymptotic coefficient')
validate(abs(math.sqrt(lim)-0.11734823643978197)<1e-14,'asymptotic norm coefficient')

for t in [.25,.5,.75]:
    target=(t*(1-t))**1.5*I
    for n in [80,200,500]:
        scaled=n**1.5*norm_sq(n,t)
        validate(abs(scaled/target-1)<.055,'interior asymptotic sample')
validate(norm_sq(2,.33)>norm_sq(2,.5),'finite degree not always centered')
print('PASS', checks, 'finite identity and quadrature assertions')
print('analytic leading squared coefficient:', format(lim,'.17g'))
print('analytic leading norm coefficient:', format(math.sqrt(lim),'.17g'))
