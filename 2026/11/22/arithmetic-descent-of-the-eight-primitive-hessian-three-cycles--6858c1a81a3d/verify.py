"""Exact checks for the arithmetic of Hessian three-cycles (requires SymPy)."""
import sympy as S

x, z = S.symbols('x z')
Q = lambda e: S.Poly(e, x, domain=S.QQ)

# Homogeneous iterates: [U:V] -> [(4V-U)^3:27 U^2 V].
u, v = Q(x), Q(1)
pairs = []
for _ in range(3):
    u, v = (4*v-u)**3, 27*u**2*v
    assert u.gcd(v).degree() == 0
    pairs.append((u, v))
fixed = pairs[0][0] - Q(x)*pairs[0][1]
assert fixed == -Q((x-1)*(7*x**2+4*x+16))*4
third = u-Q(x)*v
primitive, rem = third.div(fixed)
assert rem.is_zero and third.degree() == 27 and primitive.degree() == 24
assert third.gcd(third.diff()).degree() == 0

point_polys = [
    x**6+84*x**5+11040*x**4-47936*x**3+204288*x**2-33792*x+4096,
    19*x**6+912*x**5+18240*x**4-54272*x**3+47616*x**2+3072*x+4096,
    37*x**12+15540*x**11+2026416*x**10-30549568*x**9+86526720*x**8
    +656409600*x**7+378470400*x**6-4591042560*x**5+6717505536*x**4
    -4462477312*x**3+1588592640*x**2+25165824*x+16777216,
]
assert primitive.monic() == Q(S.prod(point_polys)).monic()
G = z**4+420*z**3+57456*z**2+174528*z+269568
sum_polys = [z*z+84*z+10512, z*z+48*z+1008, G]

def irreducible_at_five(poly, var):
    f = S.Poly(poly, var, modulus=5)
    assert f.degree() == S.degree(poly, var)
    a = y = S.Poly(var, var, modulus=5)
    n = f.degree()
    exponents = {n//ell for ell in S.primefactors(n)}
    for i in range(1, n+1):
        a = (a**5).rem(f)
        if i in exponents:
            assert (a-y).gcd(f).degree() == 0
    assert a == y

for f in point_polys:
    irreducible_at_five(f, x)
irreducible_at_five(G, z)

(u1, v1), (u2, v2), _ = pairs
for point, trace in zip(point_polys, sum_polys):
    f = Q(point)
    numer = Q(x)*v1*v2+u1*v2+u2*v1
    denom = v1*v2
    s = (numer*denom.invert(f)).rem(f)
    # Horner evaluation in Q[x]/(f) avoids composing large expressions.
    test = Q(0)
    for c in S.Poly(trace, z).all_coeffs():
        test = (test*s+Q(c)).rem(f)
    assert test.is_zero

assert [S.discriminant(f, z) for f in sum_polys[:2]] == [-3*108**2, -3*24**2]
assert S.discriminant(G, z) == 2**24*3**20*7**2*37*211**2
a, b, c, d = S.Poly(G, z).all_coeffs()[1:]
assert S.expand((z-288)*(z*z-57168*z+55759104)) == z**3-b*z**2+(a*c-4*d)*z+4*b*d-a*a*d-c*c

q = S.Poly(G, z, modulus=13)
assert q == S.Poly(z*(z-5)*(z*z-4*z+2), z, modulus=13)
assert q.gcd(q.diff()).degree() == 0
assert pow(8, 6, 13) == 12  # the quadratic discriminant is 8
print('PASS: period-three polynomials, cycle-sum fields and squarefree Frobenius certificate')
