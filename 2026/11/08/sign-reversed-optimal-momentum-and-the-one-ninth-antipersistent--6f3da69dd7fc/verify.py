"""Exact symbolic checks for a scalar heavy-ball recursion driven by AR(1) noise.

Run: python verify.py
Requires Python 3.9+ and SymPy 1.10+.
"""
import sympy as sp

b, q, c, t = sp.symbols('b q c t', real=True)
M = sp.Matrix([[b, -b, -q], [1, 0, 0], [0, 0, q]])
B = sp.Matrix([-1, 0, 1])
ss = sp.symbols('s0:6')
S = sp.Matrix([[ss[0], ss[1], ss[2]],
               [ss[1], ss[3], ss[4]],
               [ss[2], ss[4], ss[5]]])
res = S - M*S*M.T - B*B.T
positions = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
sol = sp.solve([res[i,j] for i,j in positions], ss, dict=True)
assert len(sol) == 1
variance = sp.factor(sol[0][ss[0]])
N = 1+b+b*q-b*q**2-b**2*q-b**2*q**2
D = (1-b)*(1+2*b)*(1-q**2)*(1+b*q**2-b*q)
assert sp.cancel(variance-N/D) == 0
R = sp.cancel((1-q**2)*variance)
E = q*b*(b-1)-b-q
D0 = (1-b)*(1+2*b)*(1+b*q**2-b*q)
assert sp.cancel(R-1+2*b*(1-q)*E/D0) == 0
D1 = (1-b)*(1+2*b)**2*(1+b*q**2-b*q)
extra = 2*b*(1+q)*(2+b-q*(b**2+b+1))/D1
assert sp.cancel(R-1/(1+2*b)**2-extra) == 0
assert sp.cancel(sp.diff(R,b).subs(b,0)-2*q*(1-q)) == 0
assert sp.factor(R.subs(q,-1)-1/(1+2*b)**2) == 0
z = sp.cancel(R.subs({q:-1+t*t,b:1-c*t}))
assert sp.simplify(sp.limit(z,t,0)-sp.Rational(1,9)) == 0
linear = sp.limit((z-sp.Rational(1,9))/t,t,0)
assert sp.simplify(linear-(4*c/sp.Integer(27)+4/(9*c))) == 0
assert sp.simplify(linear.subs(c,sp.sqrt(3))-8*sp.sqrt(3)/27) == 0
for qq,bb,expected in [(sp.Rational(-1,2),sp.Rational(1,4),sp.Rational(184,171)),
                       (sp.Rational(1,2),sp.Rational(-1,4),sp.Rational(328,255)),
                       (sp.Rational(-1,2),sp.Integer(0),sp.Rational(4,3))]:
    assert variance.subs({q:qq,b:bb}) == expected
    P = S.subs(sol[0]).subs({q:qq,b:bb})
    Mm = M.subs({q:qq,b:bb})
    assert P == Mm*P*Mm.T+B*B.T
print('PASS: symbolic Lyapunov identity, two rational factorizations, derivative, critical expansion, exact examples')
