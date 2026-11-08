"""Exact symbolic checks for Hopf criticality in the two-variable epidemic–opinion reduction.

Requires Python 3 and sympy. Run: python CHECK.py
These checks support an analytic proof; testing alone is not a proof of a Hopf theorem.
"""
import sympy as sp

x, y, q, d0, d1 = sp.symbols('x y q d0 d1', real=True)
s, w = sp.symbols('s w', positive=True)
F = x*(-d0-d1*y+q*x*(1-x))
G = x-y
z = sp.Matrix([F,G]); coords = (x,y)
J = z.jacobian(coords)
g = -d0-d1*s+q*s*(1-s)
qH = 1/(s*(1-2*s))
d1H = (1+w**2)/s
d0H = s/(1-2*s)-w**2
subH = {x:s,y:s,q:qH,d0:d0H,d1:d1H}
assert sp.simplify(g.subs({q:qH,d0:d0H,d1:d1H})) == 0
JH = sp.simplify(J.subs(subH))
assert JH == sp.Matrix([[1,-(1+w**2)],[1,-1]])
assert sp.simplify(JH.trace())==0
assert sp.simplify(JH.det()-w**2)==0

# The exact nonlinear normal form in real canonical coordinates.
X,Y=sp.symbols('X Y', real=True)
xnew = s+X
ynew = s+(X+w*Y)/(1+w**2)
Fx = sp.expand(F.subs({x:xnew,y:ynew,q:qH,d0:d0H,d1:d1H}))
nonlinear = -qH*s*X**2-(w/s)*X*Y-qH*X**3
assert sp.simplify(Fx-(-w*Y+nonlinear)) == 0
Gy = sp.expand((d1H*s*G.subs({x:xnew,y:ynew})-Fx)/w)
assert sp.simplify(Gy-(w*X-nonlinear/w)) == 0

f=nonlinear
h=-nonlinear/w
# The usual planar first Lyapunov coefficient for X'=-wY+f, Y'=wX+h.
D=lambda z,i,j=0,k=0:sp.diff(z,X,i,Y,j)
fxx=D(f,2); fxy=D(f,1,1); fyy=D(f,0,2)
hxx=D(h,2); hxy=D(h,1,1); hyy=D(h,0,2)
fxxx=D(f,3); fxyy=D(f,1,2); hxxy=D(h,2,1); hyyy=D(h,0,3)
zero={X:0,Y:0}
l1=sp.factor(((fxxx+fxyy+hxxy+hyyy)/16+
 (fxy*(fxx+fyy)-hxy*(hxx+hyy)-fxx*hxx+fyy*hyy)/(16*w)).subs(zero))
expected=(4*s-1-2*(1-2*s)*w**2)/(8*s*(1-2*s)**2*w**2)
assert sp.simplify(l1-expected)==0

# Equilibrium branch and speed at which the real parts cross zero when q varies.
T=s*q*(1-2*s)-1
gs=sp.diff(g,s)
sg=-sp.diff(g,q)/gs
Tprime=sp.factor(sp.diff(T,q)+sp.diff(T,s)*sg)
expected_T=s*(1-2*s)+s*(1-s)*(1-4*s)/((1-2*s)*w**2)
assert sp.simplify(Tprime.subs({q:qH,d1:d1H})-expected_T)==0

cases=[
    (sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1,4),sp.Integer(5),sp.Integer(8),sp.Integer(-2),sp.Rational(1,8)),
    (sp.Rational(1,3),sp.Rational(1,2),sp.Rational(3,4),sp.Rational(15,4),sp.Integer(9),sp.Rational(9,4),-sp.Rational(7,9)),
]
for S,W,D0,D1,Q,L1,TP in cases:
    h={s:S,w:W}
    assert sp.simplify(d0H.subs(h)-D0)==0
    assert sp.simplify(d1H.subs(h)-D1)==0
    assert sp.simplify(qH.subs(h)-Q)==0
    assert sp.simplify(l1.subs(h)-L1)==0
    assert sp.simplify(expected_T.subs(h)-TP)==0
    lower=sp.simplify(S-(1-2*S)*W**2)
    assert 0 < lower < S < sp.Rational(1,2)
    assert sp.simplify(g.subs({q:Q,d0:D0,d1:D1}) + Q*(s-lower)*(s-S))==0
    assert D0 > 0 and D1 > 0 and Q > 0

# The first Lyapunov coefficient passes through zero in the admissible domain.
s0=sp.Rational(1,3)
w0=sp.sqrt(sp.Rational(1,2))
assert sp.simplify(l1.subs({s:s0,w:w0}))==0
assert d0H.subs({s:s0,w:w0})>0
print('PASS: equilibrium, Jacobian, canonical normal form, first Lyapunov coefficient,')
print('      two opposite-criticality rational witnesses, transversality,')
print('      endemic root ordering, and admissible sign-change point.')
