"""Exact, standalone checks for six consecutive triple-pattern/cycle covariances."""
from fractions import Fraction
from itertools import permutations
from math import factorial, comb

PATTERNS = ("123", "132", "213", "231", "312", "321")


def pattern(p, a):
    triple = p[a - 1:a + 2]
    return ''.join(str(sorted(triple).index(v) + 1) for v in triple)


def cycle_count(p):
    seen = set()
    count = 0
    for i in range(len(p)):
        if i in seen:
            continue
        count += 1
        j = i
        while j not in seen:
            seen.add(j)
            j = p[j] - 1
    return count


def numerators(n, a):
    return dict(zip(PATTERNS, (
        3 * n - 2,
        9 * n - 14 - 12 * a,
        12 * a - 3 * n - 2,
        12 * a - 9 * n + 10,
        3 * n - 2 - 12 * a,
        10 - 3 * n,
    )))


def fixed_point_counts(n, a, p):
    F = 0
    for s, rank in zip((a, a + 1, a + 2), map(int, p)):
        if rank == 1:
            F += comb(n - s, 2)
        elif rank == 2:
            F += (s - 1) * (n - s)
        else:
            F += comb(s - 1, 2)
    return F


def two_cycle_counts(n, a, p):
    return {
        '123': 0, '132': a, '213': n - a - 1,
        '231': n - a - 2, '312': a - 1, '321': n - 2,
    }[p]


def three_cycle_counts(p):
    return int(p in ('231', '312'))


def verify_closed_forms():
    count = 0
    for n in range(3, 501):
        for a in range(1, n - 1):
            for p in PATTERNS:
                numer = 6 * (fixed_point_counts(n, a, p)
                             + two_cycle_counts(n, a, p)
                             + three_cycle_counts(p)) - 3 * n * (n - 2) - 2
                assert numer == numerators(n, a)[p], (n, a, p, numer)
                count += 1
    return count


def verify_enumeration():
    checked = 0
    for n in range(3, 10):
        totals = {(a, p): 0 for a in range(1, n - 1) for p in PATTERNS}
        total_cycles = 0
        for pi in permutations(range(1, n + 1)):
            cyc = cycle_count(pi)
            total_cycles += cyc
            for a in range(1, n - 1):
                totals[a, pattern(pi, a)] += cyc
        mean_cycles = Fraction(total_cycles, factorial(n))
        harmonic = sum((Fraction(1, j) for j in range(1, n + 1)), Fraction())
        assert mean_cycles == harmonic
        for (a, p), v in totals.items():
            empirical = Fraction(v, factorial(n)) - harmonic / 6
            predicted = Fraction(numerators(n, a)[p], 6 * n * (n - 1) * (n - 2))
            assert empirical == predicted, (n, a, p, empirical, predicted)
            checked += 1
        print('exact permutation enumeration n =', n, 'total permutations =', factorial(n))
    return checked


if __name__ == '__main__':
    algebraic = verify_closed_forms()
    enumerated = verify_enumeration()
    print('PASS:', algebraic, 'closed-form substitution cells;',
          enumerated, 'exhaustive covariance cells')
