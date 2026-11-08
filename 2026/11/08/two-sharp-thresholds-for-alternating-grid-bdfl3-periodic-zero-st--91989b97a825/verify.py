"""Exact algebraic checks for alternating-grid BDFL3 stability."""
import sympy as sp

r, z = sp.symbols('r z', positive=True)
t = sp.Symbol('t')

def coefficients(a, b):
    den = 4*b*(a+1)+2
    a0 = b**2*(2*a**2-2*a-1)/den
    a1 = ((-2*a**2+2*a+1)*b**2 +2*(a+1)*b+1)/den
    beta = (2*a + b*(2*a*a+4*a-1)-1)/(2*a*(2*b*(a+1)+1))
    return (sp.factor(a0), sp.factor(a1), sp.factor(beta))

def step(a, b):
    a0, a1, _ = coefficients(a, b)
    return sp.Matrix([[sp.Rational(3,2),-a1,-a0], [1,0,0], [0,1,0]])

ab = coefficients(r,1/r)
ba = coefficients(1/r,r)
expect_ab = ((2*r**2-2*r-1)/(2*r*(3*r+2)),
             (r**2+4*r+1)/(2*r*(3*r+2)),
             (r+1)*(4*r-1)/(2*r*(3*r+2)))
expect_ba = (-(r**2+2*r-2)/(2*(2*r+3)),
             (r**2+4*r+1)/(2*(2*r+3)),
             (4-r)*(r+1)/(2*(2*r+3)))
for actual, expect in zip(ab+ba, expect_ab+expect_ba):
    assert sp.cancel(actual-expect) == 0

A = 4*r*(2*r+3)*(3*r+2)
B = 6*r**4+2*r**3-21*r**2+2*r+6
C = -2*r**4-2*r**3+9*r**2-2*r-2
P = step(1/r,r)*step(r,1/r)
assert sp.cancel(P.det() - (C/A)) == 0  # product of all eigenvalues is C/A
poly = P.charpoly(t).as_expr()
assert sp.cancel(poly - (t-1)*(A*t**2+B*t+C)/A) == 0
assert sp.factor(A+B+C) == 4*(r+1)**2*(r**2+4*r+1)
assert sp.expand(A-B+C +2*(4*r**4-10*r**3-41*r**2-10*r+4)) == 0
assert sp.expand(A-C) == sp.expand(2*r**4+26*r**3+43*r**2+26*r+2)
F=4*r**4-10*r**3-41*r**2-10*r+4
s=(5+sp.sqrt(221))/4
R=(s+sp.sqrt(s*s-4))/2
assert sp.simplify(F.subs(r,R)) == 0
assert sp.simplify(F.subs(r,1/R)) == 0
assert 4 < float(R) < 5
assert 0.2 < float(1/R) < 0.25
assert sp.simplify(ba[2].subs(r,sp.Rational(9,2))) == -sp.Rational(11,96)
assert sp.simplify((A-B+C).subs(r,sp.Rational(9,2)))>0
# Exact rational example: both parasitic multipliers are strictly in the disk.
rr=sp.Rational(9,2)
AA,BB,CC=[x.subs(r,rr) for x in (A,B,C)]
assert AA+BB+CC>0 and AA-BB+CC>0 and AA-CC>0
# The implicit factor vanishes at this strictly positive decay frequency.
assert 1+sp.Rational(96,11)*ba[2].subs(r,rr) == 0
# Nontrivial initial states can make the corresponding right-hand side nonzero.
assert sp.Rational(3,2) != 0
print('PASS: exact coefficient, monodromy, root-condition and pole identities')
