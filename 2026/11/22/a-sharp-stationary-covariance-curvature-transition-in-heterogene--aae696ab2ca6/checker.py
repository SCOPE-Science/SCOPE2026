"""Reproducible checks for stationary heterogeneous telegraph covariance jets.
Standard library only. All assertions are finite checks, not a substitute for proof.
"""
from fractions import Fraction as F
from math import factorial, gamma, isclose, sqrt

COUNT=0

def check(x):
 global COUNT
 assert x
 COUNT+=1

def moment(n,r,nu,v):
 # stationary Y has a zero-mean double-exponential law
 if n%2:return F(0)
 return F(factorial(n),1) * (v*v / (r*(r+2*nu)))**(n//2)

def mixed(n,r,nu,v):
 # E[Sigma Y^n], derived independently by stationary moment balance
 if n%2==0:return F(0)
 return r*moment(n+1,r,nu,v)/((n+1)*v)

def generator(poly,r,nu,v):
 # Keys are (degree, orientation power in {0,1})
 out={}
 def add(k,a):out[k]=out.get(k,F(0))+a
 for (n,s),c in poly.items():
  if n>0:add((n-1,1-s), c*n*v)
  if s: add((n,1),-c*2*nu)
  if n>0: add((n,s),-c*r)
  elif n==0 and s==0: pass
  # At reset, Y=0 and Sigma is redrawn fairly. sigma term reset
  elif s: add((0,s),-c*r)
 return {k:v for k,v in out.items() if v}

def bilinear(g,h,r,nu,v):
 out=F(0)
 for (n,s),a in h.items():
  for (m,z),b in g.items():
   check(z==0)
   out+=a*b*(moment(m+n,r,nu,v) if s==0 else mixed(m+n,r,nu,v))
 return out

for p in (3,5,7):
 alpha=F(2*(p-1),p)
 beta=F(1,p)
 for r in (F(1,2),F(1),F(2),F(5),F(9)):
  for nu in (F(1,4),F(1),F(3)):
   for v in (F(1,2),F(1),F(7,3)):
    g={(p,0):beta**p}
    M2=bilinear(g,g,r,nu,v)
    d1=bilinear(g,generator(g,r,nu,v),r,nu,v)
    d2=bilinear(g,generator(generator(g,r,nu,v),r,nu,v),r,nu,v)
    check(d1/M2==-r/2)
    check(d2/M2==r*(alpha*r-4*nu)/(2*(alpha+2)))
    check((d2>0)==(r>4*nu/alpha))

# In the non-polynomial case the absolute stationary moments are gamma integrals.
for alpha in (0.1,0.25,0.5,0.75,1,1.25,1.5,1.9):
 p=2/(2-alpha);beta=1/p
 for r,nu,v in ((.3,2,1),(3,1,2),(.7,.1,.9),(10,.6,1.5)):
  lam=sqrt(r*(r+2*nu))/v
  M2=beta**(2*p)*gamma(2*p+1)/lam**(2*p)
  ggpp=p*(p-1)*beta**(2*p)*gamma(2*p-1)/lam**(2*p-2)
  lhs=(v*v*ggpp-r*nu*M2)/M2
  rhs=r*(alpha*r-4*nu)/(2*(alpha+2))
  check(isclose(lhs,rhs,rel_tol=1e-10,abs_tol=1e-10))
  d1=-r*M2/2
  r_infer=-2*d1/M2
  nu_infer=(alpha*r_infer-2*(alpha+2)*lhs/r_infer)/4
  v_infer=sqrt(r_infer*(r_infer+2*nu_infer))*(M2/(beta**(2*p)*gamma(2*p+1)))**(1/(2*p))
  check(isclose(r_infer,r,rel_tol=1e-9))
  check(isclose(nu_infer,nu,rel_tol=1e-9))
  check(isclose(v_infer,v,rel_tol=1e-9))
print(f"PASS: {COUNT} exact-rational and floating-point consistency assertions")
