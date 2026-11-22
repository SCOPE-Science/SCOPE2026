#!/usr/bin/env python3
"""Reproduce numerical identities for a Brownian quadratic-energy binary observation theorem.

Analytic optimality of all encoders and uniqueness is proved in RESULT.md;
this verifier does not turn finite evaluations into a universal proof.
"""
from fractions import Fraction as F
import mpmath as mp

mp.mp.dps = 70

def phi(a):
    return mp.exp(-a*a/2) / mp.sqrt(2*mp.pi)
def tail(a):
    return mp.erfc(a/mp.sqrt(2))/2

def below(a):
    return mp.mpf('0.5')-tail(a)

def f(a):
    return 2*a*a-2-a*phi(a)*(1/tail(a)-1/below(a))

def information(a):
    return a*a*phi(a)**2/(tail(a)*below(a))

# Exact Brownian covariance integral (no quadrature approximations).
# ∫_0^1 min(t,x)^2 dt / x^2 = x/3 + 1-x = 1-2x/3
for num,den in [(1,11),(1,3),(1,2),(3,4),(9,10),(1,1)]:
    x=F(num,den)
    covfactor=(x**3/F(3,1)+x*x*(1-x))/(x*x)
    assert covfactor == 1 - F(2,3)*x
assert F(3,4)*(1-F(2,3)*F(3,4)) == F(3,8)
# Var(∫W_t^2dt)=4∫_{0<=s<=t<=1}s² ds dt=1/3.
assert 4*(F(1,3)-F(1,4))/1 == F(1,3)

root=mp.findroot(f,(mp.mpf('1.4'),mp.mpf('1.55')))
assert abs(f(root)) < mp.mpf('1e-60')
assert mp.mpf('1.48207') < root < mp.mpf('1.48208')
I=information(root)
risk=mp.mpf(1)/3-mp.mpf(9)/64*I
fraction=mp.mpf(27)/64*I
prob=2*tail(root)
assert abs(risk+fraction/3-mp.mpf(1)/3) < mp.mpf('1e-60')
assert mp.mpf('0.55')<fraction<mp.mpf('0.551')
assert mp.mpf('0.138')<prob<mp.mpf('0.139')
# Check two-cell levels reproduce the original 1/2 prior mean.
high=mp.mpf('0.5')+mp.mpf(3)/8*root*phi(root)/tail(root)
low=mp.mpf('0.5')-mp.mpf(3)/8*root*phi(root)/below(root)
assert abs(prob*high+(1-prob)*low-mp.mpf('0.5'))<mp.mpf('1e-60')
assert abs(prob*(high-mp.mpf('.5'))**2+(1-prob)*(low-mp.mpf('.5'))**2-mp.mpf(9)/64*I)<mp.mpf('1e-60')
# Checks of the unique crossing, not a replacement for the monotonicity proof.
for k in range(1,50):
    a=mp.mpf(k)/20
    left=(1-a*phi(a)/below(a))/a**2
    right=(1+a*phi(a)/tail(a))/a**2
    assert left>0 and right>1
    if k>1:
        assert left+right<prev
    prev=left+right

# Independent numerical conditional moment check by Gaussian integration.
for a in [mp.mpf('0.4'), root, mp.mpf('2.2')]:
    m=2*mp.quad(lambda z:(z*z-1)*phi(z),[a,mp.inf]);
    assert abs(m-2*a*phi(a))<mp.mpf('1e-60')
    p=2*mp.quad(lambda z:phi(z),[a,mp.inf])
    assert abs(p-2*tail(a))<mp.mpf('1e-60')

print('VERIFY_OK: Brownian covariance and total-variance rational identities; Gaussian-tail integration; posterior centroids; 1-bit optimum root.')
for k,v in [('a_star',root),('tail_bit_probability',prob),('explained_normalized_chisquare_variance',I),('optimal_risk',risk),('optimal_recovered_variance_fraction',fraction),('posterior_energy_high',high),('posterior_energy_low',low)]:
    print(k+'='+mp.nstr(v,40))
