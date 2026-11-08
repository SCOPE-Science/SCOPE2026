#!/usr/bin/env python3
"""Standalone arithmetic and seeded simulation checks for the Gaussian tensor-train identity-risk law."""
from fractions import Fraction
from math import isclose


def identity_risk(d: int, n: int, r: int) -> Fraction:
    """Exact Var(||omega||^2) / ||I_(n**d)||_F^2, with Gaussian cores."""
    assert d >= 2 and n >= 1 and r >= 1
    e, eta = Fraction(1, n), Fraction(1, r)
    u = 1 + 2 * e * eta
    v = e + eta + e * eta
    for _ in range(2, d):
        u, v = u + 2 * e * eta * v, eta * u + e * (1 + eta) * v
    return n**d * (u + 2 * e * v - 1)


def check():
    count = 0
    for d in range(2, 9):
        for n in range(1, 8):
            for r in range(1, 10):
                x = identity_risk(d, n, r)
                assert x > 2
                if r == 1:
                    assert x == n**d * (Fraction(n + 2, n)**d - 1)
                if d == 2:
                    assert x == Fraction(2 * (2*n + r + 1), r)
                if d == 3:
                    expected = Fraction(2*(2*n*n*r+n*n+2*n*r+4*n+r*r+2*r+1), r*r)
                    assert x == expected
                count += 1
    for d in range(2, 7):
        for n in range(2, 9):
            prev = identity_risk(d, n, 1)
            for r in range(2, 32):
                current = identity_risk(d, n, r)
                assert current < prev
                prev = current
                count += 1
    # Fixed-order, critical-rank scaling: approach to 2 + 4/c.
    for d in range(2, 6):
        for c in (Fraction(1, 2), Fraction(1), Fraction(3)):
            n = 90 if d <= 3 else 18
            r = max(1, round(float(c*n**(d-1))))
            exact = float(identity_risk(d, n, r))
            target = 2 + 4 / float(c)
            assert abs(exact - target) < 0.5
            count += 1
    # Long-chain square-root bond-rank scaling, from the exact transfer.
    def fourth_ratio_float(d, n, r):
        e, eta = 1.0/n, 1.0/r
        u, v = 1 + 2*e*eta, e+eta+e*eta
        for _ in range(2, d):
            u, v = u+2*e*eta*v, eta*u+e*(1+eta)*v
        return u+2*e*v
    from math import sqrt, exp
    for n, c in ((2,1.0),(3,1.0),(3,2.0),(5,1.0)):
        d = 100000
        r = round(c*sqrt(d))
        q = fourth_ratio_float(d,n,r)
        target = exp(2/((n-1)*c*c))
        assert abs(q-target)/target < .03, (n,c,q,target)
        count += 1
    # Independent random-core numerical check; not used as proof.
    try:
        import numpy as np
    except ImportError:
        print(f"VERIFY_OK {count} exact checks; numpy not installed, optional simulation skipped")
        return
    rng = np.random.default_rng(20261103)
    for d,n,r,trials in ((2,2,2,80000),(3,2,2,90000),(3,3,2,100000)):
        stats = []
        for _ in range(0, trials, 2000):
            batch = min(2000, trials - len(stats))
            core = rng.normal(size=(batch,n,r))
            for _j in range(2, d):
                next_core = rng.normal(size=(batch,r,n,r))
                core = np.einsum('bit,btju->biju',core,next_core, optimize=True).reshape(batch,-1,r)
            terminal = rng.normal(size=(batch,r,n))
            tensor = np.matmul(core,terminal) / (r ** ((d-1)/2))
            norms = np.sum(tensor*tensor,axis=(1,2))
            stats.extend(norms.tolist())
        sample = np.var(stats, ddof=1) / (n**d)
        expected = float(identity_risk(d,n,r))
        assert abs(sample-expected)/expected < .19, (d,n,r,sample,expected)
        count += 1
    print(f"VERIFY_OK {count} exact/simulation checks")


if __name__ == '__main__':
    check()
