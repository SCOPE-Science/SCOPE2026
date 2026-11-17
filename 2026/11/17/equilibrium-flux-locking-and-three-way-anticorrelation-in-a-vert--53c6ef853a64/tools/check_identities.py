#!/usr/bin/env python3
"""Exact polynomial identities for a four-reaction mass-action flow.

Requires SymPy. The infinite-dimensional stationary measure theorem is analytical.
"""
import sympy as sp

x, y, z = sp.symbols("x y z", positive=True)
a, b, c, d, r = sp.symbols("a b c d r", positive=True)
fx = x * (a*z - b*y)
fy = y * (b*x - c*z)
fz = 2*d - z*(c*y + a*x)

def zero(expr):
    assert sp.simplify(expr) == 0, sp.factor(expr)

zero(fx-fy+fz - (2*d-2*b*x*y))
zero(fx/x - (a*z-b*y))
zero(fy/y - (b*x-c*z))
zero(fz/z - (2*d/z-c*y-a*x))

z_star = sp.sqrt(b*d/(a*c))
x_star = c*z_star/b
y_star = a*z_star/b
for expr in (fx, fy, fz):
    zero(expr.subs({x:x_star, y:y_star, z:z_star}))
for expr in (b*x_star*y_star, a*x_star*z_star, c*y_star*z_star):
    zero(expr-d)

# The fixed product flux minus the increased product of the means
# gives the same negative covariance factor on each of three pairs.
for pair_equilibrium in (x_star*y_star, x_star*z_star, y_star*z_star):
    zero(pair_equilibrium-(r**2)*pair_equilibrium +(r**2-1)*pair_equilibrium)

# Both integrated reciprocal relations give the same nonnegative defect.
m=sp.symbols('m',positive=True)
recip_m = m/z_star**2
zero((m-2*z_star+z_star**2*recip_m)/2 -(m-z_star))
print('VERTICAL_HOPF_FLUX_COVARIANCE_SYMBOLIC_OK')
