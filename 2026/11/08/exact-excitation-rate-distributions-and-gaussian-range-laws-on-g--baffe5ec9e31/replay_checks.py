#!/usr/bin/env python3
"""Cross-check two exact counting constructions against complete state dynamics."""
from exact_coefficients import rate_counts, equal_arm_fast, zero_count
from direct_trajectories import census

TESTS = [(2,2,2),(2,2,2,2),(2,2,2,2,2),(3,3,3),
         (3,3,3,3),(4,4,4),(2,3,4),(2,2,3,3),(2,3,3,4)]
for lengths in TESTS:
    expected = rate_counts(lengths)
    assert expected == census(lengths,'CCA')
    actual_ghm = census(lengths,'GHM')
    assert {rate/3: count for rate, count in expected.items()} == dict(actual_ghm)
    assert expected[min(expected)] == zero_count(lengths)
    if len(set(lengths)) == 1:
        r, n = len(lengths), lengths[0]
        assert list(expected.values()) == equal_arm_fast(r,n)
    print('REPLAY_OK', lengths, len(expected), 'activity classes')
print('ALL_REPLAYS_OK')
