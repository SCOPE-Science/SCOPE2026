"""Exact checks for the two quadratic-Hopf physical-time asymptotics.
Run: python checker.py  (requires sympy; optional scipy for numerical tests).
"""
import sympy as s
th=s.symbols('th',real=True)
c,t=s.cos(th),s.sin(th)
z=s.sqrt(2)

def check(label,omega,sigma,P,Q,ic,ip,amp,timecoef):
 C=s.expand(c*P+t*Q)
 D=s.expand(c*Q-t*P)
 assert s.simplify(s.integrate(C,(th,0,2*s.pi)))==0
 assert s.simplify(s.integrate(D,(th,0,2*s.pi)))==0
 assert s.simplify(s.integrate(C*D,(th,0,2*s.pi))-ic)==0
 F=s.integrate(C,th)
 assert s.simplify(s.integrate(D*D-F*D,(th,0,2*s.pi))-ip)==0
 assert s.simplify((sigma*s.pi/omega)*omega**2/ic-amp)==0
 assert s.simplify(amp*ip/omega**3-timecoef)==0
 assert float(sigma*(-ic/(2*s.pi*omega))) < 0
 print(label,'symbolic identity tests: PASS')

check('origin',s.Integer(1),1,c*c/s.Integer(4)+c*t/5-t*t/3,c*t,
      s.pi/240,293*s.pi/5400,s.Integer(240),586*s.pi/45)
check('lower focus',z,-1,c*c/4-z*c*t/5-2*t*t/3,c*t,
      -z*s.pi/48,793*s.pi/2700,s.Integer(48),793*z*s.pi/225)

# A separate numerical integration checks the predicted leading periods and amplitudes.
try:
 import numpy as np
 from scipy.integrate import solve_ivp
 from scipy.optimize import brentq
 def vec(_t,Z,d):
  x,y=Z
  return [d*x-y+x*x/4+x*y/5-y*y/3,x*(1+y)]
 def first_return(radius,d,branch):
  level=0.0 if branch==0 else -3.0
  def gate(_t,Z):return Z[1]-level
  gate.direction=1 if branch==0 else -1
  gate.terminal=False
  o=solve_ivp(lambda t,Z:vec(t,Z,d),(0,12),(radius,level),events=gate,
              max_step=.055,rtol=2e-11,atol=2e-12)
  matches=[(T,X) for T,X in zip(o.t_events[0],o.y_events[0]) if T>2]
  assert matches
  T,X=matches[0]
  return X[0]-radius,T
 for branch in (0,1):
  mu=2e-5
  d=mu if branch==0 else .6-mu
  rr=(240 if branch==0 else 48)*mu
  rad=np.sqrt(rr)
  p=brentq(lambda r:first_return(r,d,branch)[0],rad*.5,rad*1.5,xtol=1e-11)
  T=first_return(p,d,branch)[1]
  base=2*np.pi if branch==0 else np.sqrt(2)*np.pi
  drift=(586*np.pi/45 if branch==0 else 793*np.sqrt(2)*np.pi/225)*mu
  assert abs(p/rad-1)<.015
  assert abs((T-base)/drift-1)<.001
  print('branch',branch,'numeric amplitude ratio',p/rad,'period-drift ratio',(T-base)/drift)
except ImportError:
 print('scipy absent: exact symbolic checks were completed; optional integration skipped.')
print('ALL EXACT IDENTITIES PASS')
