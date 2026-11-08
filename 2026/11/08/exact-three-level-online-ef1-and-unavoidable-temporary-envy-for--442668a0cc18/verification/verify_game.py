#!/usr/bin/env python3
"""Exact, self-contained alternating-game verifier for terminal EF1.

Three agents, four sequential goods; each positive value is an ordinal rank.
This certificate checks an adaptive adversary, not merely fixed sequences.
"""
from itertools import product


def violates_ef1(values, recipients):
    """Complete terminal EF1 test using only value ranks."""
    bundles = [[t for t in range(4) if recipients[t] == i] for i in range(3)]
    # Positivity forces every EF1 outcome to have one double and two singletons.
    if sorted(len(b) for b in bundles) != [1, 1, 2]:
        return True
    owner = next(i for i in range(3) if len(bundles[i]) == 2)
    pair = bundles[owner]
    for i in range(3):
        if i == owner:
            continue
        own = values[bundles[i][0]][i]
        if own < min(values[pair[0]][i], values[pair[1]][i]):
            return True
    return False


def adversary_can_force(levels, first_two="free"):
    """Compute OR-over-new-vector, AND-over-allowed-recipient game value."""
    vectors = tuple(product(range(levels), repeat=3))
    visited = [0] * 5

    def force(values, recipients):
        t = len(values)
        visited[t] += 1
        if t == 4:
            return violates_ef1(values, recipients)
        for vector in vectors:
            if t == 1 and first_two == "different":
                allowed = (i for i in range(3) if i != recipients[0])
            elif t == 1 and first_two == "same":
                allowed = (recipients[0],)
            else:
                allowed = range(3)
            if all(force(values + (vector,), recipients + (i,)) for i in allowed):
                return True
        return False

    return force((), ()), visited


def main():
    cases = [
        (3, "free", False),
        (3, "different", True),
        (3, "same", True),
        (4, "free", True),
    ]
    for levels, rule, expected in cases:
        got, nodes = adversary_can_force(levels, rule)
        print("levels=%d first_two=%s adversary_wins=%d depth_counts=%s" %
              (levels, rule, got, nodes))
        assert got is expected, (levels, rule, got, expected)
    print("ALL FOUR GAME VALUES VERIFIED")


if __name__ == "__main__":
    main()
