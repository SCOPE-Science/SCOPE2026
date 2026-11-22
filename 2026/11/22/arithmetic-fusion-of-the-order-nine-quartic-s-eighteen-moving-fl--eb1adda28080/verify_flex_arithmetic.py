"""Exact arithmetic check of the canonical flex divisor of X^4 + X Y^3 + Y Z^3."""
from sympy import symbols, Matrix, diff, expand, Poly, groebner, gcd

X, Y, Z, x, y = symbols('X Y Z x y')
F = X**4 + X*Y**3 + Y*Z**3
H = Matrix([[diff(F, a, b) for b in (X,Y,Z)] for a in (X,Y,Z)]).det()
Q = 8*X**3*Y**2 - 2*X**2*Z**3 - Y**5
assert expand(H - 54*Z*Q) == 0
f = F.subs({X:x,Y:y,Z:1})
q = Q.subs({X:x,Y:y,Z:1})
g = groebner([f, q], y, x, order='lex')
assert [expand(p.as_expr()) for p in g.polys] == [y + 11*x**4 - 27*x**13, expand(x**2*(729*x**18 - 270*x**9 - 2))]
p = 729*x**18 - 270*x**9 - 2
assert gcd(Poly(p,x), Poly(diff(p,x),x)).degree() == 0
# Rabin criterion for degree 18 over F_7: 7^18 fixes x and the two prime-degree tests.
P = Poly(x**18 + 3*x**9 + 5, x, modulus=7)
h = Poly(x,x,modulus=7)
for n in range(1,19):
    h = h.pow(7).rem(P) if hasattr(h,'pow') else (h**7).rem(P)
    if n == 6:
        assert h == Poly(-3*x,x,modulus=7)
        assert gcd(P,h-Poly(x,x,modulus=7)).degree()==0
    if n == 9:
        assert h == Poly(2*x**10-2*x,x,modulus=7)
        assert gcd(P,h-Poly(x,x,modulus=7)).degree()==0
assert h == Poly(x,x,modulus=7)
assert P.degree() == 18
assert (729 % 7)==1 and (-270 % 7)==3 and (-2 % 7)==5
# At infinity, F=X(X^3+Y^3); at its four points, Q is nonzero.
# The affine origin has tangent Y=0 and contact order four because F(X,0,1)=X^4.
assert f.subs(y,0)==x**4
# Three rational flexes on C_Q: the origin, and [0:1:0],[-1:1:0].
for a,b,c in [(0,0,1),(0,1,0),(-1,1,0)]:
    assert F.subs({X:a,Y:b,Z:c})==0 and H.subs({X:a,Y:b,Z:c})==0
print('ORDER_NINE_QUARTIC_ARITHMETIC_FLEX_DIVISOR_OK')
