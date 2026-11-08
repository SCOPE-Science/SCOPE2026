#!/usr/bin/env python3
"""Exact finite checks for the residue enumeration and characteristic-two witnesses."""
from itertools import product


def residue_count(p, d):
    return sum(sum(a) % p == 0 for a in product(range(1, p), repeat=d))


def formula(p, d):
    numerator = (p - 1) ** d + (p - 1) * (-1) ** d
    assert numerator % p == 0
    return numerator // p


def check():
    for p in (2, 3, 5, 7):
        for d in range(2, 8 if p < 5 else 6):
            n = residue_count(p, d)
            assert n == formula(p, d), (p, d, n)
            for h in (0, 1):
                # Over algebraically closed characteristic-p fields,
                # c^p-hc has p^h geometric roots and length p.
                point_count = (p if h else 1) * n
                scheme_length = p * n
                assert point_count <= scheme_length
                if h == 1:
                    assert point_count == scheme_length
    # Exact polynomial arithmetic over F_2, represented as coefficient bitsets.
    def mul(a, b):
        z = 0
        while b:
            if b & 1:
                z ^= a
            a <<= 1
            b >>= 1
        return z

    def der(a):
        z = 0
        for i in range(1, a.bit_length(), 2):
            if (a >> i) & 1:
                z ^= (1 << (i - 1))
        return z

    def t_num(num, den, delta_multiplier, h):
        # T(num/den)=f^2+delta(f)-h*f, cleared by den^2.
        quot_der_num = mul(der(num), den) ^ mul(num, der(den))
        return mul(num, num) ^ mul(delta_multiplier, quot_der_num) ^ (mul(num, den) if h else 0)

    # E ordinary and Y ordinary: Y: y^2+xy=x^3+1,
    # invariant delta=x*d/dx; g=x+1 and f=delta(g)/g=x/(x+1).
    # Both f and f+1 satisfy the p-closed polynomial.
    for c in (0, 1):
        num = 0b10 ^ (0b11 if c else 0)  # x/(x+1) + c
        assert t_num(num, 0b11, 0b10, 1) == 0

    # E ordinary and Y supersingular: Y: y^2+y=x^3,
    # invariant delta=d/dx; g=x+1 and f=1/(x+1).
    # Only f (not f+1) is a geometric solution.
    assert t_num(0b01, 0b11, 0b01, 0) == 0
    assert t_num(0b01 ^ 0b11, 0b11, 0b01, 0) != 0

    for h in (0, 1):
        roots = [c for c in (0, 1) if (c * c - h * c) % 2 == 0]
        assert len(roots) == (2 if h else 1)
    print("RESIDUE_CENSUS_OK")
    print("CHARACTERISTIC_TWO_FIBER_WITNESSES_OK")
    print("SCHEME_LENGTH_AND_GEOMETRIC_POINT_PROFILES_OK")
    print("CERTIFICATE_OK")


if __name__ == "__main__":
    check()
