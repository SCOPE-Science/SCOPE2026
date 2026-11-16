#!/usr/bin/env python3
"""Independent finite checks for a four-tap Pauli-magnitude triangle theorem.

The classification proof is analytic; this program checks exact cubic-root
witnesses, the reconstruction identity and deterministic test configurations.
It is not a substitute for the all-parameter proof.
"""
from fractions import Fraction as F
from cmath import exp
from math import pi, acos, sqrt, isclose
from random import Random

class Eisenstein:
    """Exact Q(omega) coordinates a+b*omega, omega^2+omega+1=0."""
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    def __add__(self, other):
        o = coerce(other)
        return Eisenstein(self.a+o.a, self.b+o.b)
    __radd__ = __add__
    def __neg__(self): return Eisenstein(-self.a, -self.b)
    def __sub__(self, other): return self + -coerce(other)
    def __rsub__(self, other): return coerce(other) + -self
    def __mul__(self, other):
        o = coerce(other)
        return Eisenstein(self.a*o.a-self.b*o.b, self.a*o.b+self.b*o.a-self.b*o.b)
    __rmul__ = __mul__
    def conj(self): return Eisenstein(self.a-self.b, -self.b)
    def __eq__(self, other):
        o = coerce(other)
        return (self.a,self.b)==(o.a,o.b)
    def __repr__(self): return f'({self.a})+({self.b})omega'

def coerce(x):
    return x if isinstance(x, Eisenstein) else Eisenstein(x)

def corr(q):
    return [sum((q[j+k]*q[j].conj() for j in range(len(q)-k)), Eisenstein(0)) for k in range(len(q))]

omega=Eisenstein(0,1)
omega2=omega*omega
powers=[Eisenstein(1),omega,omega2]
for j in range(3):
    q=[Eisenstein(1),-F(3,2)*powers[(-j)%3],3*powers[j],Eisenstein(2)]
    assert corr(q)==[Eisenstein(F(65,4)),Eisenstein(0),Eisenstein(0),Eisenstein(2)]
    assert [v*v.conj() for v in q]==[Eisenstein(1),Eisenstein(F(9,4)),Eisenstein(9),Eisenstein(4)]
print('Exact Eisenstein-triple certificates: 3')

def corr_complex(q):
    return [sum(q[j+k]*q[j].conjugate() for j in range(len(q)-k)) for k in range(len(q))]

def pair(A,B,C,D):
    r,s= A*C,B*D
    k=D*D-A*A
    if not abs(r-s)+1e-10 < abs(k) < r+s-1e-10:
        raise ValueError('This magnitude vector is not in the strict triangle region')
    if abs(r-s)>1e-9:
        x=abs(s*s-r*r)/abs(k)
        theta=0 if k*(s*s-r*r)>0 else pi/2
        d=D*exp(1j*theta)
        proj=(x*x+r*r-s*s)/(2*x)
        height=sqrt(max(0,r*r-proj*proj))
        Us=[complex(proj,height), complex(proj,-height)]
        z=x
    else:
        d=D
        angle=pi/3 if k>0 else 0
        theta=acos(abs(k)/(2*r))
        Us=[r*exp(1j*(angle+theta)),r*exp(1j*(angle-theta))]
        z=0
    vectors=[]
    for U in Us:
        V=z-U
        b=(V/d).conjugate()
        c=U/A
        q=[complex(A),b,c,complex(d)]
        for x0,expect in zip(q,[A,B,C,D]):
            assert isclose(abs(x0),expect,rel_tol=1e-8,abs_tol=1e-8)
        vectors.append(q)
    v0,v1=vectors
    for x0,x1 in zip(corr_complex(v0),corr_complex(v1)):
        assert abs(x0-x1)<1e-7*(1+abs(x0))
    assert abs(v0[1]-v1[1])>1e-7
    assert A!=D

rng=Random(20260428)
checks=0
for A in range(1,6):
 for B in range(1,6):
  for C in range(1,6):
   for D in range(1,6):
    if A!=D and abs(A*C-B*D)<abs(A*A-D*D)<A*C+B*D:
     pair(A,B,C,D)
     checks+=1
assert checks>100
print('Full integer magnitude-grid reconstruction tests:',checks)
for _ in range(300):
 A,B,C,D=(rng.uniform(0.25,6.0) for j in range(4))
 if abs(A*C-B*D)<abs(A*A-D*D)<A*C+B*D:
    pair(A,B,C,D)
    checks+=1
print('Integer and real-valued reconstruction checks:',checks)
print('Standalone verification checks passed; universal assertions require the written proof.')
