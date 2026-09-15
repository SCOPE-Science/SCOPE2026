"""T1: C4 lex lead terms squarefree verification + T2: diamond GB + leads.
Also P4 (path) and star comparisons to test sharpness of 2-connectedness."""
import sympy as sp

def case(name, n, diag, edges, esyms, order_vars):
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
    nz = [(g) for g in gens if g != 0]
    G = sp.groebner(gens, *order_vars, order='lex')
    print(f"=== {name}: {len(nz)} nonzero gens, lex GB len {len(G.polys)}")
    ok = True
    for f in G.polys:
        e = f.as_expr()
        # lead term under lex order_vars: leading monomial
        poly = sp.Poly(e, *order_vars)
        lt = poly.leading_monomial() if hasattr(poly, 'leading_monomial') else None
        print(f"  GB elt deg {f.total_degree()}: {str(e)[:130]}")
    # check: GB == gens (up to scale)? i.e., minors already a GB?
    print(f"  GB length vs nonzero gens: {len(G.polys)} vs {len(nz)}")
    return M, gens

a, b, c, d = sp.symbols('a b c d')
p, q, r, s, t = sp.symbols('p q r s t')

# C4
case("C4", 4, [a, b, c, d], [(0,1),(1,2),(2,3),(0,3)], [p, q, r, s], [a,b,c,d,p,q,r,s])
# Diamond (missing edge 02)
case("diamond", 4, [a, b, c, d], [(0,1),(0,3),(1,2),(2,3),(1,3)], [p,s,q,r,t], [a,b,c,d,p,q,r,s,t])
