#!/usr/bin/env python3
"""Exact symbolic and numerical checks for a rank-one Sylvester sketch benchmark."""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad

A = sp.diag(1, 3)
B = sp.diag(2, 4)
E = sp.eye(2)
F = sp.Matrix([[1,0],[0,0]])
X = F
Y = -F
assert A*X+Y*B+F == sp.zeros(2)
assert E*X+Y*E == sp.zeros(2)
sep = sorted(abs(A[i,i]-B[j,j]) for i in range(2) for j in range(2))
assert sep == [1,1,1,3]
assert A.is_positive_definite and B.is_positive_definite
# Symbolic scalar projected equations, where s=u_2**2 and t=v_2**2.
s,t=sp.symbols('s t',real=True)
assert sp.simplify((1+2*s)-(2+2*t)-(2*(s-t)-1)) == 0
# Exact resonance density integral via t=(sinh r)^2/2.
r=sp.symbols('r', real=True, positive=True)
q=sp.sinh(r)**2/2
kernel=sp.simplify(sp.diff(q,r)/sp.sqrt(q*(q+sp.Rational(1,2))))
assert kernel == sp.Integer(2)
C=float(2*sp.asinh(1)/sp.pi**2)
assert math.isclose(C,0.1786036301358262,rel_tol=1e-13)

def conditional_probability(tval,R):
    a=0.5-tval
    d=math.sqrt(1-tval)/(2*R)
    if a>=0:
        v=math.sqrt(d*d+4*a)
        lo=max(0.,(v-d)/2)
        hi=min(1.,(v+d)/2)
    else:
        discr=d*d+4*a
        if discr<=0:return 0.
        v=math.sqrt(discr)
        lo=max(0.,(d-v)/2)
        hi=min(1.,(d+v)/2)
    return (2/math.pi)*(math.asin(hi)-math.asin(lo)) if hi>lo else 0.

def exact_tail_prob(R):
    cutoff=math.asin(math.sqrt(0.5))
    def f(theta):
        return (2/math.pi)*conditional_probability(math.sin(theta)**2,R)
    return quad(f,0,cutoff,epsabs=2e-11)[0]+quad(f,cutoff,math.pi/2,epsabs=2e-11)[0]

for R in [10,20,50,100,500]:
    p=exact_tail_prob(R)
    print('R=',R,'tail=',format(p,'.12g'),'R*tail=',format(R*p,'.12g'))
    assert abs(R*p-C)<0.02
print('EXACT_OPERATOR_CHECKS_OK; TAIL_CONSTANT=',repr(C))
