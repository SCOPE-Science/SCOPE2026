import sympy as sp

v1,v2,v3,v4 = sp.symbols('v1 v2 v3 v4')
t,a,b,c = sp.symbols('t a b c')
A = (v1-v4)*(v2-v3)
B = (v1-v3)*(v2-v4)
D = sp.expand(A*(t-(t+b))*((t+a)-(t+c)) - B*(t-(t+c))*((t+a)-(t+b)))
q = sp.expand(D)
assert t not in q.free_symbols
assert sp.Poly(q,a,b,c).total_degree() == 2
H = sp.hessian(q,(a,b,c))
vand = (v1-v2)*(v1-v3)*(v1-v4)*(v2-v3)*(v2-v4)*(v3-v4)
assert sp.factor(H.det() - 2*vand) == 0

q0 = sp.expand(q.subs({v1:0,v2:1,v3:2,v4:3}))
assert sp.factor(q0 - (-3*a*b + 4*a*c - b*c)) == 0
H0 = sp.hessian(q0,(a,b,c))
assert H0.det() == 24

# Blow-up charts of A^3_{a,b,c} at the origin.  The strict transform of q0=0
# is obtained after dividing by the square of the exceptional coordinate.
u,w = sp.symbols('u w')
charts = [
    sp.expand(q0.subs({a:1,b:u,c:w})),
    sp.expand(q0.subs({a:u,b:1,c:w})),
    sp.expand(q0.subs({a:u,b:w,c:1})),
]
expected = [
    (-3*u + 4*w - u*w, {u:4,w:-3}, -12),
    (-3*u + 4*u*w - w, {u:sp.Rational(1,4),w:sp.Rational(3,4)}, -sp.Rational(3,4)),
    (-3*u*w + 4*u - w, {u:-sp.Rational(1,3),w:sp.Rational(4,3)}, -sp.Rational(4,3)),
]
for g,(ge,crit,val) in zip(charts, expected):
    assert sp.expand(g-ge)==0
    sol = sp.solve([sp.diff(g,u),sp.diff(g,w)],[u,w], dict=True)
    assert sol == [crit]
    assert sp.simplify(g.subs(crit)-val)==0
    assert val != 0

print('NORMAL_QUADRATIC=', sp.factor(q))
print('HESSIAN_DET=', sp.factor(H.det()))
print('NORMALIZED_QUADRATIC=', q0)
print('BLOWUP_CHARTS=', charts)
print('VERIFY_OK')
