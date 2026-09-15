"""Full colon GB print + membership tests."""
import sympy as sp

a, b, c, d, p, q, r, s, t = sp.symbols('a b c d p q r s t')
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

J = gens + [1 - t*p]
G = sp.groebner(J, a, b, c, d, p, q, r, s, t, order='lex')
print("total len =", len(G.polys))
for f in G.polys:
    e = f.as_expr()
    print("  [t?", t in e.free_symbols, "]", str(e)[:400])
