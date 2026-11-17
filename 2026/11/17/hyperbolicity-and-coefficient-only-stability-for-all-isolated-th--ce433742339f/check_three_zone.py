#!/usr/bin/env python3
"""Exact-rational checks of an affine Hamiltonian crossing-cycle identity.
This supplementary check verifies a published three-center example and its
reversed-time counterpart. General dynamical conclusions use the proof.
"""
from fractions import Fraction as F
from math import sqrt

# Affine Hamiltonian coefficients in (a,b,c,alpha,beta) ordering.
L = tuple(map(F, ['4','8','-5/2','3/2','11/4']))
C = tuple(map(F, ['0','2','-2','2/3','2/3']))
R = tuple(map(F, ['4','2','-10','-4','-4']))

def h(coeff,x,y):
    a,b,c,alpha,beta=coeff
    return b*y*y/2-c*x*x/2+a*x*y+alpha*y-beta*x

def identity_data(L,C,R):
    aL,bL,_,alL,_=L
    a,b,_,al,_=C
    aR,bR,_,alR,_=R
    r=-(aR+alR)/bR
    l=(aL-alL)/bL
    A=b*r+a+al
    B=b*l-a+al
    D=h(C,1,r)-h(C,-1,l)
    return r,l,A,B,D,b

r,l,A,B,D,b=identity_data(L,C,R)
assert (r,l,A,B,D,b)==(F(0),F(5,16),F(2,3),F(31,24),F(-1259,768),F(2))
S=295865
tcoef=F(31,11280)
ucoef=F(1,705)
t2=tcoef*tcoef*S
u2=ucoef*ucoef*S
assert A*tcoef==B*ucoef
assert 2*D+b*(t2-u2)==0
assert (tcoef*tcoef*S)== -2*D*B*B/(b*(B*B-A*A))
# Hamiltonian values at all four points are pairs of rational + radical.
# For a quadratic in y = q0+q1 sqrt(S), calculate coefficients exactly.
def hrad(coeff,x,y0,y1):
    a,b,c,alpha,beta=coeff
    return (b*(y0*y0+S*y1*y1)/2-c*x*x/2+a*x*y0+alpha*y0-beta*x,
            b*y0*y1+a*x*y1+alpha*y1)
assert hrad(R,1,r,tcoef)==hrad(R,1,r,-tcoef)
assert hrad(L,-1,l,-ucoef)==hrad(L,-1,l,ucoef)
assert hrad(C,1,r,tcoef)==hrad(C,-1,l,ucoef)
assert hrad(C,1,r,-tcoef)==hrad(C,-1,l,-ucoef)
assert A>0 and B>A and b>0
assert b*b*t2>A*A and b*b*u2>B*B
# The exact squared radical is a published three-center crossing solution.
t=float(tcoef)*sqrt(S)
u=float(ucoef)*sqrt(S)
q=(float(A)-float(b)*t)*(float(B)+float(b)*u)/((float(B)-float(b)*u)*(float(A)+float(b)*t))
assert 7.16<q<7.17, q
assert q>1
# Reversing all vector fields reverses time, exchanging attraction and
# repulsion, while the geometric crossing ratio remains the same.
Lminus=tuple(-v for v in L)
Cminus=tuple(-v for v in C)
Rminus=tuple(-v for v in R)
r2,l2,A2,B2,D2,b2=identity_data(Lminus,Cminus,Rminus)
assert (r2,l2,A2,B2,D2,b2)==(r,l,-A,-B,-D,-b)
q2=(float(A2)-float(b2)*t)*(float(B2)+float(b2)*u)/((float(B2)-float(b2)*u)*(float(A2)+float(b2)*t))
assert abs(q2-q)<1e-12
assert 0<1/q2<1 and B2<A2
# Check the parameter-only identity for a rationally chosen valid gap t,u.
# When A*t=B*u, the return-ratio displacement is proportional to B-A.
assert A*tcoef==B*ucoef
numer=2*b*(A*ucoef-B*tcoef)
den_left=(B-b*ucoef*sqrt(S))*(A+b*tcoef*sqrt(S))
assert numer<0 and den_left<0 # numerator is coefficient of sqrt(S)
print('THREE_ZONE_HAMILTONIAN_RATIONAL_CERTIFICATE_OK')
print('published_example_multiplier_approx',format(q,'.12f'))
print('time_reverse_multiplier_approx',format(1/q,'.12f'))
