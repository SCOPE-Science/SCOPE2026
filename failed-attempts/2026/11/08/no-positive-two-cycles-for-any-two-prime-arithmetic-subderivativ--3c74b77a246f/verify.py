"""Finite regression checks for the two-prime arithmetic-subderivative theorem.

No finite check substitutes for the symbolic nine-case proof in RESULT.md.
"""
from itertools import combinations, product
from math import gcd

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
MAX_N = 100000


def val(n, p):
    a = 0
    while n % p == 0:
        a += 1
        n //= p
    return a


def subderivative(n, p, q):
    a = val(n, p)
    b = val(n, q)
    return a * (n // p) + b * (n // q)


def complete_cycle_candidate_cases(p, q):
    # For a hypothetical positive two-periodic point, N N' = p^2 q^2.
    # This checks the 9 possible exponent splits of that equation.
    cases = []
    for u, v in product(range(3), repeat=2):
        N = p ** u * q ** v
        Nprime = p ** (2-u) * q ** (2-v)
        shift_rhs = (u-1) * q + (v-1) * p
        if N > 1 and Nprime > 1 and (Nprime - N) == shift_rhs:
            cases.append((u, v))
    assert cases == [(1, 1)], (p, q, cases)


count_two_cycle = 0
fixed_seen = 0
for p, q in combinations(PRIMES, 2):
    complete_cycle_candidate_cases(p, q)
    for n in range(1, MAX_N+1):
        m = subderivative(n, p, q)
        if m > 0 and subderivative(m, p, q) == n:
            if m != n:
                count_two_cycle += 1
                raise AssertionError((p, q, n, m))
            fixed_seen += 1
            a, b = val(n, p), val(n, q)
            assert (a == p and b == 0) or (a == 0 and b == q)

assert count_two_cycle == 0
print('VERIFY_OK pairs=45 n_per_pair=100000 split_cases_per_pair=9')
print('primitive_period_two=0 fixed_states_encountered=' + str(fixed_seen))
print('symbolic_scope: proof covers all distinct primes and all positive integers')
