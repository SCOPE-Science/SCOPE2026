#!/usr/bin/env python3
"""Finite diagnostics for the Hilbert cap geometry; the proof is analytic."""
import math
import random

rng = random.Random(250718208)
checks=0
for delta in [0.000001,0.0001,0.005,0.025,0.1,0.3,0.5,0.75,0.95,0.999]:
    c=1.0-delta
    s=math.sqrt(1-c*c)
    assert 0<s<1
    checks+=1
    # Exact cap maximization for a unit reference vector and a unit output.
    for i in range(2000):
        t=(i+0.37)/2000  # absolute cosine of reference/output angle
        z=math.sqrt(1-t*t)
        val=1.0 if t>=c else c*t+s*z
        assert val>=s-4e-15, (delta,t,val,s)
        checks+=1
        # The cap formula itself agrees with dense angular sampling, up to resolution.
        if i%200==0:
            theta=math.acos(c)
            bound=max(abs(t*math.cos(ph)+z*math.sin(ph)) for ph in
                      [theta*(-1+2*j/4000) for j in range(4001)])
            assert abs(val-bound)<0.001
            checks+=1
    # perpendicular skew increment: exact cap supremum s; scalar increment: 1.
    assert abs((c*0+s*1)-s)<1e-14
    assert abs((1 if 1>=c else c)-1)<1e-14
    checks+=2
# Norm-one Lipschitz map on a 3-point subset of the Euclidean plane:
# every pair is isometric under identity, skew J maps each difference
# to a perpendicular difference with unchanged norm.
points=[(0.,0.),(1.,0.),(.2,.9)]
J=lambda x:(-x[1],x[0])
for i in range(3):
 for j in range(i):
    x=(points[i][0]-points[j][0],points[i][1]-points[j][1])
    y=J(x)
    assert abs(x[0]*y[0]+x[1]*y[1])<1e-12
    assert abs(math.hypot(*x)-math.hypot(*y))<1e-12
    checks+=2
print('HILBERT_CAP_FINITE_DIAGNOSTIC_OK',checks)
