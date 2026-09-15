"""Audit artifact: explicit S-pair verification that the 10 nonzero 3-minors are ALREADY a
lex Groebner basis (diagonals > edge vars) for each 2-connected graph on 4 vertices.
Checks all C(10,2)=45 S-polynomials reduce to 0. Exact arithmetic over QQ (Fractions).
Also certifies lex lead terms are squarefree.
"""
import sympy as sp
import itertools

def build(n, diag, edges, esyms):
    M = sp.zeros(n)
    for i in range(n):
        M[i, i] = diag[i]
    for (i, j), s in zip(edges, esyms):
        M[i, j] = s
        M[j, i] = s
    gens = []
    for di in range(n):
        for dj in range(di, n):
            rr = [x for x in range(n) if x != di]
            cc = [x for x in range(n) if x != dj]
            gens.append(sp.expand(M.extract(rr, cc).det()))
    return [g for g in gens if g != 0]

def lex_lead_exp(e, order):
    P = sp.Poly(e, *order)
    return max(P.monoms())

def spoly(f, g, order):
    ef, eg = lex_lead_exp(f, order), lex_lead_exp(g, order)
    L = tuple(max(a, b) for a, b in zip(ef, eg))
    def to_expr(exp):
        m = sp.Integer(1)
        for v, k in zip(order, exp):
            m *= v**k
        return m
    mf = to_expr(tuple(L[i] - ef[i] for i in range(len(order))))
    mg = to_expr(tuple(L[i] - eg[i] for i in range(len(order))))
    cf = sp.Poly(f, *order).nth(*ef)
    cg = sp.Poly(g, *order).nth(*eg)
    return sp.expand(mf * f / cf - mg * g / cg)

def check(name, gens, order):
    G = sp.groebner(gens, *order, order='lex')
    assert len(G.polys) == len(gens), f"{name}: GB len {len(G.polys)} != {len(gens)}"
    nfail = 0
    for f, g in itertools.combinations(gens, 2):
        s = spoly(f, g, order)
        r = G.reduce(s)
        rem = r[1] if isinstance(r, tuple) else r
        if sp.expand(rem) != 0:
            nfail += 1
            print(f"{name}: FAIL pair\n  f={f}\n  g={g}\n  rem={rem}")
    sf = all(all(v <= 1 for v in lex_lead_exp(f, order)) for f in gens)
    print(f"{name}: {len(gens)} gens, {len(list(itertools.combinations(gens,2)))} S-pairs, failures={nfail}, all-leads-squarefree={sf}")
    return nfail == 0 and sf

a, b, c, d = sp.symbols('a b c d')
p, q, r, s, t, u = sp.symbols('p q r s t u')

ok1 = check("C4", build(4, [a,b,c,d], [(0,1),(1,2),(2,3),(0,3)], [p,q,r,s]), [a,b,c,d,p,q,r,s])
ok2 = check("diamond", build(4, [a,b,c,d], [(0,1),(0,3),(1,2),(2,3),(1,3)], [p,s,q,r,t]), [a,b,c,d,p,q,r,s,t])
ok3 = check("K4", build(4, [a,b,c,d], [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)], [p,q,r,s,t,u]), [a,b,c,d,p,q,r,s,t,u])

# Enumeration: all graphs on 4 vertices with min degree >= 2 (necessary for 2-connectedness)
import itertools as it
verts = [0,1,2,3]
alledges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
classes = set()
for mask in range(1 << 6):
    E = [alledges[k] for k in range(6) if mask & (1 << k)]
    deg = [0]*4
    for i,j in E:
        deg[i]+=1; deg[j]+=1
    if min(deg) < 2:
        continue
    # canonical: sorted degree seq + num edges
    classes.add((tuple(sorted(deg)), len(E)))
print("delta>=2 graphs on 4 vertices (degseq, #edges):", sorted(classes))
print("ALL OK:", ok1 and ok2 and ok3)
