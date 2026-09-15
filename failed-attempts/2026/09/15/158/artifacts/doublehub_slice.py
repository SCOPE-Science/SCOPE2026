"""Section of double-hub V: random 3-plane in A^13, count degree; plus hunt for extra components
by examining V cap {c=d=e=0} (all-leaf-diagonal slice): restrict gens, compute GB/dim of slice.
If slice has unexpected dimension => extra component signal.
"""
import sympy as sp
import random

a,b,c,d,e = sp.symbols('a b c d e')
h = sp.symbols('h')
p1,p2,p3 = sp.symbols('p1 p2 p3')
q1,q2,q3 = sp.symbols('q1 q2 q3')
vars13 = [a,b,c,d,e,h,p1,p2,p3,q1,q2,q3]
M = sp.Matrix([
 [a,h,p1,p2,p3],
 [h,b,q1,q2,q3],
 [p1,q1,c,0,0],
 [p2,q2,0,d,0],
 [p3,q3,0,0,e],
])
gens = []
for di in range(5):
    for dj in range(di,5):
        rr=[x for x in range(5) if x!=di]; cc=[x for x in range(5) if x!=dj]
        gens.append(sp.expand(M.extract(rr,cc).det()))

# Slice c=d=e=0
sl = [sp.expand(g.subs({c:0,d:0,e:0})) for g in gens]
slnz = [f for f in sl if f != 0]
print(f"slice c=d=e=0: {len(slnz)} nonzero restricted polys")
for f in slnz:
    print("  deg", sp.Poly(f, *vars13).total_degree(), "::", str(f)[:200])
G = sp.groebner(slnz, b, a, h, p1, p2, p3, q1, q2, q3, order='lex')
print("slice lex GB len:", len(G.polys))
for f in G.polys:
    e_ = f.as_expr()
    print("  vars:", sorted(str(x) for x in e_.free_symbols), "deg", f.total_degree(), "::", str(e_)[:220])
