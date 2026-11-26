"""Reproducible exact checks for the private-incumbents committee family."""
from fractions import Fraction
from itertools import combinations


def instance(k):
    candidates = set(range(k + 1))
    elected = set(range(k))
    ballots = [{i, k} for i in range(k)] + [set(range(k))]
    return candidates, elected, ballots


def check_core_and_pareto(k):
    candidates, W, ballots = instance(k)
    n = k + 1
    quota = Fraction(n, k)
    utilities = [len(ballot & W) for ballot in ballots]
    assert utilities == [1] * k + [k]
    total = 0
    for size in range(1, n + 1):
        for coalition in combinations(range(n), size):
            for r in range(1, k + 2):
                for choice in combinations(candidates, r):
                    total += 1
                    if size >= quota * r:
                        assert not all(len(ballots[i] & set(choice)) > utilities[i]
                                       for i in coalition)
    for choice in combinations(candidates, k):
        chosen = set(choice)
        weakly_better = all(len(a & chosen) >= utilities[i]
                            for i, a in enumerate(ballots))
        strictly_better = any(len(a & chosen) > utilities[i]
                              for i, a in enumerate(ballots))
        assert not (weakly_better and strictly_better)
    return total


def check_fractional_witness(k):
    n = k + 1
    y = [Fraction(1, 2)] * k + [Fraction(0)]
    z = [Fraction(0)] * k + [Fraction(1)]
    x = {(i, k): Fraction(1) for i in range(k)}
    for i in range(n):
        approvals = {i, k} if i < k else set(range(k))
        u = 1 if i < k else k
        assert sum((x.get((i, c), 0) for c in approvals), Fraction(0)) == (u + 1) * y[i]
        for c in approvals:
            assert 0 <= x.get((i, c), 0) <= z[c] <= 1
            if c < k:
                assert x.get((i, c), 0) <= y[i]
    assert all(Fraction(0) <= t <= 1 for t in y)
    ratio = sum(y) / (Fraction(n, k) * sum(z))
    assert ratio == Fraction(k*k, 2*(k + 1))
    assert (ratio >= 1) == (k >= 3)
    return ratio


if __name__ == '__main__':
    tested = 0
    for k in range(1, 8):
        tested += check_core_and_pareto(k)
        ratio = check_fractional_witness(k)
        print(f'k={k}: exhaustive integer checks OK; fractional ratio={ratio}')
    for k in range(8, 101):
        check_fractional_witness(k)
    print(f'PASS: {tested} integral (coalition, proposal) cases; '
          'exact rational witness for 100 seat counts; '
          'the all-size upper bound is proved symbolically in RESULT.md.')
