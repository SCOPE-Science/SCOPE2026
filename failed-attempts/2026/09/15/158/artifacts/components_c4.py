"""Section analysis: cut V(I3) for C4 by random hyperplanes to isolate components.
Idea: if V is irreducible of dimension D in A^8, a general linear section of codim D is finite
of cardinality = degree. If V has extra components of various dims, sections behave differently.
Also: look for an obvious extra component. E.g., check vanishing loci:

Component hunt A: matrices where the 4-cycle structure forces block structure.
X = [[a,p,0,s],[p,b,q,0],[0,q,c,r],[s,0,r,d]].
Observe: if p=q=r=s=0 then X=diag(a,b,c,d), and ALL 3-minors vanish?? det of diag-deleted =
product of 3 diagonal entries... e.g. M33=abc. Not identically zero. So diagonal locus is NOT contained.

Component hunt B: locus where two opposite edge vars vanish? e.g. p=r=0:
X = [[a,0,0,s],[0,b,q,0],[0,q,c,0],[s,0,0,d]]. This is block-permutation: rows/cols (1,4),(2,3).
det-computations: all 3-minors vanish identically? Let's test symbolically.
Similarly q=s=0.
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
gens = {}
for di in range(4):
    for dj in range(di, 4):
        rr = [x for x in rows4 if x != di]
        cc = [x for x in rows4 if x != dj]
        gens[(di, dj)] = sp.expand(M.extract(rr, cc).det())

for spec, name in [
    ({p: 0, r: 0}, "p=r=0"),
    ({q: 0, s: 0}, "q=s=0"),
    ({p: 0, q: 0, r: 0, s: 0}, "all edges 0"),
    ({a: 0, b: 0, c: 0, d: 0}, "all diag 0"),
]:
    print(f"=== {name} ===")
    for k, g in gens.items():
        v = sp.expand(g.subs(spec))
        print(f"  M_{k} -> {v}   zero={v == 0}")
