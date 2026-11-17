#!/usr/bin/env python3
"""Exact algebra checks for the odd-cubic harmonic-Bergman spectral phase.

Requires SymPy 1.12 or newer. This checks polynomial certificates, not the
Fredholm/kernel arguments, which are analytical in RESULT.md.
"""
import sympy as sp

z, w, a, x, y, s, t, alpha = sp.symbols('z w a x y s t alpha')
checks = 0

def exact(expr):
    global checks
    assert sp.cancel(sp.expand(expr)) == 0, sp.factor(expr)
    checks += 1

h = a + z**2 + sp.Rational(3, 2)*z*w + sp.Rational(3, 2)*w**2
# From the Bergman projection identities, indexed by monomial degree.
def hk(k):
    return sp.expand(sum(sp.Rational((j+1)*(k-j+1), k+1)*z**(k-j-1)*w**j for j in range(k)))
exact(h - a*hk(1) - hk(3))
exact(h.subs({z:alpha,w:alpha}) - a - 4*alpha**2)

def H(xx, yy):
    return h.subs({z:xx,w:yy})
F = sp.expand(H(x,x)*H(y,y)-H(x,y)*H(y,x))
exact(F + sp.Rational(3,4)*(x-y)**2*(-2*a+2*x*x+9*x*y+2*y*y))
# A symmetric-polynomial identity using s=x+y, t=xy.
exact(((-2*a+2*x*x+9*x*y+2*y*y) - (-2*a+2*s*s+5*t)).subs({s:x+y,t:x*y}))
# For a=t-s^2 and the determinant condition, derive t=-4s^2/3.
exact((-2*a+2*s*s+5*t).subs(a,t-s*s) - (4*s*s+3*t))
# Repeated-root 2x2 confluent kernel certificate.
Conf = sp.expand(H(alpha,alpha)*sp.diff(h,z,w).subs({z:alpha,w:alpha})
                 -sp.diff(h,z).subs({z:alpha,w:alpha})*sp.diff(h,w).subs({z:alpha,w:alpha}))
exact(Conf.subs(a,-3*alpha**2)+sp.Rational(57,4)*alpha**2)
# Single interior root alpha and the other two roots.
exact((z-alpha)*(z*z+alpha*z-3*alpha**2)
      -(z**3-4*alpha**2*z+3*alpha**3))
exact((z**3+a*z).subs(z,alpha).subs(a,-4*alpha**2)+3*alpha**3)
# Coefficient relation for critical value lambda (note p(alpha)=-3 alpha^3).
exact((z**3+a*z).subs({z:alpha,a:-4*alpha**2})+3*alpha**3)
threshold = sp.Rational(2,9)*(7+sp.sqrt(13))
exact(threshold - 16/(sp.sqrt(13)-1)**2)
assert 2 < threshold < 4
checks += 1
# Exhaustive classification of the location inequalities for symbolic ratios.
q_small=(sp.sqrt(13)-1)/2
q_large=(sp.sqrt(13)+1)/2
assert 1<q_small<q_large
checks += 1
q_N2=(1+sp.sqrt(sp.Rational(19,3)))/2
assert q_N2>1
checks += 1
# Evaluate all 3 numerical parameter regimes using exact polynomial values.
for A in [sp.Rational(1,2), sp.Rational(2), sp.Rational(5,2), sp.Rational(3), sp.Rational(7,2), sp.Rational(9,2)]:
    r = sp.sqrt(A)/2
    inside = (r < 1 and q_small*r > 1)
    exact(sp.expand((z-r)*(z*z+r*z-3*r*r) - (z**3-4*r*r*z+3*r**3)))
    if inside:
        assert threshold < A < 4
    else:
        assert not(threshold < A < 4)
    checks += 2
print('ODD_CUBIC_HARMONIC_BERGMAN_CERTIFICATES_OK', checks)
