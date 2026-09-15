"""Factor the univariate section polynomial for C5: degree 20 in w.
If it splits with distinct factors -> analyze. Also count real roots."""
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
Glex = sp.groebner(list(G.polys), u, v, w, order='lex')
uni = None
for f in Glex.polys:
    e = f.as_expr()
    if e.free_symbols == {w}:
        uni = sp.Poly(e, w)
        break
print("uni deg:", uni.degree())
print("disc zero?", uni.discriminant() == 0)
fac = sp.factor_list(uni.as_expr(), w)
print("number of factors:", len(fac[1]))
for base, exp in fac[1]:
    print("  deg", sp.Poly(base, w).degree(), "mult", exp, "::", str(base)[:150])
