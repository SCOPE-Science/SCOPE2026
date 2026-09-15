"""Deeper hunt: solve exactly on slices. Since V(I3) has dim>=5 (main comp), slice by fixing
5 coords generically -> expect finite solutions. Observe whether solutions have det=0 always.
Also try Groebner elimination of (I : det) to test if det is zerodivisor mod I:
  (I:det) strictly bigger than I  <=> det is zerodivisor <=> either reducible or nonradical issue.
9-var GB again (with t). Previous colon I:p took a while but finished. Try I:det.
"""
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
detX = sp.expand(M.det())
J = gens + [1 - t*detX]
G = sp.groebner(J, a, b, c, d, p, q, r, s, t, order='lex')
print("total len =", len(G.polys))
nontrivial = []
for f in G.polys:
    e = f.as_expr()
    print("  [t?", t in e.free_symbols, "]", str(e)[:300])
