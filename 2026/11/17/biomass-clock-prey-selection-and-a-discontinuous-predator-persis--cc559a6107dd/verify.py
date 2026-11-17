#!/usr/bin/env python3
"""Symbolic and numerical corroboration of symmetric two-prey predator dynamics."""
import math
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
x,y,z,r,c,a,b=sp.symbols('x y z r c a b',positive=True)
s=x+y; w=x-y;q=w/s
fx=x*(r-r*x-c*y-a*z)
fy=y*(r-r*y-c*x-a*z)
fz=z*(b*s-1)
sdot=sp.expand(fx+fy)
qdot=sp.factor((sp.diff(q,x)*fx+sp.diff(q,y)*fy))
assert sp.simplify(qdot+(r-c)*s*q*(1-q*q)/2)==0
assert sp.simplify(sdot -s*(r-(r+c)*s/2-(r-c)*s*q*q/2-a*z))==0
# Numerical comparisons against exact biomass-clock formula and all terminal regimes.
cases=[(2.,0.5,1.1,.7, .8,.3,.2), (2.,3.,1.1,1.1, .9,.3,.1), (2.,3.,1.1,2., .9,.3,.1), (2.,3.,1.1,2., .3,.9,.1), (2.,3.,1.1,2., .5,.5,.1), (2.,2.,1.1,1.6, .9,.3,.1), (2.,1.,1.1,.3, .3,.9,.1), (2.,3.,1.1,1.6, .6,.6,.5), (2.,3.,1.1,1.1, .6,.6,.5)]
results=[]
for R,C,A,B,X,Y,Z in cases:
 def f(t,U):
  xx,yy,zz,bb,pp=U
  ss=xx+yy
  qq=(xx-yy)/ss
  if abs(R-C)<1e-12 or abs(X-Y)<1e-14: dd=0.
  elif R>C: dd=(R-C)*qq*qq/2
  else: dd=(C-R)*(1-qq*qq)/2
  return [xx*(R-R*xx-C*yy-A*zz), yy*(R-R*yy-C*xx-A*zz), zz*(B*ss-1),ss,ss*dd]
 sol=solve_ivp(f,(0,300),(X,Y,Z,0.,0.),rtol=2e-10,atol=1e-12,dense_output=True,max_step=.25)
 assert sol.success
 q0=(X-Y)/(X+Y)
 for t in [0.5,1,2,5,10,30]:
  xx,yy,zz,clock,penalty=sol.sol(t)
  qq=(xx-yy)/(xx+yy)
  if q0:
   ratio=q0/math.sqrt(1-q0*q0)*math.exp(-(R-C)*clock/2)
   pred=ratio/math.sqrt(1+ratio*ratio)
   assert abs(qq-pred)<1e-7,(R,C,B,t,qq,pred)
  else: assert abs(qq)<1e-8
 xx,yy,zz,clock,penalty=sol.y[:,-1]
 qq=(xx-yy)/(xx+yy)
 if R>C or R==C or abs(q0)<1e-14: qinf=0 if R>C or abs(q0)<1e-14 else q0
 else: qinf=math.copysign(1,q0)
 dinf=(R+C+(R-C)*qinf*qinf)/2
 sinf=min(R/dinf,1/B)
 zinf=max(0,(R-dinf*sinf)/A)
 assert abs((xx+yy)-sinf)<2e-5,(R,C,B,'s',xx+yy,sinf)
 assert abs(zz-zinf)<2e-5,(R,C,B,'z',zz,zinf)
 if R==C or abs(q0)<1e-14: expectedpenalty=0.
 elif R>C: expectedpenalty=-.5*math.log1p(-q0*q0)
 else: expectedpenalty=-math.log(abs(q0))
 assert abs(penalty-expectedpenalty)<2e-6,(R,C,B,penalty,expectedpenalty)
 results.append((R,C,B,round(sinf,7),round(zinf,7),round(qq,7),round(penalty,7)))
# Exact integral identity: for \(k=r-c>0\), write Q=q^2/(1-q^2)
# and use Q=Q0*exp(-kB). Its integral is (log(1+Q0))/2.
# For \(k<0\), use P=(1-q^2)/q^2 and P=P0*exp(kB).
Q=sp.symbols('Q',positive=True)
assert sp.simplify(sp.diff(sp.log(1+Q)/2,Q)-sp.Rational(1,2)/(1+Q))==0
print('VERIFY_OK symbolic_frequency_and_mass=2 exact_biomass_clock_cases=',len(cases),'sample_times=',len(cases)*6,'integrated_penalties=',len(cases),'long_run_equilibria=',len(cases))
print(results)
