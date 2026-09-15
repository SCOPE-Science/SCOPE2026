"""Second C5 plane (different seed) to confirm irreducibility signal of section."""
import sympy as sp
import random

a,b,c,d,e,p,q,r,s,t = sp.symbols('a b c d e p q r s t')
vars10 = [a,b,c,d,e,p,q,r,s,t]
M = sp.Matrix([
 [a,p,0,0,t],
 [p,b,q,0,0],
 [0,q,c,r,0],
 [0,0,r,d,s],
 [t,0,0,s,e],
])
gens = []
for di in range(5):
    for dj in range(di,5):
        rr=[x for x in range(5) if x!=di]; cc=[x for x in range(5) if x!=dj]
        gens.append(sp.expand(M.extract(rr,cc).det()))

for seed in (7, 123):
    random.seed(seed)
    u,v,w = sp.symbols('u v w')
    plane = {}
    for i,V in enumerate(vars10):
        plane[V] = random.randint(-2,2)*u + random.randint(-2,2)*v + random.randint(-2,2)*w + random.randint(-2,2)
    sub = [sp.expand(g.subs(plane)) for g in gens]
    G = sp.groebner(sub, u, v, w, order='grlex')
    Glex = sp.groebner(list(G.polys), u, v, w, order='lex')
    uni = None
    for f in Glex.polys:
        e = f.as_expr()
        if e.free_symbols == {w}:
            uni = sp.Poly(e, w)
            break
    if uni is None:
        print(seed, ": no univariate found; lex len", len(Glex.polys))
        continue
    fac = sp.factor_list(uni.as_expr(), w)
    print(f"seed {seed}: uni deg {uni.degree()}, nfactors {len(fac[1])}, degs {sorted(sp.Poly(b,w).degree() for b,_ in fac[1])}")
