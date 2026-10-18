import sympy as sp

e = sp.symbols("e", positive=True)
A = sp.diag(1, 2, 4)
b = sp.Matrix([1, 1, e])

m = {j: sp.expand((b.T * (A**j) * b)[0]) for j in range(1, 5)}
assert m[1] == 3 + 4*e**2
assert m[2] == 5 + 16*e**2
assert m[3] == 9 + 64*e**2
assert m[4] == 17 + 256*e**2

G = sp.Matrix([[m[2], m[3]], [m[3], m[4]]])
rhs = sp.Matrix([m[1], m[2]])
delta = sp.factor(G.det())
assert sp.simplify(delta - 4*(1 + 100*e**2)) == 0
c0, c1 = map(sp.factor, G.inv()*rhs)
assert sp.simplify(c0 - 3*(1+62*e**2)/(2*(1+100*e**2))) == 0
assert sp.simplify(c1 + (1+34*e**2)/(2*(1+100*e**2))) == 0
x2 = sp.simplify(c0*b + c1*A*b)
expected = sp.Matrix([
    (1+76*e**2)/(1+100*e**2),
    (1+118*e**2)/(2*(1+100*e**2)),
    e*(50*e**2-1)/(2*(1+100*e**2)),
])
assert all(sp.simplify(x2[i]-expected[i]) == 0 for i in range(3))

w = {e: sp.Rational(1,10)}
assert [sp.simplify(z.subs(w)) for z in x2] == [sp.Rational(22,25), sp.Rational(109,200), -sp.Rational(1,80)]
assert list(A.inv()*sp.Matrix([1,1,sp.Rational(1,10)])) == [sp.Rational(1), sp.Rational(1,2), sp.Rational(1,40)]

# Irreducible SPD Stieltjes perturbation witness.
d = sp.Rational(1,20)
At = sp.Matrix([[1,-d,0],[-d,2,-d],[0,-d,4]])
bt = sp.Matrix([1,1,sp.Rational(1,10)])
assert At[0,0] > 0
assert At[:2,:2].det() == sp.Rational(799,400)
assert At.det() == sp.Rational(639,80)
assert At[0,1] < 0 and At[1,2] < 0
Ab = At*bt
A2b = At*Ab
Gt = sp.Matrix([[Ab.dot(Ab), Ab.dot(A2b)], [Ab.dot(A2b), A2b.dot(A2b)]])
rhst = sp.Matrix([Ab.dot(bt), A2b.dot(bt)])
ct = Gt.inv()*rhst
x2t = sp.simplify(ct[0]*bt + ct[1]*Ab)
assert x2t[2] == -sp.Rational(900492530,220852842849)
solt = At.inv()*bt
assert list(solt) == [sp.Rational(32791,31950), sp.Rational(1682,3195), sp.Rational(1009,31950)]
assert all(v > 0 for v in solt)
print("VERIFY_OK")
