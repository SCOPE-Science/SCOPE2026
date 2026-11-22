"""Reproduce exact dispersion witnesses and numerical boundary checks.

This checker verifies finite rational identities and selected numerical cases;
proof of universal statements is in RESULT.md, not inferred from testing.
"""
from fractions import Fraction as F
from math import exp, log, isclose


def rational_moments(shape, success):
    """Exact conditional moments of NB(shape, success) given positive count.

    Here NB(k) = (shape)_k/k! * (1-success)**shape * success**k.
    shape must be a positive integer for exact rational arithmetic.
    """
    r = F(shape)
    q = F(success)
    s = 1 - (1-q)**shape
    z = q/(1-q)
    mu = r*z/s
    factorial2 = r*(r+1)*z*z/s
    return mu, factorial2


def overdispersion(shape, success, retention):
    mu, fact2 = rational_moments(shape, success)
    B = mu-1
    A = fact2-2*mu+2
    t = F(retention)
    return -1 + A*t - B*B*t*t


def direct_finite_moments(shape, success, retention, stop=150):
    """Independent finite-sum approximation (not an exhaustive proof)."""
    r, q, t = shape, float(success), float(retention)
    nb = (1-q)**r
    normalizer = 1-nb
    mass = 0.0
    mean = 0.0
    second = 0.0
    for k in range(1, stop+1):
        nb *= (r+k-1)*q/k
        p = t*nb/normalizer
        if k == 1:
            p += 1-t
        mass += p
        mean += k*p
        second += k*k*p
    return mass, second-mean*mean-mean


def float_A_over_B(r,q):
    s = -__import__('math').expm1(r*__import__('math').log1p(-q))
    z = q/(1-q)
    mu = r*z/s
    factorial2 = r*(r+1)*z*z/s
    return (factorial2-2*mu+2)/(mu-1)


def bisection(f, lo, hi, iters=100):
    fa, fb = f(lo), f(hi)
    assert fa<0<fb
    for _ in range(iters):
        mid = (lo+hi)/2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def main():
    r=5
    q=F(3,10)
    mu,f2=rational_moments(r,q)
    assert mu == F(500000,194117)
    assert overdispersion(r,q,F(1)) == F(-421000000,37681409689)
    assert overdispersion(r,q,F(1,2)) == F(2479941473,21532234108)
    assert overdispersion(r,q,F(0)) == -1
    assert overdispersion(r,q,F(1)) < 0 < overdispersion(r,q,F(1,2))
    for t in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        mass, delta = direct_finite_moments(r,q,t)
        exact = float(overdispersion(r,q,t))
        assert abs(mass-1) < 1e-12 and abs(delta-exact) < 1e-11
    # Check strict inequalities and boundary position for sample real shapes.
    for r in (1.05,1.2,2.0,3.0,5.0,20.0,100.0):
        qd=bisection(lambda q:float_A_over_B(r,q)-2,1e-5,0.95)
        qc=1-(r+1)**(-1/r)
        assert 0 < qd < qc < 1
        for q in (qd*0.8,qd,(qd+qc)/2,qc,(1+qc)/2):
            s=1-(1-q)**r
            z=q/(1-q)
            mu=r*z/s
            f2=r*(r+1)*z*z/s
            B=mu-1
            A=f2-2*mu+2
            assert A < 2*B*B + 1e-8
        print(f"shape={r:g} q_d={qd:.12f} q_c={qc:.12f}")
    for r in (0.2,0.5,0.9,1.0):
        for q in (0.05,0.2,0.45,0.7,0.9):
            s=1-(1-q)**r
            z=q/(1-q)
            mu=r*z/s
            f2=r*(r+1)*z*z/s
            B=mu-1
            A=f2-2*mu+2
            assert A >= 2*B*B - 1e-8
    print('Exact rational witness and sampled numerical checks: PASS')


if __name__ == '__main__':
    main()
