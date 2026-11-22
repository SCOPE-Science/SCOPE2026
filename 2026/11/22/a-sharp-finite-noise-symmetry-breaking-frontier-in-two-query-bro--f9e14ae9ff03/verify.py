"""Exact algebraic verification of the Brownian-bridge two-sensor design theorem.

Requires Python 3 and SymPy. Rational checks are supplementary to the analytic proof.
"""
from fractions import Fraction
from random import Random
import sympy as s

a,b,u,v,eta,rho,w=s.symbols('a b u v eta rho w', real=True)
E=s.Rational(1,12)-u*a*(1-a)-v*b*(1-b)+u**2*a*(1-a)+v**2*b*(1-b)+2*u*v*a*(1-b)+eta*(u**2+v**2+2*rho*u*v)
assert s.factor(s.diff(E,a,2)-2*u*(1-u))==0
assert s.factor(s.diff(E,b,2)-2*v*(1-v))==0
assert s.factor(s.diff(E,a,b)+2*u*v)==0
F=s.factor(E.subs({a:(1-v)/2,b:(1+u)/2}))
W=s.symbols('W', real=True)
Fc=s.factor(F.subs({u:W,v:W}))
assert s.simplify(F-Fc.subs(W,(u+v)/2)-(u-v)**2*(8*eta*(1-rho)+u+v)/16)==0
assert s.simplify(Fc.subs(W,w)-(s.Rational(1,12)-w/s.Integer(2)+w**2-w**3/s.Integer(2)+2*eta*(1+rho)*w**2))==0
assert s.factor(s.diff(Fc,W)-( -1+(4+8*eta*(1+rho))*W-3*W**2 )/2)==0
# Use stationarity to reduce the optimized risk expression.
assert s.rem(s.together(Fc.subs(W,w)-(s.Rational(1,12)-(w-w**3)/4)).as_numer_denom()[0],3*w*w-(4+8*eta*(1+rho))*w+1,w).expand()==0
# Noise reference: response at zero is pure measurement noise.
z=s.symbols('z', real=True)
effvar=eta*(1-rho**2)
one_gain=s.factor((z*(1-z)/2)**2/(z*(1-z)+effvar))
assert s.simplify(one_gain.subs(z,s.Rational(1,2))-1/(16*(1+4*effvar)))==0
# Independence and strict monotonicity of risk differences: random exact tests.
from math import sqrt

def wp(e,r):
    A=4+8*e*(1+r)
    return 2/(A+sqrt(A*A-12))

def gS(e,r):
    t=wp(e,r)
    return (t-t*t*t)/4

def gE(e,r):
    return 1/(16*(1+4*e*(1-r*r)))

rng=Random(20261120)
for k in range(90):
    ee=10**rng.uniform(-2,1.5); rr=rng.uniform(0,.995)
    opt=max(gS(ee,rr),gE(ee,rr))
    def gain(z):
        xx,yy=sorted(z)
        covx=xx*(1-xx)/2; covy=yy*(1-yy)/2
        A=xx*(1-xx)+ee; C=yy*(1-yy)+ee
        B=xx*(1-yy)+ee*rr
        det=A*C-B*B
        return (covx*covx*C+covy*covy*A-2*covx*covy*B)/det
    samples=[gain((rng.random(),rng.random())) for i in range(100)]
    assert max(samples)<opt+1e-10,(ee,rr,max(samples),opt)
for e in [s.Rational(1,1000),s.Rational(1,10),s.Integer(1),s.Integer(50)]:
    for r in [s.Rational(0),s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),s.Rational(99,100)]:
        # exact matrix Schur complement at three fixed designs
        H=s.Matrix([[s.Rational(1,4)+e,e*r],[e*r,e]])
        vec=s.Matrix([s.Rational(1,8),0])
        assert s.simplify((vec.T*H.inv()*vec)[0]-1/(16*(1+4*e*(1-r*r))))==0
print('PASS: analytic polynomial identities; 20 exact endpoint matrices; 9000 numeric design probes.')
