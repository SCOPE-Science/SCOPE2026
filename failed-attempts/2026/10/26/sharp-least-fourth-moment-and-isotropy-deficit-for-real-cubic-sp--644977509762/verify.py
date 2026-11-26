"""Exact rational verification of the cubic harmonic fourth-moment identity.

Requires Python 3 and SymPy. Run: python3 verify.py.
The 210 quartic coefficient comparisons constitute an exhaustive finite
symbolic identity check in a basis of the entire real harmonic cubic space.
"""
from math import comb
import sympy as sp

x, y, z = sp.symbols('x y z')
a = sp.symbols('a0:7', real=True)
r2 = x*x + y*y + z*z
basis = [
    z*(5*z*z - 3*r2),
    x*(5*z*z - r2),
    y*(5*z*z - r2),
    z*(x*x - y*y),
    2*x*y*z,
    x*(x*x - 3*y*y),
    y*(3*x*x - y*y),
]
assert all(sp.expand(sp.diff(p, x, 2) + sp.diff(p, y, 2) + sp.diff(p, z, 2)) == 0 for p in basis)
cubic_monomials = [x**i*y**j*z**(3-i-j) for i in range(4) for j in range(4-i)]
C = sp.Matrix([[sp.Poly(b, x, y, z).coeff_monomial(m) for b in basis] for m in cubic_monomials])
assert C.rank() == 7, 'The basis must span the complete harmonic cubic space.'
f = sp.expand(sum(aa*bb for aa, bb in zip(a, basis)))
w = (x, y, z)
T = sp.MutableDenseNDimArray.zeros(3, 3, 3)
for i in range(3):
    for j in range(3):
        for k in range(3):
            T[i, j, k] = sp.diff(f, w[i], w[j], w[k]) / 6
assert all(sp.expand(sum(T[i, i, k] for i in range(3))) == 0 for k in range(3))
M = sp.Matrix(3, 3, lambda i, j: sum(T[i, p, q]*T[j, p, q] for p in range(3) for q in range(3)))
t = sp.expand(sp.trace(M))
u = sp.expand(sp.trace(M*M))

def df(n):
    return sp.factorial2(n) if n > 0 else sp.Integer(1)

def sphere_average(expr):
    """Average over S^2; exact spherical moments, no sampling."""
    out = sp.S.Zero
    for (i, j, k), coeff in sp.Poly(sp.expand(expr), x, y, z).terms():
        if i % 2 == 0 and j % 2 == 0 and k % 2 == 0:
            out += coeff * df(i-1)*df(j-1)*df(k-1) / df(i+j+k+1)
    return sp.expand(out)

E2 = sphere_average(f**2)
E4 = sphere_average(f**4)
assert sp.Poly(E2-sp.Rational(2, 35)*t, a).is_zero
residual = sp.Poly(E4-sp.Rational(4, 5005)*(7*t*t+6*u), a)
assert residual.is_zero
# Verify all 210 quartic coefficient slots, including coefficients that vanish.
quartic_slots = 0
for i0 in range(5):
    for i1 in range(5-i0):
        for i2 in range(5-i0-i1):
            for i3 in range(5-i0-i1-i2):
                for i4 in range(5-i0-i1-i2-i3):
                    for i5 in range(5-i0-i1-i2-i3-i4):
                        i6 = 4-i0-i1-i2-i3-i4-i5
                        powers = (i0, i1, i2, i3, i4, i5, i6)
                        assert residual.coeff_monomial(sp.prod(v**p for v, p in zip(a, powers))) == 0
                        quartic_slots += 1
assert quartic_slots == comb(10, 6) == 210
xyz = x*y*z
assert sphere_average(xyz*xyz) == sp.Rational(1, 105)
assert sphere_average(xyz**4) == sp.Rational(1, 5005)
assert sp.simplify(sphere_average(xyz**4)/sphere_average(xyz**2)**2) == sp.Rational(315, 143)
print('PASS seven linearly independent harmonic cubic basis functions')
print('PASS exact 2nd spherical moment polynomial identity')
print('PASS all 210 quartic coefficients of exact 4th moment identity')
print('PASS sharp xyz witness and normalized ratio 315/143')
