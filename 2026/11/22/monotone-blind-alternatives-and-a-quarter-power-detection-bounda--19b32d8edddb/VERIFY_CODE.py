"""Exact-arithmetic checks for a scalar uniformity U-statistic.

Requires Python 3 and SymPy. All identities are checked over the rationals.
This script verifies finite algebra; the analytical CLT arguments are given
separately in the proof and are not asserted to follow from code.
"""
import sympy as s

x, y, c, d, r = s.symbols('x y c d r', real=True)
count = 0

def check(expr):
    global count
    assert s.cancel(expr) == 0, s.factor(expr)
    count += 1

f = 1 + c * (2*x-1) + d * (6*x*x-6*x+1)
F = s.integrate(f.subs(x,y), (y,0,x))
check(F - (x + c*(x*x-x) + d*(2*x**3-3*x*x+x)))
check(s.integrate(f,(x,0,1))-1)
mu = s.integrate(x*f,(x,0,1))
mu2 = s.integrate(x*x*f,(x,0,1))
check(mu-(s.Rational(1,2)+c/6))
check(mu2-(s.Rational(1,3)+c/6+d/30))
Emax = 1-s.integrate(F*F,(x,0,1))
Delta = s.factor(Emax-2*mu+mu2)
check(Delta-(d/15-c*c/30-d*d/210))

# Independently integrate the actual symmetric U kernel over x<y.
# For x<y, h(x,y)=-x+(x^2+y^2)/2.
k_lt = -x+(x*x+y*y)/2
integral_xy = 2*s.integrate(s.integrate(k_lt*f.subs(x,y),(y,x,1))*f,(x,0,1))
check(Delta-integral_xy)

cr = 14*r/(7+r*r)
dr = 14*r*r/(7+r*r)
check(Delta.subs({c:cr,d:dr}))
check(s.factor(f.subs({c:s.Rational(56,113),d:s.Rational(14,113)})-
              (84*x*x+28*x+71)/113))
check(Delta.subs({c:s.Rational(56,113),d:s.Rational(14,113)}))
check(Delta.subs(d,0)+c*c/30)

# First Hoeffding projection (irrelevant constants suppressed).
L = s.expand(2*x*F+2*s.integrate(y*f.subs(x,y),(y,x,1))-2*x+x*x)
mean_L = s.integrate(L*f,(x,0,1))
V = s.factor(s.integrate(L*L*f,(x,0,1))-mean_L**2)
check(V.subs({c:0,d:0})-s.Rational(1,45))
check(V.subs(d,0)+(28*c**4+15*c*c-140)/6300)
Vcurve=(56595+80311*r**4-6282*r**6)/(7425*(7+r*r)**3)
check(V.subs({c:cr,d:dr})-Vcurve)
check(s.diff(Vcurve,r)+14*r*(30319*r**4-160622*r*r+24255)/
      (7425*(r*r+7)**4))
check(V.subs({c:s.Rational(56,113),d:s.Rational(14,113)})-
      s.Rational(233091814,10713510225))

# Verify the algebraic equivalence to the published order-statistic formula
# on deterministic rational samples, not by stochastic simulation.
for xs in [[s.Rational(1,7),s.Rational(3,5)],
           [s.Rational(2,17),s.Rational(3,11),s.Rational(7,10)],
           [s.Rational(1,8),s.Rational(3,8),s.Rational(2,3),s.Rational(7,8)]]:
    n = len(xs)
    kernel = lambda a,b: max(a,b)-a-b+(a*a+b*b)/2
    U = sum(kernel(xs[i],xs[j]) for i in range(n) for j in range(i+1,n))*s.Rational(2,n*(n-1))
    ordered = sum((2*(i-n)+(n-1)*z)*z for i,z in enumerate(sorted(xs),start=1))*s.Rational(1,n*(n-1))
    check(U-ordered)

print(f'PASS: {count} independent exact-arithmetic assertions')
