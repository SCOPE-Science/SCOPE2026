"""Separate finite checks of the one-vacancy cycle equilibrium census.

Run with Python 3.10+; no external packages.  Tests do not substitute for
proof of the infinite identities or limiting exponential rate.
"""

from fractions import Fraction
from itertools import product
from math import comb, factorial


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def theoretical_count(red, blue):
    """Nonmonochromatic equilibrium type words with vacancy fixed."""
    same_ends = binom(red - 1, blue) + binom(blue - 1, red)
    distinct_ends = 2 * sum(
        binom(h, red - h - 1) * binom(h, blue - h - 1)
        for h in range(red + blue)
    )
    return same_ends + distinct_ends


def payoff(state, pos):
    """Fraction of occupied neighboring vertices of different color."""
    length = len(state)
    assert state[pos] != '.'
    neighbors = [state[(pos - 1) % length], state[(pos + 1) % length]]
    present = [v for v in neighbors if v != '.']
    if not present:
        return Fraction(0)
    return Fraction(sum(v != state[pos] for v in present), len(present))


def direct_nash(state):
    """Reconstruct every agent's payoff before/after its only possible jump."""
    arr = list(state)
    vacant = arr.index('.')
    assert arr.count('.') == 1
    for old in range(len(arr)):
        if old == vacant:
            continue
        before = payoff(arr, old)
        arr[vacant], arr[old] = arr[old], '.'
        after = payoff(arr, vacant)
        arr[old], arr[vacant] = arr[vacant], '.'
        if after > before:
            return False
    return True


def run_criterion(word):
    """Separately implement the proved local characterization."""
    n = len(word)
    assert n >= 3
    if word[0] == word[-1]:
        return all(
            (word[i - 1] != word[i] and word[i + 1] != word[i])
            for i in range(1, n - 1)
            if word[i] != word[0]
        )
    return (
        word[0] != word[1]
        and word[-1] != word[-2]
        and all(not (word[i - 1] == word[i] == word[i + 1]) for i in range(1, n - 1))
    )


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def total_formula(n):
    return fibonacci(n + 2) + (-1, 0, 1)[n % 3]


def test():
    orientation_count = 0
    for n in range(3, 17):
        observed = {}
        for word_tuple in product('AB', repeat=n):
            word = ''.join(word_tuple)
            actual = direct_nash('.' + word)
            criterion = run_criterion(word)
            assert actual == criterion, (n, word, actual, criterion)
            orientation_count += 1
            if actual:
                red = word.count('A')
                blue = n - red
                observed[red, blue] = observed.get((red, blue), 0) + 1
        for red in range(1, n):
            blue = n - red
            assert observed.get((red, blue), 0) == theoretical_count(red, blue), (n, red, blue)
        assert sum(observed.values()) == total_formula(n), n

    coefficient_checks = 0
    for n in range(3, 81):
        total = 2  # the two monochromatic words
        for red in range(1, n):
            blue = n - red
            value = theoretical_count(red, blue)
            assert value == theoretical_count(blue, red)
            assert value > 0
            total += value
            coefficient_checks += 1
        assert total == total_formula(n)

    for m in range(2, 81):
        balanced = 2 * sum(binom(h, m - h - 1) ** 2 for h in range(2 * m))
        assert balanced == theoretical_count(m, m)
        assert balanced <= binom(2 * m, m)

    # One small full labeled-assignment census on a cycle with 4 sites.
    # One A and two B agents are distinguishable; every vacancy is examined.
    from itertools import permutations
    agents = ('A0', 'B0', 'B1')
    labeled_count = 0
    for vacancy in range(4):
        for placement in permutations(agents):
            assignment = ['.'] * 4
            sites = [i for i in range(4) if i != vacancy]
            for site, label in zip(sites, placement):
                assignment[site] = label[0]
            labeled_count += direct_nash(''.join(assignment))
    assert labeled_count == 4 * factorial(1) * factorial(2) * theoretical_count(1, 2)
    print(f"PASS: {orientation_count:,} explicit rational-payoff cases (n=3..16)")
    print(f"PASS: {coefficient_checks:,} exact fixed-composition formula comparisons (n=3..80)")
    print("PASS: balanced coefficient identities (m=2..80), full labeled four-site check")
    print("LIMIT: finite checks do not certify the infinite proof or asymptotic theorem")


if __name__ == '__main__':
    test()
