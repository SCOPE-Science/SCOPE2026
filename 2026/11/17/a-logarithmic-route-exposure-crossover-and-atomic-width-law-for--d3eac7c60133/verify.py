#!/usr/bin/env python3
"""Reproducibility checks for Gaussian widths of parallel-route unit-flow simplices."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr, ndtri


def projection_radius(scores, lengths):
    """Width of orthogonal route simplex along unit projected Gaussian normal."""
    vec = np.asarray(scores, dtype=float) / np.sqrt(lengths)
    b = 1.0 / np.sqrt(np.asarray(lengths, dtype=float))
    perpendicular = vec - (np.dot(vec, b) / np.dot(b, b)) * b
    scores_projected = np.sqrt(lengths) * perpendicular
    return np.ptp(scores_projected) / np.linalg.norm(perpendicular)


def p_exact(m, ell, length):
    r = math.sqrt(length / ell)
    integrand = lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi) * ndtr(r*z)**m
    return quad(integrand, -10, 10, epsabs=1e-11, epsrel=1e-11)[0]


def run():
    rng = np.random.default_rng(20261110)
    deterministic = 0
    # Independently build edge-incidence route vectors, then project in their
    # affine-span direction to compare width to independent Gaussian scores.
    for lengths in ([2,3,4], [2,2,2,5], [3,3,3,3,3], [2,6,2,3,2,4]):
        m = len(lengths)-1
        lengths = np.asarray(lengths)
        ambient = sum(lengths)
        V = np.zeros((len(lengths),ambient))
        start=0
        for i,L in enumerate(lengths):
            V[i,start:start+L] = 1
            start += L
        basis = (V[1:]-V[0]).T
        Q,_ = np.linalg.qr(basis,mode='reduced')
        for _ in range(12):
            g = rng.standard_normal(ambient)
            u = Q@(Q.T@g)
            u /= np.linalg.norm(u)
            true_width = np.ptp(V@u)
            raw_scores = V@g
            formula_width = projection_radius(raw_scores,lengths)
            assert abs(true_width-formula_width)<5e-12,(lengths,true_width,formula_width)
            deterministic += 1
    # Exact Gaussian exposure integral vs an independent Monte Carlo draw.
    m=64; ell=3; L=27
    exact = 2*p_exact(m,ell,L)
    ordinary = rng.standard_normal((70000,m))*math.sqrt(ell)
    exceptional = rng.standard_normal(70000)*math.sqrt(L)
    exposure = (exceptional>ordinary.max(axis=1)) | (exceptional<ordinary.min(axis=1))
    observed=float(exposure.mean())
    assert abs(observed-exact)<0.014,(observed,exact)
    # Critical limit joint checks: atom mass equals nonexposure probability;
    # finite m should approximate the Gaussian-event prediction.
    comparisons=[]
    for c in [0.8,2.0,5.0]:
        m=3072; ell=2; L=max(2,round(c*ell*math.log(m)))
        b=math.sqrt(c); a=math.sqrt(2)
        z=rng.standard_normal(16000)
        regular=rng.standard_normal((16000,m))
        s0=math.sqrt(L)*z
        left=regular.min(axis=1)*math.sqrt(ell)
        right=regular.max(axis=1)*math.sqrt(ell)
        is_exposed=(s0>right)|(s0<left)
        expectation=2*(1-ndtr(a/b))
        # Actual finite rounded length determines slight difference from c.
        assert abs(np.mean(is_exposed)-expectation)<0.11,(c,L,np.mean(is_exposed),expectation)
        scaled=(np.maximum(right,s0)-np.minimum(left,s0))/math.sqrt(ell*math.log(m))
        a_finite=ndtri(1-1/m)/math.sqrt(math.log(m))
        b_finite=math.sqrt(L/(ell*math.log(m)))
        finite_proxy=a_finite+np.maximum(a_finite,b_finite*np.abs(z))
        assert abs(float(np.mean(scaled))-float(np.mean(finite_proxy)))<0.14,(c,L,float(np.mean(scaled)),float(np.mean(finite_proxy)))
        comparisons.append((c,L,round(float(np.mean(is_exposed)),4),round(float(expectation),4),round(float(np.mean(scaled)),4)))
    print('PARALLEL_PATH_WIDTH_PASS incidence_cases=%d exact_exposure=%.8f empirical_exposure=%.8f critical=%s' % (deterministic,exact,observed,comparisons))

if __name__=='__main__':run()
