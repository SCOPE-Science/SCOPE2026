"""Numerical primary decomposition probe for C4: sample V(I_3) via random linear slices.
Strategy: intersect V(I_3) (8-dim ambient) with random affine linear spaces of complementary
dimension and count/track components. Since no Singular/M2, use sympy nsolve from many starts
and homotopy-style counting, plus exact dimension via Groebner over QQ with lex elimination.

First: Groebner basis of I_3(C4) to get dimension/degree info.
"""
import sympy as sp

a, b, c, d, p, q, r, s = sp.symbols('a b c d p q r s')
M = sp.Matrix([
    [a, p, 0, s],
    [p, b, q, 0],
    [0, q, c, r],
    [s, 0, r, d],
])
rows4 = list(range(4))
gens = []
for di in range(4):
    for dj in range(di, 4):
        rr = [x for x in rows4 if x != di]
        cc = [x for x in rows4 if x != dj]
        gens.append(sp.expand(M.extract(rr, cc).det()))

# Groebner with grevlex
G = sp.groebner(gens, a, b, c, d, p, q, r, s, order='grlex')
print("grevlex GB computed, len =", len(G.polys))
for f in G.polys:
    print("  deg", f.total_degree(), ":", str(f.as_expr())[:200])
