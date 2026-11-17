"""Finite exhaustive tests for cyclic consecutive-block approval elections.

Run: python checker.py
All score comparisons use exact integers (scaled Thiele weights).
The infinite-domain classification is proved analytically in RESULT.md.
"""
from itertools import combinations
from math import comb, lcm


def binomial(a, b):
    return comb(a, b) if 0 <= b <= a else 0


def triple_winner_count(n, k):
    if not 0 <= k <= n or n < 3:
        raise ValueError("require n>=3 and 0<=k<=n")
    if k in (0, n):
        return 1
    if 3 * k <= n:
        return (n * binomial(n - 2 * k - 1, k - 1)) // k
    if 3 * (n - k) <= n:
        h = n - k
        return (n * binomial(n - 2 * h - 1, h - 1)) // h
    result = 0
    for t in range(1, n + 1):
        term = n * binomial(t, k - t) * binomial(t, n - k - t)
        if term:
            assert term % t == 0
            result += term // t
    return result


def score_and_balanced(n, r, committee, cumulative):
    counts = [sum(int((i + j) % n in committee) for j in range(r)) for i in range(n)]
    q, h = divmod(r * len(committee), n)
    optimum = (n - h) * cumulative[q] + h * cumulative[q + 1] if h else n * cumulative[q]
    return sum(cumulative[v] for v in counts), optimum, max(counts) - min(counts) <= 1


def test_instance(n, r, weights, test_count):
    f = [0]
    for x in weights:
        f.append(f[-1] + x)
    winners = [0] * (n + 1)
    explored = 0
    for k in range(n + 1):
        for choice in combinations(range(n), k):
            score, upper, balanced = score_and_balanced(n, r, set(choice), f)
            assert score <= upper, (n, r, k, choice, score, upper)
            assert (score == upper) == balanced, (n, r, k, choice)
            winners[k] += (score == upper)
            explored += 1
        assert winners[k] > 0
        if test_count:
            assert winners[k] == triple_winner_count(n, k), (n, k, winners[k])
    return explored


def main():
    total_triple = 0
    for n in range(3, 17):
        denominator = lcm(1, 2, 3)
        total_triple += test_instance(n, 3, [denominator // i for i in (1, 2, 3)], True)
    print(f"Triple-window PAV: PASS; {total_triple} committees for n=3..16")

    total_general = 0
    for n in range(3, 11):
        for r in range(2, min(n, 7) + 1):
            denominator = lcm(*range(1, r + 1))
            total_general += test_instance(n, r, [denominator // i for i in range(1, r + 1)], r == 3)
            total_general += test_instance(n, r, list(range(r, 0, -1)), r == 3)
    print(f"All-block generality, two distinct strictly decreasing rules: PASS; {total_general} committee-rule evaluations")

    print("n=12 winner counts by committee size:", [triple_winner_count(12, k) for k in range(13)])


if __name__ == "__main__":
    main()
