#!/usr/bin/env python3
"""Reproduce symbolic identities for periodic variable-metric proximal splitting.

Requires SymPy.  This is a finite symbolic verification, not an independence proof.
"""
import sympy as S

r, s, q, t, w = S.symbols('r s q t w', real=True, nonzero=True)
M = s * S.Matrix([[1, r], [r, 1]])
z = S.Matrix([0, t]); u = S.Matrix([w, 0])
# Proximal operator of indicator(span(e1)) and indicator(span(e2))
y = z - M.inv() * u
x = S.Matrix([S.factor(y[0] + M[0,1]/M[0,0]*y[1]), 0])
yh = x + M.inv() * u
zp = S.Matrix([0, S.factor(yh[1]+M[1,0]/M[1,1]*yh[0])])
up = S.simplify(u + M*(x-zp))
T = S.Matrix([[r*r,-r/s],[s*r*(1-r*r),r*r]])
assert S.simplify(zp[1]-(T*S.Matrix([t,w]))[0]) == 0
assert S.simplify(up[0]-(T*S.Matrix([t,w]))[1]) == 0
assert S.simplify(up[1]) == 0
assert S.factor(T.det()-r*r) == 0

T1 = T.subs(s,1)
Tq = T.subs(s,q)
P = S.simplify(Tq*T1)
tr = S.factor(P.trace()); det = S.factor(P.det())
assert S.simplify(tr-(2*r**4-r*r*(1-r*r)*(q+1/q))) == 0
assert S.simplify(det-r**4) == 0
assert S.factor((S.eye(2)-P).det() - (1-tr+det)) == 0
assert S.factor((S.eye(2)+P).det() - (1+tr+det)) == 0
assert S.factor((1+tr+det)*q -
    (q*(1+3*r**4)-r*r*(1-r*r)*(q*q+1))) == 0

p = S.symbols('p', real=True)
K = (1+3*p**2)/(p*(1-p))
assert S.factor(K-6 - (3*p-1)**2/(p*(1-p))) == 0
assert S.factor(K.diff(p)) == (3*p-1)*(p+1)/(p*p*(p-1)**2)
assert S.simplify((3+2*S.sqrt(2))+(3-2*S.sqrt(2))-6) == 0

Prat = P.subs({r:S.Rational(3,5),q:6})
assert Prat == S.Matrix([[S.Rational(57,625),-S.Rational(63,250)],
                         [S.Rational(3024,3125),-S.Rational(783,625)]])
assert S.simplify((S.eye(2)+Prat).det()+S.Rational(4,125)) == 0
spec = list(Prat.eigenvals())
assert any(v < -1 for v in [z.evalf() for z in spec])

# Verify rational endpoint equality via the characteristic polynomial.
rc=S.sqrt(S.Rational(1,3)); qc=3+2*S.sqrt(2)
Pcrit=S.simplify(P.subs({r:rc,q:qc}))
assert S.simplify((S.eye(2)+Pcrit).det()) == 0
assert S.simplify(Pcrit.det()-S.Rational(1,9)) == 0

# Rational-grid spectra checks are illustrative, not exhaustive.
for rr in [S.Rational(j,20) for j in range(1,20)]:
    for qq in [S.Rational(1,5),S.Rational(1,2),S.Integer(1),S.Integer(2),S.Integer(5)]:
        pp=P.subs({r:rr,q:qq})
        # Schur condition for quadratic with determinant in (0,1).
        assert 1-pp.trace()+pp.det() > 0
        assert 1+pp.trace()+pp.det() > 0
        assert 1-pp.det() > 0
print('VERIFY_OK exact prox reduction, two-period spectrum, sharp threshold, critical endpoint, rational divergence witness, 95 rational-grid cases')
