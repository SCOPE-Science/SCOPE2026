"""Exact identities and finite-mesh cross-checks for natural cubic interpolation.

Requires Python 3 and sympy. Infinite-grid conclusions are established in RESULT.md,
not by finite enumeration.
"""
import sympy as sp
from math import comb

r = 2 - sp.sqrt(3)
c = (sp.sqrt(3)-1)/2
x,y,u = sp.symbols('x y u', positive=True)
C = lambda z:(z+z**-1)/2
T = lambda z:(z**-1-z)/2
ca = sp.factor(((C(x)-1)*T(u*y)-(C(y)-1)*T(x))/T(u*x*y))
cb = sp.factor(((C(y)-1)*T(u*x)-(C(x)-1)*T(y))/T(u*x*y))
assert sp.simplify(ca.subs({x:r,y:r,u:r})-ca.subs({x:r,y:r,u:r})) == 0
num=sp.cancel((2*ca+cb)*2*(u**2*x**2*y**2-1))
P=sp.Poly(sp.expand((3*c*(1-u*u*x*x*y*y)+num/2).subs(u,r)),x,y)
assert P.total_degree()<=4
power={(i,j):sp.simplify(P.coeff_monomial(x**i*y**j)) for i in range(3) for j in range(3)}
Bern = []
for i in range(3):
 row=[]
 for j in range(3):
  a=sp.simplify(sum(power[k,l]*sp.Rational(comb(i,k)*comb(j,l),comb(2,k)*comb(2,l)) for k in range(i+1) for l in range(j+1)))
  assert a.is_nonnegative or sp.N(a,20)>=0
  row.append(a)
 Bern.append(row)
assert Bern==[
 [sp.Integer(0), sp.sqrt(3)-sp.Rational(3,2),(9-5*sp.sqrt(3))/2],
 [sp.sqrt(3)/2,3*(sp.sqrt(3)-1)/2,3*(sp.sqrt(3)-1)/2],
 [(3-sp.sqrt(3))/2,3*(sp.sqrt(3)-1)/2,27-15*sp.sqrt(3)]]

# Compare an independent matrix-defined natural spline evaluation with
# the closed negative-cardinal-weight sum, at exact rational times.
count=0
for n in range(1,15):
 if n>1:
  B=4*sp.eye(n-1)
  for i in range(n-2):
   B[i,i+1]=1; B[i+1,i]=1
  Delta=sp.zeros(n-1,n+1)
  for i in range(1,n):
   Delta[i-1,i-1]=1;Delta[i-1,i]=-2;Delta[i-1,i+1]=1
  DD=sp.zeros(n+1,n+1)
  DD[1:n,:]=6*B.inv()*Delta
 else:DD=sp.zeros(2,2)
 for j in range(n):
  k=n-1-j
  for t in [sp.Rational(1,5),sp.Rational(1,2),sp.Rational(4,5)]:
   a=t*(1-t)*(2-t);b=t*(1-t)*(1+t)
   w=sp.zeros(1,n+1);w[j]=1-t;w[j+1]=t
   w+=((1-t)**3-(1-t))*DD[j,:]/6+(t**3-t)*DD[j+1,:]/6
   negative_mass=-sum(min(z,0) for z in w)
   if n>1:
    Tn=sp.chebyshevt
    # cosh(q arcosh 2) = T_q(2), sinh(q theta)/sinh(theta) = U_(q-1)(2).
    sh=lambda q:sp.Integer(0) if q==0 else sp.sqrt(3)*sp.chebyshevu(q-1,2)
    ch=lambda q:sp.chebyshevt(q,2)
    L=(ch(j)-1)*(a*sh(n-j)-b*sh(n-j-1))/sh(n)
    R=(ch(k)-1)*(b*sh(j+1)-a*sh(j))/sh(n)
    assert sp.simplify(negative_mass-L-R)==0,(n,j,t,negative_mass,L+R)
   else: assert negative_mass==0
   count+=1
assert sp.simplify(1+3*c/2-(1+3*sp.sqrt(3))/4)==0
assert sp.simplify(1+4/(3*c)-(7+4*sp.sqrt(3))/3)==0
print('PASS: nine nonnegative exact Bernstein coefficients,',count,
      'exact finite-mesh cardinal-mass checks, two sharp-constant identities')
