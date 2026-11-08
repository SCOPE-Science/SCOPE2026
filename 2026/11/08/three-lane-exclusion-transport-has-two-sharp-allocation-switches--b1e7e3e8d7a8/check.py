#!/usr/bin/env python3
"""Supplementary exact-arithmetic and finite-generator checks for three-lane current allocation.

Requires Python 3 standard library and SymPy. This checker is supplemental to the
analytical proof of the continuum-density optimization.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import sympy as s

x,y,z,A,g = s.symbols('x y z A g', real=True)
e2=x*y+y*z+z*x
e3=x*y*z
J=sum(v*(1-v)*(A+g*(1-v)) for v in (x,y,z))
assert s.factor((J-(2*A+g)*e2-3*g*e3).subs(z,1-x-y))==0
# Schur (degree three) is exact at x+y+z=1.
schur=sum(t*(t-u)*(t-v) for t,u,v in ((x,y,z),(y,x,z),(z,x,y)))
assert s.factor((1-4*e2+9*e3-schur).subs(z,1-x-y))==0
assert s.factor((1-4*(z*(1-z)+(1-z)**2/s.Integer(4))+9*z*(1-z)**2/s.Integer(4)) - z*(3*z-1)**2/4)==0

p_uniform={x:s.Rational(1,3),y:s.Rational(1,3),z:s.Rational(1,3)}
p_face={x:s.Rational(1,2),y:s.Rational(1,2),z:0}
p_corner={x:1,y:0,z:0}
JU=s.factor(J.subs(p_uniform));JF=s.factor(J.subs(p_face));JC=s.factor(J.subs(p_corner))
assert s.simplify(JU-2*(3*A+2*g)/9)==0
assert s.simplify(JF-(2*A+g)/4)==0
assert JC==0
assert s.simplify((JU-JF)-(6*A+7*g)/36)==0
assert s.simplify((JF-JC)-(2*A+g)/4)==0
q=s.symbols('q',real=True)
assert s.factor(J.subs({A:1,g:q,z:1-x-y})-(2+q)*e2.subs(z,1-x-y)-3*q*e3.subs(z,1-x-y))==0
# Equality and local-stability checks from tangent Hessians and boundary derivative.
t=s.symbols('t',real=True)
f=t*(1-t)*(A+g*(1-t))
assert s.simplify(s.diff(f,t,2).subs(t,s.Rational(1,3))+2*(A+g))==0
assert s.simplify(s.diff(f,t).subs(t,0)-s.diff(f,t).subs(t,s.Rational(1,2))-(A+s.Rational(5,4)*g))==0
assert s.simplify(J.subs({x:t,y:1-t,z:0})-(2*A+g)*t*(1-t))==0
assert s.factor(J.subs(g,-2*A).subs(z,1-x-y)+6*A*e3.subs(z,1-x-y))==0

# Local-maxima/stability thresholds and the non-symmetric interior saddle.
h=s.symbols('h', real=True)
curve=s.factor(J.subs({x:h,y:h,z:1-2*h}))
root=s.factor(-(2*A+g)/(3*g))
assert s.factor(s.diff(curve,h).subs(h,root))==0
# Along the symmetric path and the antisymmetric split, curvatures oppose.
curv_sym=s.factor(s.diff(curve,h,2).subs(h,root))
curv_asym=s.factor(2*s.diff(f,t,2).subs(t,root))
assert s.simplify(curv_sym+curv_asym)==0
assert s.simplify(curv_sym-(-6*g*(3*root-1)))==0
zz,tt=s.symbols('zz tt',real=True)
facepath=s.expand(J.subs({x:(1-zz)/2+tt,y:(1-zz)/2-tt,z:zz}))
faceat=s.simplify(facepath.subs({zz:0,tt:0}))
assert s.factor((facepath-faceat).subs({g:-s.Rational(4,5)*A,tt:0})-3*A*zz**2*(1-2*zz)/10)==0

nchecks=0
# Exhaustive rational-simplex grid at broad representatives in the three regimes.
for denom in [3,4,5,6,7,8,9,10,12,15,20,30,40,50]:
  for num in [-5,-3,-2,s.Rational(-19,10),-1,s.Rational(-9,10),s.Rational(-6,7),s.Rational(-4,5),s.Rational(-1,2),0,1,3]:
    a=F(str(num)) if not isinstance(num,s.Rational) else F(int(num.p),int(num.q))
    if a>=F(-6,7): upper=F(2,9)*(3+2*a)
    elif a>=-2: upper=(2+a)/4
    else: upper=F(0)
    for i in range(denom+1):
      for j in range(denom-i+1):
        k=denom-i-j
        p=[F(i,denom),F(j,denom),F(k,denom)]
        e2f=p[0]*p[1]+p[1]*p[2]+p[0]*p[2]
        e3f=p[0]*p[1]*p[2]
        val=(2+a)*e2f+3*a*e3f
        assert val<=upper,(denom,a,p,val,upper)
        nchecks+=1

# Uniform stationary distribution for every particle-count sector: exact global balance.
# Forward and backward rates have positive offset epsilon and prescribed difference.
for gamma in (F(-3),F(-2),F(-6,7),F(-4,5),F(-1,2),F(1)):
  for L in (2,3,4):
    count=0
    for bits in product((0,1),repeat=3*L):
      net=F(0)
      for lane in range(3):
        for k in range(L):
          kp=(k+1)%L
          a,b=bits[lane*L+k],bits[lane*L+kp]
          if a==b:continue
          d=sum(bits[l*L+k]+bits[l*L+kp] for l in range(3) if l!=lane)
          drift=F(1)+gamma*F(d,2)
          forward=F(1)+max(drift,F(0)); backward=F(1)+max(-drift,F(0))
          net += (backward-forward) if (a,b)==(1,0) else (forward-backward)
      assert net==0,(gamma,L,bits,net)
      count+=1
    nchecks+=count

# A nontrivial finite-ring canonical current equals the analytic L/(L-1) correction.
for L in (3,4):
 for gamma in (F(-2),F(-6,7),F(1)):
  for Ns in ((1,1,1),(1,1,2),(2,1,2)):
    if any(n>L for n in Ns): continue
    matching=[bits for bits in product((0,1),repeat=3*L) if all(sum(bits[i*L:(i+1)*L])==Ns[i] for i in range(3))]
    for lane in range(3):
      expected=F(Ns[lane]*(L-Ns[lane]),L*(L-1))*(F(1)+gamma*sum((F(Ns[j],L) for j in range(3) if j!=lane),F(0)))
      observed=F(0)
      for bits in matching:
        # use the bond (0,1) only; translation invariance handles all other bonds
        a,b=bits[lane*L],bits[lane*L+1]
        d=sum(bits[j*L]+bits[j*L+1] for j in range(3) if j!=lane)
        drift=F(1)+gamma*F(d,2)
        observed+= (F(1)+max(drift,F(0))) * (a==1 and b==0) - (F(1)+max(-drift,F(0))) * (a==0 and b==1)
      observed/=len(matching)
      assert observed==expected,(gamma,L,Ns,lane,observed,expected)
      nchecks+=1

# Two-lane comparison when the sum of the two densities is 1.
u=s.symbols('u',real=True)
J2=u*(1-u)*(A+g*(1-u))+(1-u)*u*(A+g*u)
assert s.factor(J2-(2*A+g)*u*(1-u))==0
print('PASS: symbolic identities, complete finite-generator balances, exact canonical currents,',nchecks,'additional exact rational checks')
