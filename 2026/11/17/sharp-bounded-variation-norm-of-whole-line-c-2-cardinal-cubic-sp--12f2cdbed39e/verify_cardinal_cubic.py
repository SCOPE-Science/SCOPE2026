#!/usr/bin/env python3
"""Independent algebraic and numerical checks for cubic cardinal interpolation variation."""
import math
import random
import sympy as sp

s=sp.sqrt(3); r=2-s; t=-r
alpha=sp.simplify((1-sp.sqrt(r))/(3-s))
K=sp.simplify((2+s+2*sp.sqrt(r))/3)
A=lambda z: -s+6*z-3*(3-s)*z*z
primitive=lambda z: -s*z+3*z*z-(3-s)*z**3
assert sp.simplify(t*t+4*t+1)==0
assert sp.simplify(A(alpha))==0
assert 0<float(alpha)<1
assert float(A(0))<0 and float(A(1))>0
# Exact reduction: step total variation is one plus the absolute tail-quadratic integral.
# Green kernel m_j = sqrt(3)(t**|j+1| - t**|j|).
def M(j):return s*(t**abs(j+1)-t**abs(j))
for j in range(-12,13):
    source=6*(int(j==-1)-int(j==0))
    assert sp.simplify(M(j-1)+4*M(j)+M(j+1)-source)==0
# Derivative on central step interval has positive minimum at both endpoints.
assert sp.simplify(M(-1)+M(0))==0
assert 1-float(M(-1))/6>0
# Shape of the tail derivative for j >= 0 has one critical zero alpha.
assert sp.simplify(M(0)+s*(1+r))==0
# Direct geometric total variation: center is 1; two tails are copies of zero-endpoint intervals.
# On each right interval derivative = M(j)*A(u)/6.
# Int abs A = -2*int_0^alpha A, and |M(0)|/(1-r)=3.
assert sp.simplify(abs(M(0)) if False else -M(0)-3*(1-r))==0
assert sp.simplify(1-2*primitive(alpha)-K)==0
print('EXACT_GREEN_RECURRENCE_AND_ALL_ORDER_STEP_TAILS_PASS')
print('EXACT_SHARP_NORM',K,'=',float(K),'turning_point=',float(alpha))

# Independent integration with arbitrary spline data using finite tridiagonal linear solves.
import numpy as np
from scipy.linalg import solve_banded

def numeric_variation(sample, radius=1, cut_margin=0):
    # y at consecutive integer knots, with natural end second derivatives 0.
    n=len(sample); b=np.zeros((3,n)); b[1,:]=4.0; b[0,1:]=1; b[2,:-1]=1
    rhs=np.zeros(n); rhs[1:-1]=6*(sample[2:]-2*sample[1:-1]+sample[:-2])
    # Natural boundary: enforce zero moments at finite ends independently.
    b[1,0]=b[1,-1]=1.;b[0,1]=0.;b[2,-2]=0.
    m=solve_banded((1,1),b,rhs)
    assert max(abs(m[0]),abs(m[-1]))<1e-12
    V=0.
    for j in range(n-1):
        d=float(sample[j+1]-sample[j]); a=float(m[j]);c=float(m[j+1])
        # q(u)=d+[a(-2+6u-3u^2)+c(-1+3u^2)]/6
        p=np.array([(c-a)/2, a, d-a/3-c/6])
        roots=np.roots(p)
        splits=[0.,1.]+[float(z.real) for z in roots if abs(z.imag)<1e-9 and 1e-12<z.real<1-1e-12]
        splits.sort()
        P=lambda z:p[0]*z*z*z/3+p[1]*z*z/2+p[2]*z
        V+=sum(abs(P(hi)-P(lo)) for lo,hi in zip(splits,splits[1:]))
    return V

rng=np.random.default_rng(20261114)
N=140
step=np.zeros(N);step[N//2:]=1.
val=numeric_variation(step)
assert abs(val-float(K))<2e-10,(val,float(K))
# Actual nontrivial BV vectors, comparison to analytical infinite bound.
for trial in range(1200):
    increments=np.zeros(N-1)
    count=int(rng.integers(1,16))
    ii=rng.choice(np.arange(15,N-16),size=count,replace=False)
    increments[ii]=rng.normal(size=count)
    data=np.r_[0,np.cumsum(increments)]
    amp=numeric_variation(data)
    bound=float(K)*np.abs(increments).sum()
    assert amp<=bound+4e-8,(trial,amp,bound)
print('INDEPENDENT_FINITE_MATRIX_AND_RANDOM_BV_STRESS_PASS 1200')
print('STEP_VARIATION_NUMERIC',repr(val))
print('ALL_CARDINAL_CUBIC_VARIATION_CHECKS_PASS')
