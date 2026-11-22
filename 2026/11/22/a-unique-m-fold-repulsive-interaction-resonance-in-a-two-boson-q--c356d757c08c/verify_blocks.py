#!/usr/bin/env python3
"""Independent sector-Jacobi and rational crossing certificate (SymPy)."""
import sympy as sp
x, u, m = sp.symbols('x u m', real=True)

# Block determinants are constructed independently of the claimed cubics.
# For the singlet, the nonzero coupled doublon state has energy u.
S = sp.Matrix([[u,-sp.sqrt(2*(m+1)),0],
               [-sp.sqrt(2*(m+1)),0,-sp.sqrt(2*(m-1))],
               [0,-sp.sqrt(2*(m-1)),0]])
T = sp.Matrix([[u,-sp.sqrt(2),0],
               [-sp.sqrt(2),0,-sp.sqrt(m-2)],
               [0,-sp.sqrt(m-2),0]])
qs = sp.expand((x*sp.eye(3)-S).det())
qt = sp.expand((x*sp.eye(3)-T).det())
assert sp.simplify(qs-(x**3-u*x**2-4*m*x+2*(m-1)*u)) == 0
assert sp.simplify(qt-(x**3-u*x**2-m*x+(m-2)*u)) == 0
assert sp.simplify(qs-qt-m*(u-3*x)) == 0
assert sp.simplify(qt.subs(x,u/3)-2*u*(9*(m-3)-u*u)/27) == 0
# Cubic sign alternation makes the only potential common root the simple
# root within (0,u), at the unique positive U=3sqrt(m-3) (m>=4).
assert sp.simplify(qs.subs(x,0)-2*(m-1)*u) == 0
assert sp.simplify(qt.subs(x,0)-(m-2)*u) == 0
assert sp.simplify(qs.subs(x,u)+2*(m+1)*u) == 0
assert sp.simplify(qt.subs(x,u)+2*u) == 0
for degree in range(4,31):
    critical = 3*sp.sqrt(degree-3)
    energy = sp.sqrt(degree-3)
    assert sp.simplify(qs.subs({m:degree,u:critical,x:energy})) == 0
    assert sp.simplify(qt.subs({m:degree,u:critical,x:energy})) == 0
    # Simple root check in both blocks.
    assert sp.simplify(sp.diff(qs,x).subs({m:degree,u:critical,x:energy})) != 0
    assert sp.simplify(sp.diff(qt,x).subs({m:degree,u:critical,x:energy})) != 0
print('BLOCK_IDENTITY_OK symbolic_cubics=2 symbolic_crossing=1 resonance_sizes=27')
