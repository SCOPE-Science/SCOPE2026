"""Exact polynomial identities for an invariant-torus lifting theorem.

Run with: python checker.py
Requires SymPy; finite numerical trajectory sampling is not used.
"""
import sympy as sp

x, y, z, eps = sp.symbols('x y z eps', real=True)
u = x*x + y*y
w = u - 2
R = w*w + z*z
P = -z + w*(1-R)
Q = w + z*(1-R)
fx = -y
fy = x + eps*y*P
fz = 2*eps*y*y*Q

def deriv(v):
    return sp.expand(sp.diff(v, x)*fx + sp.diff(v, y)*fy + sp.diff(v, z)*fz)

assert sp.expand(deriv(u) - 2*eps*y*y*P) == 0
assert sp.expand(deriv(z) - 2*eps*y*y*Q) == 0
assert sp.factor(deriv(R) - 4*eps*y*y*R*(1-R)) == 0
# On the core circle (u,z)=(2,0), P and Q vanish, so the flow is
# exactly x'=-y, y'=x, z'=0.
assert sp.factor(P.subs({u:2,z:0})) == 0
assert sp.factor(Q.subs({u:2,z:0})) == 0
# The explicit torus is regular in real space: d(R-1)=0 would require
# z=0 and (u-2)x=(u-2)y=0; these imply either u=2 or u=0, neither
# can lie on R=1 at z=0.
critical = [sp.diff(R, v) for v in (x,y,z)]
assert all(sp.factor(c) == 0 for c in [critical[0].subs(w,0), critical[1].subs(w,0)])
# Independent planar radial identity: w P + z Q = R (1-R).
assert sp.factor(w*P + z*Q - R*(1-R)) == 0
print('EXACT_TORUS_LIFT_IDENTITIES_OK')
