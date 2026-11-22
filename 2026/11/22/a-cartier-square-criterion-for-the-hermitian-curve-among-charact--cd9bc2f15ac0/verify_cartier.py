#!/usr/bin/env python3
"""Exact finite-field consistency checks for the cyclic-quintic Cartier classification.

Pure Python, no third-party libraries. These finite checks supplement, rather
than replace, the symbolic proof valid over every algebraically closed field.
"""
from itertools import product


def gf_mul(x, y, modulus, degree):
    r = 0
    while y:
        if y & 1:
            r ^= x
        y >>= 1
        x <<= 1
        if x & (1 << degree):
            x ^= modulus
    return r


def gf_pow(x, e, mod, degree):
    r = 1
    while e:
        if e & 1:
            r = gf_mul(r, x, mod, degree)
        x = gf_mul(x, x, mod, degree)
        e >>= 1
    return r


def gf4mul(x, y):
    return gf_mul(x, y, 0b111, 2)


def gf4sqrt(x):
    return gf4mul(x, x)


def gf4rank(M):
    a = [row[:] for row in M]
    n, m = len(a), len(a[0])
    rank = 0
    for col in range(m):
        pivot = next((i for i in range(rank, n) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = gf_pow(a[rank][col], 2, 0b111, 2)
        a[rank] = [gf4mul(x, inv) for x in a[rank]]
        for i in range(n):
            if i != rank and a[i][col]:
                factor = a[i][col]
                a[i] = [u ^ gf4mul(factor, v)
                        for u, v in zip(a[i], a[rank])]
        rank += 1
    return rank


def gf4_matmul(A, B):
    return [[sum_xor(gf4mul(A[i][k], B[k][j]) for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def sum_xor(iterable):
    r = 0
    for x in iterable:
        r ^= x
    return r


# Basis of regular differentials indexed by degree-<=2 monomials h in
# h dx / y^4 on the smooth projective plane quintic y^5 = f(x).
BASIS = ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2))
INDEX = {ij: k for k, ij in enumerate(BASIS)}


def derived_cartier_matrix(a, b, c, d):
    # Compute the plane-curve Stoehr--Voloch mixed partial in characteristic 2:
    # C(h dx/F_y) = (partial_x partial_y (F*h))^(1/2) dx/F_y,
    # F = y^5 + x^4 + a*x^3 + b*x^2 + c*x + d, F_y = y^4.
    F = {(0, 5): 1, (4, 0): 1, (3, 0): a,
         (2, 0): b, (1, 0): c, (0, 0): d}
    M = [[0] * len(BASIS) for _ in BASIS]
    for j, (ih, jh) in enumerate(BASIS):
        for (ix, iy), coeff in F.items():
            ex, ey = ix + ih, iy + jh
            # Mixed partial only survives odd exponents in both variables.
            if (ex & 1) and (ey & 1):
                assert (ex - 1) % 2 == 0 and (ey - 1) % 2 == 0
                target = ((ex - 1) // 2, (ey - 1) // 2)
                assert target in INDEX, (target, a, b, c, d)
                M[INDEX[target]][j] ^= gf4sqrt(coeff)
    return M


def smooth_quartic(a, b, c, d):
    # f'=a*x^2+c. In characteristic 2, f'==0 iff a=c=0;
    # if a!=0 its only (double) root t satisfies t^2=c/a.
    if a == c == 0:
        return False
    if a == 0:
        return True
    ainv = gf_pow(a, 2, 0b111, 2)
    t = gf4sqrt(gf4mul(c, ainv))
    coeffs = (d, c, b, a, 1)
    val = 0
    for z in reversed(coeffs):
        val = gf4mul(val, t) ^ z
    return val != 0


def verify_all_quartics_over_f4():
    profile_counts = {}
    smooth_count = 0
    for a, b, c, d in product(range(4), repeat=4):
        if not smooth_quartic(a, b, c, d):
            continue
        smooth_count += 1
        M = derived_cartier_matrix(a, b, c, d)
        rank1 = gf4rank(M)
        # Cartier is inverse-Frobenius-semilinear; over F4 the inverse
        # Frobenius is squaring, so C^2 has matrix M*M^(2).
        M2twisted = [[gf4sqrt(x) for x in row] for row in M]
        P2 = gf4_matmul(M, M2twisted)
        rank2 = gf4rank(P2)
        # C^3 has matrix M * M^(2) * M^(4) = P2 * M over F4.
        P3 = gf4_matmul(P2, M)
        rank3 = gf4rank(P3)
        predicted = (3, 0 if (a == b == 0) else 1, 0)
        assert (rank1, rank2, rank3) == predicted, (a,b,c,d,rank1,rank2,rank3)
        profile_counts[predicted] = profile_counts.get(predicted, 0) + 1
    assert smooth_count == 4**4 - 4**3 == 192
    assert profile_counts == {(3,0,0): 12, (3,1,0): 180}
    print('GF4_SMOOTH_QUARTICS=192; CARTIER_PROFILES', profile_counts)


def verify_hermitian_maximality_f16():
    # F16=F2[t]/(t^4+t+1), standard irreducible polynomial 0b10011.
    # Count affine solutions to y^5=x^4+x and add the unique point at infinity.
    n = 1
    for x in range(16):
        rhs = gf_pow(x, 4, 0b10011, 4) ^ x
        for y in range(16):
            if gf_pow(y, 5, 0b10011, 4) == rhs:
                n += 1
    assert n == 65
    # genus six: Hasse--Weil upper bound 16+1+12*4=65.
    assert n == 16 + 1 + 2*6*4
    print('HERMITIAN_F16_POINTS=65; HASSE_WEIL_BOUND=65')


if __name__ == '__main__':
    verify_all_quartics_over_f4()
    verify_hermitian_maximality_f16()
    print('CYCLIC_QUINTIC_CHAR2_CARTIER_VERIFIED_OK')
