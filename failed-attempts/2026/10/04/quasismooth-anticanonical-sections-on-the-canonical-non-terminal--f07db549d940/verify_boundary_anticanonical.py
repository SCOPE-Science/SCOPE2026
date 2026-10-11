#!/usr/bin/env python3
"""Exact regression checks for the boundary anticanonical theorem."""
from math import isqrt


def tau(n: int) -> int:
    s = 0
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            s += 1 if d*d == n else 2
    return s


def canonical(r: int, a: int, b: int) -> bool:
    d = b-a
    return 0 <= d <= r and a <= r+d


def terminal(r: int, a: int, b: int) -> bool:
    d = b-a
    return 0 <= d < r and a < r+d


def singleton_ok(D: int, w: int, other: int) -> bool:
    """Fletcher singleton test using outside weights 1 and `other`."""
    return D % w == 0 or (D-1) % w == 0 or (D-other) % w == 0


def qs_on_boundary(r: int, a: int, b: int) -> bool:
    """For canonical nonterminal boundary pairs, all larger strata are automatic.

    On b-a=r, z^2 has degree D, so only the a-axis singleton is nonautomatic.
    On a=r+(b-a), y^3 has degree D, so only the b-axis singleton is nonautomatic.
    At their intersection either test gives the same verdict.
    """
    d = b-a
    D = r+a+b
    checks = []
    if d == r:
        assert D == 2*b
        checks.append(singleton_ok(D, a, b))
    if a == r+d:
        assert D == 3*a
        checks.append(singleton_ok(D, b, a))
    assert checks
    return all(checks)


def explicit(r: int, a: int, b: int) -> bool:
    return ((b == a+r and ((2*r) % a == 0 or (2*r-1) % a == 0))
            or (a,b) == (r,r)
            or (a,b) == (2*r-1,3*r-2))


def boundary_pairs(r: int):
    # The triangular classification gives a<=2r and b<=3r on the boundary.
    for a in range(1, 2*r+1):
        for b in range(a, 3*r+1):
            if canonical(r,a,b) and not terminal(r,a,b):
                yield a,b


def main():
    for r in range(2,151):
        B=list(boundary_pairs(r))
        assert len(B)==3*r
        q=[p for p in B if qs_on_boundary(r,*p)]
        e=[p for p in B if explicit(r,*p)]
        assert q==e, (r,q,e)
        assert len(q)==tau(2*r)+tau(2*r-1)+1, (r,len(q))
    print('VERIFY_OK r=2..150')
    print('boundary_count=3r; quasismooth_count=tau(2r)+tau(2r-1)+1')

if __name__=='__main__':
    main()
