#!/usr/bin/env python3
"""Independent integer checks for maximal lattice segments in a family of parallelograms.

The statements for arbitrary parameters are proved in RESULT.md; these bounded
checks provide a reproducible cross-check, not a substitute for the proof.
"""
from math import gcd


def predicted(q, k):
    assert q >= 2 and k >= 1
    a, r = divmod(k, q)
    diameter = (q + 2) * k - a - (r > 0)
    count = ((q - 1) * a + 1 if r == 0
             else (q - 1) * k + 1 - (r - 1) * (k - a - 1))
    return diameter, count


def independent_points(q, k):
    # Invert (x,y) = s(1,q)+t(q+2,1) without using slice bounds.
    determinant = q * (q + 2) - 1
    return [(x, y)
            for x in range(k * (q + 3) + 1)
            for y in range(k * (q + 1) + 1)
            if 0 <= (q + 2) * y - x <= k * determinant
            and 0 <= q * x - y <= k * determinant]


def brute(q, k):
    p = independent_points(q, k)
    diameter, n_segments, directions = 0, 0, set()
    for i, (x, y) in enumerate(p):
        for X, Y in p[i + 1:]:
            h = gcd(abs(X - x), abs(Y - y))
            if h > diameter:
                diameter, n_segments, directions = h, 0, set()
            if h == diameter and h > 0:
                n_segments += 1
                vx, vy = (X - x) // h, (Y - y) // h
                if vx < 0 or (vx == 0 and vy < 0):
                    vx, vy = -vx, -vy
                directions.add((vx, vy))
    return diameter, n_segments, directions


def slice_count(q, k):
    """Exact cross-sectional count using integer ceiling/floor, no residue formula."""
    L = q + 2
    D = (q + 2) * k - (k + q - 1) // q
    ans = 0
    for y in range(k * (q + 1) + 1):
        low_t, high_t = max(0, y - q * k), min(k, y)
        # x=(y+(q*L-1)*t)/q
        low_x_num = y + (q * L - 1) * low_t
        high_x_num = y + (q * L - 1) * high_t
        left = (low_x_num + q - 1) // q
        right = high_x_num // q
        if right - left == D:
            ans += 1
    return ans


def verify():
    n_brute = 0
    for q in range(2, 7):
        for k in range(1, 6):
            actual_d, actual_n, actual_dirs = brute(q, k)
            expected_d, expected_n = predicted(q, k)
            assert (actual_d, actual_n) == (expected_d, expected_n), (q, k)
            assert actual_dirs == {(1, 0)}, (q, k, actual_dirs)
            n_brute += 1
    n_slice = 0
    for q in range(2, 31):
        for k in range(1, 46):
            assert slice_count(q, k) == predicted(q, k)[1], (q, k)
            n_slice += 1
    print('PASS: %d full independent point-pair enumerations, %d exact integer slice counts.'
          % (n_brute, n_slice))
    print('All full enumerations also had unique primitive direction (1,0).')

if __name__ == '__main__':
    verify()
