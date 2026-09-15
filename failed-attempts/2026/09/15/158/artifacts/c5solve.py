"""Solve the C5 3-plane section: GB in 3 vars, count solutions via lex elimination + univariate root isolation."""
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

random.seed(42)
u,v,w = sp.symbols('u v w')
plane = {}
for i,V in enumerate(vars10):
    plane[V] = random.randint(-2,2)*u + random.randint(-2,2)*v + random.randint(-2,2)*w + random.randint(-2,2)
sub = [sp.expand(g.subs(plane)) for g in gens]
G = sp.groebner(sub, u, v, w, order='grlex')
print("grlex len:", len(G.polys))
degs = sorted(f.total_degree() for f in G.polys)
print("degs:", degs)
Glex = sp.groebner(list(G.polys), u, v, w, order='lex')
print("lex len:", len(Glex.polys))
for f in Glex.polys:
    e = f.as_expr()
    print("vars:", sorted(str(x) for x in e.free_symbols), "deg:", f.total_degree(), "::", str(e)[:250])
