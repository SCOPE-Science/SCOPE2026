#!/usr/bin/env python3
"""Exact verification of the jittered heavy-ball stability boundary.

Run: python verify_heavyball.py (requires SymPy >=1.12)
No empirical sampling is used as evidence for the theorem.
"""
from fractions import Fraction as F
from itertools import product
import sympy as S

checks = 0

def check(condition, description):
    global checks
    assert condition, description
    checks += 1

z,a,b,v,r,l=S.symbols('z a b v r l')
e=S.Matrix([1,0]); E=e*e.T
M=S.Matrix([[a,-b],[1,0]])
T=S.Matrix([[a*a+v,-2*a*b,b*b],[a,-b,0],[1,0,0]])
char=S.expand(T.charpoly(z).as_expr())
check(S.expand(char-(z**3+(b-a*a-v)*z*z+(a*a*b-b*b-b*v)*z-b**3))==0,"moment characteristic polynomial")
D=(1-b)*((1+b)**2-a*a)
W=S.Matrix([[1+b,a],[a,1+b]])/D
check(all(S.factor(t)==0 for t in W-M*W*M.T-E),"deterministic forced covariance")
check(S.factor(W.det()-1/((1-b)**2*((1+b)**2-a*a)))==0,"positive definite covariance determinant")
vcrit=S.factor(D/(1+b))
K=lambda X: S.simplify(M*X*M.T+v*X[0,0]*E)
check(all(S.factor(t)==0 for t in K(W)-W-(v*W[0,0]-1)*E),"covariance comparison")
check(all(S.factor(t)==0 for t in K(K(W))-W-(v*W[0,0]-1)*(E+K(E))),"two-step strict comparison")
check(S.factor(S.det(E+K(E)) -(1+v))==0,"strict cone comparison determinant")
check(S.factor(char.subs(z,1)+(1+b)*(v-vcrit))==0,"unit-root crossing identity")

# A sample of exact covariance recursions and parameter values.
for aq in [S.Rational(-1,1),S.Rational(0),S.Rational(1,3),S.Rational(4,5)]:
  for bq in [S.Rational(0),S.Rational(1,4),S.Rational(1,2)]:
    if abs(aq)<1+bq:
      vq=S.factor(vcrit.subs({a:aq,b:bq}))
      check(vq>0,"deterministic stable margin")
      check(S.factor(char.subs({a:aq,b:bq,v:vq,z:1}))==0,"exact boundary root")
      check(S.factor(char.subs({a:aq,b:bq,v:vq/2,z:1}))>0,"below boundary sign")
      check(S.factor(char.subs({a:aq,b:bq,v:2*vq,z:1}))<0,"above boundary sign")

# Arbitrary dimension: slope of the modal threshold is strictly negative.
alpha, lam, sigma2=S.symbols('alpha lam sigma2',positive=True)
astar=1+b-alpha*lam
boundary=S.factor(vcrit.subs(a,astar)/(alpha*lam)**2)
check(S.factor(boundary - (2*(1-b)/(alpha*lam)-(1-b)/(1+b)))==0,"general modal law")
check(S.factor(S.diff(boundary,lam) +2*(1-b)/(alpha*lam**2))==0,"worst mode is maximal eigenvalue")

# Exact deterministic-Chebyshev tuning.
t=S.symbols('t',positive=True)
beta=((t-1)/(t+1))**2
alpha_mu=4/(t+1)**2
alpha_L=4*t*t/(t+1)**2
for y,target in [(alpha_mu,2*t**3/(t*t+1)),(alpha_L,2/(t*(t*t+1)))]:
 check(S.factor(boundary.subs({b:beta,alpha:y,lam:1})-target)==0,"Chebyshev modal endpoint")
check(S.factor(2/(t*(t*t+1))-1/t**2 + (t-1)**2/(t*t*(t*t+1)))==0,"strict GD/HB tolerance comparison")

# Exact two-point jitter, kappa=9, sigma^2=4/49.
a0=S.Rational(-1)
b0=S.Rational(1,4)
v0=S.Rational(81,196)
T0=T.subs({a:a0,b:b0,v:v0})
p0=S.factor(T0.charpoly(z).as_expr())
check(S.factor(p0-(3136*z**3-3648*z**2+264*z-49)/3136)==0,"exact high-mode polynomial")
check(S.factor(p0.subs(z,1))<0,"unstable real root above one")
for eig in [1,9]:
    rate=(1-S.Rational(1,5)*eig)**2+(S.Rational(1,5)*eig)**2*S.Rational(4,49)
    check(rate < 1,"GD remains mean-square stable")
    check(rate == S.Rational(788 if eig==1 else 1108,1225),"GD rate exact")

# Exhaustively enumerate actual two-point random recurrence for 0..8 steps.
# This independently checks that the 3x3 moment dynamics corresponds to the process.
for curvature in (F(1),F(9)):
  alpha=F(1,4)
  beta=F(1,4)
  aa=F(1)+beta-alpha*curvature
  variance=(alpha*curvature)**2*F(4,49)
  TT=((aa*aa+variance,-2*aa*beta,beta*beta),(aa,-beta,F(0)),(F(1),F(0),F(0)))
  for init in ((F(1),F(0)),(F(1),F(1)),(F(0),F(1))):
    u,w,old=init[0]**2,init[0]*init[1],init[1]**2
    for steps in range(9):
      # enumerated second moments at the same k
      UU=WW=OO=F(0)
      for signs in product((-1,1),repeat=steps):
        x,prev=init
        for sign in signs:
          x,prev=(F(1)+beta-alpha*curvature*(F(1)+F(sign*2,7)))*x-beta*prev,x
        UU+=x*x;WW+=x*prev;OO+=prev*prev
      divisor=2**steps
      check((UU/divisor,WW/divisor,OO/divisor)==(u,w,old),"exact exhaustive moment enumeration")
      u,w,old=(TT[0][0]*u+TT[0][1]*w+TT[0][2]*old,
               TT[1][0]*u+TT[1][1]*w,
               TT[2][0]*u)

print(f"PASS: {checks} independent exact checks; no finite enumeration used as infinite proof.")
print("Chebyshev-HB: sigma² < 2/[sqrt(kappa)*(kappa+1)] (strict).")
print("Optimal GD: sigma² < 1/kappa (strict).")
print("At kappa=9 and xi=±2/7, HB high mode is unstable while GD is stable.")
