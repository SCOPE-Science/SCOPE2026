"""Exact symbolic verification for the period-two sampled double-integrator result.
Requires Python 3 and SymPy. The proof itself is in RESULT.md; this script checks
its matrix identities and the exact rational instability witness.
"""
import sympy as sp

a, b, kp, kd, h = sp.symbols("a b kp kd h", positive=True, real=True)

def M(t):
    return sp.Matrix([
        [1 - kp*t**2/2, t - kd*t**2/2],
        [-kp*t, 1 - kd*t],
    ])

# Constant-period map identities.
Mh = M(h)
trh = sp.factor(sp.trace(Mh))
deth = sp.factor(Mh.det())
assert sp.factor(trh - (2 - kd*h - kp*h**2/2)) == 0
assert sp.factor(deth - (1 - kd*h + kp*h**2/2)) == 0
assert sp.factor(1 - trh + deth - kp*h**2) == 0
assert sp.factor(1 + trh + deth - (4 - 2*kd*h)) == 0
assert sp.factor(1 - deth - (kd*h - kp*h**2/2)) == 0
assert sp.factor(deth + 1 - (2 - kd*h + kp*h**2/2)) == 0

# Period-two monodromy identities.
P = sp.simplify(M(b) * M(a))
trP = sp.factor(sp.trace(P))
detP = sp.factor(P.det())
phi = kp**2*a**2*b**2 + 4*a*b*(kd**2-kp) - 4*kd*(a+b) + 8
assert sp.factor(detP - (kp*a**2 - 2*kd*a + 2)*(kp*b**2 - 2*kd*b + 2)/4) == 0
assert sp.factor(1 - trP + detP - kp*(a+b)*(a+b-kd*a*b)) == 0
assert sp.factor(1 + trP + detP - phi/2) == 0

# Exact rational witness: both fixed intervals are Schur stable, but the
# alternating two-step monodromy has a multiplier below -1.
kp0, kd0 = sp.Integer(2), sp.Rational(3, 2)
a0, b0 = sp.Rational(1, 10), sp.Rational(13, 10)
M1 = sp.simplify(M(a0).subs({kp: kp0, kd: kd0}))
M2 = sp.simplify(M(b0).subs({kp: kp0, kd: kd0}))
P0 = sp.simplify(M2*M1)
tr0 = sp.factor(sp.trace(P0))
det0 = sp.factor(P0.det())
phi0 = sp.factor(phi.subs({kp: kp0, kd: kd0, a: a0, b: b0}))
assert phi0 == sp.Rational(-253, 1250)
assert tr0 == sp.Rational(-1086, 625)
assert det0 == sp.Rational(1591, 2500)
# For each fixed interval h, the three Jury quantities are positive and |det|<1.
for h0 in (a0, b0):
    t0 = sp.factor(sp.trace(M(h0).subs({kp: kp0, kd: kd0})))
    d0 = sp.factor(M(h0).subs({kp: kp0, kd: kd0}).det())
    assert sp.factor(1-t0+d0) > 0
    assert sp.factor(1+t0+d0) > 0
    assert abs(d0) < 1
# p(-2)>0 and p(-1)<0 for p(z)=z^2-tr(P)z+det(P), so a root lies in (-2,-1).
p_minus2 = sp.factor(4 + 2*tr0 + det0)
p_minus1 = sp.factor(1 + tr0 + det0)
assert p_minus2 == sp.Rational(2903, 2500)
assert p_minus1 == sp.Rational(-253, 2500)

print("VERIFY_OK symbolic_matrix_identities=10 exact_witness=1")
print(f"phi_witness={phi0} trace={tr0} determinant={det0}")
print(f"p(-2)={p_minus2} p(-1)={p_minus1}")
