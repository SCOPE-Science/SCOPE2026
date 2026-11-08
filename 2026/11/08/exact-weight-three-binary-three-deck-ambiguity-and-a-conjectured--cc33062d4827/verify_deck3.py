#!/usr/bin/env python3
"""Independent finite tests for the exact binary weight-three three-deck theorem."""

from collections import defaultdict
from itertools import combinations
from math import comb
from random import Random


def word_from_gaps(g):
    a, b, c, d = g
    return "0" * a + "1" + "0" * b + "1" + "0" * c + "1" + "0" * d


def direct_deck(word):
    counts = {"".join(bits): 0 for bits in __import__("itertools").product("01", repeat=3)}
    for positions in combinations(range(len(word)), 3):
        key = "".join(word[i] for i in positions)
        counts[key] += 1
    return tuple(counts[key] for key in sorted(counts))


def dynamic_deck(word):
    counts = {"": 1}
    for letter in word:
        snapshot = counts.copy()
        for subsequence, amount in snapshot.items():
            if len(subsequence) < 3:
                longer = subsequence + letter
                counts[longer] = counts.get(longer, 0) + amount
    return tuple(counts.get(key, 0) for key in
                 ("000", "001", "010", "011", "100", "101", "110", "111"))


def proposed_partner(g):
    a, b, c, d = g
    if (b - c) % 3 != 0:
        return None
    t = (b - c) // 3
    if t == 0 or a + t < 0 or d - t < 0:
        return None
    return (a + t, c, b, d - t)


def collision_formula(n):
    total = n - 3
    return sum(total - 4 * t - 2 * h + 1
               for t in range(1, total // 4 + 1)
               for h in range((total - 4 * t) // 2 + 1))


def collision_quasipolynomial(n):
    if n % 4 == 0:
        return n * (n - 4) * (n - 5) // 48
    if n % 4 == 2:
        return (n - 1) * (n - 2) * (n - 6) // 48
    return (n - 1) * (n - 3) * (n - 5) // 48


def all_gaps(total):
    for a in range(total + 1):
        for b in range(total - a + 1):
            for c in range(total - a - b + 1):
                yield (a, b, c, total - a - b - c)


def main():
    number_of_words = 0
    number_of_pairs = 0
    for n in range(3, 20):
        fibers = defaultdict(list)
        for g in all_gaps(n - 3):
            word = word_from_gaps(g)
            if n <= 16:
                assert direct_deck(word) == dynamic_deck(word), (n, g)
                deck = direct_deck(word)
            else:
                deck = dynamic_deck(word)
            fibers[deck].append(g)
            number_of_words += 1
        pairs = 0
        for group in fibers.values():
            assert len(group) <= 2, (n, group)
            if len(group) == 2:
                a, b = group
                assert proposed_partner(a) == b and proposed_partner(b) == a, (n, a, b)
                pairs += 1
            else:
                assert proposed_partner(group[0]) is None, (n, group)
        expected = collision_formula(n)
        assert pairs == expected == collision_quasipolynomial(n), (n, pairs, expected)
        assert len(fibers) == comb(n, 3) - expected
        number_of_pairs += pairs
    rng = Random(630511)
    tested_large_pairs = 0
    for _ in range(250):
        n = rng.randrange(20, 401)
        # Random weak compositions, selected without relying on deck identities.
        cuts = sorted(rng.sample(range(n), 3))
        g = (cuts[0], cuts[1]-cuts[0]-1, cuts[2]-cuts[1]-1, n-cuts[2]-1)
        assert sum(g) == n - 3
        partner = proposed_partner(g)
        if partner is not None:
            tested_large_pairs += 1
            assert partner != g
            assert proposed_partner(partner) == g
            assert dynamic_deck(word_from_gaps(g)) == dynamic_deck(word_from_gaps(partner))
    assert tested_large_pairs >= 10, tested_large_pairs
    assert collision_formula(7) == 1
    assert dynamic_deck("1000110") == dynamic_deck("0110001")
    for n in range(20, 401):
        assert collision_formula(n) == collision_quasipolynomial(n)
    print("PASS: all fixed-weight-three deck fibers and involution for lengths 3 through 19")
    print("PASS: direct and dynamic three-subsequence algorithms agree for lengths 3 through 16")
    print(f"PASS: {number_of_words} words, {number_of_pairs} doubleton fibers")
    print(f"PASS: 250 seeded larger-word samples ({tested_large_pairs} admissible partners), quasipolynomial to length 400")


if __name__ == "__main__":
    main()
