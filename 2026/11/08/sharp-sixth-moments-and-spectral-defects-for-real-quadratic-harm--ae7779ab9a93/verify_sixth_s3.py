#!/usr/bin/env python3
"""Exact reproducibility checks for sixth moments of real quadratic harmonics on S^3."""
from itertools import product
import sympy as sp

u,v,w = sp.symbols('u v w')
eigen = (u,v,w,-u-v-w)
S = sp.expand(sum(x*x for x in eigen))
T = sp.expand(sum(x**3 for x in eigen))
P = sp.prod(eigen)

def sphere_moment(degree):
    # Squared coordinates of a uniform S^3 point have Dirichlet(1/2,1/2,1/2,1/2) law.
    ans = sp.Integer(0)
    for k0 in range(degree+1):
      for k1 in range(degree-k0+1):
       for k2 in range(degree-k0-k1+1):
        k3=degree-k0-k1-k2
        ks=(k0,k1,k2,k3)
        term=sp.factorial(degree)/sp.rf(2,degree)
        for eig, k in zip(eigen,ks):
            term *= sp.rf(sp.Rational(1,2),k)*eig**k/sp.factorial(k)
        ans+=term
    return sp.expand(ans)

M2=sphere_moment(2)
M6=sphere_moment(6)
assert sp.expand(M2-S/12)==0
normalized=sp.Rational(9,14)*(15*S**3-144*P*S+16*T**2)
assert sp.expand(M6*12**3-normalized)==0
assert len(sp.Poly(M6,u,v,w).terms())==28
print('FULL_DIRICHLET_SIXTH_MOMENT_POLYNOMIAL_IDENTITY_OK',len(sp.Poly(M6,u,v,w).terms()))

lower_shape=(1,1,-1,-1)
upper_shape=(3,-1,-1,-1)
def normalized_sixth(vals):
    s=sp.Integer(sum(t*t for t in vals))
    t=sum(x**3 for x in vals)
    p=sp.prod(vals)
    return sp.factor(sp.Rational(9,14)*(15-144*p/s**2+16*t**2/s**3))
assert normalized_sixth(lower_shape)==sp.Rational(27,7)
assert normalized_sixth(upper_shape)==15
for a in range(-3,4):
 for b in range(-3,4):
  for c in range(-3,4):
   vals=(a,b,c,-a-b-c)
   if vals==(0,0,0,0):continue
   y=normalized_sixth(vals)
   assert sp.Rational(27,7)<=y<=15
print('ENDPOINTS_AND_342_RATIONAL_SPECTRAL_TESTS_OK',sp.Rational(27,7),15)

# Verify the two exact nonnegative-defect decompositions.
R=sp.Rational(9,14)*(15-144*P/S**2+16*T**2/S**3)
lo=sp.Rational(9,14)*(144*(sp.Rational(1,16)-P/S**2)+16*T**2/S**3)
hi=sp.Rational(9,14)*(144*(P/S**2+sp.Rational(1,48))+16*(sp.Rational(1,3)-T**2/S**3))
assert sp.factor(R-sp.Rational(27,7)-lo)==0
assert sp.factor(15-R-hi)==0
print('EXACT_TWO_SIDED_SPECTRAL_DEFICIT_IDENTITIES_OK')

# A 3x3 matrix coefficient of SO(3) becomes a traceless 4x4 quadratic form.
a,b,c,d=sp.symbols('q0 q1 q2 q3')
Q=(a,b,c,d)
Rquat=sp.Matrix([
[a*a+b*b-c*c-d*d,2*(b*c-a*d),2*(b*d+a*c)],
[2*(b*c+a*d),a*a-b*b+c*c-d*d,2*(c*d-a*b)],
[2*(b*d-a*c),2*(c*d+a*b),a*a-b*b-c*c+d*d]
])
def associated_B(expr):
    poly=sp.Poly(expr,*Q)
    B=sp.zeros(4)
    for i in range(4):
       B[i,i]=poly.coeff_monomial(Q[i]**2)
       for j in range(i+1,4):
          B[i,j]=B[j,i]=poly.coeff_monomial(Q[i]*Q[j])/2
    assert sp.expand((sp.Matrix(Q).T*B*sp.Matrix(Q))[0]-expr)==0
    assert sp.trace(B)==0
    return B
Bs=[associated_B(Rquat[i,j]) for i in range(3) for j in range(3)]
for k in range(9):
  for l in range(9):
    assert sp.trace(Bs[k]*Bs[l])==(4 if k==l else 0)
assert len(Bs)==9
print('SO3_QUATERNION_NINE_DIMENSIONAL_ISOMETRY_OK',len(Bs))
assert associated_B(Rquat[0,0]).eigenvals()=={sp.Integer(1):2,sp.Integer(-1):2}
assert associated_B(sp.trace(Rquat)).eigenvals()=={sp.Integer(3):1,sp.Integer(-1):3}
print('ROTATION_MATRIX_COEFFICIENT_EQUALITY_MODES_OK')
print('ALL_S3_SIXTH_MOMENT_CHECKS_OK')
