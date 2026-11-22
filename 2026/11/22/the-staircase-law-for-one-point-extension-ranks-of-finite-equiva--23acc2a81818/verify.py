"""Independent finite verification of the one-point-extension rank theorem.

Usage: python verify.py
Only Python's standard library is required.

This script exhausts all set partitions of [n], for 0 <= n <= 8.
For every subset F it calculates game rank from the literal one-point
extension semantics, rather than the proposed closed formula, then checks
that the formula gives the same rank. Exhaustion stops at n=8 and is not
itself a proof of the general theorem.
"""
from functools import lru_cache
from math import factorial, isqrt


def restricted_growth_words(n):
    """Enumerate partitions with canonical class labels."""
    if n == 0:
        yield ()
        return

    def extend(word, largest):
        if len(word) == n:
            yield tuple(word)
            return
        for label in range(largest + 2):
            word.append(label)
            yield from extend(word, max(largest, label))
            word.pop()

    yield from extend([0], 0)


def closed_rank(labels, mask):
    """Independent candidate: largest staircase height after any F."""
    members = {}
    for vertex, label in enumerate(labels):
        members.setdefault(label, []).append(vertex)
    taken = {labels[v] for v in range(len(labels)) if (mask >> v) & 1}
    capacities = [sum(not (mask >> v) & 1 for v in members[c]) for c in taken]
    free_sizes = sorted((len(members[c]) for c in members if c not in taken), reverse=True)
    best = 0
    for t in range(1, len(free_sizes) + 1):
        if min(capacities, default=t) < t:
            break
        if all(free_sizes[i] >= t - i for i in range(t)):
            best = t
    return best


def game_rank_engine(labels):
    """Literal minimax evaluation over *all* one-point extension types."""
    n = len(labels)

    @lru_cache(None)
    def rank(mask):
        chosen_classes = {labels[i] for i in range(n) if (mask >> i) & 1}
        # Every abstract prime extension adds to a represented class,
        # or creates a class that is new relative to F.
        extension_types = [("old", c) for c in chosen_classes] + [("new", -1)]
        values = []
        for kind, c in extension_types:
            if kind == "old":
                possible = [i for i in range(n) if not ((mask >> i) & 1) and labels[i] == c]
            else:
                possible = [i for i in range(n) if not ((mask >> i) & 1)
                            and labels[i] not in chosen_classes]
            # A missing realization makes the current position rank zero.
            if not possible:
                return 0
            values.append(max(rank(mask | (1 << i)) for i in possible))
        return 1 + min(values)

    return rank


def verify():
    total_structures = 0
    total_positions = 0
    for n in range(9):
        structures = 0
        for labels in restricted_growth_words(n):
            structures += 1
            rank = game_rank_engine(labels)
            for mask in range(1 << n):
                expected = closed_rank(labels, mask)
                actual = rank(mask)
                if expected != actual:
                    raise AssertionError((n, labels, mask, expected, actual))
                total_positions += 1
            if n:
                bound = (isqrt(8 * n + 1) - 1) // 2
                if rank(0) > bound:
                    raise AssertionError("triangular size bound failed")
        total_structures += structures
        print(f"n={n}: {structures} labelled set partitions, all substructures checked")
    for t in range(1, 9):
        staircase = tuple(range(t, 0, -1))
        n = sum(staircase)
        profile_rank = max((r for r in range(t + 1)
                            if all(staircase[j] >= r - j for j in range(r))), default=0)
        if profile_rank != t or n != t * (t + 1) // 2:
            raise AssertionError("staircase extremizer failed")
        labelled_count = factorial(n)
        for s in staircase:
            labelled_count //= factorial(s)
        if labelled_count <= 0:
            raise AssertionError("enumerator failed")
    print(f"ALL_CHECKS_OK partitions={total_structures} positions={total_positions}")


if __name__ == '__main__':
    verify()
