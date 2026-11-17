#!/usr/bin/env python3
"""Numerical checks for the S^3 spherical nearest-vertex law of two orthogonal regular polygons.
Uses only the Python standard library; computations are checks, not the general proof.
"""
import math
import random


def parameters(p, q):
    assert isinstance(p, int) and p >= 3 and isinstance(q, int) and q >= 3
    a, b = math.cos(math.pi/p), math.cos(math.pi/q)
    c = a*b / math.hypot(a, b)
    C = p*q*(a*a + b*b)**3.5 / (
        3*math.pi**2 * a**4 * b**4 * math.sin(math.pi/p) * math.sin(math.pi/q))
    return c, C


def near_tail_quadrature(p, q, epsilon, steps=4096):
    """Integrate the exact Haar law with an analytically integrated second angle.
    Valid for sufficiently small positive epsilon below the clipping thresholds.
    """
    a, b = math.cos(math.pi/p), math.cos(math.pi/q)
    theta, phi = math.pi/p, math.pi/q
    c, C = parameters(p, q)
    t = c + epsilon
    assert t < min(a,b)
    z0 = 1/t**2 - 1/b**2
    assert z0 > 1 and z0 < 1/a**2
    u0 = math.acos(1 / math.sqrt(z0))

    def integrand(u):
        z = 1/t**2 - 1/math.cos(u)**2
        if z <= 1:
            return 0.0
        v0 = math.acos(min(1.0, 1 / math.sqrt(z)))
        if v0 >= phi:
            return 0.0
        return (t*t / math.cos(u)**2 - 1) * (phi-v0) + t*t*(math.tan(phi)-math.tan(v0))

    assert steps % 2 == 0
    h = (theta-u0)/steps
    sm = integrand(u0) + integrand(theta)
    for j in range(1, steps):
        sm += (4 if j%2 else 2) * integrand(u0 + j*h)
    return p*q / math.pi**2 * sm*h/3


def direct_sample_cdf(p, q, threshold, seed=917, trials=80000):
    """Direct Gaussian-sphere sampling, independent of polar integration."""
    rng = random.Random(seed)
    count = 0
    cos_p = [math.cos(2*math.pi*j/p) for j in range(p)]
    sin_p = [math.sin(2*math.pi*j/p) for j in range(p)]
    cos_q = [math.cos(2*math.pi*j/q) for j in range(q)]
    sin_q = [math.sin(2*math.pi*j/q) for j in range(q)]
    for _ in range(trials):
        z = [rng.gauss(0, 1) for i in range(4)]
        s = math.sqrt(sum(v*v for v in z))
        z = [v/s for v in z]
        biggest = max(max(z[0]*cos_p[j] + z[1]*sin_p[j] for j in range(p)),
                      max(z[2]*cos_q[j] + z[3]*sin_q[j] for j in range(q)))
        count += biggest <= threshold
    return count/trials


def full_exact_integral(p,q,t, steps=400):
    """The exact double integral with midpoint quadrature, for noncritical t."""
    theta,phi = math.pi/p,math.pi/q
    total=0.0
    for i in range(steps):
        u=(i+0.5)*theta/steps
        upper=min(1.0,t*t / math.cos(u)**2)
        for j in range(steps):
            v=(j+0.5)*phi/steps
            lower=max(0.0,1-t*t / math.cos(v)**2)
            total+=max(0.0,upper-lower)
    return total / (steps*steps)


def run():
    for p,q in [(3,3),(3,5),(4,4),(4,5),(5,5),(5,7),(8,12)]:
        c,C=parameters(p,q)
        assert 0<c<1 and C>0
        for eps in [0.001,0.0005]:
            val=near_tail_quadrature(p,q,eps)
            ratio=val/(C*eps**3)
            assert 0.97<ratio<1.03,(p,q,eps,ratio)
        print(f"({p},{q}) c={c:.12f} C={C:.12f}: tail checks PASS")
    # Independent local tangent-volume derivation for the 4D cross-polytope.
    c,C=parameters(4,4)
    assert abs(c-0.5)<1e-14
    assert abs(C-512/(3*math.pi**2))<1e-12
    print("Cross-polytope independent tangent-simplex coefficient: PASS")
    # Away from the tail, compare an entirely separate direct Gaussian-sphere experiment.
    for p,q,t in [(4,5,0.75),(3,5,0.7),(5,5,0.8)]:
        exact=full_exact_integral(p,q,t)
        sampled=direct_sample_cdf(p,q,t)
        assert abs(exact-sampled)<0.012,(p,q,t,exact,sampled)
        print(f"({p},{q}) t={t}: direct sampling {sampled:.5f}, integral {exact:.5f}: PASS")
    print("ALL TESTS PASSED")

if __name__ == '__main__':
    run()
