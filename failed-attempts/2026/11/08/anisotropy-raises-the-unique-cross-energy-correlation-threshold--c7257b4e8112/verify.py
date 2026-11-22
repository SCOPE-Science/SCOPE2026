#!/usr/bin/env python3
"""Reproduce the rational stationary fourth-moment identity and exact transition algebra.

Requires Python 3 and SymPy (tested with SymPy 1.13+). All main identities
are symbolic, with no extrapolation from sampled values.
"""
import functools
import sympy as sp

A,B,g,d=sp.symbols('A B g d',positive=True)
s=A+B
p=A*B
U=2*g**4+7*s*g**3+(6*s*s+8*p)*g**2+12*p*s*g
V=8*g**4+34*s*g**3+(54*s*s-4*p)*g**2+36*s**3*g+8*s**4+4*s*s*p
H=d*U-V
DEN=d**2*s*(A+g)*(2*A+g)*(B+g)*(2*B+g)*(d+2)*(s+g)*(A+2*B+g)*(2*A+B+g)
TARGET=2*H/DEN

# First independent route: stationary generator of (X_i,X_j,n_i,n_j).
def orientation_moment(k,l):
    if k%2 or l%2:return sp.S.Zero
    if k+l==0:return sp.S.One
    return (sp.factorial2(k-1) if k else 1)*(sp.factorial2(l-1) if l else 1)/sp.prod(d+2*z for z in range((k+l)//2))
@functools.lru_cache(None)
def moment(a,b,c,e):
    if a+b==0:return orientation_moment(c,e)
    src=(a*moment(a-1,b,c+1,e) if a else 0)+(b*moment(a,b-1,c,e+1) if b else 0)
    if c+e:
        src+=g*orientation_moment(c,e)*moment(a,b,0,0)
    return sp.factor(src/(a*A+b*B+(g if c+e else 0)))
var_a=moment(2,0,0,0)
var_b=moment(0,2,0,0)
generator_cov=sp.factor(moment(2,2,0,0)-var_a*var_b)
assert sp.factor(var_a-1/(d*A*(A+g)))==0
assert sp.factor(var_b-1/(d*B*(B+g)))==0
assert sp.factor(generator_cov-TARGET)==0

# Second independent route: decomposition over stationary Poisson intervals.
# On a segment of duration t, orientation remains fixed and contributes
# w_A=(1-exp(-A*t))/A, with the same duration shared by both coordinates.
phi=lambda z:g/(g+z)
coeff=[1,-2,1]
C=sp.factor(sum(coeff[i]*coeff[j]*phi(i*A+j*B) for i in range(3) for j in range(3))/(A*A*B*B))
PA=sp.factor((phi(2*B)-2*phi(A+2*B)+phi(2*A+2*B))/(A*A))
PB=sp.factor((phi(2*A)-2*phi(B+2*A)+phi(2*A+2*B))/(B*B))
SA=1/(A*(A+g)); SB=1/(B*(B+g))
E_SASB=(C+PA*SB+PB*SA)/(1-phi(2*s))
E_HAB=C/(1-phi(2*s))
clock_cov=sp.factor((E_SASB-SA*SB-2*E_HAB/(d+2))/d**2)
assert sp.factor(clock_cov-TARGET)==0

# Coefficient-ratio ordering ensuring unique critical rate for d>4.
uk=[0,12*p*s,6*s*s+8*p,7*s,2]
vk=[8*s**4+4*s*s*p,36*s**3,54*s*s-4*p,34*s,8]
assert sp.factor(sp.expand(sum(uk[k]*g**k for k in range(5))-U))==0
assert sp.factor(sp.expand(sum(vk[k]*g**k for k in range(5))-V))==0
assert sp.factor(vk[4]/uk[4]-4)==0
assert sp.factor(vk[3]/uk[3]-sp.Rational(34,7))==0
assert sp.factor(7*vk[2]-34*uk[2] - (174*s*s-300*p))==0
assert sp.factor(vk[1]-sp.Integer(12)*uk[1]-36*s*(A-B)**2)==0
assert sp.factor(vk[2]-9*uk[2]+76*p)==0
# Anisotropy enhancement at fixed total trap strength s.
g_ref=3*s/(d-4)
assert sp.factor(H.subs(g,g_ref)+ (A-B)**2*s*s*(2*d+1)*(4*d-7)/(d-4)**2)==0
S,P=sp.symbols('S P')
H_sp=sp.expand((d*(2*g**4+7*S*g**3+(6*S*S+8*P)*g**2+12*P*S*g) - (8*g**4+34*S*g**3+(54*S*S-4*P)*g**2+36*S**3*g+8*S**4+4*S*S*P)))
assert sp.expand(H_sp.subs({S:s,P:p})-H)==0
assert sp.factor(sp.diff(H_sp,P)-4*((2*d+1)*g*g+3*d*S*g-S*S))==0
assert sp.factor((sp.diff(H_sp,P)/4).subs({S:s,g:g_ref})/s**2-(8+54/(d-4)+81/(d-4)**2))==0

# An exact isotropic limit: the already classical one-axis result is not
# counted as a new consequence of the anisotropic classification.
assert sp.factor(TARGET.subs(B,A)-2*((d-4)*g-6*A)/(A*d*d*(A+g)**2*(2*A+g)*(3*A+g)*(d+2)))==0

# Numerical checks are supplementary only: these do not certify the theorem.
def evalH(rate,dim,aa,bb):return float(H.subs({g:rate,d:dim,A:aa,B:bb}))
def bisect(dim,aa,bb):
    assert dim>4
    low=3*(aa+bb)/(dim-4)
    hi=low*2+1
    while evalH(hi,dim,aa,bb)<=0:hi*=2
    for _ in range(110):
        mid=(low+hi)/2
        if evalH(mid,dim,aa,bb)>0:hi=mid
        else:low=mid
    return (low+hi)/2

if __name__=='__main__':
    # Keep reference values explicit for a reproducible nontrivial example.
    assert abs(bisect(5,1,2)-9.325485849042439)<1e-10
    assert abs(bisect(6,1,2)-4.743416490252567)<1e-10
    assert abs(bisect(5,1,1)-6)<1e-10
    print('PASS: two symbolic derivations, coefficient-ratio identities, anisotropy shift, isotropic limit, and three root checks')
