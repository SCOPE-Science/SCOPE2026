#!/usr/bin/env python3
"""Reproduce exact polynomial identities and independent numerical checks.
Requires Python 3, sympy, numpy, scipy. Numerical tests are not proofs.
"""
import sympy as sp
import numpy as np
from scipy.optimize import root, brentq

p,e,z,a,b=sp.symbols('p e z a b', real=True)
q=2*p-1
H=sp.Matrix([[sp.Rational(1,2),p,1-p],[1-p,sp.Rational(1,2),p],[p,1-p,sp.Rational(1,2)]])
avec=sp.Matrix([a,b,-a-b]); d=sp.ones(3,1)+e*avec
u,v=sp.symbols('u v', real=True)
X=sp.Matrix([u,v,1-u-v]); D=sp.expand(d.dot(X))
B=[[[2*H[i,j]*H[i,k]+H[i,j]*H[j,k]+H[i,k]*H[k,j] for k in range(3)] for j in range(3)] for i in range(3)]
Wpair=2*H*X
Wtri=sp.Matrix([sum(B[i][j][k]*X[j]*X[k] for j in range(3) for k in range(3)) for i in range(3)])
for weights in (Wpair,Wtri):
 assert sp.simplify(X.dot(weights)-1)==0
x0=sp.Matrix([sp.Rational(1,3)+e*(-a-2*b)/(3*q),sp.Rational(1,3)+e*(2*a+b)/(3*q),sp.Rational(1,3)+e*(-a+b)/(3*q)])
assert sp.simplify(sum(x0)-1)==0
assert sp.simplify(d.dot(x0)-1)==0
assert all(sp.simplify(t)==0 for t in (2*H*x0-d))
vec0=sp.Matrix([X[i]*(D*Wpair[i]-d[i]) for i in range(2)])
J0=vec0.jacobian([u,v]); tr0=sp.trace(J0)
vand=(a-b)*(a+2*b)*(-2*a-b)
S2=a*a+b*b+(a+b)**2
expected=e**2*S2/3+e**3*vand/(3*q)
assert sp.simplify(sp.factor(tr0.subs({u:x0[0],v:x0[1]})-expected))==0
assert sp.simplify(J0.det().subs({u:sp.Rational(1,3),v:sp.Rational(1,3),e:0})-q**2/3)==0
mix=sp.Matrix([X[i]*(D*((1-z)*Wpair[i]+z*Wtri[i])-d[i]) for i in range(2)])
J=mix.jacobian([u,v]); tt=sp.trace(J)
assert sp.simplify(tt.subs({u:sp.Rational(1,3),v:sp.Rational(1,3),e:0})+z*q**2/3)==0
assert sp.simplify(sp.diff(tt,z).subs(z,0).subs({u:x0[0],v:x0[1]}).diff(e).subs(e,0))==0
assert sp.simplify(sp.diff(tr0,u).subs({u:sp.Rational(1,3),v:sp.Rational(1,3),e:0}))==0
assert sp.simplify(sp.diff(tr0,v).subs({u:sp.Rational(1,3),v:sp.Rational(1,3),e:0}))==0
print('Exact identities: normalized population, equilibrium, trace, determinant, and mixed first-order derivative passed')

def trace_at(p0, rates, eps, alpha):
 Hn=np.array([[.5,p0,1-p0],[1-p0,.5,p0],[p0,1-p0,.5]])
 Bn=np.zeros((3,3,3))
 for i in range(3):
  for j in range(3):
   for k in range(3): Bn[i,j,k]=2*Hn[i,j]*Hn[i,k]+Hn[i,j]*Hn[j,k]+Hn[i,k]*Hn[k,j]
 dn=1+eps*np.array(rates,float)
 def fun(x):
  xx=np.array([x[0],x[1],1-x[0]-x[1]])
  W=(1-alpha)*2*(Hn@xx)+alpha*np.einsum('ijk,j,k->i',Bn,xx,xx)
  return (xx*((dn@xx)*W-dn))[:2]
 sol=root(fun,[1/3,1/3],tol=1e-12)
 assert np.max(np.abs(fun(sol.x)))<1e-10
 h=2e-6
 J=np.column_stack([(fun(sol.x+h*np.eye(2)[j])-fun(sol.x-h*np.eye(2)[j]))/(2*h) for j in range(2)])
 return np.trace(J)

for rates in [(1,-1,0),(1,0,-1)]:
 for eps in [.01,.02,.04]:
  alpha=brentq(lambda t:trace_at(.75,rates,eps,t),0,.15,xtol=2e-12)
  S=sum(r*r for r in rates)
  V=(rates[0]-rates[1])*(rates[1]-rates[2])*(rates[2]-rates[0])
  pred=S/.5**2*eps**2+V/.5**3*eps**3
  assert abs(alpha-pred)<40*eps**4
  assert trace_at(.75,rates,eps,alpha+1e-4)<0
  assert trace_at(.75,rates,eps,0)>0
  print('rates',rates,'epsilon',eps,'critical',format(alpha,'.12g'),'cubic approximation',format(pred,'.12g'))
print('All checks passed')
