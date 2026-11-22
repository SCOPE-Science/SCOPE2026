"""Reproducibility checks for exact five-character observation on two circular arcs.
All symbolic identities are exact; numerical eigenvalue checks are supplementary.
"""
import sympy as S
import numpy as np
from math import sin, cos, pi, sqrt

t,c,s,L,y=S.symbols('t c s L y',real=True)
V=S.Matrix([S.Rational(1,4),-t,S.Rational(1,2)+t*t,-t,S.Rational(1,4)])
Z=S.Matrix([0,0,1,0,0]);B=S.Matrix.hstack(Z,V)
C={0:L}
for j in range(1,5):C[j]=S.expand(s*S.chebyshevu(j-1,c)/j*S.chebyshevt(j,t))
G=S.Matrix(5,5,lambda i,j:C[abs(i-j)])
Q=B.T*B
K=B.T*G*B
P=y*y+c*(2*c*c-1)*y-2*c*c
D=S.expand((K[0,0]-(L-s*y)*Q[0,0])*(K[1,1]-(L-s*y)*Q[1,1])-(K[0,1]-(L-s*y)*Q[0,1])**2)
A=(-6*c**3+4*c**2+c-2)*y+5*c**2-2*c
E=(2*c**3-S.Rational(16,3)*c**2+3*c+S.Rational(4,3))*y-c**2+4*c-4
assert S.simplify(S.rem(S.expand(D/s**2-t**2*(A+E*t**2)),P,y))==0
assert S.factor(S.rem(S.expand(D/s**2),P,y)-t**2*(A+E*t**2))==0
low=1+S.Rational(2,3)*(1-c*c)
high=low+S.Rational(1,3)*(1-c*c)**2
assert S.factor(low*low+(2*c*c-1)*low-2+S.Rational(8,9)*(1-c*c)**2)==0
assert S.factor(high*high+(2*c*c-1)*high-2-c**4*(1-c*c)**2/9)==0
A1=-6*c**3+4*c*c+c-2
B1=2*c**3-S.Rational(16,3)*c*c+3*c+S.Rational(4,3)
assert S.factor(A.subs(y,c*low)-4*c*(c-1)**3*(c+1)*(3*c+4)/3)==0
P5=6*c**5-10*c**4-19*c**3+33*c**2+24*c-36
assert S.factor(E.subs(y,c*high)-(c-1)**2*(c+1)*P5/9)==0

def bern(poly,n):
 a=S.symbols('a:'+str(n+1))
 f=sum(a[k]*S.binomial(n,k)*c**k*(1-c)**(n-k) for k in range(n+1))
 v=S.solve(S.Poly(poly-f,c).coeffs(),a)
 assert len(v)==n+1
 return [v[w] for w in a]
assert bern(A1,3)==[-2,S.Rational(-5,3),0,-3]
assert bern(B1,3)==[S.Rational(4,3),S.Rational(7,3),S.Rational(14,9),1]
assert bern(P5,5)==[-36,S.Rational(-156,5),S.Rational(-231,10),S.Rational(-68,5),S.Rational(-33,5),-2]
assert S.series((2*S.Symbol('a')-2*S.sin(S.Symbol('a'))*S.cos(S.Symbol('a'))*(S.sqrt((2*S.cos(S.Symbol('a'))**2-1)**2+8)-(2*S.cos(S.Symbol('a'))**2-1))/2)/S.pi,S.Symbol('a'),0,7).coeff(S.Symbol('a'),5)==S.Rational(64,135)/S.pi
cnt=9
for a in np.linspace(0.08,1.5,31):
 cc=cos(a); p=2*cc**2-1; yy=cc*(sqrt(p*p+8)-p)/2
 lam=(2*a-2*sin(a)*yy)/pi
 D0=np.subtract.outer(np.arange(-2,3),np.arange(-2,3))
 for beta in np.linspace(a,pi/2,101):
  moments=np.empty(5)
  moments[0]=2*a/pi
  for k in range(1,5):moments[k]=2*sin(k*a)*cos(k*beta)/(pi*k)
  M=moments[np.abs(D0)]
  mineig=np.linalg.eigvalsh(M)[0]
  assert mineig<=lam+1e-11,(a,beta,mineig,lam)
  if abs(beta-pi/2)<1e-12: assert abs(mineig-lam)<2e-11
  elif abs(beta-pi/2)>0.02:assert mineig<lam-1e-13
  cnt+=1
print('FIVE_MODE_TWO_ARC_CHECK_PASS',cnt)
