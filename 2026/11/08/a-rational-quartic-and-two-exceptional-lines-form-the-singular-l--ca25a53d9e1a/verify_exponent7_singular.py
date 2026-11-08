"""Exact computations for the swept threefold of an exponent-seven Grassmann curve.

Requirements: Python 3 and SymPy. All identities are over the rationals.
"""
import itertools
import sympy as sp

t, s, u = sp.symbols('t s u')
a, b, c = sp.symbols('a b c')

def frame(z):
    return sp.Matrix([
        [1, z, z**2, z**3, z**4, 0],
        [0, 1, 2*z, 3*z**2, 4*z**3, 0],
        [0, 0, 1, 3*z, 6*z**2, z],
    ])

R = frame(t)
assert sp.factor(frame(s).col_join(R).det()) == -(s-t)**7
A = R[:, :3]
C = R[:, 3:]
assert A.det() == 1
assert sp.factor(C.det()) == t**7
G = sp.simplify(A.inv() * C)
H = sp.simplify((C.inv()*A).subs(t, 1/u))
assert G == sp.Matrix([
    [t**3, 3*t**4, t**3],
    [-3*t**2, -8*t**3, -2*t**2],
    [3*t, 6*t**2, t],
])
assert H == sp.Matrix([
    [4*u**3, 3*u**2, 2*u],
    [-3*u**4, -2*u**3, -u**2],
    [6*u**3, 3*u**2, u],
])

def minor_gcd(M):
    vals = [sp.expand(M.extract(I, J).det())
            for I in itertools.combinations(range(3), 2)
            for J in itertools.combinations(range(3), 2)]
    g = sp.Integer(0)
    for v in vals:
        g = sp.gcd(g, v)
    return sp.factor(g)

D = G.diff(t)
E = H.diff(u)
assert sp.simplify(D.det()) == 0
assert sp.simplify(E.det()) == 0
assert sp.factor(minor_gcd(D)/t).is_number and minor_gcd(D) != 0
assert sp.factor(minor_gcd(E)/u).is_number and minor_gcd(E) != 0
assert D.subs(t,0).rank() == 1
assert E.subs(u,0).rank() == 1
assert D.subs(t,1).rank() == 2
assert E.subs(u,1).rank() == 2

# Projective kernel equations for the normalization differential.
P = sp.Matrix([[a,b,c]]) * D
L = c - 4*t*b + 3*t**2*a
Q = t*(b - t*a)
assert sp.expand(P[0]-3*L-6*Q) == 0
assert sp.expand(P[1]-4*t*P[0]) == 0
assert sp.expand(P[2]-L) == 0

T = sp.Matrix([[a,b,c]]) * E
M = c + 2*a - 2*u*b
Q2 = u*(a-u*b)
assert sp.expand(T[0]-18*u*u*M+24*u*Q2) == 0
assert sp.expand(T[1]-6*u*M+6*Q2) == 0
assert sp.expand(T[2]-M) == 0

# The generic kernel vector maps to the quartic; the boundary kernels to lines.
assert sp.Matrix([[1,t,t**2]])*D == sp.zeros(1,3)
assert sp.Matrix([[u,1,0]])*E == sp.zeros(1,3)
assert G.subs(t,0) == sp.zeros(3)
assert H.subs(u,0) == sp.zeros(3)
assert sp.Matrix([[1,t,t**2]])*sp.Matrix.hstack(sp.eye(3), G) == R[0,:]
assert sp.simplify(sp.Matrix([[u,1,0]])*sp.Matrix.hstack(H, sp.eye(3))
                   - sp.Matrix([[u**4,u**3,u**2,u,1,0]])) == sp.zeros(1,6)
print('VERIFY_OK')
print('two-point determinant = -(s-t)^7')
print('finite-chart critical ideal: (c-4tb+3t^2a, t(b-ta))')
print('infinity-chart critical ideal: (c+2a-2ub, u(a-ub))')
print('reduced critical locus: quartic section plus two exceptional lines')
