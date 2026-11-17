#!/usr/bin/env python3
"""Reproduce the exact two-shortest-geodesic crossing probability on a flat cylinder."""
import numpy as np
import sympy as sp

A, B = sp.symbols('A B', positive=True)
J1 = A*B*(1-B)-A**3/sp.Integer(3)
J2 = A*(1-A)*(1-B)-(1-B)**3/sp.Integer(3)
regions = [
    (J1, 0, sp.Rational(1,2), A, sp.Rational(1,2), sp.Rational(29,540)),
    (J1, 0, sp.Rational(1,2), sp.Rational(1,2), 1-A,
      -sp.Rational(139,540)+4*sp.log(2)/9),
    (J2, 0, sp.Rational(1,2), 1-A, 1,
      sp.Rational(47,144)-sp.Rational(125,288)*sp.log(2)),
    (J2, sp.Rational(1,2), 1, A, 1,
      sp.Rational(77,432)-sp.Rational(67,288)*sp.log(2)),
]
acc=sp.Integer(0)
for J, lowA, highA, lowB, highB, expected in regions:
    integrand=sp.expand(J/A)/4+sp.expand(J*A/B**2)/12
    value=8*sp.integrate(sp.integrate(integrand,(B,lowB,highB)),
                         (A,lowA,highA))
    assert sp.simplify(value-expected)==0, (value, expected)
    acc+=value
truth=sp.Rational(65,216)-sp.Rational(2,9)*sp.log(2)
assert sp.simplify(acc-truth)==0

# The absolute difference of independent uniforms on [-alpha,alpha] and
# [-beta,beta], alpha >= beta, has expectation alpha/2+beta**2/(6*alpha).
# Direct quadrature of the elementary conditional expectation tests it.
for alpha,beta in [(0.6,0.2),(1.7,1.7),(2.2,1.1)]:
    formula=alpha/2+beta**2/(6*alpha)
    y=np.linspace(-beta,beta,20001)
    avg=np.trapezoid((alpha*alpha+y*y)/(2*alpha), y)/(2*beta)
    assert abs(avg-formula)<1e-8

rng=np.random.default_rng(20261112)
theo=float(truth)
N=150000
for circumference,height in [(1.,1.),(12.,.07),(.03,20.)]:
    # Four independent endpoints, with uniform horizontal phase modulo L.
    horizontal_start=rng.random((N,2))*circumference
    endpoints=rng.random((N,4))*height
    horizontal_delta=rng.uniform(-circumference/2,circumference/2,(N,2))
    a=endpoints[:,1]-endpoints[:,0]
    b=endpoints[:,3]-endpoints[:,2]
    low=np.maximum(np.minimum(endpoints[:,0],endpoints[:,1]),
                   np.minimum(endpoints[:,2],endpoints[:,3]))
    high=np.minimum(np.maximum(endpoints[:,0],endpoints[:,1]),
                    np.maximum(endpoints[:,2],endpoints[:,3]))
    overlap=high-low
    slope=horizontal_delta[:,0]/a-horizontal_delta[:,1]/b
    start=(horizontal_start[:,0]-horizontal_start[:,1]
            +horizontal_delta[:,0]/a*(low-endpoints[:,0])
            -horizontal_delta[:,1]/b*(low-endpoints[:,2]))
    end=start+slope*overlap
    cross=(overlap>0)&(np.floor(np.minimum(start,end)/circumference)<
                          np.floor(np.maximum(start,end)/circumference))
    observed=float(np.mean(cross))
    se=np.sqrt(theo*(1-theo)/N)
    assert abs(observed-theo)<6*se, (circumference,height,observed,theo)
print('CYLINDER_CROSSING_CHECKS_OK')
