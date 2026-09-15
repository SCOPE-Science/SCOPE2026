"""Elimination / dimension probe for C4 I3.
- Lex GB eliminating to small variable sets to find equations of projections.
- Then analyze components.
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

# Transcendence: test which subsets are algebraically independent mod I by elimination.
# Try lex with p,q,r,s last (eliminate a,b,c,d first) to see relation among edge vars.
G1 = sp.groebner(gens, a, b, c, d, p, q, r, s, order='lex')
print("lex a>b>c>d>p>q>r>s done, len =", len(G1.polys))
for f in G1.polys:
    e = f.as_expr()
    print("  vars:", sorted(str(s_) for s_ in e.free_symbols), "deg", f.total_degree(), ":", str(e)[:300])
