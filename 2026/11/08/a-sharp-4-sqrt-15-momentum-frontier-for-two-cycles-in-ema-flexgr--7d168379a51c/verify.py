#!/usr/bin/env python3
"""Reproduce exact EMA moment-map cycle and Floquet polynomial identities.

Requires Python 3, SymPy, and NumPy. This is a finite symbolic/numerical
check of the displayed identities, not an independent proof of novelty.
"""
import math
import sympy as sp
import numpy as np

b, X, U, W = sp.symbols('b X U W', real=True)
z = sp.Symbol('z')
c = (1-b)/(1+b)
h = 2/c**2   # eta/a, where a = eta*c^2/2
S = b*U+(1-b)*X
V = b*W+(1-b)*X**2
# Branch maps near the two cycle points; sign(S) is fixed there.
Fplus = sp.Matrix([X-h*S**2/V, S, V])
Fminus = sp.Matrix([X+h*S**2/V, S, V])
plus = {X:1, U:-c, W:1}
minus = {X:-1, U:c, W:1}
assert all(sp.simplify(t) == 0 for t in (Fplus.subs(plus)-sp.Matrix([-1,c,1])))
assert all(sp.simplify(t) == 0 for t in (Fminus.subs(minus)-sp.Matrix([1,-c,1])))
Jp = sp.simplify(Fplus.jacobian([X,U,W]).subs(plus))
Jm = sp.simplify(Fminus.jacobian([X,U,W]).subs(minus))
Jexpected = sp.Matrix([[1-8*b,-4*b/c,2*b],[1-b,b,0],[2*(1-b),0,b]])
assert all(sp.simplify(v) == 0 for v in Jp-Jexpected)
T = sp.diag(-1,-1,1)
assert all(sp.simplify(v) == 0 for v in Jm-T*Jp*T)
P = Jm*Jp
p = sp.expand(P.charpoly(z).as_expr())
p_expected = z**3+(32*b-66*b*b-1)*z**2+(b**4-32*b**3+66*b*b)*z-b**4
assert sp.factor(p-p_expected)==0
assert sp.factor(p_expected.subs(z,1)-32*b*(1-b*b))==0
q=b*b-8*b+1
assert sp.factor(p_expected.subs(z,-1)+2*q*q)==0
A=1-b**8
B=(32*b-66*b*b-1)+b**4*(b**4-32*b**3+66*b*b)
C=(b**4-32*b**3+66*b*b)+b**4*(32*b-66*b*b-1)
Q=b**4+8*b**3-2*b*b+8*b+1
R=b**6+67*b**4-32*b**3+67*b*b+1
checks=[
    A-C-(1-b*b)*q*Q,
    A+C-(1-b*b)*R,
    A+B+C-(1+b**4)*32*b*(1-b*b),
    A-B+C-(1-b**4)*2*q*q,
]
assert all(sp.factor(expr)==0 for expr in checks)
bstar=4-sp.sqrt(15)
assert sp.simplify(q.subs(b,bstar))==0
assert sp.simplify(p_expected.subs(b,bstar)-(z+1)**2*(z-bstar**4))==0

# Finite-difference checks on the *unscaled physical map* at cycle points.
def physical_step(state,beta,kappa,eta):
    x,s,v = state
    sn=beta*s+(1-beta)*kappa*x
    vn=beta*v+(1-beta)*(kappa*x)**2
    return np.array([x-eta*abs(sn)*sn/vn,sn,vn])

for beta in (0.02,0.1,0.13,0.2,0.7):
    kappa,eta=3.0,0.7
    cc=(1-beta)/(1+beta)
    amp=eta*cc**2/2
    state=np.array([amp,-kappa*cc*amp,(kappa*amp)**2])
    neg=np.array([-amp,kappa*cc*amp,(kappa*amp)**2])
    assert np.max(np.abs(physical_step(state,beta,kappa,eta)-neg))<1.e-12
    assert np.max(np.abs(physical_step(neg,beta,kappa,eta)-state))<1.e-12
    # Componentwise finite differences on positive branch, respecting v>0.
    eps=1.e-7*min(1,amp*amp)
    J=np.column_stack([(physical_step(state+eps*np.eye(3)[j],beta,kappa,eta)-
                        physical_step(state-eps*np.eye(3)[j],beta,kappa,eta))/(2*eps)
                       for j in range(3)])
    D=np.diag([amp,kappa*amp,(kappa*amp)**2])
    Jscaled=np.linalg.inv(D)@J@D
    Jsym=np.array(Jp.subs(b,beta).evalf(),dtype=float)
    assert np.max(np.abs(Jscaled-Jsym))<3.e-6, (beta,Jscaled,Jsym)
    mat=np.array(P.subs(b,beta).evalf(),dtype=float)
    rho=max(abs(np.linalg.eigvals(mat)))
    assert (rho<1)==(beta<float(bstar))

# A demonstration, not a global basin theorem: canonical zero-memory start.
for beta in (0.02,0.1):
    x,s,v=1.0,0.0,0.0
    for _ in range(5000):
        x,s,v=physical_step((x,s,v),beta,1.0,0.6)
    target=0.3*((1-beta)/(1+beta))**2
    assert abs(abs(x)-target)<1.e-6
print('VERIFY_OK')
print('beta_critical',float(bstar))
print('cycle_polynomial',p_expected)
