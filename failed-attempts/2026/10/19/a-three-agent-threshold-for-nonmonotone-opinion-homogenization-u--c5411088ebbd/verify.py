"""Reproduce exact identities for a three-node predictive-loop opinion model.

Run: python verify.py. Requires SymPy 1.12 or newer.
"""
import sympy as s

b,z,a,c=s.symbols('b z a c', real=True)
P=(s.ones(3)+3*s.eye(3))/6
B=s.diag(b,z,0)
s0=s.Matrix([1,0,0])
D=12-8*b-8*z+5*b*z
claimed_y=(1-b)*s.Matrix([8-5*z,2,2-z])/D
assert all(s.factor(v)==0 for v in (s.eye(3)-P*B)*claimed_y-P*(s.eye(3)-B)*s0)
variance=s.factor((claimed_y.dot(claimed_y)-(sum(claimed_y)**2)/3)/3)
claimed_v=2*(1-b)**2*(7*z*z-18*z+12)/(3*D**2)
assert s.factor(variance-claimed_v)==0
claimed_derivative=-4*(1-b)**2*((11*b-12)*z+12*(1-b))/(3*D**3)
assert s.factor(s.diff(variance,z)-claimed_derivative)==0
root=12*(1-b)/(12-11*b)
minimum=(1-b)**2/(2*(7*b*b-18*b+12))
assert s.factor(variance.subs(z,root)-minimum)==0
assert s.factor(variance.subs(z,1)-minimum-b*b*(1-b)**2/(6*(3*b-4)**2*(7*b*b-18*b+12)))==0
assert s.factor(variance.subs(z,0)-minimum-3*(1-b)**4/(2*(2*b-3)**2*(7*b*b-18*b+12)))==0
bb=s.Rational(3,4)
zz=s.Rational(4,5)
assert claimed_y.subs({b:bb,z:zz})==s.Matrix([s.Rational(5,13),s.Rational(5,26),s.Rational(3,26)])
assert variance.subs({b:bb,z:zz})==s.Rational(1,78)
assert variance.subs({b:bb,z:1})==s.Rational(2,147)
assert s.factor(variance.subs({b:bb,z:1})-variance.subs({b:bb,z:zz}))==s.Rational(1,1274)
# For two nodes, the difference transfer coefficient is monotone in both susceptibilities.
P2=s.Matrix([[1-a,a],[a,1-a]])
B2=s.diag(b,c)
x1,x2=s.symbols('x1 x2',real=True)
y2=(s.eye(2)-P2*B2).inv()*P2*(s.eye(2)-B2)*s.Matrix([x1,x2])
det=(1-b)*(1-c)+a*(b+c-2*b*c)
F=(1-2*a)*(1-b)*(1-c)/det
assert s.factor((y2[0]-y2[1])-F*(x1-x2))==0
# Exact finite regression points. Their role is error detection, not a proof of a continuum theorem.
for bb in (s.Rational(1,10),s.Rational(1,3),s.Rational(1,2),s.Rational(3,4),s.Rational(9,10)):
    zstar=root.subs(b,bb)
    assert 0<zstar<1
    for zz in (s.Rational(0),zstar/2,zstar,(1+zstar)/2,s.Rational(1)):
        DD=D.subs({b:bb,z:zz})
        assert DD>0
        yy=claimed_y.subs({b:bb,z:zz})
        assert all(0<=val<=1 for val in yy)
        assert s.factor((s.eye(3)-P*B.subs({b:bb,z:zz}))*yy-P*(s.eye(3)-B.subs({b:bb,z:zz}))*s0)==s.zeros(3,1)
        slope=claimed_derivative.subs({b:bb,z:zz})
        if zz<zstar: assert slope<0
        elif zz>zstar: assert slope>0
        else: assert slope==0
print('PASS: fixed points, variance, global optimum, endpoint gaps, two-node transfer, exact examples.')
