"""Reproducible finite verification of the safe-prime five-term progression theorem.
Only Python's integer arithmetic is required; bounds and checks are exhaustive.
"""
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    return all(n % d != 0 for d in range(2, isqrt(n) + 1))


def primitive_roots_safe(p):
    q = (p - 1) // 2
    # For a cyclic group of order 2q, q prime, the two prime divisors
    # of 2q are 2 and q. These modular tests characterize order 2q.
    return {x for x in range(1, p) if pow(x, 2, p) != 1 and pow(x, q, p) != 1}


def failing_differences(p):
    roots = primitive_roots_safe(p)
    if p == 5:  # there are only two primitive roots
        return list(range(1, p))
    # Precompute all a at which five consecutive terms with step d are roots.
    fail = []
    for d in range(1, p):
        has_progression = False
        for a in range(1, p):
            if all((a + j * d) % p in roots for j in range(5)):
                has_progression = True
                break
        if not has_progression:
            fail.append(d)
    return fail


def main():
    safe_primes = [p for p in range(5, 2000) if is_prime(p) and is_prime((p - 1) // 2)]
    failures = {p: failing_differences(p) for p in safe_primes}
    print('Safe primes below 2000:', safe_primes)
    print('Counts of exceptional differences:', {p: len(ds) for p, ds in failures.items()})
    print('Failure sets for the last two exceptional primes:', {p: failures[p] for p in (59, 83)})
    assert [p for p, ds in failures.items() if ds] == [5, 7, 11, 23, 47, 59, 83]
    assert failures[59] == [2, 19, 24, 25, 26, 33, 34, 35, 40, 57]
    assert failures[83] == [3, 20, 40, 43, 63, 80]
    assert all(not failures[p] for p in safe_primes if p >= 107)
    # Check strict positivity of the elementary Weil-bound margin at 2000.
    assert (2000 - 250)**2 > 39**2 * 2000
    print('PASS: every safe prime in [107,2000) works for every nonzero step.')
    print('PASS: p=83 fails, and all smaller safe primes fail.')


if __name__ == '__main__':
    main()
