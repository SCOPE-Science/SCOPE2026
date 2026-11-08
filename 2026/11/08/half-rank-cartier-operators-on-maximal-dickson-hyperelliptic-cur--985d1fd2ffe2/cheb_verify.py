"""Exact finite-field checks for Dickson-curve Cartier-rank identities.

Run with Python 3: python cheb_verify.py
No third-party dependencies are required.
"""
from math import comb


def multiply(a, b, prime):
    output = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            output[i + j] = (output[i + j] + ai * bj) % prime
    return output


def polynomial_power(base, power, prime):
    result = [1]
    while power:
        if power % 2:
            result = multiply(result, base, prime)
        power //= 2
        if power:
            base = multiply(base, base, prime)
    return result


def dickson(n):
    # D_0=2, D_1=x, D_{n}=x D_{n-1}-D_{n-2}.
    a, b = [2], [0, 1]
    if n == 0:
        return a
    if n == 1:
        return b
    for degree in range(2, n + 1):
        shifted = [0] + b
        updated = [shifted[i] - (a[i] if i < len(a) else 0)
                   for i in range(len(shifted))]
        a, b = b, updated
    return b


def rank_mod(matrix, prime):
    rows = [row[:] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows))
                      if rows[i][column] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][column], -1, prime)
        rows[rank] = [(entry * inv) % prime for entry in rows[rank]]
        for i in range(len(rows)):
            if i == rank:
                continue
            scalar = rows[i][column]
            if scalar:
                rows[i] = [(a - scalar * b) % prime
                           for a, b in zip(rows[i], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def square_zero(matrix, prime):
    size = len(matrix)
    return all(sum(matrix[i][k] * matrix[k][j]
                   for k in range(size)) % prime == 0
               for i in range(size) for j in range(size))


def check(prime, n):
    assert prime > 2 and n % 2 == 1
    assert (prime * prime + 1) % (2 * n) == 0
    genus = (n - 1) // 2
    defining = multiply(dickson(n), [2, 1], prime)
    coefficients = polynomial_power(defining, (prime - 1) // 2, prime)
    matrix = [[coefficients[prime * i - j]
               if 0 <= prime * i - j < len(coefficients) else 0
               for j in range(1, genus + 1)]
              for i in range(1, genus + 1)]
    exact_rank = rank_mod(matrix, prime)
    assert exact_rank == genus // 2, (prime, n, exact_rank)
    assert square_zero(matrix, prime), (prime, n, 'Cartier square')
    return exact_rank


def main():
    cases = ((5, 13), (7, 25), (13, 17), (31, 13), (47, 13), (73, 13))
    for prime, n in cases:
        rank = check(prime, n)
        print(f'p={prime}, n={n}, genus={(n-1)//2}, Cartier rank={rank}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
