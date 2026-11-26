#!/usr/bin/env python3
"""Reproduce exact matrix identities for paired planar subspace minimization."""

import numpy as np
import sympy as sp


def exact_integrals():
    t, x = sp.symbols('t x', positive=True, real=True)
    w = t*t / (t*t + x*x)
    overlap = (t*t - 1)**2*x*x / ((t*t + x*x)*(1 + t*t*x*x))
    expected = [
        (w, t/(t+1)),
        (w*w, t*(2*t+1)/(2*(t+1)**2)),
        (overlap, (t-1)**2/(t*t+1)),
        (overlap*w, t*(t-1)**2*(2*t*t+t+1)/(2*(t+1)*(t*t+1)**2)),
    ]
    for func, target in expected:
        result = sp.simplify(2*sp.integrate(sp.apart(func/(1+x*x), x), (x,0,sp.oo))/sp.pi)
        assert sp.factor(result-target) == 0, (func, sp.factor(result-target))
    delta2 = ((t*t-1)/(t*t+1))**2
    iid11 = (t*t+t+2)/(2*(t+1)**3)
    iid22 = t*(2*t*t+t+1)/(2*(t+1)**3)
    ortho11 = (t-1)**2*(t*t+t+2)/(2*(t+1)*(t*t+1)**2)
    ortho22 = t*(t-1)**2*(2*t*t+t+1)/(2*(t+1)*(t*t+1)**2)
    assert sp.factor(ortho11-delta2*iid11) == 0
    assert sp.factor(ortho22-delta2*iid22) == 0
    assert sp.factor(iid22-iid11) == (t-1)*(t*t+t+1)/(t+1)**3
    print('PASS: four symbolic Cauchy integrals and the exact two-step matrix identity.')


def angular_quadrature():
    n = 16384
    theta = 2*np.pi*(np.arange(n) + 0.5)/n
    u = np.stack([np.cos(theta), np.sin(theta)], axis=1)
    v = np.stack([-np.sin(theta), np.cos(theta)], axis=1)
    eye = np.eye(2)
    rng = np.random.default_rng(20261014)
    tested = 0
    for t in [1.0, 1.15, 1.7, 2.0, 3.0, 10.0, 24.0]:
        def proj(d):
            w = d*np.array([t,1.0])
            w = w/np.linalg.norm(w,axis=1)[:,None]
            return eye[None,:,:] - np.einsum('ni,nj->nij',w,w)
        p = proj(u); q = proj(v)
        a = np.mean(p,axis=0)
        orth = np.mean(p @ q @ p,axis=0)
        iid = np.mean(p @ a @ p,axis=0)
        theoretical_iid=np.diag([(t*t+t+2)/(2*(t+1)**3),t*(2*t*t+t+1)/(2*(t+1)**3)])
        theoretical_orth=((t*t-1)/(t*t+1))**2*theoretical_iid
        assert np.allclose(iid,theoretical_iid,atol=2e-12,rtol=1e-11)
        assert np.allclose(orth,theoretical_orth,atol=2e-12,rtol=1e-11)
        assert np.allclose(orth,((t*t-1)/(t*t+1))**2*iid,atol=2e-12,rtol=1e-11)
        for _ in range(30):
            e = rng.normal(size=2)
            numerator = e@orth@e
            denominator=e@iid@e
            assert abs(numerator - ((t*t-1)/(t*t+1))**2*denominator) <= 2e-11*denominator
            tested += 1
    print(f'PASS: seven full-circle deterministic matrix quadratures and {tested} error-vector tests.')
    print('Exact benchmark at condition number 4: iid max energy factor 11/27; paired max 11/75.')


if __name__ == '__main__':
    exact_integrals()
    angular_quadrature()
    print('PASS: all verification checks.')
