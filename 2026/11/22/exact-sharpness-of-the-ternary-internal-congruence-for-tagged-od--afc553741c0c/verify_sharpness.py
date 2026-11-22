#!/usr/bin/env python3
"""Exact finite checks for the 3-adic PDO_t sharpness theorem.

The infinite proof uses the published coefficient-vector valuation bound.
These checks independently verify its finite matrix obstruction and examples.
"""

def v3(n):
    if n == 0:
        return None
    n = abs(n)
    r = 0
    while n % 3 == 0:
        r += 1
        n //= 3
    return r


def weight(j):
    return 0 if j == 1 else (3*j - 4)//2


def check_matrix():
    col1 = [81, 17, 1, 0, 0, 0]
    col2 = [5256, 5985, 2274, 393, 32, 1]
    main = col1[0]*col2[1] - col2[0]*col1[1]
    assert main == 395433 and v3(main) == 2
    strict_pairs = 0
    for k in range(2, 7):
        for ell in range(1, k):
            delta = col1[ell-1]*col2[k-1] - col2[ell-1]*col1[k-1]
            vd = v3(delta)
            if (k, ell) == (2, 1):
                assert vd == 2
            elif vd is not None:
                assert vd + weight(k) + weight(ell) >= 4
                strict_pairs += 1
    a = 144
    b = 1728
    a1 = 1520 * 3**3
    b1 = 137024 * 3**4
    base = b1*a - b*a1
    assert base == 698368 * 3**7
    assert v3(base) == 7 and (base//3**7) % 3 == 1
    return strict_pairs


def tagged_partition_coefficients(limit, modulus):
    # Lin's exact generating function is
    # q * E(q^2) * E(q^3)^2 * E(q^12)^2 / (E(q)^2 * E(q^6)).
    # Coefficients of the unshifted eta quotient, modulo 3^30.
    a = [0] * limit
    a[0] = 1
    for dilation, exponent in [(1, -2), (2, 1), (3, 2), (6, -1), (12, 2)]:
        for step in range(dilation, limit, dilation):
            if exponent > 0:
                for _ in range(exponent):
                    for t in range(limit-1, step-1, -1):
                        a[t] = (a[t] - a[t-step]) % modulus
            else:
                for _ in range(-exponent):
                    for t in range(step, limit):
                        a[t] = (a[t] + a[t-step]) % modulus
    return [0] + a


def check_coefficients():
    modulus = 3**30
    f = tagged_partition_coefficients(648, modulus)
    assert f[0] == 0
    assertions = 0
    for m in range(3):
        a = f[12*3**m]
        b = f[24*3**m]
        c = f[12*3**(m+1)]
        d = f[24*3**(m+1)]
        determinant = (c*b-a*d) % modulus
        assert v3(determinant) == 2*m + 7
        assert (determinant//3**(2*m+7)) % 3 == (-1)**(m+1) % 3
        mu = 5 if m % 2 == 0 else 8
        assert (c-3*mu*a) % 3**(m+5) == 0
        assert (d-3*mu*b) % 3**(m+5) == 0
        assert v3(a) == m+2
        assertions += 5
    return assertions


def main():
    strict_pairs = check_matrix()
    assertions = check_coefficients()
    print('TAGGED_PARTS_SHARPNESS_OK', 'nonleading_finite_pairs', strict_pairs,
          'coefficient_assertions', assertions, 'depths', 3)


if __name__ == '__main__':
    main()
