"""Exact rational and independent sampling checks for a signed order polytope.

Run with: python3 checker.py
Requires only the Python standard library.
"""
from fractions import Fraction as F
from math import factorial, sqrt
from random import Random


def beta_int(a, b):
    """Integral from 0 to 1 of t**a * (1-t)**b, a,b nonnegative."""
    return F(factorial(a) * factorial(b), factorial(a + b + 1))


def analytic_strata(n):
    # Exact integrations in the three ordered sign-strata configurations.
    assert n >= 2
    vol_cap = beta_int(0, n - 1)
    assert vol_cap == F(1, n)
    vol = 1 + n * vol_cap
    assert vol == 2
    cube_cube = F(1, 4) * F(2, 2**n)
    # When one point lies in a negative cap, it must be the smaller point.
    mixed = F(1, 2) * n * beta_int(0, 2*n - 2) / (2**(n-1))
    # With both points in the same cap, integrate t >= u, then double.
    both = F(1, 4*n) * 2 * n*n * beta_int(1, 2*n - 2) / (2**(n-1))
    return (cube_cube, mixed, both)


def sample_cube_rejection(n, rng):
    """Independent ambient-cube rejection, not a stratum-mixture sampler."""
    while True:
        z = [2*rng.random()-1 for _ in range(n)]
        a, b = sorted(z)[:2]
        if a+b >= 0:
            return z


def run():
    for n in range(2, 81):
        c0, c1, c2 = analytic_strata(n)
        p = F(n, 2**(n-1)*(2*n-1))
        assert c0+c1+c2 == p
        assert c0/p == F(2*n-1, 4*n)
        assert c1/p == F(1, 2)
        assert c2/p == F(1, 4*n)
        assert p < F(1, 2**(n-1))
        assert F(n, 2*n-1) > F(1, 2)
    rng = Random(161127)
    samples=0
    for n in (2,3,4,5,6):
        tested=48000
        counts=[0,0,0]
        for _ in range(tested):
            x=sample_cube_rejection(n,rng)
            y=sample_cube_rejection(n,rng)
            cmp=all(a<=b for a,b in zip(x,y)) or all(b<=a for a,b in zip(x,y))
            if cmp:
                negatives=sum(v<0 for v in x)+sum(v<0 for v in y)
                assert negatives in (0,1,2)
                counts[negatives]+=1
        actual=sum(counts)/tested
        expected=float(F(n,2**(n-1)*(2*n-1)))
        # Normal 7-sigma tolerance on a binomial variable, plus small slack.
        tolerance=7*sqrt(expected*(1-expected)/tested)+0.001
        assert abs(actual-expected)<tolerance,(n,actual,expected)
        # The fractions of sign-strata among comparable draws are diagnostics.
        if n<=5:
            assert abs(counts[1]/sum(counts)-0.5)<0.06,(n,counts)
        samples+=tested
    print(f"SIGNED_POSITIVE_PAIR_COMPARABILITY_PASS exact_dimensions=79 ambient_rejection_pairs={samples}")

if __name__=='__main__':
    run()
