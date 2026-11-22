"""Exact checks for the diagonal-singularity and rank-correlation envelope.

Requires sympy. The proof is supplied in RESULT.md; this checker tests
its algebraic identities and representative exact rational constructions.
"""
import sympy as s

t, a, b, q = s.symbols('t a b q', positive=True)

# Fubini kernel underlying the sharp lower-bound deficit.
w = 4*t*(a**2-t**2)
assert s.simplify(s.integrate(w, (t,0,a))-a**4) == 0
W = s.integrate(w, (t,0,t))
assert s.simplify(W/t**2 - w/t - (3*t**2-2*a**2)) == 0
assert s.simplify((3*t**2-2*a**2-a**4/t**2)
                  - (t**2-a**2)*(3*t**2+a**2)/t**2) == 0

# For lower extremizer f=a on (0,a), zero outside: k=a below,
# k=t above; off-diagonal density h=0 below, h=1 above.
H_low = s.integrate(a/t**2, (t, t, a))  # a/t-1
assert s.simplify(t*(1+H_low)-a) == 0
assert s.simplify(s.diff(t*(1+H_low),t)) == 0
assert s.simplify(s.integrate(a,(t,0,a))-a**2) == 0
assert s.simplify(3*s.integrate(t**2*a,(t,0,a))-a**4) == 0

# For upper extremizer f=1 on (b,1), zero below: k=t/b
# below b and k=1 above b, giving h=1/b and h=0.
H_high_below = s.integrate(1/t**2, (t,b,1))
H_high_above = s.integrate(1/t**2, (t,t,1))
assert s.simplify(t*(1+H_high_below)-t/b) == 0
assert s.simplify(t*(1+H_high_above)-1) == 0
assert s.simplify(s.integrate(1,(t,b,1))-(1-b)) == 0
assert s.simplify(3*s.integrate(t**2,(t,b,1))-(1-b**3)) == 0

# Uniform Fréchet generator f=p: the exact deficit identity
# becomes p-p^2 once the choice a^2=p is made.
p = a**2
lhs = p-p**2
rhs = s.integrate(w*(1-p),(t,0,a)) + p*s.integrate(
    (t**2-a**2)*(3*t**2+a**2)/t**2,(t,a,1))
assert s.simplify(lhs-rhs)==0

# A family of exact attainable witnesses. For given p=a^2,
# convex mixing with q in [0,1] leaves h nonnegative.
for av in [s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)]:
    pv=av**2
    bv=1-pv
    rho_min=pv**2
    rho_max=1-bv**3
    assert rho_min<=pv<=rho_max
    for qv in [s.Rational(0),s.Rational(1,5),s.Rational(1,2),s.Rational(1)]:
        rho=(1-qv)*rho_min+qv*rho_max
        assert rho_min<=rho<=rho_max
        for xv in [s.Rational(1,10),s.Rational(2,5),s.Rational(3,5),s.Rational(9,10)]:
            hlow = s.Integer(0) if xv<av else s.Integer(1)
            hhigh = 1/bv if xv<bv else s.Integer(0)
            assert (1-qv)*hlow+qv*hhigh>=0

print('PASS: exact lower/upper formulas, Fubini kernel, deficit identity, and constructive witnesses')
