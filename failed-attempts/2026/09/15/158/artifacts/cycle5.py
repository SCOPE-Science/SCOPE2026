"""C5 test: n=5, 10 vars, 15 distinct 4-minors. Check for identically-zero minors and factor."""
import sympy as sp

def sparse_sym(n, edges, diag_syms, edge_syms):
    M = sp.zeros(n)
    for i in range(n):
        M[i, i] = diag_syms[i]
    for (i, j), s in zip(edges, edge_syms):
        M[i, j] = s
        M[j, i] = s
    return M

a,b,c,d,e,p,q,r,s,t = sp.symbols('a b c d e p q r s t')
diag = [a,b,c,d,e]
edges = [(0,1),(1,2),(2,3),(3,4),(0,4)]
esyms = [p,q,r,s,t]
M = sparse_sym(5, edges, diag, esyms)
print(M)
for di in range(5):
    for dj in range(di, 5):
        rr = [x for x in range(5) if x != di]
        cc = [x for x in range(5) if x != dj]
        v = sp.expand(M.extract(rr, cc).det())
        flag = "IDENTICALLY ZERO" if v == 0 else ""
        print(f"M_{di}{dj}: deg? terms={len(v.args) if hasattr(v,'args') else 1} {flag} :: {str(v)[:150]}")
