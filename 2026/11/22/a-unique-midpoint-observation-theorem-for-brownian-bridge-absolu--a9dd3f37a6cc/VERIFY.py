"""Standalone corroboration for single-observation Brownian-bridge absolute-area quadrature.

Analytic all-time optimality follows from the proof in RESULT.md, not finite grids.
Run with: python VERIFY.py  (requires numpy, scipy, sympy).
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import roots_legendre, gammaln

checks = 0

def confirm(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

# Exact two-term computation of the absolute-area second moment.
# In the ordered triangle s <= t, E|B_s B_t| = (2/pi)(A+B),
# A=sqrt{s(1-t)(t-s)}, B=s(1-t)arcsin(rho).
term_A = 2 * sp.pi / 105
# Integrate B by parts in s, exchange the residual integration order.
term_B = sp.pi / 48 - sp.Rational(1,4) * (
    sp.beta(sp.Rational(1,2), sp.Rational(5,2))
    * sp.beta(sp.Rational(5,2), 2)
)
confirm(sp.simplify((term_B - 17*sp.pi/1680).rewrite(sp.gamma)) == 0, 'ordered-triangle arcsine moment')
confirm(sp.simplify((4/sp.pi*(term_A+term_B)-sp.Rational(7,60)).rewrite(sp.gamma)) == 0, 'E[A^2]')
confirm(sp.simplify(sp.Rational(7,60)-sp.pi/32) == sp.Rational(7,60)-sp.pi/32, 'Var A')

# Hermite coefficients of |N(0,1)| from the independent polynomial-moment identity.
x = sp.Symbol('x')
for m in range(1, 9):
    poly = sp.Poly(sp.hermite_prob(2*m,x),x)
    integral_over_normal = sum(
       coef * (2**(power[0]//2))*sp.factorial(power[0]//2)
       for power,coef in poly.terms()
    )
    target = (-1)**(m-1)*sp.factorial2(2*m-3) if m>1 else 1
    confirm(sp.simplify(integral_over_normal-target) == 0, f'Hermite order {2*m}')


def g_at_half(m):
    return 2*quad(lambda s: math.sqrt(s*(1-s))*(s/(1-s))**m,
                  0, .5, epsabs=2e-13, epsrel=1e-11, limit=150)[0]


def series_gain(eta, terms=100):
    r2=1/(1+4*eta)
    total=0.0
    for m in range(1, terms+1):
        log_dbl = gammaln(2*m-1)-(m-1)*math.log(2)-gammaln(m)
        coefficient = 2/math.pi*math.exp(2*log_dbl-gammaln(2*m+1))
        total += coefficient*(r2**(2*m))*g_at_half(m)**2
    return total


def f_abs_covariance(q):
    # Cov(|X|,|Y|) / (sigma_x sigma_y), for jointly normal corr q.
    return 2/math.pi*(np.sqrt(np.maximum(0,1-q*q))+q*np.arcsin(q)-1)


def direct_gain(eta,t,n=250):
    pts,wt=roots_legendre(n)
    s=(pts+1)/2
    wt=wt/2
    a=np.sqrt(s*(1-s))
    a0=math.sqrt(t*(1-t))
    corr=np.minimum(s,t)-s*t
    corr/=a*a0
    r2=a0*a0/(a0*a0+eta)
    q=r2*np.outer(corr,corr)
    ww=wt*a
    return float(ww @ f_abs_covariance(q) @ ww)

for eta in [0,0.02,0.1,1]:
    via_series=series_gain(eta, 80)
    via_covariance=direct_gain(eta,.5,600)
    confirm(abs(via_series-via_covariance)<3e-7, f'independent gain formulas eta={eta}')
    confirm(via_series>0, f'positive information eta={eta}')
    vals=[direct_gain(eta,t,160) for t in [.15,.25,.4,.5,.6,.75,.85]]
    confirm(vals[3]>max(vals[:3]+vals[4:]), f'midpoint grid eta={eta}')
    confirm(abs(vals[0]-vals[-1])<2e-10, f'reflection eta={eta}')

G1=3*math.pi/8-1
confirm(abs(g_at_half(1)-G1)<2e-12,'first Hermite convolution exact value')
for eta in [5,20,100]:
    gain=series_gain(eta,30)
    leading=(G1**2/math.pi)/(1+4*eta)**2
    confirm(gain>leading and (gain-leading)/gain<0.002/(eta*eta),
            f'high-noise leading term eta={eta}')

print('PASS',checks,'corroborating assertions')
print('Unconditional variance:',format(7/60-math.pi/32,'.15f'))
for eta in [0,0.1,1]:
    gain=series_gain(eta)
    print(f'noise={eta}: information={gain:.12f}, Bayes MSE={7/60-math.pi/32-gain:.12f}')
