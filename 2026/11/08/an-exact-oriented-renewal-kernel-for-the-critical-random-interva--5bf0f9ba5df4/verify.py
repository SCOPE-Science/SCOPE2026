"""Supporting finite checks of an algebraic oriented first-return kernel.

Not an infinite-horizon proof; run with Python 3 and its standard library.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb

P, Q = Fraction(2, 3), Fraction(1, 3)

@lru_cache(None)
def admissible_paths(k, d, u):
    """Number of paths from depth k first hitting zero at its final step."""
    if k == 0:
        return int(d == 0 and u == 0)
    if d < 0 or u < 0:
        return 0
    if d + u == 0:
        return 0
    return admissible_paths(k - 1, d - 1, u) + admissible_paths(k + 2, d, u - 1)

count = 0
for k in range(1, 8):
    for u in range(0, 13):
        expected = k * comb(3*u+k, u) // (3*u+k)
        assert k * comb(3*u+k, u) % (3*u+k) == 0
        assert admissible_paths(k, 2*u+k, u) == expected
        count += 1

# Exact coefficient arrays of F(z,s), built by descent dynamic programming.
N = 11
F = {(k,u): Fraction(k, 3*u+k) * comb(3*u+k, u)
     * P**(2*u+k) * Q**u
     for k in range(1, N + 1) for u in range(N + 1) if k+3*u <= N}

# Enumerate the first-return law directly, over possible initial depth j.
# Input is uniform on one central cell, so the first-choice depth has geometric weights.
for n in range(1, N + 1):
    computed = [Fraction(0), Fraction(0)]
    # First map tau_1: j>=0, sign unchanged at this step.
    for j in range(n):
        if j == 0 and n == 1:
            computed[0] += P * Fraction(1, 2)
        if j > 0 and (n-1-j) % 3 == 0 and n-1 >= j:
            u = (n-1-j)//3
            value = P * Fraction(1, 2**(j+1)) * F[(j, u)]
            computed[u%2] += value
    # First map tau_2: depth 2, one initial side flip.
    if n-1 >= 2 and (n-3)%3 == 0:
        u = (n-3)//3
        value = Q * F[(2, u)]
        computed[(u+1)%2] += value

    # Direct finite path traversal from initial cells; only paths that first hit central at step n.
    by_path = [Fraction(0), Fraction(0)]
    for j in range(n):
        weight = P * Fraction(1, 2**(j+1))
        def walk(k, flips, remaining, mass):
            if k == 0:
                if remaining == 0:
                    by_path[flips % 2] += mass
                return
            if remaining == 0:
                return
            walk(k-1, flips, remaining-1, mass*P)
            walk(k+2, flips+1, remaining-1, mass*Q)
        walk(j, 0, n-1, weight)
    def walk2(k, flips, remaining, mass):
        if k == 0:
            if remaining == 0:
                by_path[flips%2] += mass
            return
        if remaining == 0:
            return
        walk2(k-1, flips, remaining-1, mass*P)
        walk2(k+2, flips+1, remaining-1, mass*Q)
    walk2(2, 1, n-1, Q)
    assert tuple(computed) == tuple(by_path), (n, computed, by_path)
    count += 2

# Root and exact switching transform check to safe numerical precision.
lo, hi = 0., 1.
for _ in range(70):
    mid = (lo + hi)/2
    if mid**3 + 3*mid - 2 < 0: lo = mid
    else: hi = mid
a = (lo + hi)/2
eta = 2/(3*(2-a)) - a*a/3
sigma = (1-eta)/2
assert abs(a**3 + 3*a - 2) < 1e-12
assert 0.3217878 < sigma < 0.3217880
assert 0 < eta < 1
print('PASS: supporting finite path and renewal coefficients:', count)
print('root a =',a,'side eigenvalue eta =',eta,'switch probability =',sigma)
