"""Exact rational certificate for a sextic's four-point singular basket.
Run: python3 verify.py   (requires SymPy >= 1.12).
All claims about general parameters use algebraic openness, not finite sampling.
"""
from itertools import product
import sympy as S

x,y,z = S.symbols('x y z')
vars_ = (x,y,z)
base = [
    (1,0,0),(-1,1,0),(0,1,0),(1,1,0),
    (-1,-1,1),(1,-1,1),(-1,1,1),(1,1,1),
    (0,-1,1),(-1,0,1),(0,0,1),(1,0,1),(0,1,1)
]
Q = (-31,-9,15)
monomials = [x**i*y**j*z**(6-i-j) for i in range(7) for j in range(7-i)]
assert len(monomials)==28

def local_jets(p,m):
    chart = next(i for i in range(3) if p[i])
    free = [vars_[i] for i in range(3) if i!=chart]
    sub = dict(zip(vars_,p))
    for d in range(m):
        for a in range(d+1):
            b=d-a
            yield [S.diff(t,free[0],a,free[1],b).subs(sub) for t in monomials]

rows = []
for i,p in enumerate(base):
    rows.extend(local_jets(p,2 if i in (0,2,10) else 1))
rows.extend(local_jets(Q,4))
M=S.Matrix(rows)
assert M.shape==(29,28) and M.rank()==27
kernel=M.nullspace()
assert len(kernel)==1
v=kernel[0]; d=S.ilcm(*[a.q for a in v]); c=[int(a*d) for a in v]
g=S.igcd(*c); c=[a//g for a in c]
F=S.expand(sum(a*t for a,t in zip(c,monomials)))
assert S.Poly(F,x,y,z).total_degree()==6
assert all(sum(a*b for a,b in zip(row,c))==0 for row in rows)
# The entire singular support is calculated by an exact Groebner basis.
f=S.expand(F.subs(z,1)); gx=S.diff(f,x); gy=S.diff(f,y)
G=S.groebner([f,gx,gy],x,y,order='lex',domain=S.QQ)
last=G.polys[-1].as_expr()
assert S.simplify(last - y*(5*y+3)**5/S.Integer(3125))==0
for value, expected in [(S.Integer(0),x),(S.Rational(-3,5),15*x+31)]:
    polys=[S.Poly(h.as_expr().subs(y,value),x) for h in G.polys]
    common=polys[0]
    for h in polys[1:]:common=S.gcd(common,h)
    assert common.degree()==(1 if value==0 else 3)
    assert S.factor(common.as_expr()/expected**common.degree()).is_Number
# At infinity the only singular points are (1:0:0) and (0:1:0).
assert S.factor(F.subs(z,0))==50625*x**2*y**2*(x-y)*(x+y)
for point in ((1,1,0),(1,-1,0)):
    assert any(S.diff(F,t).subs(dict(zip(vars_,point)))!=0 for t in vars_)
# The three quadratic tangent cones and the quartic tangent cone are squarefree.
P=(1,0,0),(0,1,0),(0,0,1),Q
multiplicities=(2,2,2,4)
t=S.symbols('t')
for point, expected in zip(P,multiplicities):
    chart=next(i for i in range(3) if point[i]); free=[vars_[i] for i in range(3) if i!=chart]
    U,V=S.symbols('U V')
    sub={vars_[chart]:point[chart]}
    for coordinate,sym in zip(free,(U,V)):
        sub[coordinate]=point[vars_.index(coordinate)]+sym
    loc=S.Poly(S.expand(F.subs(sub)),U,V)
    order=min(sum(exp) for exp, coeff in loc.terms() if coeff)
    assert order==expected
    tangent=sum(coeff*U**exp[0]*V**exp[1] for exp,coeff in loc.terms() if sum(exp)==order)
    poly=S.Poly(tangent.subs({U:t,V:1}),t)
    assert poly.degree()==expected
    assert S.discriminant(poly.as_expr(),t)!=0
# No line component is possible: a line must pass through Q and one
# of the four points of F\cap\{z=0\}.
for L,var in [(5*y+3*z,y),(15*x+31*z,x),(15*x-15*y+22*z,x),(3*x+3*y+8*z,x)]:
    poly=S.Poly(L,var)
    replacement=S.solve(L,var)[0]
    assert S.expand(F.subs(var,replacement))!=0
print('PASS: unique sextic, four singular support points, three ordinary nodes,')
print('ordinary quadruple point, no linear factor; geometric genus one.')
print('Degree 6, singular delta 3*1+6=9, genus 10-9=1, dual degree 30-6-12=12.')
