"""Exact symbolic checks for payoff-feedback scheduling."""
import sympy as s
x=s.symbols('x',real=True)
R,S,T,P=s.symbols('R S T P',real=True)
U=(1-x)*s.Matrix([[T,P],[R,S]])+x*s.Matrix([[R,S],[T,P]])
pi=U*s.Matrix([x,1-x]); diff=s.factor(pi[0]-pi[1]);
expected=(2*x-1)*((S-P)+x*(R-T-S+P))
assert s.simplify(diff-expected)==0,(diff,expected)
g=x*(1-x)*(2*x-1)
a,b,c,d=s.symbols('a b c d')
f=g*(a+b*x); h=g*(c+d*x)
assert s.expand(f*s.diff(h,x)-h*s.diff(f,x)-g**2*(a*d-b*c))==0
# Witness two stage payoffs: B, R and baseline G in (R,S,T,P) convention
payoffs={'B':(s.Integer(2),s.Integer(2),s.Integer(1),s.Integer(1)),
         'E':(s.Integer(1),s.Integer(10),s.Integer(4),s.Integer(1)),
         'G':(s.Rational(9,8),s.Rational(1,8),s.Integer(1),s.Integer(1))}
targets={'B':(1,0),'E':(9,-12),'G':(s.Rational(-7,8),1)}
for name,p in payoffs.items():
 r,ss,t,pp=p
 A,B=ss-pp,r-t-ss+pp
 assert (A,B)==targets[name],(name,A,B)
assert s.factor(g.subs(x,s.Rational(3,4)))==s.Rational(3,32)
assert s.Rational(3,4)*s.Rational(1,8)*s.Rational(1,2)==s.Rational(3,64)
assert s.Rational(7,8)*s.Rational(3,4)*s.Rational(1,8)==s.Rational(21,256)
assert 12*s.Rational(21,256)*8==s.Rational(63,8)
assert 8-s.Rational(63,8)==s.Rational(1,8)
# Numerical sanity check, not used as infinite/analytical proof
from scipy.integrate import solve_ivp
def flow(init, A, B, t=8):
 sol=solve_ivp(lambda time,Y: [float(Y[0]*(1-Y[0])*(2*Y[0]-1)*(A+B*Y[0]))],(0,t),[init],rtol=1e-12,atol=1e-14)
 assert sol.success
 return sol.y[0,-1]
zB=flow(.75,1,0); zBE=flow(zB,9,-12)
zE=flow(.75,9,-12); zEB=flow(zE,1,0)
assert zE==.75 and .75<zBE<.875<zEB<1
print('symbolic identities PASS; exact rational witnesses PASS')
print('illustrative (not proof) B then E',zBE,'E then B',zEB)
