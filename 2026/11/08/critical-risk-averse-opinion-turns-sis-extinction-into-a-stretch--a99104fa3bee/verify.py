"""Exact local coefficients and numerical diagnostics for a coupled opinion--SIS model.

The proof of globality, asymptotic integration, and novelty is in RESULT.md;
the numerical experiments here are diagnostics only.
"""
from fractions import Fraction
import math
import sympy as sp
from scipy.integrate import solve_ivp

p,y,kp,kx=sp.symbols('p y kp kx',real=True)
F=sp.tanh((1+kp*p+kx*y*y)*y)-y
series=sp.series(F.subs(p,0),y,0,8).removeO().expand()
c=sp.Rational(1,3)-kx
d=sp.Rational(2,15)-kx
assert sp.simplify(series.coeff(y,3)+c)==0
assert sp.simplify(series.coeff(y,5)-d)==0
assert sp.simplify(sp.diff(F,p).subs({p:0,y:0}))==0
assert sp.simplify(sp.series(sp.diff(F,p).subs(p,0),y,0,4).removeO().coeff(y,1)-kp)==0

cases = [sp.Rational(1,6),sp.Rational(1,10),sp.Rational(1,5)]
assert -(sp.Rational(2,15)-sp.Rational(1,10))/(sp.Rational(1,3)-sp.Rational(1,10))<0
assert -(sp.Rational(2,15)-sp.Rational(1,5))/(sp.Rational(1,3)-sp.Rational(1,5))>0
for k in cases:
    assert sp.Rational(1,3)-k>0
    A=2*(sp.Rational(1,3)-k)
    Q=-(sp.Rational(2,15)-k)/(sp.Rational(1,3)-k)
    assert sp.simplify(Q+ d.subs(kx,k)/c.subs(kx,k))==0

# Exact test case and distinct neutral initial-opinion boundary.
b=sp.Rational(1,2)
tau=sp.Integer(1)
kk=sp.Rational(1,6)
assert sp.simplify(2*(sp.Rational(1,3)-kk)/tau-sp.Rational(1,3))==0
assert sp.simplify(-((sp.Rational(2,15)-kk)/(sp.Rational(1,3)-kk))-sp.Rational(1,5))==0
assert sp.simplify(b*sp.sqrt(2*tau/(sp.Rational(1,3)-kk))-sp.sqrt(3))==0

# Time-transformed integration in log p avoids underflow, and E(t) measures
# the finite logarithmic prefactor directly.
bb=0.5
kpp=0.5
kxx=1/6
ta=1.0
C=(1/3-kxx)
A=2*C/ta
Q=-(2/15-kxx)/C
B=bb*math.sqrt(2*ta/C)

def rhs(t,Y):
    y,logp=Y
    pp=math.exp(logp) if logp > -730 else 0.0
    yp=(math.tanh((1+kpp*pp+kxx*y*y)*y)-y)/ta
    lp=-bb*(y+(1-y)*pp)
    return [yp,lp]

check_times=[100,400,1600,6400,25600,40000]
r=solve_ivp(rhs,(0,max(check_times)),[0.6,math.log(0.4)],t_eval=check_times,rtol=2e-11,atol=2e-13,max_step=3.0)
assert r.success,r.message
vals=[]
for t,(yy,ll) in zip(check_times,r.y.T):
    w=1/(yy*yy)
    K=w-A*t-Q*math.log(t)
    H=ll+B*math.sqrt(t)
    vals.append((t,yy,ll,K,H))
assert abs(vals[-1][3]-vals[-2][3])<0.01,(vals[-2],vals[-1])
assert abs(vals[-1][4]-vals[-2][4])<0.01,(vals[-2],vals[-1])
assert vals[-1][2] < -300
print('VERIFY_OK')
print('Taylor: -c*y^3 + d*y^5; c=1/3-kx, d=2/15-kx')
print('Example: A=1/3, Q=1/5, B=sqrt(3)')
for line in vals:
    print('t=%d y=%.10g logp=%.10g K_approx=%.9f logP_approx=%.9f'%line)
