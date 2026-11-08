"""Reproduce exact first/second equilibrium-count moments for iid types on cycles.

Only Python's standard library is needed. Run: python verify_cycle_equilibria.py
"""
from fractions import Fraction as Q
from itertools import product


def matrix_multiply(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def matrix_power(a, n):
    size = len(a)
    result = tuple(tuple(Q(i == j) for j in range(size)) for i in range(size))
    while n:
        if n & 1:
            result = matrix_multiply(result, a)
        a = matrix_multiply(a, a)
        n //= 2
    return result


def trace_power(a, n):
    p = matrix_power(a, n)
    return sum(p[i][i] for i in range(len(p)))


def equilibrium_count(types):
    n = len(types)
    answer = 0
    for action in product((-1, 1), repeat=n):
        if all(types[i] * action[i] * (action[(i - 1) % n] + action[(i + 1) % n]) >= 0
               for i in range(n)):
            answer += 1
    return answer


def analytic_moments(n):
    # Mean via a 2-state edge-sign transfer and the even parity projection.
    C = ((Q(1), Q(1)), (Q(1), Q(0)))
    R = ((Q(0), Q(1)), (Q(1), Q(1)))
    A = tuple(tuple((C[i][j] + R[i][j]) / 2 for j in range(2)) for i in range(2))
    D = ((Q(1), Q(0)), (Q(0), Q(-1)))
    mean = trace_power(A, n) + trace_power(matrix_multiply(A, D), n)

    # Two independent proposed profiles share the same random type at each vertex.
    states = tuple(product((1, -1), repeat=2))
    def admissible(sign_left, sign_right, conformist):
        return (sign_left + sign_right >= 0) if conformist else (sign_left + sign_right <= 0)
    K = tuple(tuple(Q(sum(admissible(e, ep, c) and admissible(f, fp, c)
                            for c in (True, False)), 2)
                    for ep, fp in states) for e, f in states)
    total = Q(0)
    for characters in (lambda e, f: 1, lambda e, f: e,
                       lambda e, f: f, lambda e, f: e * f):
        diag = tuple(tuple(Q(characters(*states[j])) if i == j else Q(0)
                           for j in range(4)) for i in range(4))
        total += trace_power(matrix_multiply(K, diag), n)
    return mean, total


def recurrence_second(n):
    # Radical-free integer recurrence for each characteristic polynomial.
    # Trace(K^n) from eigenvalues: a_±, -1, -1/2.
    pair_a = [Q(2), Q(5, 2)]
    for i in range(2, n + 1):
        pair_a.append(Q(5, 2) * pair_a[-1] - Q(1, 2) * pair_a[-2])
    # Trace((K D_e)^n): zero at odd n; for even n 2(-1)^(n/2)
    # times b_+^(n/2)+b_-^(n/2), b sum 7/4, b product 1/4.
    mixed = Q(0)
    if n % 2 == 0:
        m = n // 2
        pair_b = [Q(2), Q(7, 4)]
        for i in range(2, m + 1):
            pair_b.append(Q(7, 4) * pair_b[-1] - Q(1, 4) * pair_b[-2])
        mixed = Q(4) * (-1) ** m * pair_b[m]
    return pair_a[n] + Q(-1) ** n + Q(-1, 2) ** n + mixed + 2 + 2 * Q(-1, 2) ** n


def run():
    cases = 0
    for n in range(3, 11):
        moment_sum = sum_z2 = 0
        empty_count = 0
        for types in product((-1, 1), repeat=n):
            z = equilibrium_count(types)
            moment_sum += z
            sum_z2 += z * z
            empty_count += (z == 0)
            cases += 1
        e, e2 = analytic_moments(n)
        assert Q(moment_sum, 2 ** n) == e, (n, 'mean')
        assert Q(sum_z2, 2 ** n) == e2, (n, 'second moment')
        assert recurrence_second(n) == e2, (n, 'closed second moment')
        expected_empty = 2 if n % 4 == 2 else 0
        assert empty_count == expected_empty, (n, 'no equilibrium')
        print(f'n={n} mean={e} second={e2} empty_types={empty_count}/{2**n}')
    assert cases == sum(2 ** n for n in range(3, 11))
    print(f'VERIFIED: {cases} type configurations, full action-profile checks, first and second moments.')


if __name__ == '__main__':
    run()
