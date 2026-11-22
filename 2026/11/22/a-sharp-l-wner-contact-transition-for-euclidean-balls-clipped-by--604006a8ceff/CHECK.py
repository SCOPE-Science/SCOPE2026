#!/usr/bin/env python3
"""Independent numerical diagnostics for the ball--coaxial-cylinder theorem.

The exact global proof is analytic; finite grids below cannot certify it.
"""
import math

def predicted(d,s):
    c2=1-s*s
    x=min(1.0,1/(d*c2)) if c2>0 else 1.0
    u=(1-c2*x)/(s*s)
    return x,u

def objective(d,x,u):
    return math.log(x)+(d-1)*math.log(u)

tests=0
for d in (3,4,7,12):
    threshold=math.sqrt((d-1)/d)
    for s in (0.15,0.35,0.6,threshold,0.91,0.99):
        x,u=predicted(d,s)
        c2=1-s*s
        assert 0<x<=1+1e-11 and c2*x+s*s*u<=1+1e-11
        assert abs(c2*x+s*s*u-1)<1e-11
        if s>=threshold:
            assert abs(x-1)<1e-11 and abs(u-1)<1e-11
        else:
            assert abs(x-1/(d*c2))<1e-11
            assert abs(u-(d-1)/(d*s*s))<1e-11
            # Normalized rim contact has covariance I/d.
            assert abs(c2*x-1/d)<1e-11
            assert abs(s*s*u/(d-1)-1/d)<1e-11
        optimum=objective(d,x,u)
        # Independent one-dimensional feasibility/grid optimizer.
        gridbest=-float('inf')
        for j in range(1,20001):
            v=j/20001.0
            w=(1-c2*v)/(s*s)
            if w>0: gridbest=max(gridbest,objective(d,v,w))
        assert gridbest<=optimum+1e-8,(d,s,gridbest,optimum)
        assert optimum-gridbest<1e-2,(d,s,gridbest,optimum)
        tests+=1
print(f"All {tests} shape/containment/grid/contact checks passed")
