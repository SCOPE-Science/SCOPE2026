"""Search for rank<=1 symmetric structured locus (=Veronese-type component).
Points of V(I3) include rank<=2 symmetric matrices with C4 sparsity. Rank<=1 matrices with
sparsity: X = v v^T with v1 v3 = 0 and v2 v4 = 0 (the two zero positions).
So rank-1 locus = union of 4 linear-space pieces (v1=0 or v3=0) x (v2=0 or v4=0):
  L00: v1=v2=0; L01: v1=v4=0; L10: v3=v2=0; L11: v3=v4=0.
Each gives a 2-dim cone component of the rank<=1 locus. But is rank<=1 locus a COMPONENT of V,
or contained in closure of rank-2 locus? Dimension count will tell.

Key algebraic test for primality: find f*g in I (or rad(I)) with neither in I/rad, or find
points on distinct components. Better: compute I : J for suitable J to detect embedded/
extra components.

Candidate splitting: consider D = p q r s (product of edge vars)? Or Delta factors?
Alternative: saturate I w.r.t. various elements and see if saturation is strictly bigger
but still proper — indicates non-prime (either reducible or nonradical).

Since sympy Groebner is slowish but workable (10 cubics in 8 vars took seconds), try:
 1. I : p  (colon) via elimination: {f : f*p in I} = (1/t)(I cap ... ) use standard trick:
    I:p = (I + <1 - t p>) cap R. Needs 9-var GB. Might be heavy but try with timeout.
 2. I : (abcd...) etc.
Also try prime-test-by-localization: invert all diagonal vars? Or invert edge vars?

Cheaper first probe: restrict to affine chart, e.g. set s=1 (dehomogenize w.r.t. one var?
not homogeneous... but can still look at D(s) and D(pqrs)): compute elimination to see
whether V cap D(pqrs) is irreducible and whether V has components inside V(pqrs).

Start: colon I:p via sympy with extra variable t.
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

J = gens + [1 - t*p]
G = sp.groebner(J, a, b, c, d, p, q, r, s, t, order='lex')
print("colon gars done len =", len(G.polys))
for f in G.polys:
    e = f.as_expr()
    if t not in e.free_symbols:
        print("COLON ELT:", str(e)[:400])
