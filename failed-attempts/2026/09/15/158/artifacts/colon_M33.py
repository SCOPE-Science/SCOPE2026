"""Decisive dimension test for double-hub: is V(I) irreducible of dim 10 (codim 3 in A^13)?
Slice c=d=e=0 (=codim 3 linear section): expected dim 10-3=7 if proper section. Slice equations involve
ONLY p1..q3 (6 vars): V_slice = A^4(a,b,h + free? a,b,h unconstrained: 3 free) x W, W in A^6 defined by 2x2 minors
of [[p1,p2,p3],[q1,q2,q3]] (rank<=1 locus: (p1q2-p2q1)^2 etc. — squares of 2x2 minors!). W = rank<=1 cone dim 4.
So slice dim = 3 + 4 = 7. Proper! Consistent with dim-10 irreducible. (Slice polys are squares (p1q2-p2q1)^2:
V_slice non-reduced but set-theoretically fine.)

So double-hub still consistent with prime. Time check: need to decide. Remaining plan:
- The general proof needs Z-irreducibility for all 2-connected G — hardest and uncertain within clock.
- Strongest auditable deliverable: prove n=4 classification completely (C4, diamond, K4: all 2-connected n=4 graphs)
  => TARGET for n=4 (a complete theorem), and honestly scope the general-n route as conjecture with evidence.
  But claim_route TARGET requires the COMPLETE target (all n). n=4-only = EMERGENT_FINDING.

Check remaining time budget: try ONE general structural argument now:
Schur-route induction: for G 2-connected, pick edge... Actually attempt: prove primeness for graphs with a vertex v
with G-v = complete? Hmm.

Alternative general attack — symmetric Laplace/Desnanot-Jacobi + liaison: dense symmetric I_{n-1} prime via ... 
For sparse, try induction on n using colon by principal minor Delta = det(X_{G-v}):
  I_{n-1}(X_G) : Delta ?= I_{n-2}(X_{G-v})-type prime + ... If both colon and (I,Delta) chains behave, primality by
  localization exact sequence. Test on C4: colon I : M33? Compute with t-greatest lex.

Let me run colon I:M33 for C4 (bounded), which informs the induction route.
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
        rr = [x for x in range(4) if x != di]
        cc = [x for x in range(4) if x != dj]
        gens.append(sp.expand(M.extract(rr, cc).det()))
M33 = sp.expand(a*b*c - a*q**2 - c*p**2)
print("M33 =", M33)
J = gens + [1 - t*M33]
G = sp.groebner(J, t, a, b, c, d, p, q, r, s, order='lex')
print("total len =", len(G.polys))
for f in G.polys:
    e = f.as_expr()
    print("  [t?", t in e.free_symbols, "]", str(e)[:250])
