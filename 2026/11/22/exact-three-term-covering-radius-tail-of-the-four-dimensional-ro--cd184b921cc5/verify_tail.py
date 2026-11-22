#!/usr/bin/env python3
"""Exact coefficient certificates and deterministic quadrature consistency checks
for the near-covering-radius spherical CDF of the D4 root-lattice cell.
No third-party packages are required.
"""
from fractions import Fraction as F
from math import sqrt
from itertools import product

def cube_avg_moment(exponents):
    # independently uniform coordinates on [-1,1]
    out=F(1)
    for k in exponents:
        if k%2: return F(0)
        out*=F(1,k+1)
    return out

def U_moment(p):
    from math import factorial
    ans=F(0)
    for a in range(p+1):
      for b in range(p+1-a):
        c=p-a-b
        ans+=F(factorial(p),factorial(a)*factorial(b)*factorial(c))*cube_avg_moment((2*a,2*b,2*c))
    return ans

assert U_moment(0)==1
assert U_moment(1)==1
assert U_moment(2)==F(19,15)
# Probability = 3 * integral_{[-1,1]^3} t_max(U,e)^4 du
# t_max = e + U/2 e^2 + (U + U^2)/2 e^3 + ...
# fourth-power bracket = 1 + 2 U e + (2 U + 7/2 U^2)e^2 + O(e^3).
coeff=[24,48,24*(2*U_moment(1)+F(7,2)*U_moment(2))]
assert coeff==[F(24),F(48),F(772,5)]

# 24 vertices of V(D4), the 24-cell: 8 axes and 16 half-cube corners
vertices=set()
for i in range(4):
  for sign in (-1,1):
    v=[F(0)]*4;v[i]=F(sign);vertices.add(tuple(v))
for signs in product((-1,1),repeat=4):
  vertices.add(tuple(F(s,2) for s in signs))
assert len(vertices)==24
for v in vertices:
    assert sum(a*a for a in v)==1
    for i in range(4):
        for j in range(i+1,4):
            assert abs(v[i])+abs(v[j])<=1
# Each axis vertex has 8 adjacent half-cube vertices;
# verify the tangent cone at e1 has a cubical cross-section at x1=1-t.
a=tuple([F(1)]+[F(0)]*3)
neighbors=[v for v in vertices if sum(x*y for x,y in zip(v,a))==F(1,2)]
assert len(neighbors)==8
assert set(tuple(2*v[j] for j in range(1,4)) for v in neighbors)==set(product((-1,1),repeat=3))

# Check the exact rational coefficients by a completely separate binomial-series recursion:
# Let t=e+sum_{k>=2} c_k e^k solve t-(1+U)t^2/2=e-e^2/2.
# Polynomial arithmetic in U with rational coefficients.
def add(P,Q):
    return tuple((P[i] if i<len(P) else F(0))+(Q[i] if i<len(Q) else F(0)) for i in range(max(len(P),len(Q))))
def mul(P,Q):
    R=[F(0)]*(len(P)+len(Q)-1)
    for i,x in enumerate(P):
        for j,y in enumerate(Q):R[i+j]+=x*y
    return tuple(R)
c=[(F(0),)]*6
c[1]=(F(1),)
for k in range(2,6):
    prod=(F(0),)
    for i in range(1,k):
        prod=add(prod,mul(c[i],c[k-i]))
    c[k]=tuple(x/F(2) for x in mul((F(1),F(1)),prod))
    if k==2: c[k]=add(c[k],(F(-1,2),))
# coefficient in t^4 at e^4,e^5,e^6
T={4:(F(1),),5:(F(0),),6:(F(0),)}
for k in T:
    polynomial=(F(0),)
    for i in range(1,k):
      for j in range(1,k-i):
        for h in range(1,k-i-j):
          ell=k-i-j-h
          if ell>=1:
            polynomial=add(polynomial,mul(mul(c[i],c[j]),mul(c[h],c[ell])))
    T[k]=polynomial
exact=[sum(v*U_moment(j)*24 for j,v in enumerate(T[k])) for k in (4,5,6)]
assert exact==coeff,(exact,coeff)

# Fixed deterministic 3D Simpson product integration. This is NOT used as proof.
def approx(e,N=48):
    h=2/N
    nodes=[(-1+h*i, 1 if i in (0,N) else (4 if i%2 else 2)) for i in range(N+1)]
    s=0.0
    for x,wx in nodes:
      for y,wy in nodes:
        for z,wz in nodes:
          U=x*x+y*y+z*z; A=1+U
          t=(2*e-e*e)/(1+sqrt(1-2*A*e+A*e*e))
          s+=wx*wy*wz*t**4
    return 3*(h/3)**3*s
for eps in (F(1,200),F(1,100)):
    e=float(eps)
    actual=approx(e)
    pred=sum(float(coeff[j])*e**(4+j) for j in range(3))
    assert abs(actual-pred)<1000*e**7,(e,actual,pred)
print('PASS: 24 exact vertices and cubical tangent, U moments, two coefficient derivations, numerical integrals')
print('Tail coefficients: 24, 48, 772/5')
