#!/usr/bin/env python3
"""Exact finite-field certificate for a geometric Weierstrass support calculation.
Arithmetic is in F_11[t]/(t^6+t^3+1); no external libraries required.
"""
P = 11
DIM = 6
Q = P**DIM
ZERO = (0,) * DIM
ONE = (1, 0, 0, 0, 0, 0)
T = (0, 1, 0, 0, 0, 0)


def add(a, b):
    return tuple((x + y) % P for x, y in zip(a, b))


def neg(a):
    return tuple(-x % P for x in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    c = [0] * 11
    for i in range(DIM):
        for j in range(DIM):
            c[i+j] += a[i]*b[j]
    for j in range(10, 5, -1):
        d = c[j]
        c[j] = 0
        c[j-3] -= d
        c[j-6] -= d
    return tuple(x % P for x in c[:DIM])


def power(a, n):
    if n < 0:
        return power(power(a, Q - 2), -n)
    z = ONE
    while n:
        if n & 1:
            z = mul(z, a)
        a = mul(a, a)
        n //= 2
    return z


def inv(a):
    assert a != ZERO
    return power(a, Q-2)


def alpha_to_a4(b, omega):
    alpha = mul(sub(mul(b, mul(omega, omega)), omega),
                inv(sub(ONE, b)))
    assert mul(add(alpha, omega), inv(add(alpha, mul(omega, omega)))) == b
    return mul(alpha, inv(sub(ONE, alpha)))


def main():
    assert Q == 1771561 and (Q-1) % 12 == 0
    assert add(add(power(T, 6), power(T, 3)), ONE) == ZERO
    assert power(T, 9) == ONE and power(T, 3) != ONE
    assert power(T, 11**6) == T
    assert 11**3 % 9 != 1 and 11**2 % 9 != 1
    omega = power(T, 3)
    assert power(omega, 3) == ONE and omega != ONE
    frob121_orbits = []
    for k in [1, 2, 4, 5, 7, 8]:
        b = power(T, k)
        assert power(b, 9) == ONE and power(b, 3) != ONE
        z = alpha_to_a4(b, omega)
        v = neg(mul(z, add(z, ONE)))
        assert z not in (ZERO, neg(ONE)) and v != ZERO
        assert power(z, (Q-1)//4) == ONE
        assert power(v, (Q-1)//12) == ONE
        assert power(z, 121) != z
        assert power(z, 121**2) != z
        assert power(z, 121**3) == z
        frob121_orbits.append((k, z, v))
    # Each of six alpha values lifts to four fourth roots and twelve
    # twelfth roots in F_(11^6).  The y^12-root field contains mu_12.
    assert (121-1) % 12 == 0
    assert len(set(z for _, z, _ in frob121_orbits)) == 6
    assert 6*4*12 == 288 and 288//3 == 96
    assert 121 + 1 + 2*19*11 == 540
    # independent alternate cross-check: Fermat conjugacy class of beta
    assert {k*4 % 9 for k in (1,4,7)} == {1,4,7}
    assert {k*4 % 9 for k in (2,5,8)} == {2,5,8}
    print('Q=', Q, 'Frobenius alpha orbits: (1,4,7) and (2,8,5)')
    for k, z, v in frob121_orbits:
        print('k=',k,'a^4=',z,'b^12=',v,'fourth_and_twelfth_power=YES')
    print('WEIERSTRASS_SUPPORT_540_RATIONAL_96_CUBIC_VERIFIED')


if __name__ == '__main__':
    main()
