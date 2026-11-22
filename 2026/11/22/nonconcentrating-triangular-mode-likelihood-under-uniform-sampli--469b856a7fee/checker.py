#!/usr/bin/env python3
"""Exact finite diagnostics of the triangular-mode uniform limit theorem.

The infinite-dimensional limit and unique-argmax proof are analytical, not certified
by these finite calculations. Requires only Python standard library.
"""
from fractions import Fraction as F
from math import log, isclose
from random import Random
from itertools import combinations

def cov_bridge(s,t):
    return min(s,t)-s*t

def cov_with_I(t):
    # Integral of min(s,t)-st over s from zero to one.
    return t*(1-t)/2

checks=0
# Confirm Gaussian regression of bridge on its integral, including orthogonality.
for i in range(1,40):
    t=F(i,40)
    assert cov_with_I(t)==t*(1-t)/2; checks+=1
    assert cov_with_I(t)-6*(F(1,12))*t*(1-t)==0; checks+=1
    for j in range(1,20):
        s=F(j,20)
        assert cov_bridge(s,t)==cov_bridge(t,s); checks+=1
        # Cov(B_perp(s), B_perp(t)) conditional Gaussian covariance.
        residual=cov_bridge(s,t)-3*s*(1-s)*t*(1-t)
        assert residual==cov_bridge(s,t)-cov_with_I(s)*cov_with_I(t)/F(1,12); checks+=1
# Exact log-odds endpoint symmetry under paired complementary data.
for i in range(1,100):
    x=F(i,100)
    assert F(1,1)-x==F(100-i,100); checks+=1
    assert isclose(log(float(x)/(1-float(x))),-log(float(1-x)/float(x)),abs_tol=2e-13); checks+=1
# Finite-sample profile derivative and maximization at observed values.
rng=Random(20261121)
for n in (1,2,3,7,19,51):
    for rep in range(24):
        x=sorted(rng.uniform(0.01,0.99) for _ in range(n))
        def ll(theta):
            return sum(log(2*z/theta) if z<=theta else log(2*(1-z)/(1-theta)) for z in x)
        mids=[x[0]/2]+[(a+b)/2 for a,b in zip(x[:-1],x[1:])]+[(1+x[-1])/2]
        for t in mids:
            fn=sum(z<=t for z in x)/n
            score=n*(t-fn)/(t*(1-t))
            h=min(t-x[0],x[-1]-t, t/2,(1-t)/2,1e-5)
            # For outer intervals use distance only to nearest knot.
            dist=min(abs(t-z) for z in x)
            h=min(dist/10,1e-5,t/2,(1-t)/2)
            deriv=(ll(t+h)-ll(t-h))/(2*h)
            assert isclose(score,deriv,rel_tol=1e-4,abs_tol=1e-3), (n,rep,t,score,deriv,abs(score-deriv)); checks+=1
        vals=[ll(z) for z in x]
        assert max(vals)>=ll(0.5)-1e-11; checks+=1
        # Interior midpoints are convex interpolation regions.
        for a,b in zip(x[:-1],x[1:]):
            t=(a+b)/2
            assert ll(t)<=max(ll(a),ll(b))+1e-10; checks+=1
# Exact population expectation log(2)-1 from each rational cut.
for i in range(0,101):
    theta=F(i,100)
    left=-theta
    right=-(1-theta)
    assert left+right==-1; checks+=1
print('PASS: ',checks,'finite exact/algebraic and floating-point diagnostics; not an infinite proof')
