"""Reproduce the exact four-point monotone interpolation bounds."""
import sympy as S
x=S.symbols('x',real=True)
def tails(nodes):
    L=[S.prod((x-v)/(u-v) for v in nodes if v!=u) for u in nodes]
    return [S.factor(sum(L[k:])) for k in range(1,4)]
def extrema(p):
    candidates=[-S.Integer(1),S.Integer(1)]+[z for z in S.solve(S.diff(p,x),x) if z.is_real and abs(float(z))<=1]
    return [(z,S.simplify(p.subs(x,z))) for z in candidates]
nodes=[-S.Integer(1),-S.Rational(1,2),S.Rational(1,2),S.Integer(1)]
T=tails(nodes)
assert all(S.simplify(a-b)==0 for a,b in zip(T,[(x+1)*(4*x*x-8*x+7)/6,-(x+1)*(2*x-3)*(2*x+1)/6,(x+1)*(2*x-1)*(2*x+1)/6]))
delta=(10+7*S.sqrt(7))/162
z=-S.Rational(1,3)+S.sqrt(7)/6
assert S.simplify(T[2].subs(x,z)+delta)==0
assert S.simplify(T[0].subs(x,-z)-(1+delta))==0
for p in T:
    for r,v in extrema(p):
        assert float(v)>=-float(delta)-1e-12,(p,r,v,'minimum')
        assert float(v)<=1+float(delta)+1e-12,(p,r,v,'maximum')
U=tails([-S.Integer(1),-S.Rational(1,3),S.Rational(1,3),S.Integer(1)])
duni=13*S.sqrt(39)/108-S.Rational(1,2)
assert S.simplify(U[1].subs(x,-S.sqrt(39)/9)+duni)==0
for p in U:
    for r,v in extrema(p):
        assert float(v)>=-float(duni)-1e-12
        assert float(v)<=1+float(duni)+1e-12
assert float(duni)>float(delta)
print('PASS: all three monotone step interpolants, critical points, endpoints, both sharpness witnesses and equal-grid comparison.')
print('Chebyshev-Lobatto defect',S.simplify(delta),float(delta))
print('Equal-grid global defect',S.simplify(duni),float(duni))
