"""Reproduce finite identity checks for a three-alternative approval-weighted veto core.
Run with Python 3.9 or later; no nonstandard packages needed.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, log

RANKINGS = list(permutations((0, 1, 2)))


def weakly_survives(profile, c):
    """Literal strict-blocking definition, with singleton top-ranked approvals."""
    approvers = sum(row[0] == c for row in profile)
    if not approvers:
        return False
    disapprovers = [row for row in profile if row[0] != c]
    for bits in range(1, 1 << len(disapprovers)):
        coalition = [p for k, p in enumerate(disapprovers) if bits & (1 << k)]
        better = sum(
            all(p.index(d) < p.index(c) for p in coalition)
            for d in (0, 1, 2)
        )
        if 3 * len(coalition) > approvers * (3 - better):
            return False
    return True


def count_condition(profile, c):
    a = sum(p[0] == c for p in profile)
    b = sum(p[-1] == c for p in profile)
    others = [d for d in (0, 1, 2) if d != c]
    y = [sum(p.index(d) < p.index(c) for p in profile if p[0] != c)
         for d in others]
    return (a > 0 and 2*a >= len(profile) and 3*b <= a
            and all(3*q <= 2*a for q in y))


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for a in range(n+1):
            for rest in compositions(n-a, k-1):
                yield (a,) + rest


def exact_probability(n):
    """Finite theorem formula, with collapsed multinomial categories."""
    numerator = 0
    for a in range((n+1)//2, n+1):
        for b in range(min(a//3, n-a) + 1):
            u = n-a-b
            for r in range(u+1):
                s = u-r
                if 3*(b+r) > 2*a or 3*(b+s) > 2*a:
                    continue
                numerator += (factorial(n)//(factorial(a)*factorial(b)*factorial(r)*factorial(s))) * 2**(a+b)
    return Fraction(3*numerator, 6**n)


def exact_probability_from_rankings(n):
    numerator = 0
    count = 0
    for multiplicities in compositions(n,6):
        profile = [p for j,p in enumerate(RANKINGS) for _ in range(multiplicities[j])]
        direct = [c for c in range(3) if weakly_survives(profile,c)]
        predicted = [c for c in range(3) if count_condition(profile,c)]
        assert direct == predicted, (n, multiplicities, direct, predicted)
        assert len(direct) <= 1
        count += 1
        if direct:
            numerator += factorial(n)//__import__('math').prod(factorial(z) for z in multiplicities)
    return Fraction(numerator, 6**n), count


def leading_constant():
    """Rational lattice sum from the sharp subsequence asymptotic."""
    t = Fraction(16, 27)
    return Fraction(4,3)*(19*t/(1-t)**2 + 10/(1-t))


def main():
    total = 0
    for n in range(1,10):
        literal, cases = exact_probability_from_rankings(n)
        formula = exact_probability(n)
        assert formula == literal, (n, literal, formula)
        print(f'n={n}: {cases} ranking histograms; probability={formula}')
        total += cases
    assert exact_probability(12) == Fraction(24023,157464)
    assert leading_constant() == Fraction(14904,121)
    rate = log(Fraction(27,16))/6
    assert 0.0872 < rate < 0.0873
    print(f'PASS: {total} exhaustive histogram checks, n=12 formula and exact prefactor')


if __name__ == '__main__':
    main()
