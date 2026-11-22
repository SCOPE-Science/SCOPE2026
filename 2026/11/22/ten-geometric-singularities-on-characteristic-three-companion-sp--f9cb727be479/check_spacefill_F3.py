#!/usr/bin/env python3
"""Exact finite-field verification for a pair of space-filling quintic surfaces.

Requires Python 3 and SymPy. All tests are polynomial calculations in F_3.
The geometric interpretation of these calculations is supplied in RESULT.md.
"""
import sympy as sp

x, s, t, u, z, a, b, c = sp.symbols('x s t u z a b c')
mod = 3
phi = lambda A, B: A**3 * B - A * B**3

def quintic(beta):
    return (s * phi(x, s) + t * phi(s, t) + u * phi(t, u)
            + (beta * x + u) * phi(u, x))

F = quintic(1)
assert sp.Poly(sp.expand(F.subs(u, -u) - quintic(2)), x, s, t, u, modulus=3).is_zero
partials = [sp.diff(F, v) for v in (x, s, t, u)]

# No projective critical points on x=0: cover that hyperplane by its three standard affine charts.
for coord in (s, t, u):
    equations = [p.subs({x: 0, coord: 1}, simultaneous=True) for p in partials]
    variables = tuple(v for v in (s, t, u) if v != coord)
    basis = sp.groebner(equations, *variables, order='lex', modulus=mod)
    assert len(basis.polys) == 1 and basis.polys[0].is_one
print('No projective singularities with x=0: PASS')

# The four partial derivatives generate the following three-element lexicographic Groebner basis.
G = sp.groebner([p.subs(x, 1) for p in partials], s, t, u,
                order='lex', modulus=mod)
assert len(G.polys) == 3 and G.is_zero_dimensional
s0, t0, P = [p.as_expr() for p in G.polys]
A = u**2 + 1
B = u**2 - u - 1
H = u**6 - u**5 + u**4 + u**3 - u + 1
expected = A * B * H**3
assert sp.Poly(P-expected, u, modulus=mod).is_zero
assert sp.diff(s0,s) == 1 and sp.diff(s0,t) == 0
assert sp.diff(t0,t) == 1 and sp.diff(t0,s) == 0
s_value = sp.solve(s0, s)[0]
t_value = sp.solve(t0, t)[0]

# Over F_3, A and B are irreducible quadratics and H is an irreducible sextic.
for Q in (A,B):
    assert sp.Poly(Q,u,modulus=3).is_irreducible
assert sp.Poly(H,u,modulus=3).is_irreducible
assert sp.gcd(A,B, modulus=3) == 1
assert sp.gcd(A,H, modulus=3) == 1
assert sp.gcd(B,H, modulus=3) == 1
assert sp.gcd(H, sp.diff(H, u), modulus=3) == 1
print('Jacobian algebra length 22, three Frobenius orbits 2+2+6: PASS')

# Use polynomial modular reduction to inspect Hessians on the geometric support.
f = F.subs(x, 1)
hess = sp.hessian(f, (s,t,u))
def reduce_at(expr, modulus):
    expr = sp.expand(expr.subs({s:s_value,t:t_value}, simultaneous=True))
    return sp.rem(expr, modulus, u, modulus=3)
D = reduce_at(hess.det(), P)
assert sp.Poly(D + (u**3+u**2-1)*H**3,u,modulus=3).rem(sp.Poly(P,u,modulus=3)).is_zero
assert sp.gcd(D, A*B, modulus=3) == 1
assert sp.rem(D, H, u, modulus=3) == 0
print('Four ordinary quadratic nodes, Hessian degenerate at six other points: PASS')

# On H=0, a nonzero cross product of two Hessian rows spans its null line.
hr = hess.applyfunc(lambda p: reduce_at(p, H))
v = sp.Matrix([
    hr[0,1]*hr[1,2] - hr[0,2]*hr[1,1],
    hr[0,2]*hr[1,0] - hr[0,0]*hr[1,2],
    hr[0,0]*hr[1,1] - hr[0,1]*hr[1,0]
]).applyfunc(lambda p: sp.rem(p, H, u, modulus=3))
expected_v = [-u**5-u**3-1, -u**3, -u**4-u**3+u**2-u-1]
assert all(sp.rem(v[i]-expected_v[i],H,u,modulus=3) == 0 for i in range(3))
assert all(sp.gcd(k,H,modulus=3) == 1 for k in v)
assert all(sp.rem(sum(hr[i,j]*v[j] for j in range(3)),H,u,modulus=3)==0
           for i in range(3))

# A cubic term along the Hessian null line is nonzero at all six points.
# Ordinary third derivatives are unusable in characteristic three, so extract
# the polynomial coefficient directly, prior to reducing in F_3.
a,b,c = sp.symbols('a b c')
cubic = sp.Poly(sp.expand(f.subs({s:s+z*a,t:t+z*b,u:u+z*c},
                                     simultaneous=True)),z).coeff_monomial(z**3)
cubic_eval = sp.rem(sp.expand(cubic.subs(
    {s:s_value,t:t_value,a:v[0],b:v[1],c:v[2]}, simultaneous=True)),
    H, u, modulus=3)
assert sp.rem(cubic_eval-(u**5-u**4-u**3+1), H,u,modulus=3)==0
assert sp.gcd(cubic_eval,H,modulus=3) == 1
print('Six corank-one, cubic-null-direction wild singularities: PASS')
print('Singular subscheme: 4 reduced points and 6 curvilinear length-three points.')
print('Full singular scheme length: 22. No F_3-rational singularities.')
