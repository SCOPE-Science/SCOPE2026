"""Standalone checks for Poisson-mixture BV-to-L2 sharp error identities.

Run with Python 3 and the sympy and mpmath packages. Numerical tests
illustrate analytic identities; the accompanying mathematical proof establishes
the quantified sharp claims.
"""
import math
from fractions import Fraction

import mpmath as mp
import sympy as sp

checks = 0

def verify(value, label):
    global checks
    if not value:
        raise AssertionError(label)
    checks += 1

# Formal differential identity proving convexity in logarithmic radius.
r, c, s = sp.symbols('r c s', real=True)
D = 1 - 2*r*c + r*r
Bprime = -r*s/D
Bdouble = sp.factor(-r*sp.diff(Bprime, r))
verify(sp.simplify(Bdouble-r*(1-r*r)*s/D**2)==0, 'positive log-radius curvature identity')

# Exact local second derivative at a half circle: the independent formula
# uses the boundary derivative of the angular phase function.
Btheta = -sp.Rational(1,2)+2*r/(1+r)-r*r/(1+r*r)
verify(sp.factor(Btheta + (1-r)**3/(2*(1+r)*(1+r*r)))==0,
       'exact half-circle quadratic curvature')

# Exact spectral formula and differentiated dilogarithmic expression.
z = sp.symbols('z', positive=True)
H = (sp.polylog(2,z) - sp.polylog(2,-z))/2
Hprime = (sp.atanh(z))/z
verify(sp.simplify(sp.expand_func(sp.diff(H,z))-(sp.log(1+z)-sp.log(1-z))/(2*z))==0, 'odd dilogarithm derivative')

mp.mp.dps=45
pi=mp.pi

def oddH(u):
    if u==0: return mp.mpf('0')
    if u==1: return pi*pi/8
    return (mp.polylog(2,u)-mp.polylog(2,-u))/2

def exact_poisson_sq(r):
    return (oddH(1)-2*oddH(r)+oddH(r*r))/(2*pi*pi)

# Independent Fourier partial sums; rigorous tail bound <=1/(2*pi^2*N).
for rho in [mp.mpf('0'),mp.mpf('0.1'),mp.mpf('0.4'),mp.mpf('0.8'),mp.mpf('0.99')]:
    N=5000
    approx=sum((1-rho**n)**2/n**2 for n in range(1,N,2))/(2*pi*pi)
    verify(abs(approx-exact_poisson_sq(rho)) < 1/(2*pi*pi*(N-1)),
           f'Fourier check at radius {rho}')
    if rho>0:
        formula=mp.log((1+rho*rho)/(1+rho)**2)/(2*pi*pi*rho)
        numeric=mp.diff(exact_poisson_sq,rho)
        verify(abs(formula-numeric)<mp.mpf('1e-35'), 'exact radius derivative')

# Strict positive angular derivative for mixed Poisson radii.
for weights,radii in [([1],[mp.mpf('0')]),
                       ([mp.mpf('.25'),mp.mpf('.75')],[mp.mpf('.2'),mp.mpf('.9')]),
                       ([mp.mpf('.5'),mp.mpf('.5')],[mp.mpf('.5'),mp.mpf('1')])]:
    for theta in [mp.mpf('.13'),mp.mpf('.7'),mp.mpf('1.9'),mp.mpf('3.0')]:
        def A(q):
            if q==1:return (pi-theta)/2
            if q==0:return mp.mpf('0')
            return mp.atan2(q*mp.sin(theta),1-q*mp.cos(theta))
        val = mp.fsum(weights[i]*weights[j]*(A(1)-A(radii[i])-A(radii[j])+A(radii[i]*radii[j]))
                      for i in range(len(weights)) for j in range(len(weights)))
        verify(val>mp.mpf('1e-25'), 'strict angular monotonicity in a mixture')

# Regime constants for fractional Poisson smoothing.
def spectral_sq(alpha,t,N=120000):
    return sum((1-math.exp(-t*n**alpha))**2/(n*n) for n in range(1,N,2))/(2*math.pi**2)

def subcritical_coefficient(alpha):
    return (1-2**(-(2-2*alpha)))*mp.zeta(2-2*alpha)/(2*pi*pi)

def supercritical_coefficient(alpha):
    if alpha==1: return mp.log(2)/(2*pi*pi)
    return mp.gamma(1-1/alpha)*(1-2**(1/alpha-1))/(2*pi*pi)

# Values need only be roughly in asymptotic regimes: not a limit proof.
for alpha,t,limit in [(0.25,0.001,subcritical_coefficient(.25)*.001**2),
                      (0.5,0.0007,.0007**2*math.log(1/.0007)/(2*math.pi**2)),
                      (0.75,0.002,supercritical_coefficient(.75)*.002**(1/.75)),
                      (1,0.0005,supercritical_coefficient(1)*.0005)]:
    val=spectral_sq(alpha,t)
    ratio=val/float(limit)
    # The alpha=1/2 convergence is only logarithmic.
    verify(.77<ratio<1.25,f'fractional asymptotic cross-check ({alpha}, {ratio})')

verify(abs(exact_poisson_sq(mp.mpf('0'))-mp.mpf(1)/16)<mp.mpf('1e-40'),
       'mean projection boundary normalization')
for r in [mp.mpf('0.95'),mp.mpf('0.995'),mp.mpf('0.9999')]:
    ratio=exact_poisson_sq(r)/(1-r)
    target=mp.log(2)/(2*pi*pi)
    verify(abs(ratio/target-1)<mp.mpf('0.1'), 'critical Poisson slope')

print(f'PASS: {checks} exact-symbolic and numerical consistency assertions')
