#!/usr/bin/env python3
"""Independent finite checks for the finite strict-weak-order rank theorem.

Execute: python3 weakorder_rank_verify.py
Uses only Python standard library. The finite checks support, but cannot replace,
the all-size induction in RESULT.md.
"""
from functools import lru_cache
from itertools import product
import random


@lru_cache(maxsize=None)
def interval_rank(widths):
    """Weighted split recurrence; independent of the extension game below."""
    if not widths:
        return 0
    return max(min(width, 1 + interval_rank(widths[:j]),
                   1 + interval_rank(widths[j + 1:]))
               for j, width in enumerate(widths))


def canonical(rank):
    if rank == 0:
        return ()
    previous = canonical(rank - 1)
    return previous + (rank,) + previous


def subsequence_contains(widths, sought):
    j = 0
    for width in widths:
        if j < len(sought) and width >= sought[j]:
            j += 1
    return j == len(sought)


def compositions(n):
    for mask in range(1 << (n - 1)):
        out = []
        run = 1
        for j in range(n - 1):
            if mask & (1 << j):
                out.append(run)
                run = 1
            else:
                run += 1
        out.append(run)
        yield tuple(out)


def direct_rank_game(widths):
    """Minimax over all actual one-point extension types and host replies.

    A state records the numbers of distinct marked elements in host levels.
    Types: one new element in each existing marked class, or one new class
    in any of the gaps between consecutive marked host levels (including
    the end gaps). All legal host realizations of each type are enumerated.
    """
    level_count = len(widths)

    @lru_cache(maxsize=None)
    def rank(state):
        marked_levels = [i for i, count in enumerate(state) if count > 0]
        extension_types = []
        # Join an already marked incomparability class.
        for i in marked_levels:
            if state[i] < widths[i]:
                reply = list(state)
                reply[i] += 1
                extension_types.append([tuple(reply)])
            else:
                extension_types.append([])
        # Introduce a new incomparability class at each cut.
        limits = [-1] + marked_levels + [level_count]
        for left, right in zip(limits, limits[1:]):
            replies = []
            for i in range(left + 1, right):
                reply = list(state)
                reply[i] = 1
                replies.append(tuple(reply))
            extension_types.append(replies)
        if not extension_types or any(not replies for replies in extension_types):
            return 0
        return 1 + min(max(rank(reply) for reply in replies)
                       for replies in extension_types)

    def claimed_relative_rank(state):
        selected = [i for i, count in enumerate(state) if count > 0]
        limits = [-1] + selected + [level_count]
        resources = [widths[i] - state[i] for i in selected]
        resources.extend(interval_rank(widths[left + 1:right])
                         for left, right in zip(limits, limits[1:]))
        return min(resources)

    states_checked = 0
    for state in product(*(range(a + 1) for a in widths)):
        actual = rank(state)
        claimed = claimed_relative_rank(state)
        if actual != claimed:
            raise AssertionError((widths, state, actual, claimed))
        states_checked += 1
    return states_checked, rank((0,) * level_count)


def main():
    state_total = 0
    sequence_total = 0
    per_n_max = []
    minimal_rank2 = []
    minimal_rank3 = []
    for n in range(1, 12):
        best = 0
        for widths in compositions(n):
            states, actual = direct_rank_game(widths)
            state_total += states
            sequence_total += 1
            direct = interval_rank(widths)
            if actual != direct:
                raise AssertionError(("whole rank", widths, actual, direct))
            # A separate left-to-right pattern embedding test.
            canonical_rank = max(t for t in range(8)
                                 if subsequence_contains(widths, canonical(t)))
            if actual != canonical_rank:
                raise AssertionError(("canonical", widths, actual, canonical_rank))
            best = max(best, actual)
            if actual >= 2 and n == 4:
                minimal_rank2.append(widths)
            if actual >= 3 and n == 11:
                minimal_rank3.append(widths)
        per_n_max.append(best)
        # Direct numerical threshold from the proposed minimal-size law.
        expected_best = max(t for t in range(8) if 2 ** (t + 1) - t - 2 <= n)
        if best != expected_best:
            raise AssertionError(("threshold", n, best, expected_best))
    assert minimal_rank2 == [(1, 2, 1)], minimal_rank2
    assert minimal_rank3 == [(1, 2, 1, 3, 1, 2, 1)], minimal_rank3
    assert per_n_max == [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3], per_n_max

    # Extra nonexhaustive independent pattern-versus-recursion checks.
    random.seed(1532604)
    random_cases = 1200
    for _ in range(random_cases):
        h = random.randint(0, 65)
        widths = tuple(random.randint(1, 7) for _ in range(h))
        r = interval_rank(widths)
        by_subseq = max(t for t in range(8)
                        if subsequence_contains(widths, canonical(t)))
        if r != by_subseq:
            raise AssertionError(("random", widths, r, by_subseq))
    for t in range(1, 7):
        pattern = canonical(t)
        assert len(pattern) == 2 ** t - 1
        assert sum(pattern) == 2 ** (t + 1) - t - 2
        assert interval_rank(pattern) == t
    print('CHECK_OK')
    print('ALL_COMPOSITIONS_THROUGH_N=11', sequence_total)
    print('ALL_MARKED_STATES_THROUGH_N=11', state_total)
    print('INDEPENDENT_RANDOM_PROFILE_TESTS', random_cases)
    print('UNIQUE_MINIMAL_RANK_2', minimal_rank2)
    print('UNIQUE_MINIMAL_RANK_3', minimal_rank3)
    print('MAX_RANKS_FOR_N_1_THROUGH_11', per_n_max)
    print('CANONICAL_SIZES_RANK_1_THROUGH_6',
          [sum(canonical(t)) for t in range(1, 7)])


if __name__ == '__main__':
    main()
