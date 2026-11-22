#!/usr/bin/env python3
"""Exact polynomial and independent numerical checks of the stated modal identities.

Run with Python 3, using only its standard library. Finite numerical tests are diagnostics,
not substitutes for the analytic quantifier arguments in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, acos, sin, cos, pi


def add(a,b):
    z=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a): z[i]+=x
    for i,x in enumerate(b): z[i]+=x
    return trim(z)
def mul(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return trim(z)
def scale(a,c): return trim([c*x for x in a])
def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

# Use y=q^2. A=(y^2-12y+24)/24, rho=(12-y)/12.
A=[F(1),-F(1,2),F(1,24)]
rho=[F(1),-F(1,12)]
absB2=[F(0),F(1),-F(1,4),F(1,48)]  # y(y^2-12y+48)/48
assert add(mul(A,A),mul(rho,absB2))==[F(1)]

# B/q = br + i bi/sqrt(3); C/q=cr+i ci/sqrt(3).
br=[-F(1),F(1,8)]
bi=[F(0),-F(1,8)]
cr=[F(1),-F(5,24),F(1,96)]
ci=[F(0),-F(1,8),F(1,96)]
assert add(cr,mul(rho,br))==[F(0)]
assert add(ci,scale(mul(rho,bi),-1))==[F(0)]
# q= sqrt(8): real offdiagonal parts vanish. q=sqrt(12): B=sqrt(3)-3i.
assert sum(c*F(8)**i for i,c in enumerate(br))==0
assert sum(c*F(12)**i for i,c in enumerate(br))==F(1,2)
assert sum(c*F(12)**i for i,c in enumerate(bi))==-F(3,2)
assert sum(c*F(12)**i for i,c in enumerate(cr))==0
assert sum(c*F(12)**i for i,c in enumerate(ci))==0


def mat_terms(delta,n):
    y=12.0-delta
    q=sqrt(y)
    aa=1-y/2+y*y/24
    theta=acos(max(-1.0,min(1.0,aa)))
    b=q*(y-8)/8-1j*q*y/(8*sqrt(3))
    rr=delta/12
    cc=-rr*b.conjugate()
    cs=cos(n*theta)
    fac=sin(n*theta)/sin(theta)
    # M^n, real M^n, weight rho, phase.
    M=((complex(cs),fac*b),(fac*cc,complex(cs)))
    P=((cs,(fac*b).real),((fac*cc).real,cs))
    return M,P,rr,theta,b


def vec_norm2(z): return sum(abs(t)**2 for t in z)
def apply(m,u): return (m[0][0]*u[0]+m[0][1]*u[1],m[1][0]*u[0]+m[1][1]*u[1])
def weighted_norm2(u,rho): return rho*abs(u[0])**2+abs(u[1])**2

for delta in (9.0,4.0,1.0,0.25,0.01):
    for n in (0,1,2,7,22):
        M,P,rho,theta,b=mat_terms(delta,n)
        for u in ((1.,0.),(0.,1.),(0.3,-0.7)):
            v=apply(M,u)
            assert abs(weighted_norm2(v,rho)-weighted_norm2(u,rho))<2e-10
            p=apply(P,u)
            D=cos(n*theta)**2 + (b.real/abs(b))**2*sin(n*theta)**2
            assert abs(weighted_norm2(p,rho)-D*weighted_norm2(u,rho))<2e-10

for delta in (1e-3,1e-4,1e-5):
    _,_,_,theta,_=mat_terms(delta,1)
    n=round(pi/(2*theta))
    M,P,rho,theta,b=mat_terms(delta,n)
    gain_complex=sqrt(vec_norm2(apply(M,(0.,1.))))
    gain_projected=sqrt(vec_norm2(apply(P,(0.,1.))))
    assert abs(sqrt(delta)*gain_complex-2*sqrt(3))<0.09
    assert abs(sqrt(delta)*gain_projected-sqrt(3))<0.09

# q^2=8 has P_n=cos(n theta)I even though M_n has imaginary offdiagonals.
for n in range(10):
    M,P,_,theta,_=mat_terms(4.,n)
    assert abs(P[0][1])+abs(P[1][0])<1e-12
print('VERIFY_OK: exact polynomial identities, weighted complex invariant,')
print('projected output energy identity, sharp near-CFL gain, and interior notch')
