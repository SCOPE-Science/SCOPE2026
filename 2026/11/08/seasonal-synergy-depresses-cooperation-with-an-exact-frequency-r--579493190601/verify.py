"""Exact symbolic reproducibility for the forced public-goods mean-response theorem.

Requires Python 3 and SymPy. Run: python verify.py
The nonzero-frequency periodic-orbit existence and smooth parameter dependence
follow from the hyperbolic Poincare-map implicit-function theorem, not
from finite computation.
"""
import sympy as s

x, r, w, e, om = s.symbols('x r w epsilon omega', real=True)
z = s.Matrix([x, r])
f_d = (3*x + 3*(w-1)*x**2 + (w-1)**2*x**3)/4
f_c = r*(1 + 3*w*x + 3*w*(w-1)*x**2 + w*(w-1)**2*x**3)/4 - 1
F = s.Matrix([x*(1-x)*(f_c-f_d),
              e*(r-s.Rational(3,2))*(s.Rational(7,2)-r)*
              (-x*f_c+2*(1-x)*f_d)])
sub = {x: s.Rational(2,3), r:s.Integer(2), w:s.Integer(1)}
J = F.jacobian(z).subs(sub)
g = F.diff(w).subs(sub)
assert F.subs(sub) == s.zeros(2,1)
assert J == s.Matrix([[s.Rational(1,6),s.Rational(1,6)],
                      [-3*e/2,-3*e/8]])
assert g == s.Matrix([s.Rational(8,27), -2*e/3])
assert s.factor(J.det()) == 3*e/16
assert s.simplify(J.trace()-(4-9*e)/24) == 0

# First Fourier amplitude in the convention u(t)=Re(h exp(i omega t)).
Q_complex = 9*e-48*om**2+s.I*om*(18*e-8)
h = s.Matrix([128*s.I*om/(9*Q_complex),
              -16*e*(1+2*s.I*om)/Q_complex])
assert all(s.simplify(v) == 0 for v in (s.I*om*s.eye(2)-J)*h-g)

# For the second-order mean response, average the quadratic Taylor equation.
D = s.expand_complex(Q_complex*s.conjugate(Q_complex))
H = [s.hessian(F[k],z).subs(sub) for k in range(2)]
C = F.diff(w).jacobian(z).subs(sub)
d = F.diff(w,2).subs(sub)
force_mean = s.zeros(2,1)
for k in range(2):
    value = d[k]/4
    for j in range(2):
        value += C[k,j]*s.re(s.expand_complex(h[j]))/2
        for l in range(2):
            value += H[k][j,l]*s.re(s.expand_complex(h[j]*s.conjugate(h[l])))/4
    force_mean[k] = s.factor(s.simplify(s.expand_complex(value)))
mean_second = -J.inv()*force_mean
K = s.factor(mean_second[0]); K_expected = (
    -256*om**2*(3*e+4)/(9*((9*e-48*om**2)**2+(18*e-8)**2*om**2)))
assert s.simplify(K-K_expected) == 0

# Unique strictly negative correction at all positive frequencies, epsilon>4/9;
# its magnitude has one maximum at omega=sqrt(3 epsilon)/4.
t = s.symbols('t', positive=True)
response = -K_expected.subs(om**2,t)
deriv = s.factor(s.diff(response,t))
assert s.simplify(deriv.subs(t,3*e/16)) == 0
# derivative sign comes from positive factor times (constant - 2304 t^2)
numer,denom = s.fraction(deriv)
assert s.simplify(numer+256*(3*e+4)*(256*t**2-9*e**2)) == 0
assert s.simplify(denom - ((9*e-48*t)**2+(18*e-8)**2*t)**2) == 0
peak = s.simplify(K_expected.subs(om**2,3*e/16))
assert s.simplify(peak + 64*(3*e+4)/(9*(9*e-4)**2)) == 0
assert peak.subs(e,1) == -s.Rational(448,225)
assert s.simplify(K_expected.subs(e,1).subs(om**2,s.Rational(3,16))+s.Rational(448,225)) == 0
print('VERIFY_OK')
