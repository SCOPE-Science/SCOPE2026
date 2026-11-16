"""Reproduce finite-dimensional rank tests for two great-hypersphere traces.
The infinite-dimensional classification is established by the proof, not by these tests.
"""
import itertools
import math
import numpy as np
from fractions import Fraction


def exponents(d, n):
    if d == 1:
        return [(n,)]
    return [(k,) + y for k in range(n + 1) for y in exponents(d - 1, n - k)]


def restriction_matrix(d, ell, tangent):
    cols = exponents(d, ell)
    rows = {a: i for i, a in enumerate(exponents(d-1, ell))}
    a = np.zeros((len(rows), len(cols)))
    for col, exp in enumerate(cols):
        if tangent == 'infinity':
            if exp[0] == 0:
                key = exp[1:]
                a[rows[key], col] = 1
        elif tangent is None:
            if exp[1] == 0:
                key = exp[:1] + exp[2:]
                a[rows[key], col] = 1
        else:
            key = (exp[0] + exp[1],) + exp[2:]
            a[rows[key], col] = tangent ** exp[1]
    return a


def laplacian_matrix(d, ell):
    cols = exponents(d, ell)
    if ell < 2:
        return np.zeros((0, len(cols)))
    rows = {a: i for i, a in enumerate(exponents(d, ell-2))}
    a = np.zeros((len(rows), len(cols)))
    for col, exp in enumerate(cols):
        for k, power in enumerate(exp):
            if power >= 2:
                reduced = list(exp)
                reduced[k] -= 2
                a[rows[tuple(reduced)], col] += power * (power-1)
    return a


def expected_nullity(d, ell, q):
    if q is None:
        return 0
    ans = 0
    for k in range(1, ell // q + 1):
        ans += math.comb(ell-k*q+d-3, d-3)
    return ans


def numerical_nullity(d, ell, angle_type):
    if angle_type == 2:
        tangent = 'infinity'
    elif angle_type == 3:
        tangent = math.sqrt(3)
    elif angle_type == 4:
        tangent = 1.0
    else:
        tangent = 2.0
    matrix = np.concatenate([laplacian_matrix(d, ell),
                             restriction_matrix(d, ell, None),
                             restriction_matrix(d, ell, tangent)])
    s = np.linalg.svd(matrix, compute_uv=False)
    rank = int(sum(s > max(s) * 2e-9))
    return len(exponents(d, ell)) - rank


def rising(a, n):
    out = 1.0
    for j in range(n):
        out *= a+j
    return out


def main():
    checks = 0
    for d, max_ell in ((3, 7), (4, 6), (5, 4)):
        for ell in range(max_ell+1):
            for q in (2,3,4,None):
                observed = numerical_nullity(d, ell, q)
                expected = expected_nullity(d, ell, q)
                assert observed == expected, (d,ell,q,observed,expected)
                checks += 1
    for d in range(3,9):
        prev = float('inf')
        for ell in range(1,21):
            c = (rising(.5,ell)*rising(d/2,ell) /
                 (rising(1,ell)*rising((d-1)/2,ell)))
            assert c <= prev + 1e-10
            prev = c
            exact_ratio = (ell+.5)*(ell+d/2) / ((ell+1)*(ell+(d-1)/2))
            if ell < 20:
                next_c = (rising(.5,ell+1)*rising(d/2,ell+1) /
                          (rising(1,ell+1)*rising((d-1)/2,ell+1)))
                assert abs(next_c/c - exact_ratio) < 1e-10
            checks += 1
    print('PASS:', checks, 'finite independent rank/moment checks')
    for d,ell,q in ((4,3,3),(4,4,3),(5,5,2),(3,6,3)):
        print('example',d,ell,q,expected_nullity(d,ell,q))


if __name__ == '__main__':
    main()
