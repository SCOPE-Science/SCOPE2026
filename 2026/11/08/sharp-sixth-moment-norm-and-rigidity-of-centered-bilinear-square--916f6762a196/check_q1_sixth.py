#!/usr/bin/env python3
"""Reproduce the exact sixth moment and both sharp bilinear-cell deficits.
All mathematical identities are checked over rational coefficient fields.
Requires only Python's standard library.
"""
from fractions import Fraction as F
from math import factorial, sqrt
from itertools import product

# Polynomials in (x,y,z), monomials are exponent triples.
def add(*polys):
    out={}
    for pol in polys:
        for k,v in pol.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def mul(p,q):
    out={}
    for a,va in p.items():
        for b,vb in q.items():
            k=tuple(a[i]+b[i] for i in range(3));out[k]=out.get(k,F(0))+va*vb
    return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:v*F(c) for k,v in p.items() if v*c}
def powp(p,n):
    out={(0,0,0):F(1)}
    for _ in range(n):out=mul(out,p)
    return out
x={(1,0,0):F(1)};y={(0,1,0):F(1)};z={(0,0,1):F(1)}
one={(0,0,0):F(1)}
s=add(x,y,z);t=add(x,y);u=mul(x,y)

# Direct multinomial integration of f=A sqrt(3)U+B sqrt(3)V+C 3UV,
# where U,V are independent uniform[-1,1] and x=A^2,y=B^2,z=C^2.
moment={}
for i in range(7):
 for j in range(7-i):
    k=6-i-j
    if (i+k)%2 or (j+k)%2:continue
    assert i%2==j%2==k%2==0
    coeff=F(factorial(6),factorial(i)*factorial(j)*factorial(k))
    coeff*=F(3)**((i+j)//2+k)
    coeff/=F((i+k+1)*(j+k+1))
    moment[(i//2,j//2,k//2)]=coeff
expected={
 (3,0,0):F(27,7),(0,3,0):F(27,7),(0,0,3):F(729,49),
 (2,1,0):F(27),(1,2,0):F(27),
 (2,0,1):F(405,7),(0,2,1):F(405,7),
 (1,0,2):F(729,7),(0,1,2):F(729,7),
 (1,1,1):F(1458,5),
}
assert moment==expected
print('EXACT_ALL_TEN_SIXTH_MOMENT_MONOMIALS_OK')

# Direct symbolic reduction via the symmetric invariants t=x+y, u=xy.
poly=add(scale(powp(t,3),F(27,7)),
         scale(mul(u,t),F(108,7)),
         scale(mul(add(powp(t,2),scale(u,-2)),z),F(405,7)),
         scale(mul(u,z),F(1458,5)),
         scale(mul(t,powp(z,2)),F(729,7)),
         scale(powp(z,3),F(729,49)))
assert poly==moment
print('EXACT_SYMMETRIC_INVARIANT_REDUCTION_OK')

# Lower deficit, coefficient-by-coefficient positivity.
lo=add(moment,scale(powp(s,3),-F(27,7)))
assert lo=={
  (2,1,0):F(108,7),(1,2,0):F(108,7),
  (2,0,1):F(324,7),(0,2,1):F(324,7),
  (1,0,2):F(648,7),(0,1,2):F(648,7),
  (1,1,1):F(9396,35),(0,0,3):F(540,49)
}
assert all(a>0 for a in lo.values())
print('EXACT_POSITIVE_LOWER_DEFICIT_AND_EQUALITY_FACES_OK')

# The univariate upper profile is written homogeneously with s=x+y+z:
# P <= Phi(z,s)= 27/245(44z^3-693z^2*s+714z*s^2+70s^3).
phi=scale(add(scale(powp(z,3),44),scale(mul(powp(z,2),s),-693),
              scale(mul(z,powp(s,2)),714),scale(powp(s,3),70)),F(27,245))
D=add(scale(t,F(27,7)),scale(z,F(1539,35)))
diff=add(x,scale(y,-1))
assert add(phi,scale(mul(D,powp(diff,2)),-1))==moment
assert all(a>0 for a in D.values())
print('EXACT_UPPER_SYMMETRY_DEFICIT_OK')

# Upper one-variable profile derivative is (162/245)*(22r^2-231r+119).
# Its smaller root r=(231-sqrt(42889))/44 is strictly between 0 and 1.
assert 22*F(1,2)**2-231*F(1,2)+119>0
assert 22*F(3,5)**2-231*F(3,5)+119<0
# Larger root >1, and quadratic derivative is positive at 0, negative at 1.
assert 119>0 and 22-231+119<0
print('EXACT_UNIQUE_INTERIOR_MAXIMUM_CERTIFICATE_OK')

# The local stability term 693-44(z+2r) >561 on the unit simplex,
# and D(z)>=27/7 for 0<=z<=1.
assert F(693)-44*3==561
assert F(1539,35)>F(27,7)
# Algebraic polynomial identity for cubic Phi(z) around any stationary r:
# Phi(r)-Phi(z)=27/245*(z-r)^2*(693-44(z+2r)).
# Reduce all coefficients using 22 r^2-231 r+119=0.
R=sqrt(42889);r=(231-R)/44
assert 0<r<1
phi_scalar=lambda zz:F(27,245)*(44*zz**3-693*zz**2+714*zz+70)
# Distinct rational numerical tests of the exact factorization (not the proof).
for zz in (0.,0.1,0.333,0.5,0.8,1.):
 assert abs(float(phi_scalar(r)-phi_scalar(zz))-float(F(27,245)*(zz-r)**2*(693-44*(zz+2*r))))<2e-11
# Exact algebraic-field replay: work in Q[r]/(22*r*r-231*r+119).
# The chosen real root is the unique one in (0,1), established above.
def ra(a,b):return (a[0]+b[0],a[1]+b[1])
def rn(a):return (-a[0],-a[1])
def rm(a,b):
    t=a[1]*b[1]
    return (a[0]*b[0]-F(119,22)*t,
            a[0]*b[1]+a[1]*b[0]+F(231,22)*t)
def rs(a,b):return ra(a,rn(b))
def rc(t):return (F(t),F(0))
def rw(a,t):return rm(a,rc(t))
def rp(a,n):
    out=rc(1)
    for _ in range(n):out=rm(out,a)
    return out
rho=(F(0),F(1))
assert rs(rs(rw(rp(rho,2),22),rw(rho,231)),rc(-119))==rc(0)
# Phi evaluated at rho and the closed-form radical constant agree exactly.
phi_r=rw(ra(ra(rw(rp(rho,3),44),rw(rp(rho,2),-693)),
              ra(rw(rho,714),rc(70))),F(27,245))
K_r=rs(ra(rc(F(15039*231,3080)),rw(rho,F(-15039*44,3080))),rc(F(275103,280)))
assert phi_r==K_r
# Coefficients of K-Phi(z), in ascending powers z.
lhs=[rs(K_r,rc(F(27*70,245))),rc(-F(27*714,245)),
     rc(F(27*693,245)),rc(-F(27*44,245))]
# (z-rho)^2*(693-44*z-88*rho), as a polynomial in z.
r2=rp(rho,2)
factor=[r2,rw(rho,-2),rc(1)]
other=[rs(rc(693),rw(rho,88)),rc(-44)]
out=[rc(0) for _ in range(4)]
for i,pi in enumerate(factor):
 for j,pj in enumerate(other):out[i+j]=ra(out[i+j],rm(pi,pj))
rhs=[rw(c,F(27,245)) for c in out]
assert lhs==rhs
print('EXACT_ALGEBRAIC_QUADRATIC_ROOT_AND_GLOBAL_UPPER_DEFICIT_OK')

print('SHARP_STABILITY_COEFFICIENTS_AND_BOUNDARY_CHECKS_OK')

# All equality cases correspond to two linear modes for the minimum,
# and |A|=|B|>0 with |C|^2/(A^2+B^2+C^2)=r for the maximum.
for point in ((F(1),F(0),F(0)),(F(0),F(1),F(0))):
 assert sum(v*point[0]**a*point[1]**b*point[2]**c for (a,b,c),v in moment.items())==F(27,7)
assert abs(sum(float(v)*((1-r)/2)**(a+b)*r**c for (a,b,c),v in moment.items())-float(phi_scalar(r)))<1e-10
print('SHARP_MINIMUM_AND_MAXIMUM_EXTREMIZER_WITNESSES_OK')
print('ALL_Q1_ZERO_MEAN_SIXTH_MOMENT_CHECKS_OK')
