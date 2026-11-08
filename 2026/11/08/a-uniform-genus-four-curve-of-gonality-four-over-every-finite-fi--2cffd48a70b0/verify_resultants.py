"""Exact finite polynomial calculations underlying the all-characteristic smoothness argument.
Requires SymPy (tested with 1.13+). No network or external data.
"""
from math import gcd
from sympy import symbols, diff, resultant, groebner, factorint

u, v = symbols('u v')
a = u**3*v**3 + u**3 + v**3 + u + v
b = a + u**2 + v**2
R_EXPECTED = (
    982087492035469593396623616,
    5838078345771419602547015726577988403024765030400,
)

def double_resultant(f):
    return int(resultant(resultant(f, diff(f, u), v),
                         resultant(f, diff(f, v), v), u))

R1, R2 = double_resultant(a), double_resultant(b)
assert (R1, R2) == R_EXPECTED, (R1, R2)
assert gcd(R1, R2) == 338688
assert factorint(gcd(R1, R2)) == {2: 8, 3: 3, 7: 2}

for prime, f in ((2, b), (3, b), (7, a)):
    gb = groebner((f, diff(f, u), diff(f, v)), u, v,
                  modulus=prime, order='lex')
    assert list(gb) == [1], (prime, list(gb))

# Origin is a simple k-point for both bidegree (3,3) equations.
for f in (a, b):
    assert f.subs({u: 0, v: 0}) == 0
    assert diff(f, u).subs({u: 0, v: 0}) == 1
    assert diff(f, v).subs({u: 0, v: 0}) == 1
    assert (f - f.xreplace({u: v, v: u})).expand() == 0

print('PASS: exact integer double resultants, gcd, three special ideals, symmetry, rational point')
