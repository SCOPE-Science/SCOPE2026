#!/usr/bin/env python3
"""Supplementary finite numerical tests of a real 2x2 Schatten-plane norm formula."""
import math, numpy as np

def real_matrix(z,w):
    a,b=z.real,z.imag; c,d=w.real,w.imag
    return np.array([[a+c,-b+d],[b+d,a-c]],dtype=float)

def ratio(s,p,q):
    if np.allclose(s,0): return 0.
    num=float(np.max(s)) if math.isinf(q) else float(np.sum(s**q)**(1./q))
    return num/float(np.sum(s**p)**(1./p))

def g(r,p,q):
    return ratio(np.array([1+r,1-r],dtype=float),p,q)

rng=np.random.default_rng(144)
for _ in range(1500):
    z=complex(*rng.normal(size=2)); w=complex(*rng.normal(size=2))
    s=np.linalg.svd(real_matrix(z,w),compute_uv=False)
    expected=sorted([abs(z)+abs(w),abs(abs(z)-abs(w))],reverse=True)
    assert np.allclose(s,expected,rtol=1e-12,atol=1e-12)
for p,q in ((.5,.8),(.5,3.),(1.,2.),(1.,float('inf')),(2.,4.),(3.,float('inf'))):
    rr=np.linspace(0,1,501)
    assert np.all(np.diff([g(float(r),p,q) for r in rr])>0)
    for _ in range(20):
        u,v=np.linalg.qr(rng.normal(size=(2,2)))[0], np.linalg.qr(rng.normal(size=(2,2)))[0]
        sigma=np.array([rng.uniform(.01,.8),rng.uniform(.01,.8)])
        L=u@np.diag(sigma)@v.T
        rho=float(np.linalg.norm(L,2))
        assert abs(max(g(np.linalg.norm(L@np.array([math.cos(t),math.sin(t)])),p,q) for t in np.linspace(0,2*math.pi,501)) - g(rho,p,q))<2e-5
        # Numerically construct the graph in the 4D HS parameterization.
        E=np.vstack([np.eye(2),L]); Q,_=np.linalg.qr(E)
        P=Q@Q.T; P0=np.diag([1,1,0,0])
        gap=np.linalg.norm(P-P0,2)
        assert abs(gap-rho/math.sqrt(1+rho*rho))<1e-12
    r=1e-4; base=g(0,p,q)
    if math.isfinite(q):
        pred=base*(q-p)*r*r/2
        assert abs((g(r,p,q)-base)/pred-1)<2e-3
    else:
        assert abs((g(r,p,q)-base)/(base*r)-1)<2e-3
print('PASS singular values, monotonicity, full-graph norms, gaps and endpoint orders')
