"""Finite exact checks for the universal-chord formulas. Python 3, standard library only.

This enumerates finite matchings and permutations; it is not a proof of any
asymptotic assertion. All identities that are valid at arbitrary size are
proved separately in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, factorial

checks = 0


def check(test):
    global checks
    checks += 1
    if not test:
        raise AssertionError(f"Exact assertion {checks} failed")


def crossing(c, d):
    a, b = sorted(c)
    x, y = sorted(d)
    return (a < x < b < y) or (x < a < y < b)


def matchings(vertices):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for j in range(1, len(vertices)):
        for rest in matchings(vertices[1:j] + vertices[j+1:]):
            yield ((first, vertices[j]),) + rest


def count_universals(m):
    return sum(all(crossing(c, d) for d in m if d != c) for c in m)


def count_crossings(m):
    return sum(crossing(c, d) for i, c in enumerate(m) for d in m[i+1:])


def gap_factorial_sum(total, parts):
    if parts == 1:
        return factorial(total)
    return sum(factorial(s) * gap_factorial_sum(total-s, parts-1)
               for s in range(total+1))


def count_formula_num_den(n, k):
    return n * gap_factorial_sum(n-k, k), k


# Complete unlabeled chord-matchings through seven chords.
for n in range(1, 8):
    population = Counter()
    factorial_moments = [0] * (n+1)
    total = 0
    c0_count = 0
    for m in matchings(tuple(range(2*n))):
        total += 1
        u = count_universals(m)
        population[u] += 1
        c0_count += int((0, n) in m and all(crossing((0, n), d)
                                                 for d in m if d != (0, n)))
        check(0 <= u <= n)
        check(u != n-1 or n == 1)
        for k in range(1, n+1):
            factorial_moments[k] += comb(u, k)
    check(total == factorial(2*n) // (2**n * factorial(n)))
    check(sum(population.values()) == total)
    check(population[n] == 1)
    for k in range(1, n+1):
        numerator, denominator = count_formula_num_den(n, k)
        check(factorial_moments[k] * denominator == numerator)
    check(c0_count == factorial(n-1))
    check(factorial_moments[1] == n * factorial(n-1))
    print(f"n={n}: {total} chord matchings, universal-count histogram {dict(sorted(population.items()))}")

# Conditional structure for a specified universal diameter.
for n in range(1, 9):
    N = n-1
    crossings = Counter()
    universal_counts = Counter()
    for p in permutations(range(N)):
        m = ((0, n),) + tuple((j+1, n+1+p[j]) for j in range(N))
        check(all(crossing(m[0], d) for d in m[1:]))
        U = count_universals(m)
        V = 1 + sum(p[j] == j and set(p[:j]) == set(range(j))
                    for j in range(N))
        check(U == V)
        inv = sum(p[i] > p[j] for i in range(N) for j in range(i+1, N))
        X = count_crossings(m)
        check(X == N + comb(N, 2) - inv)
        crossings[X] += 1
        universal_counts[U] += 1
    check(sum(crossings.values()) == factorial(N))
    mean = sum(Fraction(x * count, factorial(N)) for x, count in crossings.items())
    variance = sum(Fraction(count, factorial(N)) * (x-mean)**2
                   for x, count in crossings.items())
    check(mean == N + Fraction(comb(N, 2), 2))
    check(variance == Fraction(N*(N-1)*(2*N+5), 72))
    if N:
        expected_extra = sum(Fraction(factorial(j)*factorial(N-j-1), factorial(N))
                             for j in range(N))
        via_counts = sum(Fraction((U-1)*count, factorial(N))
                         for U, count in universal_counts.items())
        check(via_counts == expected_extra)
    print(f"n={n}: {factorial(N)} conditional permutations, conditional crossing variance {variance}")

print(f"PASS: {checks:,} exact finite assertions")
