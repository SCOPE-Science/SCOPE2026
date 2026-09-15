"""Verify squarefree lex leads for C4, diamond; compute K4 (dense symmetric 4x4) lex GB + leads.
Lex order: diagonals first (a>b>c>d), then edge vars. Claim: each nonzero (n-1)-minor has squarefree lead.
"""
import sympy as sp
import time

def analyze(name, n, diag, edges, esyms, order):
    t0 = time.time()
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
    nz = [g for g in gens if g != 0]
    print(f"=== {name}: {len(nz)} nonzero minors, GB computing...")
    G = sp.groebner(gens, *order, order='lex')
    print(f"    GB len {len(G.polys)} ({time.time()-t0:.1f}s). GB==minors: {len(G.polys)==len(nz)}")
    allsf = True
    for f in G.polys:
        e = f.as_expr()
        # lex lead: max exponent tuple lexicographically in `order` variable sequence
        P = sp.Poly(e, *order)
        monoms = P.monoms()
        lm_exp = max(monoms)
        sqfree = all(v <= 1 for v in lm_exp)
        allsf = allsf and sqfree
        lt_str = "*".join(f"{v}**{ee}" if ee > 1 else f"{v}" for v, ee in zip(order, lm_exp) if ee)
        print(f"    lead={lt_str} squarefree={sqfree} :: {str(e)[:110]}")
    print(f"    ALL SQUAREFREE: {allsf}")
    return allsf

a, b, c, d = sp.symbols('a b c d')
p, q, r, s, t, u = sp.symbols('p q r s t u')

analyze("C4", 4, [a,b,c,d], [(0,1),(1,2),(2,3),(0,3)], [p,q,r,s], [a,b,c,d,p,q,r,s])
analyze("diamond", 4, [a,b,c,d], [(0,1),(0,3),(1,2),(2,3),(1,3)], [p,s,q,r,t], [a,b,c,d,p,q,r,s,t])
# K4 dense: edges 01,02,03,12,13,23
analyze("K4", 4, [a,b,c,d], [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)], [p,q,r,s,t,u],
        [a,b,c,d,p,q,r,s,t,u])
