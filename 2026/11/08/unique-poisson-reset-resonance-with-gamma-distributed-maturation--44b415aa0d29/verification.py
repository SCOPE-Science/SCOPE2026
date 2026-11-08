"""Reproducible algebra and numerical checks for gamma maturation in Poisson-reset phase selection.

Requires Python 3, sympy, scipy, numpy and mpmath. This is a supplemental finite
check; the statements for all positive parameters follow from the analytical proof.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq
import mpmath as mp

x,k,w=sp.symbols('x k w',positive=True)
P=k*x**4+k**2*x**3+(k-1)*w**2*x**2+(k*k-2*k)*w**2*x-w**2*(k*k+w*w)
P_exp=sp.expand(k*x*(x*x+w*w)*(k+x)-w*w*((k+x)**2+w*w))
assert sp.simplify(P-P_exp)==0
F=w*w/(x*(x*x+w*w))-k*(k+x)/((k+x)**2+w*w)
assert sp.simplify(F+P/(x*(x*x+w*w)*((k+x)**2+w*w)))==0
G=k*(k+x)/((k+x)**2+w*w)
dGdk=sp.factor(sp.diff(G,k))
assert sp.simplify(dGdk-(x*(k+x)**2+(2*k+x)*w*w)/((k+x)**2+w*w)**2)==0
assert sp.simplify(sp.limit(G,k,sp.oo)-1)==0

checks=4
for K in [.1,.25,.5,1,1.5,2,3,7,40]:
 for W in [.001,.02,.1,.5,1,3,30,300,1e4]:
  poly=lambda X:float(K*X**4+K**2*X**3+(K-1)*W**2*X**2+(K*K-2*K)*W**2*X-W**2*(K*K+W*W))
  a=0.0;b=max(1,W*4/math.sqrt(K)+20)
  while poly(b)<0:b*=2
  root=brentq(poly,a,b,xtol=2e-14)
  station=lambda X:W*W/(X*(X*X+W*W))-K*(K+X)/((K+X)**2+W*W)
  assert abs(station(root)) < 1e-6 + 2e-11/K, (K,W,root,station(root))
  assert station(root*.9)>0 and station(root*1.1)<0,(K,W)
  # Direct smooth spectral response: gamma characteristic function, not the quartic.
  resp=lambda X:(X/math.hypot(X,W))*(((1+X/K)**2+(W/K)**2)**(-K/2))
  assert resp(root)>resp(root*.90) and resp(root)>resp(root*1.1)
  checks+=4

for W in [0.01,0.25,1,3,10,30]:
 sols=[]
 for K in [.1,.2,.5,1,2,5,15,100,10000]:
  coeff=[K,K*K,(K-1)*W**2,(K*K-2*K)*W**2,-W**2*(K*K+W*W)]
  rr=np.roots(coeff)
  candidates=[z.real for z in rr if z.real>0 and abs(z.imag)<1e-6*(1+abs(z.real))]
  assert len(candidates)==1,(K,W,rr)
  sols.append(candidates[0])
 assert all(a>b for a,b in zip(sols,sols[1:])),(W,sols)
 checks+=len(sols)

# Asymptotic laws: convergence ratios at controlled small/large driving.
for K in [.25,.5,1,2,5,20]:
 for W in [1e-7,1e-6,1e-5]:
  coeff=[K,K*K,(K-1)*W**2,(K*K-2*K)*W**2,-W**2*(K*K+W*W)]
  r=brentq(lambda z:np.polyval(coeff,z),0,10,maxiter=200)
  e=W**(2/3)
  # Error in the two-term expansion is of order e^3; allowance accounts for cancellation.
  approximate=e+(1/K-1)*e*e/3
  assert abs(r/approximate-1)<0.015,(K,W,r,approximate)
  checks+=1
 for W in [1e4,1e5]:
  coeff=[K,K*K,(K-1)*W**2,(K*K-2*K)*W**2,-W**2*(K*K+W*W)]
  r=brentq(lambda z:np.polyval(coeff,z),0,10*W/math.sqrt(K),maxiter=200)
  assert abs(r/W*math.sqrt(K)-1)<0.015,(K,W,r)
  C=(K**3/(K+1))**(K/2)/math.sqrt(K+1)
  logamp= math.log(r)-.5*math.log(r*r+W*W)-K/2*math.log((1+r/K)**2+(W/K)**2)
  # Compare log amplitude with the predicted power, to avoid underflow.
  assert abs(logamp- (math.log(C)-K*math.log(W)))<.05,(K,W,logamp)
  checks+=2

# Independent integration of a gamma CDF against the stationary exponential age kernel.
mp.mp.dps=40
for K,W,R in [(1,1,1.3),(2,3,2.5),(3,0.5,.9),(.7,2,1.4)]:
  theta=1/K
  def cdf(t):return mp.gammainc(K,0,t/theta)/mp.gamma(K)
  integral=mp.quad(lambda t:R*mp.e**(-(R+1j*W)*t)*cdf(t),[0,.5,1,2,4,8,16,40])
  closed=R/(R+1j*W)*(1+theta*(R+1j*W))**(-K)
  assert abs(integral-closed)<mp.mpf('3e-12'),(K,W,R,integral,closed)
  checks+=1
print('PASS',checks,'deterministic assertions: polynomial algebra, shape ordering, unique positive root, endpoint asymptotics, independent Gamma-CDF quadrature')
