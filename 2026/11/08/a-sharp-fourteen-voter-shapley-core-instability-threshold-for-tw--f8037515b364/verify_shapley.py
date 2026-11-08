"""Exact complete finite verification for two-party, two-seat PAV TU games.

The specification reduces every profile to two positive party sizes and checks
all labeled Shapley predecessors as well as every coalition type. All arithmetic
is rational, without simulation or floating-point tolerances.
"""
from fractions import Fraction
from math import comb, factorial


def worth(a, b, s, t):
    n = a + b
    seats = 2 * (s + t) // n
    if seats == 0:
        return Fraction(0)
    if seats == 1:
        return Fraction(max(s, t))
    assert (s, t) == (a, b)  # only the grand coalition can claim two seats
    return max(Fraction(3 * a, 2), Fraction(a + b), Fraction(3 * b, 2))


def type_shapley(a, b):
    n = a + b
    first = second = Fraction(0)
    weights = [Fraction(1, n * comb(n - 1, h)) for h in range(n)]
    for s in range(a):
        for t in range(b + 1):
            mult = comb(a - 1, s) * comb(b, t)
            first += mult * weights[s + t] * (worth(a, b, s + 1, t) - worth(a, b, s, t))
    for s in range(a + 1):
        for t in range(b):
            mult = comb(a, s) * comb(b - 1, t)
            second += mult * weights[s + t] * (worth(a, b, s, t + 1) - worth(a, b, s, t))
    assert first * a + second * b == worth(a, b, a, b)
    return first, second


def subset_shapley(a, b):
    n = a + b
    mask_all = (1 << n) - 1
    weight = [Fraction(factorial(s) * factorial(n - 1 - s), factorial(n)) for s in range(n)]
    out = []
    for i in (0, a):
        score = Fraction(0)
        bit = 1 << i
        for mask in range(1 << n):
            if mask & bit:
                continue
            s = (mask & ((1 << a) - 1)).bit_count()
            t = (mask >> a).bit_count()
            delta = ((1, 0) if i == 0 else (0, 1))
            score += weight[s + t] * (worth(a, b, s + delta[0], t + delta[1]) - worth(a, b, s, t))
        out.append(score)
    return tuple(out)


def check_case(a, b):
    pa, pb = type_shapley(a, b)
    assert (pa, pb) == subset_shapley(a, b), (a, b)
    n = a + b
    failures = []
    smallest = None
    num_tested = 0
    for s in range(a + 1):
        for t in range(b + 1):
            owed = s * pa + t * pb
            target = worth(a, b, s, t)
            slack = owed - target
            num_tested += 1
            if slack < 0:
                failures.append((s, t, target, owed))
            if 0 < s + t < n and 2 * (s + t) >= n:
                if smallest is None or slack < smallest:
                    smallest = slack
    return failures, smallest, num_tested


def main():
    profiles = coalitions = 0
    minima = {}
    for n in range(2, 15):
        bad = []
        minimum = None
        for a in range(1, n // 2 + 1):
            b = n - a
            fails, slack, count = check_case(a, b)
            profiles += 1
            coalitions += count
            if minimum is None or slack < minimum:
                minimum = slack
            if fails:
                bad.append((a, b, fails))
        minima[n] = minimum
        if n <= 13:
            assert not bad, ('unexpected smaller counterexample', n, bad)
        else:
            assert len(bad) == 1 and bad[0][0:2] == (6, 8)
            assert bad[0][2] == [(6, 1, Fraction(6), Fraction(5065, 858))]
    a, b = 6, 8
    pa, pb = type_shapley(a, b)
    assert (pa, pb) == (Fraction(7127, 9009), Fraction(6947, 6006))
    assert 6 - (6 * pa + pb) == Fraction(83, 858)
    print('PASS: %d party-size profiles, %d coalition-type constraints' % (profiles, coalitions))
    print('PASS: two independent exact Shapley constructions agree for every profile')
    print('PASS: zero counterexamples through 13 voters; one party-size type at 14')
    print('PASS: first violation (6,8), coalition composition (6,1), deficit 83/858')
    print('Minimum proper entitled coalition slack by electorate size:')
    print(', '.join('%d:%s' % (n, minima[n]) for n in range(2, 15)))


if __name__ == '__main__':
    main()
