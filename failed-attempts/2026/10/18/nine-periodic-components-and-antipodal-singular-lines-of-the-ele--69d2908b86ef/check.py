"""Exact finite checks for the singular scheme of the elementary symmetric cubic.

Run: python3 check.py. All arithmetic is over F_3; no third-party modules.
These tests supplement, and do not replace, the all-n algebraic proof.
"""
from itertools import product, combinations
from math import comb


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def reduced_membership(x):
    n = len(x)
    # Supported constant lines with cardinality 1 mod 9.
    for m in range(1, n + 1, 9):
        for S in combinations(range(n), m):
            T = set(S)
            if len({x[i] for i in S}) == 1 and all(x[i] == 0 for i in range(n) if i not in T):
                return True
    if n % 9 == 2:
        # The two-block planes, counted only once here if desired.
        for m in range(1, n, 9):
            for S in combinations(range(n), m):
                T = set(S)
                if len({x[i] for i in S}) == 1 and len({x[i] for i in range(n) if i not in T}) == 1:
                    return True
    if n % 9 in (5, 8):
        r = 7 if n % 9 == 5 else 4
        for m in range(r, n, 9):
            for S in combinations(range(n), m):
                T = set(S)
                a = x[S[0]]
                if all(x[i] == a for i in S) and all(x[i] == (-a) % 3 for i in range(n) if i not in T):
                    return True
    return False


def actual_singular(x):
    n = len(x)
    if sum(x[i] * x[j] * x[k] for i, j, k in combinations(range(n), 3)) % 3:
        return False
    for i in range(n):
        if sum(x[j] * x[k] for j, k in combinations((j for j in range(n) if j != i), 2)) % 3:
            return False
    return True


def rank_mod3(M):
    B = [[v % 3 for v in row] for row in M]
    i = 0
    for j in range(len(B[0])):
        k = next((k for k in range(i, len(B)) if B[k][j]), None)
        if k is None:
            continue
        B[i], B[k] = B[k], B[i]
        scale = pow(B[i][j], -1, 3)
        B[i] = [(v * scale) % 3 for v in B[i]]
        for k in range(len(B)):
            if k != i and B[k][j]:
                fac = B[k][j]
                B[k] = [(a - fac*b) % 3 for a, b in zip(B[k], B[i])]
        i += 1
        if i == len(B):
            break
    return i


def hessian(x):
    n = len(x)
    s = sum(x) % 3
    return [[0 if i == j else (s - x[i] - x[j]) % 3 for j in range(n)] for i in range(n)]


def count(n):
    axes = sum(binom(n, m) for m in range(1, n + 1, 9))
    if n % 9 == 2:
        planes = sum(binom(n, m) for m in range(1, n, 9)) // 2
        return {'planes': planes, 'degree': planes}
    r = (7 if n % 9 == 5 else 4 if n % 9 == 8 else None)
    signs = sum(binom(n, m) for m in range(r, n, 9)) // 2 if r is not None else 0
    mult = 3 if r is not None else 1
    return {'supported_lines': axes, 'sign_lines': signs, 'degree': mult * (axes + signs)}


def block_coefficients(m, ell):
    # e3 at (a^m,b^ell): coefficients ordered a^3,a^2b,ab^2,b^3
    return [binom(m,3)%3,binom(m,2)*ell%3,m*binom(ell,2)%3,binom(ell,3)%3]


def main():
    cases = 0
    for n in range(3, 10):
        for point in product(range(3), repeat=n):
            assert actual_singular(point) == reduced_membership(point), (n, point)
            cases += 1
    # Two-block polynomial identity, uniformly in broad residue classes.
    for n in range(3, 151):
        for m in range(1,n):
            ell = n-m
            if m % 3 == ell % 3 == 1:
                assert block_coefficients(m,ell) == [(m-1)//3%3, 0, 0, (ell-1)//3%3]
                # Both partial derivative quadratics vanish identically on this plane.
                F_a = (binom(m-1,2)%3, ((m-1)*ell)%3, binom(ell,2)%3)
                F_b = (binom(m,2)%3, (m*(ell-1))%3, binom(ell-1,2)%3)
                assert F_a == F_b == (0,0,0)
    # At a generic point of a two-block critical plane, Hessian corank 2.
    assert rank_mod3(hessian([1]*4+[2]*4)) == 6  # n=8, non-coordinate sign line
    assert rank_mod3(hessian([1]+[0]*7)) == 6  # n=8, coordinate line
    assert rank_mod3(hessian([1]+[2]*10)) == 9 # n=11, plane
    assert rank_mod3(hessian([1]+[0]*3)) == 3  # n=4, reduced coordinate line
    assert count(5) == {'supported_lines':5,'sign_lines':0,'degree':15}
    assert count(8) == {'supported_lines':8,'sign_lines':35,'degree':129}
    assert count(11) == {'planes':11,'degree':11}
    assert count(14) == {'supported_lines':1015,'sign_lines':1716,'degree':8193}
    print(f'CHECK_OK F3_points={cases} block_residue_cases=11000+ examples=(5,8,11,14)')


if __name__ == '__main__':
    main()
