#!/usr/bin/env python3
"""Finite diagnostics for near-minimal random orthotope shadows.

Run with Python 3, numpy and scipy. Not a proof of asymptotic statements.
"""
import math
import numpy as np


def sphere_area(d):
    return 2 * math.pi ** (d / 2) / math.gamma(d / 2)


def low_two_term(w, t):
    d = len(w)
    m = min(w)
    scale = 2**d * t**(d-1) / (sphere_area(d) * math.factorial(d-1))
    return scale * sum((1 + m*t/d * sum(w[j]**(-2) for j in range(d) if j != i)) /
                       math.prod(w[j] for j in range(d) if j != i)
                       for i in range(d) if abs(w[i]-m) < 1e-12)


def rare_integral(w, threshold, centers, t, n=380000, seed=111):
    """Unbiased local surface-Jacobian integration on oversized tangent crosspolytopes.

    For the tested cases, each rare spherical pole region is contained in one
    of these domains. The factor of two accounts for antipodal pole signs.
    """
    d = len(w)
    rng = np.random.default_rng(seed)
    total, moments = 0., {}
    for i in centers:
        idx = [j for j in range(d) if j != i]
        # Oversized l1-ball with positive coordinate weights w_j.
        R = 1.35 * t
        z = rng.dirichlet(np.ones(d), size=n)[:, :d-1]
        signs = rng.choice([-1,1], size=(n,d-1))
        x = signs * z * R / np.array([w[j] for j in idx])
        r2 = (x*x).sum(axis=1)
        assert np.max(r2)<0.5
        area = 2**(d-1) * R**(d-1) / (math.factorial(d-1) *
                                        math.prod(w[j] for j in idx))
        B = w[i]*np.sqrt(1-r2) + np.sum(np.abs(x)*np.array([w[j] for j in idx]),axis=1)
        chosen = (B < threshold)
        jac = 1/np.sqrt(1-r2)
        contribution = 2*area/sphere_area(d) * np.mean(chosen*jac)
        total+=contribution
        # Conditional normalized first-coordinate and remaining-budget moments.
        budget = (w[idx[0]] * np.abs(x[:,0])) / max(threshold-w[i], 1e-15)
        moments[i] = (float(np.mean(chosen)),
                      float(np.sum(chosen*jac*budget)/np.sum(chosen*jac)) if np.any(chosen) else None)
    return total, moments


def run():
    # Independent sphere-sampling check for the geometric projection identity:
    # orthotope hyperplane shadow volume is the weighted absolute normal sum.
    rng = np.random.default_rng(20261109)
    a = np.array([0.8, 1.1, 1.6, 2.3])
    w = np.array([np.prod(a)/z for z in a])
    normal = rng.normal(size=(250000,4))
    normal /= np.linalg.norm(normal,axis=1)[:,None]
    projected = np.sum(np.abs(normal)*w,axis=1)
    assert projected.min() > min(w)
    assert projected.max() < np.linalg.norm(w)
    assert abs(np.mean(projected) - (math.gamma(2)/(math.sqrt(math.pi)*math.gamma(2.5)))*np.sum(w)) < .014

    # Two-term fixed-shape asymptotic: all four-dimensional facet areas distinct.
    fixed = [1.,1.4,2.,3.]
    for t in [.02, .04, .07]:
        observed,diag = rare_integral(fixed,1+t,[0],t,n=390000,seed=1111)
        expected=low_two_term(fixed,t)
        relative=abs(observed/expected-1)
        print('fixed_d4',t,observed,expected,relative)
        assert relative<.034,(t,observed,expected,relative)

    # Coalescing facets: two limiting face areas differ by alpha*t; for alpha>1
    # the second is unable to contribute to the event in the limit.
    c=1.9
    for alpha in [0., .35, .8,1.0,1.4]:
        t=.027
        w=[1.,1+alpha*t,c,c]
        observed,moments=rare_integral(w,1+t,[0,1],t,n=430000,seed=int(3000+100*alpha))
        expected=(4/(3*math.pi**2*c*c))*(1+max(1-alpha,0)**3)*t**3
        relative=abs(observed/expected-1)
        print('facet_coalescence_d4',alpha,observed,expected,relative, 'first_dirichlet_coordinate',moments[0][1])
        assert abs(moments[0][1]-.25)<.018
        assert relative<.045,(alpha,observed,expected,relative)

    print('ORTHOTOPE_MINIMUM_SHADOW_PHASE_OK')

if __name__=='__main__':run()
