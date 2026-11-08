"""Numerical and exact-finite-sum diagnostics for a shared-Gamma product model.

Run: python verify.py
Requires scipy (see requirements.txt). Numerical checks support but do not
replace the analytic asymptotic or conditional weak-limit arguments.
"""
from itertools import product
from math import exp, gamma, isfinite, lgamma, log, pi, sqrt
from scipy.integrate import quad
from scipy.special import gammaincc, kve


def asymptotic_log(a, bs, weights, t):
    m = len(bs)
    total = sum(weights)
    nu = a + m - sum(bs)
    return (
        log(pi) / 2 - lgamma(a) - sum(lgamma(v) for v in bs)
        + sum((v - 1) * log(w) for v, w in zip(bs, weights))
        + (nu / 2 - .25) * log(total)
        + ((a + sum(bs) - m) / 2 - .25) * log(t)
        - 2 * sqrt(total * t)
    )


def integer_shape_exact_log(a, bs, weights, t):
    """Exact finite Bessel-K expansion, evaluated in exponential scale."""
    assert all(isinstance(b, int) and b >= 1 for b in bs)
    total = sum(weights)
    z = 2 * sqrt(total * t)
    value = 0.
    for ks in product(*(range(b) for b in bs)):
        k = sum(ks)
        coefficient = 2 * exp(
            -lgamma(a) + sum(r * log(w*t) - lgamma(r+1) for r,w in zip(ks, weights))
            + ((a-k)/2) * log(total*t)
        )
        value += coefficient * kve(a-k,z)
    return log(value) - z


def quadrature_scaled(a, bs, weights, t):
    """Conditioning on the common factor; rescale by exp(2 sqrt(sum c_i t))."""
    total = sum(weights)
    s = sqrt(total*t)
    def f(u):
        if u <= 0: return 0.
        survival = 1.
        for b, w in zip(bs, weights):
            survival *= gammaincc(b,w*t/(s*u))
        return exp(-s*u+2*s)*u**(a-1)*survival
    # Integrate near saddle (u=1); tails beyond u=10 are negligible for t>=50.
    val = quad(f, 0, 10, epsabs=1e-13, epsrel=1e-11, limit=300, points=[1])[0]
    return (s**a/gamma(a))*val


def gig_moments(a, total, t):
    s = sqrt(total*t)
    z = 2*s
    ratio1 = kve(a+1,z)/kve(a,z)
    ratio2 = kve(a+2,z)/kve(a,z)
    mean = s*ratio1
    var = s*s*(ratio2-ratio1**2)
    return ((mean-s)/sqrt(s),var/s)


def main():
    assertions=0
    cases=[(1.,[1,1],[1.,1.]),(2.,[2,3],[1.,1.]),
           (1.7,[1,2,3],[2.,.5,1.5]),(3.,[1,3,2,4],[1.,2.,3.,4.])]
    for a,bs,weights in cases:
        old=1000.
        for t in (500.,2000.,8000.):
            logp = integer_shape_exact_log(a,bs,weights,t)
            assert isfinite(logp); assertions+=1
            ratio=exp(logp-asymptotic_log(a,bs,weights,t))
            assert 0.8<ratio<1.6; assertions+=1
            if t==8000.:
                assert abs(ratio-1)<.10; assertions+=1
            if t==2000.:
                assert ratio < old; assertions+=1
            old=ratio
    # Independent one-dimensional conditional-gamma quadrature agrees with
    # the exact Bessel-K expansion for integer shapes.
    for a,bs,weights,t in [(1.,[1,1],[1.,1.],70.),(2.,[2,3],[1.,2.],120.),
                           (1.7,[1,2,3],[2.,.5,1.5],150.)]:
        lhs=quadrature_scaled(a,bs,weights,t)
        rhs=exp(integer_shape_exact_log(a,bs,weights,t)+2*sqrt(sum(weights)*t))
        assert abs(lhs/rhs-1)<5e-9, (lhs,rhs); assertions+=1
    # b_i=1: the conditional mixing factor is exactly GIG, so verify
    # its centred mean tends to 0 and its scaled variance tends to 1/2.
    for a in (1.,2.3):
        means=[];variances=[]
        for t in (200.,2000.,10000.):
            mu,var=gig_moments(a,2.,t)
            means.append(abs(mu));variances.append(abs(var-.5))
            assert var>0 and abs(var-.5)<.09;assertions+=1
        assert means[-1]<means[0];assertions+=1
        assert variances[-1]<variances[0];assertions+=1
    print(f"PASS: {assertions} numerical identities and asymptotic diagnostics")

if __name__=='__main__':
    main()
