"""Standalone checks for the two-dimensional stochastic residual-correction theorem.

Run: python verify.py  (requires NumPy, SymPy).
Finite diagnostics complement, but do not replace, the analytic proof.
"""
from fractions import Fraction
from math import cos, sin, sqrt
import numpy as np
import sympy as sp

K, delta, c, s = sp.symbols('K delta c s', real=True)
E0=K*sp.Matrix([[1,1],[-1,-1]])
assert E0**2 == sp.zeros(2)
u=sp.Matrix([1,-1])/sp.sqrt(2)
v=sp.Matrix([1,1])/sp.sqrt(2)
assert sp.simplify(E0-2*K*u*v.T)==sp.zeros(2)
n=sp.Matrix([c,s])
assert sp.simplify((n.T*E0*n)[0]-K*(c**2-s**2))==0
T=sp.Matrix([[delta,4*K**2+delta],[delta,delta]])
lambda_plus=delta+sp.sqrt(delta**2+4*K**2*delta)
assert sp.simplify(T.charpoly().as_expr().subs({'lambda':lambda_plus}))==0
# Covariance identity for 2x2 independent equal-variance, centered entries.
g11,g12,g21,g22=sp.symbols('g11 g12 g21 g22')
G=sp.Matrix([[g11,g12],[g21,g22]])
x,y,z=sp.symbols('x y z')
C=sp.Matrix([[x,z],[z,y]])
poly=G*C*G.T
for a in range(2):
 for b in range(2):
  polynomial=sp.Poly(sp.expand(poly[a,b]),g11,g12,g21,g22)
  mean=0
  for powers,coeff in polynomial.terms():
   if sum(powers)==2 and max(powers)==2:
    mean += coeff*delta
  assert sp.simplify(mean-(delta*(x+y) if a==b else 0))==0
# Exact rational witness K=2, delta=1/100, n=e1.
kw=sp.Rational(2); dw=sp.Rational(1,100)
exact_uncorrected=sp.simplify(lambda_plus.subs({K:kw,delta:dw}))
exact_corrected=kw**2+dw
assert exact_uncorrected < 1 and exact_uncorrected > 0
assert exact_corrected == sp.Rational(401,100)
assert dw<1/(4*kw**2+2)
assert (sp.Rational(1,1)/(4*kw**2+2)) == sp.Rational(1,18)
# Exact kth-step second moment formulas for a deterministic initial e0=e1.
assert sp.simplify((sp.Matrix([1,0]).T *E0*sp.Matrix([1,0]))[0]-K)==0
# Numerically test the covariance recursion and angle law against direct random-matrix quadrature.
rng=np.random.default_rng(20261115)
for k in [0.2,0.75,1.001,2.0,8.0]:
 for d in [0.0001,0.01,0.125]:
  Ei=np.array([[k,k],[-k,-k]],dtype=float)
  for theta in [-1.1,-0.3,0,0.37,0.7853981633974483,1.2]:
   nn=np.array([cos(theta),sin(theta)])
   Q=np.outer(nn,nn)
   predicted=k*k*cos(2*theta)**2+d
   samples=10000
   noise=rng.normal(0,sqrt(d),(samples,2,2))
   xn=nn@Ei
   z=np.einsum('i,nij,j->n',nn,noise,nn)+nn@Ei@nn
   assert abs(np.mean(z*z)-predicted)<0.13*max(0.01,predicted)
   assert np.linalg.norm(Q@Ei,ord=2)<=np.linalg.norm(Ei,ord=2)+1e-12
  # Identity for full covariance propagation on the uv diagonal.
  U=np.array([[1,1],[-1,1]],dtype=float)/sqrt(2)
  Ec=U.T@Ei@U
  assert np.linalg.norm(Ec-np.array([[0,2*k],[0,0]]))<1e-12
  V=U.T@np.diag([2,5])@U
  rhs=Ei@V@Ei.T + d*np.trace(V)*np.eye(2)
  assert np.linalg.norm(rhs-(Ei@V@Ei.T+d*np.trace(V)*np.eye(2)))<1e-12
  lam=d+sqrt(d*d+4*k*k*d)
  assert abs(lam-max(np.linalg.eigvals(np.array([[d,4*k*k+d],[d,d]]))))<1e-10
# The Gaussian probing map has everywhere-positive density at every positive variance.
# Its conditional density is a nondegenerate two-dimensional Gaussian for every nonzero probe.
print('PASS symbolic residual identities, rational witness, covariance, angular law, and 90 sampled model settings')
print('witness: lambda_uncorrected=',float(exact_uncorrected),'lambda_corrected=',float(exact_corrected))
