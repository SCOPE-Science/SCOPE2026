#!/usr/bin/env python3
"""Exact algebraic checks for a fitted Gamma fixed-point discrepancy.

Requires SymPy (tested with 1.13+). Numerical values are supplementary;
all mathematical identities are checked with exact symbolic arithmetic.
"""
import math
from statistics import NormalDist
import sympy as s

x, a = s.symbols('x a', positive=True)
Q = s.Rational
checks = 0

def verify(condition, description):
    global checks
    assert condition, description
    checks += 1

# Beta(a,1) moments and pairwise kernels.
mean = a / (a + 1)
variance = a / ((a + 1)**2 * (a + 2))
shape = s.cancel(mean**2 / variance)
scale = s.cancel(variance / mean)
minimum = 2*a*a / ((a+1)*(2*a+1))
ratio_half = a / (2*(a+1))
D = s.factor(minimum/scale + (1-shape)*ratio_half - shape/2)
verify(s.simplify(shape - a*(a+2)) == 0, 'shape')
verify(s.simplify(scale - 1/((a+1)*(a+2))) == 0, 'scale')
verify(s.simplify(D - a*(a-1)/(2*(a+1)*(2*a+1))) == 0, 'Beta power family')
verify(s.simplify(s.diff(D,a).subs(a,1) - Q(1,12)) == 0, 'Beta a derivative')
verify(s.simplify(D.subs(a,1)) == 0, 'uniform blind alternative')

# The influence function of the moment-fitted discrepancy at Uniform(0,1).
I = 3*x - 3*x*x + 2*x*s.log(x)
verify(s.simplify(s.integrate(I,(x,0,1))) == 0, 'uniform IF mean')
verify(s.simplify(s.integrate(I**2,(x,0,1)) - Q(7,540)) == 0, 'uniform IF variance')

# Derivative with respect to the second Beta shape at (1,1).
# The beta score is 1+log(1-x), and the numerator derivative kernel is
# g(x)=x/4-x^2/4+x*log(x)/6.  The denominator variance is 1/12.
G = x/4 - x*x/4 + x*s.log(x)/6
verify(s.simplify(s.integrate(G,(x,0,1))) == 0, 'centered gradient')
verify(s.simplify(s.integrate(x*s.log(1-x),(x,0,1)) + Q(3,4)) == 0, 'log integral 1')
verify(s.simplify(s.integrate(x*x*s.log(1-x),(x,0,1)) + Q(11,18)) == 0, 'log integral 2')
# An integration-by-parts/beta-function evaluation.
cross = 1 - s.pi**2/12
Db = s.simplify(12*(s.integrate(x*s.log(1-x),(x,0,1))/4 -
                     s.integrate(x*x*s.log(1-x),(x,0,1))/4 + cross/6))
verify(s.simplify(Db-(19-2*s.pi**2)/12) == 0, 'Beta b derivative')
verify(s.simplify(-s.diff(D,a).subs(a,1)/Db - 1/(2*s.pi**2-19)) == 0,
       'implicit curve slope db/da')

# Gamma(3,1) null: mean 3, variance 3, E min=33/16, B=9/32.
m, v, second, Amin, B = s.Integer(3), s.Integer(3), s.Integer(12), Q(33,16), Q(9,32)
verify(s.simplify(m*Amin+(v-m*m)*B-m*m/2) == 0, 'Gamma null population discrepancy')
coef = Amin - 4*m*B - m
amin = 3-s.exp(-x)*(3+2*x+x*x/2)
bmin = 3*(1-s.exp(-x))/x-s.exp(-x)*(3+x)
IFg = s.expand((coef*(x-m)+B*(x*x-second)+2*m*(amin-Amin)+
                (v-m*m)*(bmin-2*B))/v)
H = s.expand(x*IFg)
p0 = s.expand(H).coeff(s.exp(-x),0)
p1 = s.expand(H).coeff(s.exp(-x),1)
verify(s.simplify(p0-(3*x**3/32-23*x**2/16+99*x/16-6)) == 0,'Gamma IF polynomial 0')
verify(s.simplify(p1-(-x**3-2*x**2+6)) == 0,'Gamma IF polynomial 1')

def gamma_integral_poly(p, rate):
    return sum(c*s.factorial(k)/(s.Integer(rate)**(k+1))
               for (k,), c in s.Poly(s.expand(p),x).terms())
var_gamma = s.expand((gamma_integral_poly(p0*p0,1)+
                       gamma_integral_poly(2*p0*p1,2)+
                       gamma_integral_poly(p1*p1,3))/2)
verify(s.simplify(var_gamma-Q(37,2592)) == 0, 'Gamma(3,1) null IF variance')
mean_gamma = s.expand((gamma_integral_poly(x*p0,1)+gamma_integral_poly(x*p1,2))/2)
verify(s.simplify(mean_gamma) == 0, 'Gamma(3,1) null IF mean')

ratio = s.factor(var_gamma/Q(7,540))
verify(ratio == Q(185,168), 'null-to-alternative variance ratio')
alpha = 0.05
z = NormalDist().inv_cdf(1-alpha/2)
limiting_rejection = 2*NormalDist().cdf(-z*math.sqrt(float(ratio)))
verify(abs(limiting_rejection-0.03971127879713649) < 5e-13,
       'two-sided 5 percent limiting rejection')
print(f'PASS: {checks} independent exact/analytic checks')
print('Beta(a,1) departure:',D)
print('Beta zero-curve tangent: da/db =',s.simplify(-Db/s.diff(D,a).subs(a,1)))
print('Uniform IF variance:',Q(7,540))
print('Gamma(3,1) fitted-null IF variance:',var_gamma)
print('Two-sided 5% limiting uniform-alternative rejection:',f'{limiting_rejection:.12f}')
