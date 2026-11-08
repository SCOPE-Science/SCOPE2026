#!/usr/bin/env python3
"""Exhaustive finite certificate for three-color inhibitory firefly dynamics on complete multipartite graphs."""
from collections import Counter
from itertools import product

MASKS = range(1, 8)


def initial(counts):
    return tuple(tuple(c if mask & (1 << c) else -1 for c in (0, 1, 2))
                 for mask, copies in zip(MASKS, counts) for _ in range(copies))


def update(state):
    shores = [set(c for c in row if c >= 0) for row in state]
    blinks = sum(1 in row for row in shores)
    return tuple(
        tuple(-1 if x == -1 else
              (2 if x == 2 and blinks > int(1 in shores[i]) else (x + 1) % 3)
              for x in row)
        for i, row in enumerate(state))


def classify(state):
    seen = {}
    t = 0
    while state not in seen:
        if t > 50:
            raise AssertionError('Unexpected long trajectory')
        seen[state] = t
        state = update(state)
        t += 1
    first, period = seen[state], t-seen[state]
    colors = {c for row in state for c in row if c >= 0}
    return first, period, len(colors) == 1


def realizable_as_at_least_three_shores(counts):
    return max(counts) == 2 or sum(counts) >= 3


def expected_recurrent_three(counts):
    # All shores have one and the same initial color, or exactly one
    # shore contains all three colors and all others are pure color 2.
    singleton = any(counts[k-1] >= 2 and sum(counts) == counts[k-1]
                    for k in (1, 2, 4))
    exceptional = (counts[6] == 1 and counts[3] == 2
                   and sum(counts) == 3)
    return singleton, exceptional


def expected_recurrent_four(counts):
    return (counts[4] == 1 and counts[5] == 1 and
            counts[3] in (1, 2) and
            sum(counts) == counts[3] + 2)


def main():
    tally = Counter()
    checked = 0
    for counts in product(range(3), repeat=7):
        if not realizable_as_at_least_three_shores(counts):
            continue
        checked += 1
        first, period, sync = classify(initial(counts))
        tally[first, period, sync] += 1
        assert first <= 6
        assert period in (3, 4)
        if first:
            assert period == 3 and sync
        if first == 0:
            same, anomalous = expected_recurrent_three(counts)
            if period == 3:
                assert same or anomalous
                assert sync == same
            else:
                assert expected_recurrent_four(counts) and not sync
        else:
            assert not (expected_recurrent_four(counts) or
                        any(expected_recurrent_three(counts)))
    assert checked == 2158  # Checked separately from the enumeration itself.
    # Counts of states with a fixed truncated 7-type multiplicity vector.
    expected = {
        (0, 3, True): 3,
        (0, 3, False): 1,
        (0, 4, False): 2,
        (1, 3, True): 17,
        (2, 3, True): 2009,
        (3, 3, True): 17,
        (4, 3, True): 1,
        (5, 3, True): 65,
        (6, 3, True): 43,
    }
    assert tally == Counter(expected), (checked, tally)
    # Explicit witnesses for sharp entry bounds.
    for r in range(3, 15):
        # special color set {0,2} and all other shores pure 0
        with_mixed_shore = tuple([(0,-1,-1)]*(r-1) + [(0,-1,2)])
        assert classify(with_mixed_shore)[:2] == (6,3)
        full_clique = tuple([(0,-1,-1)]*(r-1) + [(-1,-1,2)])
        assert classify(full_clique)[:2] == (3,3)
    print('REDUCED_OK vectors=%d classes=%s' % (checked, sorted(tally.items())))


if __name__ == '__main__':
    main()
