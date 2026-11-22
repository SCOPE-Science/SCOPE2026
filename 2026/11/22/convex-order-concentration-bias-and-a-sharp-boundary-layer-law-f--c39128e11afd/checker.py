"""Reproducibility checks for the common-center Poisson L2 projection theorem.

Only finite numerical diagnostics are performed here. All continuum assertions
rely on the analytic argument recorded in RESULT.md.
"""
import math
from itertools import product


def optimal(atoms):
    """A probability-weighted list of (nonnegative radius, mass) pairs."""
    assert abs(sum(p for x, p in atoms) - 1.0) < 1e-12
    assert all(0 <= x < 1 and p > 0 for x, p in atoms)
    positive = [(x, p) for x, p in atoms if x > 0]
    if not positive:
        return 0.0
    lo, hi = min(x for x, p in atoms), max(x for x, p in atoms)

    def F(t):
        return t / (1 - t * t) ** 2 - sum(
            p * x / (1 - t * x) ** 2 for x, p in atoms
        )

    for _ in range(90):
        mid = (lo + hi) / 2
        if F(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def loss(t, atoms):
    return 2 * (t * t / (1 - t * t)
        - 2 * sum(p * t * x / (1 - t * x) for x,p in atoms)
        + sum(p*q * x*y / (1 - x*y) for (x,p),(y,q) in product(atoms,repeat=2)))


def critical_tau(atoms):
    lo = min(a for a,p in atoms)
    hi = max(a for a,p in atoms)
    for _ in range(90):
        mid = (lo + hi)/2
        val = 4 * mid*mid * sum(p/(a+mid)**2 for a,p in atoms)
        if val < 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2


def limiting_error(tau, atoms):
    return 1/tau - 4*sum(p/(tau+a) for a,p in atoms) + 2*sum(
        p*q/(a+b) for (a,p),(b,q) in product(atoms,repeat=2))


def run():
    tests = 0
    assert optimal([(0.0,1.0)]) == 0.0
    tests += 1
    for x in (0.04, 0.2, 0.5, 0.9):
        assert abs(optimal([(x,1.0)])-x) < 1e-12
        assert abs(loss(x,[(x,1.0)])) < 2e-11
        tests += 2
    for m in (0.2,0.4,0.6,0.8):
        for spread in (0.01,0.04,0.08):
            assert 0 < m-spread < m+spread < 1
            atoms = [(m-spread,.5),(m+spread,.5)]
            t = optimal(atoms)
            assert m < t < m+spread
            assert loss(t,atoms) < loss(m,atoms)
            pred = m*(2+m*m)/((1-m*m)*(1+m*m))
            if spread==0.01:
                assert abs((t-m)/spread**2-pred) < 0.012
                tests+=1
            tests += 2
    for m in (0.3,0.6):
        for d in (0.02,0.07,0.12):
            assert 0<m-2*d < m+2*d<1
            narrow = [(m-d,.5),(m+d,.5)]
            wide = [(m-2*d,.5),(m+2*d,.5)]
            assert optimal(wide) > optimal(narrow)
            tests+=1
    base = [(1.0,.5),(3.0,.5)]
    tau = critical_tau(base)
    const = limiting_error(tau,base)
    assert abs(tau - 1.60113594287112) < 1e-11
    assert abs(const - 0.004319814028034) < 1e-10
    tests += 2
    for e in (0.004,0.001,0.00025):
        atoms = [(1-e*a,p) for a,p in base]
        t = optimal(atoms)
        assert abs((1-t)/e - tau) < 0.03
        assert abs(e*loss(t,atoms) - const) < 0.00018
        tests+=2
    for a,b in ((1,1.7),(1,3),(2,7),(1,10)):
        for w in (.1,.25,.5,.7,.9):
            nu=[(a,w),(b,1-w)]
            tau=critical_tau(nu)
            assert a < tau < w*a+(1-w)*b
            assert limiting_error(tau,nu)>0
            tests+=2
    print('PASS:',tests,'finite assertions; continuum proof is analytic')

if __name__=='__main__':
    run()
