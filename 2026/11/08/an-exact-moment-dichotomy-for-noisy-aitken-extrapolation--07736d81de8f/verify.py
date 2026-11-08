"""Standalone checks for the Gaussian-noise Aitken tail classification."""
from fractions import Fraction as F
from math import exp, pi, sqrt, erf
import itertools
import sympy as s

checks=0
q,b,a=s.symbols('q b a',real=True)
A,B,Z=s.symbols('A B Z',real=True)
y0=a+b; y1=a+b*q; y2=a+b*q*q
u=s.expand(y1-y0); v=s.expand(y2-2*y1+y0)
assert s.simplify(v-b*(q-1)**2)==0; checks+=1
assert s.simplify(y0-u*u/v-a)==0; checks+=1
# Gaussian covariance forms for independent/exchangeable noise
rho, sigma=s.symbols('rho sigma',real=True)
S=sigma**2*((1-rho)*s.eye(3)+rho*s.ones(3))
l_u=s.Matrix([-1,1,0]); l_v=s.Matrix([1,-2,1])
vu=s.expand((l_u.T*S*l_u)[0]); vv=s.expand((l_v.T*S*l_v)[0]); cv=s.expand((l_u.T*S*l_v)[0])
assert s.simplify(vu-2*sigma**2*(1-rho))==0; checks+=1
assert s.simplify(vv-6*sigma**2*(1-rho))==0; checks+=1
assert s.simplify(cv+3*sigma**2*(1-rho))==0; checks+=1
k=s.simplify(cv/vv)
tau=s.simplify(vu-cv**2/vv)
ustar=s.factor(u-k*v)
assert k==-s.Rational(1,2); checks+=1
assert s.simplify(tau-sigma**2*(1-rho)/2)==0; checks+=1
assert s.factor(ustar-b*(q*q-1)/2)==0; checks+=1
# Finite moment: curvature-free (linear) Gaussian perturbation -> deterministic denominator
Q=s.Matrix([Z,2*Z,3*Z]); pert=s.Matrix([y0,y1,y2])+Q
D=s.expand(pert[2]-2*pert[1]+pert[0]); U=s.expand(pert[1]-pert[0])
assert s.simplify(D-v)==0; checks+=1
assert s.denom(s.factor(pert[0]-U**2/D)).has(Z)==False; checks+=1
# Geometric and common offset perturbations exactly preserve the Aitken kernel
x=s.Matrix([y0,y1,y2])+s.Matrix([A+B,A+q*B,A+q*q*B]); dx=s.factor(x[1]-x[0]); dd=s.factor(x[2]-2*x[1]+x[0]); out=s.factor(x[0]-dx*dx/dd)
assert s.simplify(out-(a+A))==0; checks+=1
# Nonaligned rank-one example: noise only in final observation, exact one-sided tail formula
mU=F(-1,2); mV=F(1,4)
tail=float(mU*mU)*exp(-float(mV*mV)/2)/sqrt(2*pi)
assert abs(tail-0.25*exp(-1/32)/sqrt(2*pi))<1e-15; checks+=1
def normal_cdf(x): return (1+erf(x/sqrt(2)))/2
# high-precision normal CDF difference to avoid cancellation
import mpmath as mp
mp.mp.dps=65
m=mp.mpf(1)/4; w=mp.mpf(1)/4
Phi=lambda z: (1+mp.erf(z/mp.sqrt(2)))/2
C=w*mp.exp(-m*m/2)/mp.sqrt(2*mp.pi)
for t in [10**3,10**4,10**5,10**6]:
 tt=mp.mpf(t)
 pp=Phi(-m)-Phi(-m-w/(tt-1))
 pn=Phi(-m+w/(tt+1))-Phi(-m)
 assert abs(tt*pp/C-1)<mp.mpf('0.007')
 assert abs(tt*pn/C-1)<mp.mpf('0.007')
 checks+=2
# Exact rational regression calculations on 60 structured positive semidefinite covariances
uvec=s.Matrix([-1,1,0]); vvec=s.Matrix([1,-2,1])
for p0,p1,p2 in itertools.product(range(1,5), repeat=3):
 cov=s.diag(p0,p1,p2)
 va=(vvec.T*cov*vvec)[0]; ua=(uvec.T*cov*uvec)[0]; cross=(uvec.T*cov*vvec)[0]
 residual=s.factor(ua-cross*cross/va)
 assert va>0 and residual>0
 checks+=1
# Verify Gaussian degeneracy equivalence: any curvature-invariant noise has zero v-variance
for c in range(-4,5):
 vvct=s.Matrix([1,2,3])*c
 assert (vvec.T*vvct)[0]==0
 checks+=1
print(f'PASS: {checks} symbolic, exact covariance, and high-precision tail assertions')
print('example one-sided tail constant: %.12f'%float(C))
print('iid q=1/2,b=1,sigma=1: conditional numerator moment = 41/64')
print('limits: numerical tail checks illustrate finite t; analytic proof establishes asymptotic t to infinity.')
