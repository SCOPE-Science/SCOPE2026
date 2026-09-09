"""Verify G_{3,2,1} factorization, irreducibility, and exact-type classification.
Stdlib + sympy only. Prints replayable certificate."""
import sympy as sp
c = sp.Symbol('c')
a1 = c
a2 = c**3 + c
a3 = a2**3 + c
E = sp.expand(a3 - a2)   # full equation f^3(0)=f^2(0)
print("E =", E)
print("factor(E) =", sp.factor(E))
# primitive factor
G = c**4 + 3*c**2 + 3
print("G =", G, "| factor:", sp.factor(G))
assert sp.expand(c**5 * G - E) == 0, "E = c^5*G identity"
# irreducibility: Eisenstein at p=3 (all non-leading coeffs div by 3, const 3 not div by 9)
# plus sympy confirmation
print("is_irreducible(G):", sp.Poly(G, c).is_irreducible)
assert sp.Poly(G, c).is_irreducible
# no rational root (rational root test): possible +-1,+-3
for r in [1,-1,3,-3]:
    assert G.subs(c, r) != 0
# quadratic-in-y discriminant nonsquare -> no quadratic factor; confirmed by irreducibility
# exactness: for each root r of G: r!=0, a2-a1 = r^3 != 0, a2 = r^3+r != 0
# a2==0 <=> r(r^2+1)==0 <=> r^2 in {0,-1}; check resultant/gcd
print("gcd(G, c) =", sp.gcd(G, c))
print("gcd(G, c^2+1) =", sp.gcd(G, c**2+1))
print("gcd(G, c^3) [a2-a1 test] =", sp.gcd(G, c**3))
assert sp.gcd(G, c) == 1 and sp.gcd(G, c**2+1) == 1
# discriminant of G (Galois orbit datum)
print("disc(G) =", sp.discriminant(G, c))
# numeric roots + exact orbit check
roots = sp.nroots(G, n=50, maxsteps=200)
for r in roots:
    cc = complex(r)
    A1 = cc; A2 = cc**3+cc; A3 = A2**3+cc
    assert abs(A3-A2) < 1e-12, (r, A3-A2)
    assert abs(A1) > 0.5 and abs(A2-A1) > 0.5 and abs(A2) > 0.5
print("all 4 numeric roots: exact type (2,1) orbit checks pass")
print("VERIFY_OK")
