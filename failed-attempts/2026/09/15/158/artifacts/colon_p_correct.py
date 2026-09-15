"""Colon I:p gave 7-element-containing ideal C with GB of 9 polys; M00,M11,M01 don't reduce to 0.
But that's GB-of-subset; the TRUE colon ideal might be bigger. The lex computation earlier returned exactly
9 polys total (7 without t, 2 with t) — that IS the full colon (elimination is exact). So I:p = (7 elts) = C.
And M00 not in C?? But M00 in I subset I:p = C. Contradiction — unless reduction remainder wrt grlex GB is
misleading (remainder nonzero doesn't imply non-membership... actually with a TRUE GB, remainder 0 iff membership.
G7 IS a groebner basis of (colon7). If remainder(M00) != 0 then M00 not in (colon7). But M00*p in I, so M00 in I:p.
So either lex elimination missed something (sympy lex GB incomplete?) or... wait, the lex GB computation: polys
linear in t? The two t-polys: cd+qrst-r^2 and pt-1. Elimination ideal = GB intersect R = the 7 t-free polys? For lex
with t LAST?? I used order a,b,...,s,t lex with t last — elimination theorem needs t FIRST (greatest) for
contraction! With t smallest, GB cap R is NOT the elimination ideal. My colon computation is WRONG.

Redo: order t,a,b,c,d,p,q,r,s (t greatest) lex, then t-free polys = (I,1-tp) cap R = I:p. Redo for p and det.
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
G = sp.groebner(J, t, a, b, c, d, p, q, r, s, order='lex')
print("total len =", len(G.polys))
for f in G.polys:
    e = f.as_expr()
    print("  [t?", t in e.free_symbols, "]", str(e)[:300])
