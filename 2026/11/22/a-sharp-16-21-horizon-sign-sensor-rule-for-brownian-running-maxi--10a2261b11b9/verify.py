"""Reproduce exact identities and independent quadrature checks for one-bit Brownian maximum estimation."""
import math
from fractions import Fraction

from scipy.integrate import quad
from scipy.special import erfc
import sympy as sp

PI = math.pi

def phi(z):
    return math.exp(-z*z/2)/math.sqrt(2*PI)

def sf(z):
    return 0.5*erfc(z/math.sqrt(2))

def c_formula(s):
    return (2*math.sqrt(s)+math.sqrt(4-3*s)-2)/math.sqrt(2*PI)

def excess(r,d):
    if r == 0:
        return 0.0
    return 2*r*phi(d/r)-2*d*sf(d/r)

def c_quadrature(s):
    r = math.sqrt((1-s)/s)
    k = lambda d: 4*phi(2*d)-2*phi(d)
    j, _ = quad(lambda d: k(d)*excess(r,d),0,math.inf,epsabs=2e-12,epsrel=2e-12,limit=200)
    return math.sqrt(s)*(1/math.sqrt(2*PI)+j)

def risk(s):
    return 1-2/PI-c_formula(s)**2

checks = 0
def close(actual, expected, tol=2e-10):
    global checks
    assert abs(actual-expected)<tol, (actual, expected)
    checks+=1

# Reflection-principle joint density for normalized maximum A and drawdown D.
# Under f(a,d)=2(a+d)phi(a+d), both coordinates are nonnegative.
close(quad(lambda y: y*y*phi(y),0,math.inf)[0],0.5,1e-12)
close(quad(lambda y: 2*y*y*phi(y),0,math.inf)[0],1,1e-12)
close(quad(lambda y: y*y*y*phi(y),0,math.inf)[0],math.sqrt(2/PI),1e-12)

for s in [1/64, 1/10, 1/4, 1/2, 3/4, 16/21, 4/5, 9/10, 1]:
    close(c_quadrature(s),c_formula(s))

# Algebraic stationarity, uniqueness and exact optimum using SymPy.
s = sp.symbols('s',positive=True)
star = sp.Rational(16,21)
q = 2*sp.sqrt(s)+sp.sqrt(4-3*s)-2
fprime = 1/sp.sqrt(s)-sp.Rational(3,2)/sp.sqrt(4-3*s)
assert sp.simplify(fprime.subs(s,star)) == 0
checks+=1
assert sp.simplify((4-3*s)-sp.Rational(9,4)*s)==4-sp.Rational(21,4)*s
checks+=1
cs = sp.simplify(q.subs(s,star)/sp.sqrt(2*sp.pi))
assert sp.simplify(cs-sp.sqrt(2)*(sp.sqrt(21)-3)/(3*sp.sqrt(sp.pi))) == 0
checks+=1
riskstar = sp.simplify(1-2/sp.pi-cs**2)
assert sp.simplify(riskstar-(3*sp.pi-26+4*sp.sqrt(21))/(3*sp.pi)) == 0
checks+=1
assert sp.simplify((1-2/sp.pi) - (1-sp.Rational(5,2)/sp.pi) - (sp.Rational(1,2)/sp.pi)) == 0
checks+=1

# Directional derivative sign: strictly up then down.
for x in [sp.Rational(1,100), sp.Rational(1,10), sp.Rational(1,2),sp.Rational(3,4)]:
    assert float(fprime.subs(s,x)) > 0
    checks+=1
for x in [sp.Rational(4,5),sp.Rational(9,10),sp.Rational(99,100)]:
    assert float(fprime.subs(s,x)) < 0
    checks+=1

# Known marginal law M=|N(0,1)|, Bayes risk and improvement.
close(1-2/PI-risk(float(star)),c_formula(float(star))**2)
close(c_formula(1),1/math.sqrt(2*PI))
assert risk(float(star)) < risk(1) < (1-2/PI)
checks+=1
print(f"PASSED {checks} quadrature, symbolic and boundary checks")
print(f"s_star={float(star):.15g}, covariance={c_formula(float(star)):.15g}, Bayes_risk={risk(float(star)):.15g}")
print(f"terminal_risk={risk(1):.15g}, relative_improvement={(risk(1)-risk(float(star)))/risk(1):.15g}")
