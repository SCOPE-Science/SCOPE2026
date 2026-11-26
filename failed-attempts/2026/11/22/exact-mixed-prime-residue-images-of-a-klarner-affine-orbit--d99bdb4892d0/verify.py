#!/usr/bin/env python3
"""Independent finite checks for residue images of the Klarner orbit.

Uses only the Python standard library. A finite search is not a proof for all moduli.
"""
from collections import deque
from math import gcd


def orbit_image(m):
    """Exact smallest forward-invariant subset of Z/mZ containing 0."""
    assert m >= 1
    seen = {0}
    queue = deque([0])
    while queue:
        x = queue.popleft()
        for y in ((2*x) % m, (3*x+2) % m, (6*x+3) % m):
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen


def theoretical_image(b, u):
    """The theorem's explicit union at m=2*3**b*u, 3∤u and u odd."""
    assert b >= 1 and u >= 1 and gcd(u, 6) == 1
    m = 2 * 3**b * u
    out = {x for x in range(0, m, 2)}
    for j in range(b):
        residue, step = (4*3**j-1) % (2*3**(j+1)), 2*3**(j+1)
        out.update(range(residue, m, step))
    out.update(range((m-1) % (2*3**b), m, 2*3**b))
    return out


def main():
    checks = 0
    for b in range(1, 8):
        for u in (1, 5, 7, 11, 13, 17, 25, 35):
            m = 2 * 3**b * u
            actual = orbit_image(m)
            target = theoretical_image(b, u)
            assert actual == target, (b, u, sorted(actual ^ target)[:20])
            assert len(actual) == u * (3**(b+1) + 1) // 2
            checks += 1
    for N in (1, 5, 7, 11, 13, 15, 21, 27, 35, 45, 81, 105, 315, 945):
        assert N % 2 == 1
        assert orbit_image(N) == set(range(N))
        checks += 1
    assert orbit_image(6) == {0, 2, 3, 4, 5}
    assert orbit_image(18) == theoretical_image(2, 1)
    print('PASS', checks, 'exact modular-image and count comparisons')

if __name__ == '__main__':
    main()
