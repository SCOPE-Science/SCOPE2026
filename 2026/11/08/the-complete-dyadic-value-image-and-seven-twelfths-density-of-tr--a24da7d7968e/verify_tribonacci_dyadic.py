"""Standalone checks for the dyadic value set of the classical Tribonacci sequence."""
from collections import Counter
from fractions import Fraction
from math import comb, factorial


def tribonacci_prefix(n, modulus=None):
    values = [0, 1, 1]
    for _ in range(3, n):
        z = values[-1] + values[-2] + values[-3]
        if modulus:
            z %= modulus
        values.append(z)
    return values[:n]


def matrix_product(A, B, mod=None):
    C = [[sum(A[i][r] * B[r][j] for r in range(3)) for j in range(3)] for i in range(3)]
    if mod:
        C = [[x % mod for x in row] for row in C]
    return C


def matrix_power(A, exponent, mod=None):
    B = [[int(i == j) for j in range(3)] for i in range(3)]
    while exponent:
        if exponent & 1:
            B = matrix_product(B, A, mod)
        A = matrix_product(A, A, mod)
        exponent >>= 1
    return B


def polynomial_h(J=20):
    T = tribonacci_prefix(8 * J + 6)
    h = [(T[8 * u + 5] + 1) // 8 for u in range(J + 1)]
    c = [sum((-1) ** (j-i) * comb(j, i) * h[i] for i in range(j + 1)) for j in range(J + 1)]
    assert c[:5] == [1, 115, 14946, 1942640, 252498816]
    P = [Fraction(0) for _ in range(J + 1)]
    falling = [1]
    for j in range(J + 1):
        a = Fraction(c[j], factorial(j))
        for i, term in enumerate(falling):
            P[i] += a * term
        falling = [0] + falling
        for i in range(len(falling) - 1):
            falling[i] -= j * falling[i + 1]
    assert all(x.denominator % 2 for x in P)
    return P


def polynomial_mod(P, mod):
    return [(x.numerator * pow(x.denominator, -1, mod)) % mod for x in P]


def evaluate(P, u, mod):
    answer = 0
    for c in reversed(P):
        answer = (answer * u + c) % mod
    return answer


def critical_value_mod(P, m):
    mod = 1 << m
    Q = polynomial_mod([Fraction(i, 2) * P[i] for i in range(1, len(P))], mod)
    root = 0
    for bit in range(1, m + 1):
        good = [v for v in (root, root + (1 << (bit - 1))) if evaluate(Q, v, 1 << bit) == 0]
        assert len(good) == 1
        root = good[0]
    return evaluate(polynomial_mod(P, mod), root, mod)


def predicted_image(k, P):
    mod = 1 << k
    A = {x for x in range(mod) if x % 4 == 0}
    B = {x for x in range(mod) if x % 4 == 1}
    C = {x for x in range(mod) if x % min(16, mod) == 2 % min(16, mod)}
    m = max(0, k - 3)
    q = 1 << m
    critical = critical_value_mod(P, m) if m else 0
    D = {(8 * (critical + x*x) - 1) % mod for x in range(q)}
    return A | B | C | D


def square_count(m):
    def unit_square_count(t):
        return 1 if t in (1, 2) else 1 << (t - 3)
    return 1 + sum(unit_square_count(m - 2*j) for j in range((m - 1)//2 + 1))


def main():
    P = polynomial_h()
    M = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    I = [[int(i == j) for j in range(3)] for i in range(3)]
    M8 = matrix_power(M, 8)
    M32 = matrix_power(M, 32)
    D3 = [[(M8[i][j] - I[i][j]) // 4 for j in range(3)] for i in range(3)]
    D5 = [[(M32[i][j] - I[i][j]) // 16 for j in range(3)] for i in range(3)]
    assert D3 == [[3, 5, 6], [6, 9, 11], [11, 17, 20]]
    assert [[x % 4 for x in row] for row in D5] == [[1, 1, 0], [0, 1, 1], [1, 1, 2]]
    v = [0, 1, 1]
    for n in range(16):
        Mn = matrix_power(M, n)
        def scalar(D):
            return sum(Mn[0][i] * sum(D[i][j] * v[j] for j in range(3)) for i in range(3))
        assert scalar(D3) % 2 == (n + 1) % 2
        if n % 8 == 3:
            assert scalar(D5) % 4 == 2
    all_fibers = 0
    results = []
    for k in range(1, 15):
        mod = 1 << k
        count = 1 << (k + 1)
        T = tribonacci_prefix(count, mod)
        got = set(T)
        predicted = predicted_image(k, P)
        assert got == predicted, (k, got - predicted, predicted - got)
        assert len(got) == (2 if k == 1 else 4 if k == 2 else 6 if k == 3 else
                            (1 << (k - 1)) + (1 << (k - 4)) + square_count(k - 3))
        assert T[:3] == [0, 1, 1]
        # The period of the entire recurrence state equals the companion matrix order.
        assert matrix_power(M, count, mod) == I
        if k >= 2:
            assert matrix_power(M, count//2, mod) != I
        results.append((k, len(got)))
        all_fibers += mod
    assert [b for _, b in results] == [2, 4, 6, 11, 20, 39, 76, 151, 300, 599, 1196, 2391, 4780, 9559]
    print('VERIFY_OK levels=14 target_fibers=%d' % all_fibers)
    print('IMAGE_SIZES', results)
    print('CRITICAL_VALUE_MOD_2^11', critical_value_mod(P, 11))


if __name__ == '__main__':
    main()
