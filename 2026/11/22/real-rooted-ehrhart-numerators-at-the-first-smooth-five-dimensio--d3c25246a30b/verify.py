"""Exact checks for five-dimensional simplex-frustum Ehrhart numerators.

Requires Python 3 and SymPy. Run alongside certificate.json.
"""
from pathlib import Path
import json
from math import comb
import sympy as s

c, z, t = s.symbols('c z t')
h = [
    s.Integer(1),
    (c+1)*(c+6)*(c*c+7*c+16)/24,
    c*(c+1)*(c+3)*(11*c+34)/24,
    c*(c+1)*(11*c*c+19*c-18)/24,
    c*(c-2)*(c-1)*(c+1)/24,
]
H = s.expand(sum(h[k]*z**k for k in range(5)))
cert = json.loads(Path(__file__).with_name('certificate.json').read_text())
assert cert['parameter_shift'] == 2
assert cert['disc_denominator'] == 995328
assert len(cert['discriminant_polynomial_ascending']) == 20
assert all(isinstance(a, int) and a>0 for a in cert['discriminant_polynomial_ascending'])
u = s.symbols('u')
P = sum(a*u**k for k,a in enumerate(cert['discriminant_polynomial_ascending']))
assert s.expand(
    995328*s.discriminant(H,z)-c**2*(c+1)**3*P.subs(u,c-2)
) == 0
assert s.simplify(H.subs(z,-1/(c+1)) + (c**6+5*c**5+22*c**4+68*c**3+136*c**2+152*c+72)/(24*(c+1)**3)) == 0
assert s.factor(s.discriminant(H.subs(c,1),z)) == 23377
assert s.factor(s.discriminant(H.subs(c,2),z)) == 2455472
assert s.factor(H.subs(c,0)) == 1+4*z

# Independently recover the numerator by counting the integer-height slices.
for twist in range(9):
    counts=[sum(comb(n+twist*j+4,4) for j in range(n+1)) for n in range(7)]
    actual=[sum((-1)**(k-j)*comb(6,k-j)*counts[j] for j in range(k+1)) for k in range(6)]
    expected=[int(h[k].subs(c,twist)) for k in range(5)]+[0]
    assert actual == expected, (twist, actual, expected)
    for n in range(7):
        reconstructed=sum(expected[k]*comb(n+5-k,5) if n+5-k>=5 else 0 for k in range(6))
        assert counts[n] == reconstructed

# Reconstruct the Ehrhart polynomial from exact integer counts at six dilations,
# independently of the stated rational coefficient formulas.
q = s.symbols('q')
L0 = sum(h[k]*s.prod(q+5-k-j for j in range(5))/s.factorial(5) for k in range(5))
linear = s.factor(s.expand(L0).coeff(q,1))
assert s.simplify(linear-(-c**4+175*c**2+750*c+2220)/720) == 0
assert linear.subs(c,15)==s.Rational(37,12)
assert linear.subs(c,16)==-s.Rational(181,20)
# The quartic c^4-175c^2-750c-2220 has exactly one positive root
# by Descartes' rule; the signs at 15 and 16 bracket that root.
print('PASS: exact degree-19 discriminant certificate, root signs,')
print('      54 independent numerator counts, 63 Ehrhart evaluations,')
print('      and sharp integer Ehrhart-linear-coefficient threshold.')
