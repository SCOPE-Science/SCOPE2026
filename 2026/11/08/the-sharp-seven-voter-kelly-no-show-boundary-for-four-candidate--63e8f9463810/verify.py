"""Exact exhaustive certificate for four-candidate, three-seat seqPAV.

Run: python3 verify.py
Uses only the Python standard library.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement, permutations
from math import comb

M = 4
K = 3
BALLOTS = tuple(range(1, 1 << M))
ALL = (1 << M) - 1

# Multiplying every marginal score by six makes all comparisons integral:
# before any of the first three selections, one voter has weight 1, 1/2 or 1/3.
COEFF = tuple(
    tuple(
        tuple(6 // (1 + (ballot & selected).bit_count()) if ballot & (1 << c)
              else 0 for c in range(M))
        for selected in range(1 << M)
    )
    for ballot in BALLOTS
)


def winners(counts):
    """All size-three committees from all possible tie branches, as masks."""
    states = {0}
    for _ in range(K):
        next_states = set()
        for selected in states:
            scores = [
                sum(count * COEFF[index][selected][c]
                    for index, count in enumerate(counts))
                if not selected & (1 << c) else -1
                for c in range(M)
            ]
            best = max(scores)
            for c in range(M):
                if scores[c] == best:
                    next_states.add(selected | (1 << c))
        states = next_states
    assert all(mask.bit_count() == K for mask in states)
    return frozenset(states)


def winners_fraction(ballots):
    """Separate direct rational implementation using explicit greedy sequences."""
    outcomes = set()
    def rec(sequence):
        if len(sequence) == K:
            outcomes.add(sum(1 << c for c in sequence))
            return
        available = [c for c in range(M) if c not in sequence]
        selected = sum(1 << c for c in sequence)
        gain = {}
        for c in available:
            gain[c] = sum(
                (Fraction(1, 1 + (b & selected).bit_count())
                 for b in ballots if b & (1 << c)), Fraction(0, 1)
            )
        best = max(gain.values())
        for c in available:
            if gain[c] == best:
                rec(sequence + (c,))
    rec(())
    return frozenset(outcomes)


def kelly_abstention_improvement(voting, abstaining, ballot):
    with_vote = [(w & ballot).bit_count() for w in voting]
    without_vote = [(w & ballot).bit_count() for w in abstaining]
    # Kelly weak comparison holds pairwise across all winning committees.
    # Kelly strict requires one strictly better pair.
    return min(without_vote) >= max(with_vote) and max(without_vote) > min(with_vote)


def relabel(profile, permutation):
    return tuple(sorted(
        sum(1 << permutation[c] for c in range(M) if mask & (1 << c))
        for mask in profile
    ))


def run():
    totals = {}
    failures = {}
    deletion_checks = 0
    fraction_checks = 0
    for n in range(1, 8):
        profile_count = 0
        paradox_profiles = {}
        for ballot_indices in combinations_with_replacement(range(len(BALLOTS)), n):
            profile = tuple(BALLOTS[index] for index in ballot_indices)
            counts = [0] * len(BALLOTS)
            for index in ballot_indices:
                counts[index] += 1
            with_vote = winners(counts)
            if n <= 4 or (n == 7 and profile_count % 101 == 0):
                assert with_vote == winners_fraction(profile)
                fraction_checks += 1
            profitable = []
            for index in set(ballot_indices):
                counts[index] -= 1
                without_vote = winners(counts)
                counts[index] += 1
                deletion_checks += 1
                if kelly_abstention_improvement(with_vote, without_vote, BALLOTS[index]):
                    profitable.append((BALLOTS[index], without_vote))
            if profitable:
                paradox_profiles[profile] = (with_vote, profitable)
            profile_count += 1
        assert profile_count == comb(n + 14, 14)
        totals[n] = profile_count
        failures[n] = paradox_profiles
        print(f"n={n}: anonymous profiles={profile_count}, paradox profiles={len(paradox_profiles)}")
    assert all(len(failures[n]) == 0 for n in range(1, 7))
    assert len(failures[7]) == 12

    representative = (3, 3, 5, 5, 10, 12, 14)
    expected_orbit = {relabel(representative, p) for p in permutations(range(M))}
    assert len(expected_orbit) == 12
    assert set(failures[7]) == expected_orbit

    expected_with = frozenset({7, 11, 13})
    assert failures[7][representative][0] == expected_with
    good = {b: w for b, w in failures[7][representative][1]}
    assert good == {3: frozenset({7}), 5: frozenset({7})}

    for profile, (with_vote, profitable) in failures[7].items():
        assert len(with_vote) == 3
        assert len(profitable) == 2
        counter = Counter(profile)
        assert all(counter[b] == 2 for b, _ in profitable)
        for ballot, without in profitable:
            assert len(without) == 1
            assert [(w & ballot).bit_count() for w in without] == [2]
            assert sorted((w & ballot).bit_count() for w in with_vote) == [1, 2, 2]
            assert with_vote == winners_fraction(profile)
            sub = list(profile)
            sub.remove(ballot)
            assert without == winners_fraction(sub)
            fraction_checks += 2

    print('All seven electorate sizes exhausted:', sum(totals.values()), 'profiles')
    print('All distinct-ballot deletion tests:', deletion_checks)
    print('Independent exact-rational selections:', fraction_checks)
    print('At n=7 there is one candidate-relabeling orbit of 12 profiles.')
    print('Each of its profiles has two profitable ballot types, each occurring twice.')
    print('Representative: 2x{a,b}, 2x{a,c}, {b,d}, {c,d}, {b,c,d}.')
    print('Full electorate winners: {a,b,c}, {a,b,d}, {a,c,d}.')
    print('After removing either {a,b} or {a,c}: only {a,b,c}.')
    print('PASS')

if __name__ == '__main__':
    run()
