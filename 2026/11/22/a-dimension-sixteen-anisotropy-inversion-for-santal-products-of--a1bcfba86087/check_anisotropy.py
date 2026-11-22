"""Reproducible exact and high-precision checks for shifted-cube polar volume expansion.
Run: python3 check_anisotropy.py (requires SymPy, mpmath; no network).
The universal theorem follows from the analytic proof, not finite tests.
"""
from math import factorial
from fractions import Fraction
import sympy as sp
import mpmath as mp

n = sp.symbols('n', integer=True, positive=True)
a = -sp.Rational(3)/(n+2)
c = n+1
q2 = sp.factor(c*a + c*(c+1)*a*a/6 + 1)
q22 = sp.factor(c*(c+1)*a*a/2+c*(c+1)*(c+2)*a**3/6+
                c*(c+1)*(c+2)*(c+3)*a**4/72-
                (c*a+c*(c+1)*a*a/6)**2/2)
q4 = sp.factor(sp.Rational(1,2) - c*(c+1)*(c+2)*(c+3)*a**4/180)
assert sp.simplify(q2+(n-1)/(2*(n+2)))==0
assert sp.simplify(q22-9*(n+1)/(4*(n+2)**3))==0
assert sp.simplify(q4-(n**3-12*n**2-51*n-28)/(20*(n+2)**3))==0
assert all(q4.subs(n,k)<0 for k in range(2,16))
assert all(q4.subs(n,k)>0 for k in range(16,120))
assert sp.factor((n**3-12*n**2-51*n-28).subs(n,16))>0
assert sp.factor((n**3-12*n**2-51*n-28).subs(n,15))<0

# Compute E[(U_1+...+U_m)^k] exactly, using
# prod_i E(exp(z U_i)) = (sinh(z)/z)^m.
def uniform_moments(m, degree):
    half = degree//2
    poly = [Fraction(1)] + [Fraction(0)]*half
    factor = [Fraction(1, factorial(2*k+1)) for k in range(half+1)]
    for _ in range(m):
        poly = [sum(poly[j]*factor[k-j] for j in range(k+1)) for k in range(half+1)]
    return [Fraction(factorial(2*k))*poly[k] for k in range(half+1)]

mp.mp.dps = 65
mom = {m: [mp.mpf(x.numerator)/x.denominator for x in uniform_moments(m,36)] for m in (1,2,3,15,16)}

# F=E[(1-s(sum U_i + m*t))^-(n+1)] for m active coordinates.
def polar_integral(nval, active, shift, s):
    d = 1-active*s*shift
    assert d>0
    return sum(mp.binomial(nval+2*j,2*j)*mom[active][j] *
               (s/d)**(2*j)*d**(-nval-1)
               for j in range(19))

def log_product(nval,active,rho):
    shift=rho/mp.sqrt(active)
    guess=-3*shift/(nval+2)
    obj=lambda s: polar_integral(nval,active,shift,s)
    optimum=mp.findroot(lambda s: mp.diff(obj,s),(guess*mp.mpf('.8'),guess*mp.mpf('1.2')))
    # product normalized by 4^n/n! = Fmin / prod_i(1-t_i²)
    return mp.log(obj(optimum))-active*mp.log(1-shift**2)

count=0
for ndim in (2,3,15,16):
    for rho in ('0.015','0.027'):
        r=mp.mpf(rho)
        sparse=log_product(ndim,1,r)
        balanced=log_product(ndim,ndim,r)
        sign=1 if ndim>=16 else -1
        assert sign*(sparse-balanced)>0, (ndim,rho,sparse-balanced)
        beta=mp.mpf(int(sp.numer(q4.subs(n,ndim))))/int(sp.denom(q4.subs(n,ndim)))
        # sparse S4=r^4; balanced S4=r^4/n. Differential leading coefficient.
        prediction=beta*(1-mp.mpf(1)/ndim)*r**4
        assert abs((sparse-balanced)/prediction-1)<mp.mpf('0.07'), (ndim,rho,(sparse-balanced)/prediction)
        count+=1
# Independently compare moment expansion to a direct 1D integral (one active coordinate).
for ndim in (2,5,16):
    shift=mp.mpf('0.07')
    s=-mp.mpf('0.02')
    direct=mp.quad(lambda u:(1-s*(u+shift))**(-ndim-1),[-1,1])/2
    series=polar_integral(ndim,1,shift,s)
    assert abs(direct-series)<mp.mpf('1e-35'), (ndim,direct,series)
    count+=1
print('ANISOTROPY_CHECKS_OK exact_coefficients=3 sign_integer_ranges=118 numeric_pairs=8 direct_integrals=3 total_checks=',count)
