"""Standalone exact checks for the two-variable adaptive SIS spectral law.

Requires Python 3 and SymPy. Run: python verify.py
All parameters below are mathematical test inputs, not empirical data.
"""
from fractions import Fraction
from math import sqrt
import sympy as sp

t, w, q = sp.symbols('t w q', positive=True)
y = (t - 1) / (t + w)
z = (t + w) / (t * (1 + w))
F = -y + t*y*(1-y)*z
G = q * (1-z-w*y*z)
assert sp.simplify(F) == 0 and sp.simplify(G) == 0
Y, Z = sp.symbols('Y Z')
f = -Y + t*Y*(1-Y)*Z
g = q*(1-Z-w*Y*Z)
J = sp.Matrix([f,g]).jacobian([Y,Z]).subs({Y:y, Z:z})
A = (t-1)/(1+w)
B = t*(1+w)/(t+w)
K = t-1
assert sp.simplify(sp.trace(J) + A + B*q) == 0
assert sp.simplify(J.det() - K*q) == 0
assert sp.simplify(A*B-K*t/(t+w)) == 0
assert sp.simplify((K-A*B) - K*w/(t+w)) == 0

# Closed-form boundary and extremal rate example (tau=3, omega=1).
assert sp.simplify(y.subs({t:3,w:1})-sp.Rational(1,2))==0
assert sp.simplify(z.subs({t:3,w:1})-sp.Rational(2,3))==0
Jcritical = J.subs({t:3,w:1,q:2})
assert Jcritical == sp.Matrix([[-1,sp.Rational(3,4)],[-sp.Rational(4,3),-3]])
assert (Jcritical + 2*sp.eye(2))**2 == sp.zeros(2)
assert Jcritical != -2*sp.eye(2)
assert sp.simplify((sp.trace(Jcritical))**2 - 4*Jcritical.det()) == 0

# Exact-rational comparisons against the full original Jacobian.
checks = 0
for tt in [sp.Rational(x) for x in [2,3,4,7,11]]:
    for ww in [sp.Rational(x,y) for x,y in [(1,4),(1,2),(1,1),(3,2),(3,1),(8,1)]]:
        aa = A.subs({t:tt,w:ww})
        bb = B.subs({t:tt,w:ww})
        kk = tt-1
        assert 0 < aa*bb < kk
        ss = sp.sqrt(ww/(tt+ww))
        qm = kk*(1-ss)**2/bb**2
        qp = kk*(1+ss)**2/bb**2
        assert sp.simplify(qm).is_positive or float(qm)>0
        assert float(qp)>float(qm)
        assert sp.simplify((aa+bb*qm)**2-4*kk*qm)==0
        assert sp.simplify((aa+bb*qp)**2-4*kk*qp)==0
        assert sp.simplify((aa+bb*qp)/2-kk*(1+ss)/bb)==0
        for qq in [sp.Rational(1,100),sp.Rational(1,10),sp.Rational(1,3),sp.Rational(1,1),sp.Rational(5,1),sp.Rational(50,1)]:
            j = J.subs({t:tt,w:ww,q:qq})
            assert sp.simplify(j.det()-kk*qq)==0
            assert sp.simplify(sp.trace(j)+aa+bb*qq)==0
            disc=sp.factor(sp.trace(j)**2-4*j.det())
            disc2=sp.factor((aa+bb*qq)**2-4*kk*qq)
            assert sp.simplify(disc-disc2)==0
            checks += 1
print(f'PASS: symbolic equalities, exact critical Jordan example, {checks} exact-rational parameter checks.')
