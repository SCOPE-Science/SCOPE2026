"""Self-contained symbolic and numerical checks for the two-Debye threshold."""
import math
import sympy as s
from scipy.optimize import brentq
from scipy.signal import find_peaks
import numpy as np

y,z=s.symbols('y z', real=True)
R2=(3-y)/(y*(1-3*y))
B2=((1+y)/(1-y))**6*(3-y)*(1-3*y)/(64*y)
B=s.sqrt(B2)
R=s.sqrt(R2)
# Wronskian numerator of f''/f' between the two individual modes.
assert s.factor(y*(3-y)*(1-z*z)-z*(3-z)*(1-y*y)) == (y-z)*(3*y*z-y-z+3)
# Symbolic double-stationarity ratio and monotonicity.
alpha_from_stationarity=s.sqrt(z/y)*(z-1)*(1+y)**2/((1+z)**2*(1-y))
assert s.simplify((alpha_from_stationarity**2).subs(z,(3-y)/(1-3*y))-B2)==0
log_derivative=s.factor(s.diff(B2,y)/(2*B2))
wanted=-3*(y*y-6*y+1)**2/(2*y*(3-y)*(1-y)*(1+y)*(1-3*y))
assert s.simplify(log_derivative-wanted)==0
u0=3-2*s.sqrt(2)
assert s.simplify(R2.subs(y,u0)-(3+2*s.sqrt(2))**2)==0
assert s.simplify(B2.subs(y,u0)-1)==0
# Exact third and second derivative of log amplitude and threshold respectively.
LogB=3*(s.log(1+y)-s.log(1-y))+s.Rational(1,2)*(s.log(3-y)+s.log(1-3*y)-s.log(y))-s.log(8)
C=210+s.Rational(297,2)*s.sqrt(2)
assert s.simplify(s.diff(LogB,y,3).subs(y,u0)+C)==0
assert s.simplify(s.radsimp(s.simplify(s.diff(R,y,2).subs(y,u0)))-C/2)==0
assert s.simplify(s.radsimp(s.diff(R,y).subs(y,u0)))==0
# Direct polynomial coefficient calculation, independent of parametric stationary lemma.
Y=s.symbols('Y')
def coeffs(a,r):
 p=s.Poly(s.Rational(str(a))*(1-Y)*(1+s.Rational(str(r))**2*Y)**2+s.Rational(str(r))*(1-s.Rational(str(r))**2*Y)*(1+Y)**2,Y)
 return [float(c) for c in p.all_coeffs()]
def npositive(a,r):
 roots=np.roots(coeffs(a,r))
 return sum(t.real>0 and abs(t.imag)<max(1e-7,1e-7*abs(t.real)) for t in roots)
def aval(t):return float(B.subs(y,t))
def rval(t):return float(R.subs(y,t))
checks=5
for a in [0.05,0.25,0.75,1,1.5,4,12]:
 u=brentq(lambda t:aval(t)-a,1e-9,1/3-1e-9,xtol=1e-13)
 r=rval(u)
 if a==1:
  assert abs(r-(3+2*math.sqrt(2)))<1e-5
 else:
  assert npositive(a,r*.96)==1,(a,r,npositive(a,r*.96))
  assert npositive(a,r*1.04)==3,(a,r,npositive(a,r*1.04))
 checks+=2
# Independent calculation: peak counts via sampling direct loss over log-frequency;
# this tests the physical normalization rather than relying solely on the cubic.
for a in [0.15,0.5,1,2,8]:
 u=brentq(lambda t:aval(t)-a,1e-9,1/3-1e-9,xtol=1e-13)
 r=rval(u)
 x=np.linspace(-math.log(r)-4,4,50000)
 w=np.exp(x)
 for mult, expected in [(.80,1),(1.30,2)]:
  rr=r*mult
  loss=a*w/(1+w*w)+rr*w/(1+rr*rr*w*w)
  count=len(find_peaks(loss,prominence=1e-5)[0])
  assert count==expected,(a,r,mult,count)
  checks+=1
# Asymptotic sample checks (illustrative only; analytically proved in text).
for a in [1e2,1e3]:
 u=brentq(lambda t:aval(t)-a,1e-11,1/3-1e-9,xtol=1e-15)
 assert abs(rval(u)/(8*a)-1)<2e-3
 checks+=1
print('PASS',checks,'checks; cusp coefficient',float((6**s.Rational(2,3)/4)*C**s.Rational(1,3)))
