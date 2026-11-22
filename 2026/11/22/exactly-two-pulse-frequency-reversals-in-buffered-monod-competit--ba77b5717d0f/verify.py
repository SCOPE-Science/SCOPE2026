"""Reproducibility checks for the externally buffered two-Monod pulse example.

Run with: python verify.py
Analytic infinite-root uniqueness is proven in RESULT.md, not by finite tests.
"""
from fractions import Fraction
from math import factorial
import mpmath as mp
import sympy as sp

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

h, ell = sp.symbols('h ell')
poly = (1+h)*(10+ell)**2 - (1+ell)*(10+h)**2
check(sp.factor(poly - (h-ell)*(80-h*ell-h-ell)) == 0, 'factoring sign')

for n in range(2, 16):
    a = 2**(n-1)*(16-n)-10*n*(n-1)-16
    check((a<0) if n<=5 else (a>0), f'coefficient {n}')
for n in range(16, 800):
    a = 2**(n-1)*(16-n)-10*n*(n-1)-16
    check(a<0, f'coefficient {n}')

mp.mp.dps = 75

def F(t):
    return (8-t)*mp.exp(2*t)-(16+10*t*t)*mp.exp(t)+8+t

def mu_delta(t):
    high = 10*t/(1-mp.exp(-t))
    low = 10*t/mp.expm1(t)
    return (mp.log((1+high)/(1+low))-2*mp.log((10+high)/(10+low)))/t

root_minus = mp.findroot(F, (3,4))
root_plus = mp.findroot(F, (7,8))
check(mp.mpf('3.2064666589') < root_minus < mp.mpf('3.2064666590'), 'lower root')
check(mp.mpf('7.7304901603') < root_plus < mp.mpf('7.7304901604'), 'upper root')
check(abs(F(root_minus)) < mp.mpf('1e-55'), 'lower residual')
check(abs(F(root_plus)) < mp.mpf('1e-55'), 'upper residual')

for k in range(1,401):
    t = mp.mpf(k)/20
    high = 10*t/(1-mp.exp(-t))
    low = 10*t/mp.expm1(t)
    check(abs((high-low)-10*t) < mp.mpf('1e-60'), f'fixed mean {k}')
    right = 80-high*low-high-low
    check(mp.sign(right)==mp.sign(F(t)), f'analytic sign {k}')
    check(mp.sign(mu_delta(t))==mp.sign(F(t)), f'growth sign {k}')

for t, sgn in [(mp.mpf('1'), -1),(mp.mpf('5'),1),(mp.mpf('20'),-1)]:
    check(mp.sign(F(t))==sgn, 'three sign witnesses')
    check(mp.sign(mu_delta(t))==sgn, 'three growth witnesses')

# Exact resource-hazard factorization and integer-numerator expansion, independently.
z=sp.symbols('z', positive=True)
E=sp.exp(z)
H=10*z*E/(E-1)
L=10*z/(E-1)
check(sp.simplify((80-H*L-H-L)*(E-1)**2-10*((8-z)*E**2-(16+10*z**2)*E+8+z))==0,'exponential reduction')

print('PASS:', checks, 'checks')
print('T_minus =',mp.nstr(root_minus,34))
print('T_plus  =',mp.nstr(root_plus,34))
for t in [1,5,20]:print('delta(',t,') =',mp.nstr(mu_delta(mp.mpf(t)),26))
