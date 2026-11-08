#!/usr/bin/env python3
"""Exact symbolic and finite-rational checks for a two-patch linear-noise model."""
from fractions import Fraction as F
import math
import sympy as s

checks=0

def check(ok,msg):
    global checks
    assert ok, msg
    checks+=1

a,m,Q,R,T=s.symbols('a m Q R T', positive=True)
u,v,w=s.symbols('u v w')
A=s.Matrix([[-a-m,m],[m,-a-m]])
C=s.Matrix([[u,v],[v,w]])
B=s.Matrix([[Q,T],[T,R]])
stat=s.solve([*list(A*C+C*A+B)[0:2],(A*C+C*A+B)[3]],[u,v,w],dict=True)[0]
# The flattened positions include both symmetric off-diagonals.
VS=(Q+R+2*T)/(2*a)
VD=(Q+R-2*T)/(2*(a+2*m))
CSD=(Q-R)/(2*(a+m))
V1=(VS+VD+2*CSD)/4
V2=(VS+VD-2*CSD)/4
C12=(VS-VD)/4
for key,expr in [(u,V1),(v,C12),(w,V2)]:
    check(s.factor(stat[key]-expr)==0,f'stationary covariance {key}')
check(s.factor(s.diff(V1,m)-((R-Q)/(a+m)**2-(Q+R-2*T)/(a+2*m)**2)/4)==0,'derivative')
check(s.factor(s.diff(C12,m)-(Q+R-2*T)/(4*(a+2*m)**2))==0,'cross-cov derivative')
check(s.factor(V1+V2+2*C12-VS)==0,'aggregate variance')
check(s.factor((V1-V2)-(Q-R)/(2*(a+m)))==0,'variance gap')
check(s.factor(V1.subs(m,0)-Q/(2*a))==0,'isolated variance')
check(s.factor(s.limit(V1,m,s.oo)-(Q+R+2*T)/(8*a))==0,'high migration')
check(s.factor((V1-Q/(2*a))-m*(2*a*(T-Q)+(R+2*T-3*Q)*m)/(4*a*(a+m)*(a+2*m)))==0,'baseline crossover')

# Rational covariance matrices with rational positive semidefinite noise.
# Choose two integer vectors as Brownian loadings, so the covariance matrix is PSD by construction.
for x1 in range(-3,4):
 for y1 in range(-3,4):
  for x2 in range(-2,3):
   for y2 in range(-2,3):
    q=x1*x1+y1*y1
    r=x2*x2+y2*y2
    if not q or not r: continue
    t=x1*x2+y1*y2
    for aa in (F(1),F(2),F(3,2)):
      for mm in (F(0),F(1,4),F(1),F(3)):
        aaF=F(aa);mF=F(mm)
        vs=F(q+r+2*t,1)/(2*aaF)
        vd=F(q+r-2*t,1)/(2*(aaF+2*mF))
        csd=F(q-r,1)/(2*(aaF+mF))
        u1=(vs+vd+2*csd)/4
        u2=(vs+vd-2*csd)/4
        cross=(vs-vd)/4
        A11=-aaF-mF;A12=mF
        check(2*A11*u1+2*A12*cross+q==0,'moment equation 1')
        check(A12*(u1+u2)-2*(aaF+mF)*cross+t==0,'moment equation 2')
        check(2*A11*u2+2*A12*cross+r==0,'moment equation 3')
        check(u1>=0 and u2>=0 and u1*u2>=cross*cross,'PSD stationary')

# Test each monotonicity regime and the exact interior minimizer, with direct variance evaluations.
examples=[(1,4,0,1,'interior'),(1,2,0,1,'interior'),
          (1,2,-1,1,'decreasing'),(1,4,1,1,'increasing'),
          (1,4,F(3,2),1,'increasing'),(2,1,0,1,'decreasing'),
          (1,1,1,1,'constant'),(1,5,0,3,'interior')]
for q,r,t,aa,kind in examples:
    def vv(mm):
        return F(q+r+2*t,1)/(8*aa)+F(q+r-2*t,1)/(8*(aa+2*mm))+F(q-r,1)/(4*(aa+mm))
    def dsign(mm):
        return F(r-q,1)/(aa+mm)**2-F(q+r-2*t,1)/(aa+2*mm)**2
    for mm in [F(0),F(1,4),F(1),F(4),F(100)]:
        if kind=='decreasing': check(dsign(mm)<0,'decreasing')
        if kind=='increasing' and mm>0:check(dsign(mm)>0,'increasing')
        if kind=='constant':check(dsign(mm)==0,'constant')
    if kind=='interior':
        H=math.sqrt((q+r-2*t)/(r-q))
        mm=aa*(H-1)/(2-H)
        check(mm>0,'positive optimal migration')
        check(float(vv(F(mm).limit_denominator(10**7))) < float(vv(F(0))),'interior improves on isolation')
        check(float(vv(F(mm).limit_denominator(10**7))) < float(F(q+r+2*t,1)/(8*aa)),'interior improves on unlimited mixing')

print('PASS',checks,'exact and boundary assertions')
