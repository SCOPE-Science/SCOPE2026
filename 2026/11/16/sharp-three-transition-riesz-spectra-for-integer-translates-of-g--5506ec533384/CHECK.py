#!/usr/bin/env python3
"""Supplementary numerical checks for the exact translated Gaussian-Hermite Gram theorem.

Requires only the Python standard library. Numerical grids do not establish
infinite-dimensional spectral monotonicity; see the analytical proof.
"""
import math
q=math.exp(-math.pi/2)
def S(x,j):
    return sum((k+x)**j * math.exp(-2*math.pi*(k+x)**2) for k in range(-8,9))
def P(x,a): return S(x,2)+a*S(x,0)
def H(z):
    # First two terms suffice for high-accuracy evaluations of endpoint limits.
    # Evaluate Chebyshev U through recurrence.
    us=[1.,2*z]
    val=q+4*q**4*z
    for n in range(3,12):
        us.append(2*z*us[-1]-us[-2])
        val+=n*q**(n*n)*us[-1]
    return val
def R(x):
    # Exact Fourier derivative formulas; theta series truncated far below double precision.
    theta=2*math.pi*x
    d0=sum(-4*math.pi*n*q**(n*n)*math.sin(n*theta)/math.sqrt(2) for n in range(1,11))
    d2=sum((-4*math.pi*n/math.sqrt(2))*(1/(4*math.pi)-n*n/4)*q**(n*n)*math.sin(n*theta) for n in range(1,11))
    return -d2/d0
am=R(.5-1e-5);ap=R(1e-5)
astar=(S(.5,2)-S(0,2))/(S(0,0)-S(.5,0))
assert .142<am<.143 and .170<astar<.171 and .196<ap<.197
assert am<astar<ap
assert all(H(-1+2*i/1000)>.2 for i in range(1001))
for a in [0,am-.005,(am+astar)/2,astar,(astar+ap)/2,ap+.005,.35,1.]:
    arr=[P(i/2000,a) for i in range(1001)]
    amin=min(arr)
    assert abs(amin-min(P(0,a),P(.5,a)))<1e-12
    if a<am-.001: assert arr.index(max(arr))==1000
    if a>ap+.001: assert arr.index(max(arr))==0
    if am+.001<a<ap-.001: assert 0<arr.index(max(arr))<1000
print('CHECK_OK normalized_fourier=1 transitions=3 param_sets=8 grid_points=1001')
