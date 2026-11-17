#!/usr/bin/env python3
"""Exact rational interval certificates for an asymptotic hypersimplex width-variance profile.

All interval calculations use rational arithmetic, not float arithmetic.
The only transcendental inputs are alternating series with explicit tail bounds.
"""
from fractions import Fraction as F
from math import factorial, isqrt

N = 64

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[1],-x[0])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a=[u*v for u in x for v in y]
    return (min(a),max(a))
def const(x): return (F(x), F(x))
def scale(x,y): return mul(x,const(y))
def sq(x):
    if x[0]>=0: return x[0]**2,x[1]**2
    if x[1]<=0: return x[1]**2,x[0]**2
    return F(0),max(x[0]*x[0],x[1]*x[1])

def alternation(term, next_term):
    return (min(term,term+next_term),max(term,term+next_term))

def atan_interval(z):
    z=F(z)
    s=sum(((-1)**j)*z**(2*j+1)/F(2*j+1) for j in range(N))
    return alternation(s,F((-1)**N)*z**(2*N+1)/F(2*N+1))

def exp_minus(y):
    y=F(y)
    s=sum((-y)**j/F(factorial(j)) for j in range(N))
    return alternation(s,(-y)**N/F(factorial(N)))

def gauss_integral(t):
    t=F(t)
    s=sum(F((-1)**j)*t**(2*j+1)/F((2*j+1)*2**j*factorial(j)) for j in range(N))
    next_term=F((-1)**N)*t**(2*N+1)/F((2*N+1)*2**N*factorial(N))
    return alternation(s,next_term)

pi=sub(scale(atan_interval(F(1,5)),16),scale(atan_interval(F(1,239)),4))
assert F(3141592653589793,10**15)<pi[0] and pi[1]<F(3141592653589794,10**15)

S=10**55

def sqrt_bounds(x):
    lo,hi=x
    assert 0<lo
    v_lo=isqrt((lo.numerator*S*S)//lo.denominator)
    v_hi=isqrt((hi.numerator*S*S)//hi.denominator)
    return (F(v_lo,S),F(v_hi+1,S))

def inv_positive(x): return (1/x[1],1/x[0])
phi0=inv_positive(sqrt_bounds(scale(pi,2)))

def variance_interval(t):
    t=F(t)
    p=mul(phi0,exp_minus(t*t/2))
    alpha=sub(const(F(1,2)),mul(phi0,gauss_integral(t)))
    m=sub(scale(p,2),scale(alpha,2*t))
    second=scale(sub(scale(alpha,1+t*t),scale(p,t)),2)
    var=sub(sub(second,sq(m)),scale(sq(p),2))
    return var

bounds={
 F(1,2):(F(1488,100000),F(1489,100000)),
 F(1,1):(F(581,100000),F(582,100000)),
 F(5,4):(F(787,100000),F(789,100000)),
 F(3,2):(F(870,100000),F(872,100000)),
 F(2,1):(F(541,100000),F(543,100000))
}
for t, (lo,hi) in bounds.items():
    a,b=variance_interval(t)
    assert lo<a<=b<hi,(t,float(a),float(b),float(lo),float(hi))
    print('CERTIFIED',str(t),'variance in',f'({float(lo):.5f},{float(hi):.5f})')

assert bounds[F(1,1)][1]<bounds[F(1,2)][0]
assert bounds[F(1,1)][1]<bounds[F(5,4)][0]
assert bounds[F(5,4)][1]<bounds[F(3,2)][0]
assert bounds[F(2,1)][1]<bounds[F(3,2)][0]
print('CERTIFIED: distinct interior local minimum and maximum exist for t>0')
print('HYPERSIMPLEX_DIRECTIONAL_WIDTH_CERTIFICATES_PASSED')
