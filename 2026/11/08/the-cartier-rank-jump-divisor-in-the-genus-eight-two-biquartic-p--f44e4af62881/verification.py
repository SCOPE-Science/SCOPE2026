#!/usr/bin/env python3
"""Exact finite-field cross-check of the Cartier rank stratification.

Field F9 = F3[z]/(z*z+1).  This program does not use computer-algebra
packages.  Its finite sampling checks the algebraic theorem; it does not
replace its proof over all algebraically closed characteristic-three fields.
"""

from itertools import product

P = 3
Q = 9


def unpack(a):
    return (a % P, a // P)


def pack(a, b):
    return (a % P) + P * (b % P)


def add(a, b):
    u, v = unpack(a)
    w, z = unpack(b)
    return pack(u + w, v + z)


def neg(a):
    u, v = unpack(a)
    return pack(-u, -v)


def mul(a, b):
    u, v = unpack(a)
    w, z = unpack(b)
    return pack(u * w - v * z, u * z + v * w)


def power(a, n):
    r = 1
    while n:
        if n & 1:
            r = mul(r, a)
        a = mul(a, a)
        n >>= 1
    return r


def inverse(a):
    assert a
    return power(a, 7)


def cube_root(a):
    return power(a, 3)  # inverse of third-power Frobenius in F9


def rank(rows):
    x = [row[:] for row in rows]
    h = len(x)
    w = len(x[0]) if x else 0
    i = 0
    for j in range(w):
        p = next((t for t in range(i, h) if x[t][j]), None)
        if p is None:
            continue
        x[i], x[p] = x[p], x[i]
        inv = inverse(x[i][j])
        x[i] = [mul(v, inv) for v in x[i]]
        for t in range(h):
            if t != i and x[t][j]:
                f = x[t][j]
                x[t] = [add(v, neg(mul(f, u))) for v, u in zip(x[t], x[i])]
        i += 1
        if i == h:
            break
    return i


# The 8 regular differentials: five y^0 and three y^1 terms.
BASIS = [(-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0),
         (-2, 1), (-1, 1), (0, 1)]
INDEX = {v: i for i, v in enumerate(BASIS)}


def cartier_matrix(a, b, c, d, lam):
    # Laurent coefficients f = x^4 + a x^2 + c x + lam x^-4 + b x^-2 + d x^-1.
    f = {4: 1, 2: a, 1: c, -4: lam, -2: b, -1: d}
    mat = [[0] * 8 for _ in range(8)]
    for j, (i, y_exp) in enumerate(BASIS):
        if i % 3 == 2:
            ii = (i - 2) // 3
            mat[INDEX[(ii, y_exp)]][j] = 1
        if y_exp == 1:
            for e, coeff in f.items():
                if (i + e) % 3 == 2:
                    ii = (i + e - 2) // 3
                    k = INDEX[(ii, 0)]
                    mat[k][j] = add(mat[k][j], neg(cube_root(coeff)))
    return mat


def compose_cartier(mat):
    # If C(v) = M v^(1/3), then C^2(v)=M M^(1/3) v^(1/9).
    return [[sum_gf(mul(mat[i][j], cube_root(mat[j][k])) for j in range(8))
             for k in range(8)] for i in range(8)]


def sum_gf(values):
    r = 0
    for v in values:
        r = add(r, v)
    return r


def check():
    assert all(power(a, 9) == a for a in range(9))
    assert all(power(cube_root(a), 3) == a for a in range(9))
    assert len(set(BASIS)) == 8
    count_regular = 0
    count_special = 0
    for a, b, lam in product(range(9), range(9), range(1, 9)):
        for c, d in [(0,0), (1,0), (0,1), (2,2), (3,6), (7,8)]:
            M = cartier_matrix(a, b, c, d, lam)
            equality = mul(a, b) == lam
            assert rank(M) == (3 if equality else 4)
            M2 = compose_cartier(M)
            assert rank(M2) == 2
            assert all(not any(M2[row]) for row in range(8) if row not in (INDEX[(-1,0)], INDEX[(-1,1)]))
            if equality:
                count_special += 1
            else:
                count_regular += 1
    # In the symmetric one-parameter subfamily a=b=t, lam=1,
    # the rank drops at t=+1 or -1 in F3, and at no other t in F9.
    jumping = [t for t in range(9)
               if rank(cartier_matrix(t,t,0,0,1)) == 3]
    assert jumping == [1,2], jumping
    assert count_regular == 3504, count_regular
    assert count_special == 384, count_special
    print('field=F9, primitive_extension=z^2+1')
    print('tested_coefficients=3888 (648 triples (a,b,lam), six (c,d) choices)')
    print('generic_cartier_rank4_cases=' + str(count_regular))
    print('jump_cartier_rank3_cases=' + str(count_special))
    print('every_second_Cartier_rank=2')
    print('symmetric_jump_parameters_F9=[1,2]')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    check()
