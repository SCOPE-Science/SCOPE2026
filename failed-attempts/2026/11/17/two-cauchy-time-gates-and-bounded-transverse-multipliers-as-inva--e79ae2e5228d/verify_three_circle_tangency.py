"""Symbolic identities and finite asymptotic checks for three invariant circles."""
from fractions import Fraction
from math import pi,sqrt,atan
import sympy as s
from scipy.integrate import quad
import math
x,y,e=s.symbols('x y e', real=True)
r=(1-e)/2
q=s.Rational(1,10)
u,v=0,2
lam,mu,k=-4,-3,1
f1=x*x+y*y-r*r
f2=(x-1)**2+y*y-r*r
f3=x*x+(y-v)**2-q*q
A1=-lam-mu+k*(-v*x+(u-1)*y-v)
A2=lam+k*(v*x-u*y)
A3=mu+k*y
P=-y*A1*f2*f3-y*A2*f1*f3-(y-v)*A3*f1*f2
Q=x*A1*f2*f3+(x-1)*A2*f1*f3+(x-u)*A3*f1*f2
P=s.Poly(P,x,y).as_expr().expand()
Q=s.Poly(Q,x,y).as_expr().expand()
assert s.Poly(P,x,y).total_degree()==4
assert s.Poly(Q,x,y).total_degree()==4
K1=-2*y*A2*f3+2*(v*x-u*y)*A3*f2
K2=2*y*A1*f3+2*(v*(x-1)+(1-u)*y)*A3*f1
assert s.expand(s.diff(f1,x)*P+s.diff(f1,y)*Q-K1*f1)==0
assert s.expand(s.diff(f2,x)*P+s.diff(f2,y)*Q-K2*f2)==0
assert s.rem(s.Poly(s.diff(f3,x)*P+s.diff(f3,y)*Q,x),s.Poly(f3,x)).as_expr()==0
assert s.simplify(f3.subs({x:s.Rational(1,2),y:0,e:0}))==s.Rational(106,25)
assert s.simplify(A1.subs({x:s.Rational(1,2),y:0}))==4
assert s.simplify(A2.subs({x:s.Rational(1,2),y:0}))==-3
assert s.simplify(s.factor(f2.subs({x:r*s.cos(s.symbols('t')),y:r*s.sin(s.symbols('t'))})) - (e*(2*r+e)+2*r*(1-s.cos(s.symbols('t')))))==0

# General unequal-radius contact identities, including the correct opposite radius.
R1,R2,t=s.symbols('R1 R2 t', real=True)
eta=1-R1-R2
assert s.simplify(1+R1**2-R2**2-2*R1*s.cos(t) - (eta*(2*R2+eta)+2*R1*(1-s.cos(t))))==0
assert s.simplify(1+R2**2-R1**2+2*R2*s.cos(t) - (eta*(2*R1+eta)+2*R2*(1+s.cos(t))))==0

def terms(z,i,t):
 rr=(1-z)/2
 if i==1: xx,yy=rr*math.cos(t),rr*math.sin(t)
 elif i==2: xx,yy=1+rr*math.cos(t),rr*math.sin(t)
 else: xx,yy=.1*math.cos(t),2+.1*math.sin(t)
 F1=xx*xx+yy*yy-rr*rr; F2=(xx-1)**2+yy*yy-rr*rr
 F3=xx*xx+(yy-2)**2-.01
 AA1=5-2*xx-yy; AA2=-4+2*xx; AA3=-3+yy
 if i==1:
  W=AA1*F2*F3; C=-2*yy*AA2*F3+4*xx*AA3*F2
 elif i==2:
  W=AA2*F1*F3; C=2*yy*AA1*F3+4*(xx-1+yy/2)*AA3*F1
 else:
  W=AA3*F1*F2; C=float('nan')
 return W,C

def calc(z,i):
 sh=math.pi if i==2 else 0
 w=lambda t:terms(z,i,t+sh)[0]
 T=quad(lambda t:1/abs(w(t)),-math.pi,math.pi,points=[0],limit=700,epsabs=1e-9)[0]
 if i==3:return T,None
 co=lambda t:terms(z,i,t+sh)[1]/terms(z,i,t+sh)[0]
 chi=math.copysign(1,w(0))*quad(lambda t:co(t)+co(-t),0,math.pi,limit=700,epsabs=1e-8)[0]
 return T,chi
C1=25*pi*sqrt(2)/424
C2=25*pi*sqrt(2)/318
for z in [1e-3,1e-4]:
 T1,chi1=calc(z,1);T2,chi2=calc(z,2);T3,_=calc(z,3)
 assert abs(T1*sqrt(z)/C1-1)<.02
 assert abs(T2*sqrt(z)/C2-1)<.03
 assert 0<T3<.5
 assert abs(chi1)<4 and abs(chi2)<4
 sh=0
 gate=quad(lambda t:1/abs(terms(z,1,t)[0]),-sqrt(2*z),sqrt(2*z),epsabs=1e-9)[0]/T1
 assert abs(gate-.5)<.03
 print('eps',z,'scaled_T1',round(T1*sqrt(z),8),'scaled_T2',round(T2*sqrt(z),8),'T3',round(T3,8),'chi1',round(chi1,8),'chi2',round(chi2,8),'Cauchy_gate',round(gate,8))
print('VERIFY_OK quartic=2 invariance=3 cofactor=2 general_gap=2 tangency_constants=3 periodic_checks=6 cauchy_profile=2')
