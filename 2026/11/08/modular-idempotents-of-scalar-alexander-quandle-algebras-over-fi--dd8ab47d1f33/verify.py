"""Reproducible exhaustive tests for scalar Alexander-quandle algebra idempotents.

The verification is finite only. It uses the Python standard library, no third-party
packages, and has no network or file dependencies.
"""
from itertools import product


def count_prime(p, alpha):
    beta = (1 - alpha) % p
    powers = [k for k in range(p - 1)
              if (pow(alpha, k, p) + pow(beta, k, p) - 1) % p == 0]
    predicted = 1 + p ** len(powers)
    y_indices = [[((z - alpha * x) * pow(beta, -1, p)) % p
                  for x in range(p)] for z in range(p)]
    count = 0
    for coeff in product(range(p), repeat=p):
        if all((sum(coeff[x] * coeff[y_indices[z][x]]
                    for x in range(p)) - coeff[z]) % p == 0
               for z in range(p)):
            count += 1
    return powers, predicted, count


def add9(a, b):
    return ((a % 3 + b % 3) % 3) + 3 * ((a // 3 + b // 3) % 3)


def neg9(a):
    return ((-a % 3) % 3) + 3 * ((-(a // 3)) % 3)


def mul9(a, b):
    x, y = a % 3, a // 3
    u, v = b % 3, b // 3
    return ((x * u + 2 * y * v) % 3) + 3 * ((x * v + y * u) % 3)


def power9(a, k):
    result = 1
    for _ in range(k):
        result = mul9(result, a)
    return result


def count_f9(alpha):
    beta = add9(1, neg9(alpha))
    powers = [k for k in range(8)
              if add9(power9(alpha, k), power9(beta, k)) == 1]
    predicted = 1 + 3 ** len(powers)
    pairs = [[] for _ in range(9)]
    for x in range(9):
        for y in range(9):
            z = add9(mul9(alpha, x), mul9(beta, y))
            pairs[z].append((x, y))
    count = 0
    for coeff in product(range(3), repeat=9):
        if all((sum(coeff[x] * coeff[y] for x, y in pairs[z])
                - coeff[z]) % 3 == 0 for z in range(9)):
            count += 1
    return powers, predicted, count


def mul_binary(a, b, q, reduction_poly):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & q:
            a ^= reduction_poly
    return result


def power_binary(a, n, q, poly):
    result = 1
    for _ in range(n):
        result = mul_binary(result, a, q, poly)
    return result


def count_binary(q, poly, alpha):
    beta = alpha ^ 1
    powers = [k for k in range(q - 1)
              if power_binary(alpha, k, q, poly)
                 ^ power_binary(beta, k, q, poly) == 1]
    predicted = 1 + 2 ** len(powers)
    pair_mask = [[0] * q for _ in range(q)]
    for x in range(q):
        for y in range(q):
            xy = mul_binary(alpha, x, q, poly) ^ mul_binary(beta, y, q, poly)
            yx = mul_binary(alpha, y, q, poly) ^ mul_binary(beta, x, q, poly)
            pair_mask[x][y] = (1 << xy) ^ (1 << yx)
    # F[mask] encodes the coefficients of u*u when u has coefficient bitmask mask.
    F = [0] * (1 << q)
    count = 1  # mask zero is idempotent
    for mask in range(1, 1 << q):
        lowbit = mask & -mask
        x = lowbit.bit_length() - 1
        rem = mask ^ lowbit
        value = F[rem] ^ lowbit
        b = rem
        while b:
            b_low = b & -b
            y = b_low.bit_length() - 1
            value ^= pair_mask[x][y]
            b ^= b_low
        F[mask] = value
        if value == mask:
            count += 1
    return powers, predicted, count


def main():
    records = 0
    for p in (3, 5):
        for alpha in range(2, p):
            exps, expected, observed = count_prime(p, alpha)
            print(f'F{p} alpha={alpha} exps={exps} predicted={expected} observed={observed}')
            assert expected == observed
            records += 1
    for alpha in (2, 3, 4):
        exps, expected, observed = count_prime(7, alpha)
        print(f'F7 alpha={alpha} exps={exps} predicted={expected} observed={observed}')
        assert expected == observed
        records += 1
    for alpha in range(2, 9):
        exps, expected, observed = count_f9(alpha)
        print(f'F9 alpha={alpha} exps={exps} predicted={expected} observed={observed}')
        assert expected == observed
        records += 1
    for q, poly, alphas in [(4, 0b111, (2, 3)),
                             (8, 0b1011, (2, 3, 4, 5, 6, 7)),
                             (16, 0b10011, (2, 6))]:
        for alpha in alphas:
            exps, expected, observed = count_binary(q, poly, alpha)
            print(f'F{q} alpha={alpha} exps={exps} predicted={expected} observed={observed}')
            assert expected == observed
            records += 1
    print(f'VERIFY_OK checked={records}')


if __name__ == '__main__':
    main()
