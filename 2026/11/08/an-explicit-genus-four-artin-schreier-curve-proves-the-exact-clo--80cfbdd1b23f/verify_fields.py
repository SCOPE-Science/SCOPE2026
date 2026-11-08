#!/usr/bin/env python3
"""Independent explicit finite-field tests for a genus-four Artin--Schreier curve.

No external dependencies. The field bases are polynomial quotients of F_2[t].
For degrees 2, 4, and 6 the irreducible moduli are, respectively,
t^2+t+1, t^4+t+1, and t^6+t+1.
"""

def field(m, modulus):
    size = 1 << m

    def mul(a, b):
        z = 0
        while b:
            if b & 1:
                z ^= a
            b >>= 1
            a <<= 1
            if a & size:
                a ^= modulus
        return z

    def power(a, n):
        z = 1
        while n:
            if n & 1:
                z = mul(z, a)
            a = mul(a, a)
            n >>= 1
        return z

    def trace(a):
        z = 0
        for _ in range(m):
            z ^= a
            a = mul(a, a)
        assert z in (0, 1), (m, z)
        return z

    return mul, power, trace


def count_affine(m, modulus):
    mul, power, trace = field(m, modulus)
    q = 1 << m
    omega = next(w for w in range(q)
                 if w not in (0, 1) and power(w, 4) == w)
    assert mul(omega, omega) ^ omega ^ 1 == 0
    solution_count = 0
    for x in range(q):
        rhs = power(x, 9) ^ omega
        if trace(rhs) == 0:
            solution_count += 2
    return 1 + solution_count, omega


def main():
    expected = [(2, 0b111, 1), (4, 0b10011, 9), (6, 0b1000011, 1)]
    for m, modulus, n in expected:
        count, omega = count_affine(m, modulus)
        assert count == n, (m, count, n)
        print('degree', m//2, 'field_size', 1 << m,
              'omega_encoded', omega, 'points', count)
    # Explicitly verify all 64 values of x^9 belong to the unique F_8 subfield.
    _, power, trace = field(6, 0b1000011)
    for x in range(64):
        t = power(x, 9)
        assert power(t, 8) == t
        assert trace(t) == 0
    print('TRACE_VERIFICATION_OK')


if __name__ == '__main__':
    main()
