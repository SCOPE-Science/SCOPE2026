#!/usr/bin/env python3
"""Direct finite-permutation tests for right-translation cycle formulas."""
from collections import Counter
from itertools import permutations
from math import factorial, gcd, lcm


def product(a, b):
    """Right-action composition: (i^(ab)) = (i^a)^b."""
    return tuple(b[a[i]] for i in range(len(a)))


def inverse(p):
    v = [0] * len(p)
    for i, j in enumerate(p):
        v[j] = i
    return tuple(v)


def power(p, k):
    v = tuple(range(len(p)))
    for _ in range(k):
        v = product(v, p)
    return v


def cycle_type(p):
    seen, out = set(), []
    for i in range(len(p)):
        if i not in seen:
            t, d = i, 0
            while t not in seen:
                seen.add(t)
                t, d = p[t], d + 1
            out.append(d)
    return tuple(sorted(out))


def predicted_fixed(h, k):
    multiplicity = Counter(cycle_type(power(h, k)))
    centralizer = 1
    for d, m in multiplicity.items():
        centralizer *= (d ** m) * factorial(m)
    eligible = sum(1 for d, m in multiplicity.items()
                   for ell in range(1, m + 1)
                   if k % ell == 0 and gcd(d, k // ell) == 1)
    return centralizer * eligible


def translate(x, g, h):
    return h[inverse(g)[x]], product(product(inverse(h), g), h)


def actual_fixed(perms, h, k):
    n, count = len(h), 0
    for g in perms:
        for x in range(n):
            a, b = x, g
            for _ in range(k):
                a, b = translate(a, b, h)
            count += (a == x and b == g)
    return count


def mobius(k):
    primes, squarefree = 0, True
    p = 2
    while p * p <= k:
        if k % p == 0:
            primes += 1
            k //= p
            if k % p == 0:
                squarefree = False
                break
            while k % p == 0:
                k //= p
        p += 1
    if not squarefree:
        return 0
    if k > 1:
        primes += 1
    return -1 if primes % 2 else 1


def predicted_cycles(h, max_order):
    F = {d: predicted_fixed(h, d) for d in range(1, max_order + 1)}
    return {m: sum(mobius(m // d) * F[d]
                   for d in range(1, m + 1) if m % d == 0) // m
            for m in range(1, max_order + 1)}


def actual_cycles(perms, h):
    n = len(h)
    states = [(x, g) for g in perms for x in range(n)]
    visited = set()
    cycles = Counter()
    for s in states:
        if s in visited:
            continue
        t, d = s, 0
        while t not in visited:
            visited.add(t)
            d += 1
            t = translate(*t, h)
        assert t == s
        cycles[d] += 1
    assert len(visited) == n * len(perms)
    return cycles


def partitions(n):
    if n == 0:
        return 1
    arr = [0] * (n + 1)
    arr[0] = 1
    for step in range(1, n + 1):
        for i in range(step, n + 1):
            arr[i] += arr[i - step]
    return arr[n]


def main():
    total = 0
    full_profile_cases = 0
    for n in range(1, 6):
        perms = list(permutations(range(n)))
        representatives = {cycle_type(h): h for h in perms}
        for h in representatives.values():
            for k in range(1, 13):
                actual = actual_fixed(perms, h, k)
                expected = predicted_fixed(h, k)
                assert actual == expected, (n, cycle_type(h), k, actual, expected)
                total += 1
            if n <= 4:
                length_bound = lcm(*range(1, n + 1)) if n > 1 else 1
                exact = actual_cycles(perms, h)
                prediction = predicted_cycles(h, length_bound)
                assert dict(exact) == {m: c for m, c in prediction.items() if c > 0}
                assert sum(m * c for m, c in exact.items()) == n * factorial(n)
                full_profile_cases += 1
        sum_over_h = sum(predicted_fixed(h, 1) for h in perms)
        expected_sum = factorial(n) * sum(partitions(j) for j in range(n))
        assert sum_over_h == expected_sum, (n, sum_over_h, expected_sum)
    perms6 = list(permutations(range(6)))
    for ty in ((6,), (2, 2, 2)):
        h6 = next(h for h in perms6 if cycle_type(h) == ty)
        for k in (1, 2, 3, 4, 5, 6, 12):
            assert actual_fixed(perms6, h6, k) == predicted_fixed(h6, k)
            total += 1
    h4 = next(h for h in permutations(range(4)) if cycle_type(h) == (4,))
    assert dict(actual_cycles(list(permutations(range(4))), h4)) == {1: 4, 2: 2, 4: 16, 12: 2}
    print('VERIFY_OK fixed_power_tests={} full_profiles={} n_max=6'.format(total, full_profile_cases))
    print('S4_four_cycle_profile=1^4 2^2 4^16 12^2')


if __name__ == '__main__':
    main()
