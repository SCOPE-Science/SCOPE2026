#!/usr/bin/env python3
"""Independent numerical checks for sharp five-node trigonometric-quadrature positivity."""
import itertools
import math
import random
import numpy as np

pi = math.pi
h = 2*pi/5
alpha0 = (5/(4*pi))*math.acos(math.cos(pi/5)-1)-0.5
r0 = pi*alpha0/5

def numerator_formula(others):
    a,b,c,d=others
    return (math.cos((a+b-c-d)/2)+math.cos((a+c-b-d)/2)+math.cos((a+d-b-c)/2))/8

def numeric_weights(deltas):
    x=h*(np.arange(5)+np.array(deltas))
    Q=np.vstack([np.ones(5), np.cos(x),np.sin(x),np.cos(2*x),np.sin(2*x)])
    w=np.linalg.solve(Q,np.array([1,0,0,0,0],dtype=float))
    return w

def lgr_weight(deltas,j):
    x=h*(np.arange(5)+np.array(deltas)); t=x[j]; o=[x[(j+k)%5]+(2*pi if j+k>=5 else 0) for k in range(1,5)]
    den=math.prod(math.sin((t-xx)/2) for xx in o)
    # even number of sine factors, all strictly negative, so den > 0.
    return numerator_formula(o)/den

def S(s,alpha):
    r=pi*alpha/5
    A=-s[0]-s[1]+s[2]+s[3]
    B=-s[0]+s[1]-s[2]+s[3]
    C=-s[0]+s[1]+s[2]-s[3]
    return math.cos(4*pi/5+r*A)+math.cos(2*pi/5+r*B)+math.cos(r*C)

assert 0.2<alpha0<0.202
assert abs(S((-1,1,-1,1),alpha0))<1e-13
assert S((-1,1,-1,1),0.24)<-0.07
for alpha in [0,0.01,0.1,0.18,0.2,alpha0]:
    vals=[S(s,alpha) for s in itertools.product((-1,1),repeat=4)]
    assert min(vals)>=-1e-12
    assert abs(min(vals)-S((-1,1,-1,1),alpha))<1e-12
rng=random.Random(314159)
for alpha in [0.04,0.10,0.19,alpha0,0.24]:
    for _ in range(250):
        ds=[rng.uniform(-alpha,alpha) for i in range(5)]
        weights=numeric_weights(ds)
        for j in range(5):
            assert abs(weights[j]-lgr_weight(ds,j))<3e-12,(alpha,j,weights[j],lgr_weight(ds,j))
        if alpha<=alpha0:
            assert min(weights)>-1e-12
for alpha in [alpha0-1e-4,alpha0,alpha0+1e-4,0.24]:
    w=numeric_weights([0,-alpha,alpha,-alpha,alpha])
    print(f'alpha={alpha:.12f}: w0={w[0]:.12g}, min_weight={min(w):.12g}')
print('alpha_crit=',format(alpha0,'.16f'))
print('all checks passed')
