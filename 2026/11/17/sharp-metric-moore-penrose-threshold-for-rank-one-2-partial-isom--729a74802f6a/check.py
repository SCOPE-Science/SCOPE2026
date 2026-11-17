"""Exact symbolic checks for a rank-one 2-partial-isometry metric theorem.
Requires sympy (pip install sympy). The analytical proof is in RESULT.md.
"""
import sympy as sp
z = sp.symbols('z', positive=True, real=True)
c, s, a = sp.symbols('c s a', positive=True, real=True)
# Work in the real canonical basis; the phase normalization preserves T*S and S*T.
T = a*sp.Matrix([[c,0],[s,0]])
Tstar = T.T
S = 2*Tstar - Tstar*Tstar*T
P = S*T
Q = T*S
# The rank-one condition is z = a^2 and z^2*c^2-2*z+1=0, c^2+s^2=1.
def red(v):
    v = sp.expand(v).subs(a**2,z)
    v = sp.expand(v).subs(c**2,(2*z-1)/z**2)
    v = sp.expand(v).subs(s**2,(z-1)**2/z**2)
    return sp.factor(v)
# Keep normalizations symbolic using closed formulas.
P = sp.Matrix([[1,0],[0,0]])
Q = z*sp.Matrix([[c*c*(2-z),2*c*s],[c*s*(2-z),2*s*s]])
assert all(red(v)==0 for v in (Q*Q-Q))
assert red(Q.trace()-1)==0
assert red((P*Q).trace()-(2*z-1)*(2-z)/z)==0
G = sp.diag(1,2/(2-z))
assert sp.simplify(G*P-P.T*G) == sp.zeros(2)
assert sp.simplify(G*Q-Q.T*G) == sp.zeros(2)
for zz in [sp.Rational(1,2),sp.Rational(3,4),1,sp.Rational(3,2),sp.Rational(7,4)]:
    cc = sp.sqrt(2*zz-1)/zz
    ss = sp.Abs(zz-1)/zz
    TT=sp.sqrt(zz)*sp.Matrix([[cc,0],[ss,0]])
    SS=2*TT.T-TT.T*TT.T*TT
    beta=TT.T*TT.T*TT*TT-2*TT.T*TT+sp.eye(2)
    assert sp.simplify(TT*beta)==sp.zeros(2)
    assert sp.simplify(SS*TT-P)==sp.zeros(2)
    QQ=sp.simplify(TT*SS)
    assert sp.simplify(G.subs(z,zz)*QQ-QQ.T*G.subs(z,zz))==sp.zeros(2)
# Construct an exact counterexample with ||T||^2=3.
T0=sp.Matrix([[sp.sqrt(sp.Rational(5,3)),0],[sp.Rational(2,1)/sp.sqrt(3),0]])
S0=2*T0.T-T0.T*T0.T*T0
beta0=T0.T*T0.T*T0*T0-2*T0.T*T0+sp.eye(2)
Q0=sp.simplify(T0*S0)
assert sp.simplify(beta0-sp.diag(0,1))==sp.zeros(2)
assert sp.simplify(S0*T0-sp.diag(1,0))==sp.zeros(2)
assert sp.simplify(Q0-sp.Matrix([[-sp.Rational(5,3),4*sp.sqrt(5)/3],[-2*sp.sqrt(5)/3,sp.Rational(8,3)]]))==sp.zeros(2)
assert sp.simplify(Q0*Q0-Q0)==sp.zeros(2)
assert sp.simplify((sp.diag(1,0)*Q0).trace()+sp.Rational(5,3))==0
print('PASS: rank-one formulas, norm threshold, metric equations, and exact 2x2 counterexample')
