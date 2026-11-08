"""Exact-arithmetic checks for the two-class synergistic-SIS onset theorem.

Run: python verify.py    (requires sympy)
"""
import sympy as S

z = S.symbols('z', real=True)
a = (1 - 4*z*z) / ((1-z)*(1+4*z))
b = 1-a
p = 20*(1+z)/(1+4*z)
lam = 1/p
astar = (1+4*z)*(1+4*z**3)/((1+z)*(19+64*z**3))
B = (1+z)*(19+64*z**3)/((1+4*z)*(1+4*z*z))
C = -(16384*z**10+8192*z**7+6016*z**6+964*z**4+2888*z**3+361) / ((1+4*z*z)*(19+64*z**3)**2)
P = S.Matrix([[a,b],[b,a]])
K = S.diag(20,5)*P
v = S.Matrix([1,z]); u = S.Matrix([1,4*z]); L = -S.eye(2)+lam*K
assert S.simplify(K*v-p*v)==S.zeros(2,1)
assert S.simplify(K.T*u-p*u)==S.zeros(2,1)
assert S.simplify(-S.trace(L)-3*(1+4*z*z)/(4*(1-z*z)))==0

alpha=S.symbols('alpha',real=True)
m=P*v
Q=S.Matrix([lam*k*(alpha*(k-1)*m[i]**2-v[i]*m[i]) for i,k in enumerate((20,5))])
qproj=S.factor((u.dot(Q))/(u.dot(v)))
assert S.simplify(qproj-B*(alpha-astar))==0
Qc=Q.subs(alpha,astar)
kappa=-S.trace(L)
w=S.simplify(Qc/kappa)
assert S.simplify(u.dot(w))==0
assert S.simplify(L*w+Qc)==S.zeros(2,1)
mw=P*w
cross=S.Matrix([lam*k*(2*astar*(k-1)*m[i]*mw[i]-v[i]*mw[i]-w[i]*m[i]) for i,k in enumerate((20,5))])
cubic=S.Matrix([-lam*k*astar*(k-1)*v[i]*m[i]**2 for i,k in enumerate((20,5))])
assert S.simplify((u.dot(cross+cubic))/(u.dot(v))-C)==0
assert S.factor(S.diff(a,z)+3*(1+4*z*z)/((1-z)**2*(1+4*z)**2))==0
alpha_derivative=3*(256*z**6+48*z**4+200*z**3+12*z*z+19)/((1+z)**2*(19+64*z**3)**2)
assert S.simplify(S.diff(astar,z)-alpha_derivative)==0
assert S.simplify(astar.subs(z,0)-S.Rational(1,19))==0
assert S.simplify(astar.subs(z,S.Rational(1,2))-S.Rational(1,9))==0
assert S.simplify(astar.subs(z,S.Rational(1,4))-S.Rational(17,200))==0
assert S.simplify(C.subs(z,S.Rational(1,4))+S.Rational(659,800))==0
assert S.simplify(B.subs(z,S.Rational(1,4))-10)==0
assert S.simplify(lam.subs(z,S.Rational(1,4))-S.Rational(2,25))==0
print('VERIFY_OK')
