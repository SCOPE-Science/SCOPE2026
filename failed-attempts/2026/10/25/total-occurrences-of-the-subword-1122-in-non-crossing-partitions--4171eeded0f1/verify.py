#!/usr/bin/env python3
"""Finite sanity check for the total 1122 count in non-crossing partitions."""
from math import comb


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def can_append(prefix, value):
    """Reject an append that would complete a classical 1212 crossing."""
    seen_before = set()
    labels_with_value_between = set()
    for label in prefix:
        if label == value:
            labels_with_value_between.update(seen_before)
        else:
            if label in labels_with_value_between:
                return False
            seen_before.add(label)
    return True


def noncrossing_rgfs(n):
    if n == 0:
        yield ()
        return
    word = [1] * n

    def extend(i, maximum):
        if i == n:
            yield tuple(word)
            return
        for value in range(1, maximum + 2):
            prefix = word[:i]
            if can_append(prefix, value):
                word[i] = value
                yield from extend(i + 1, max(maximum, value))

    yield from extend(1, 1)


def occurrence_count(word):
    return sum(
        word[i] == word[i + 1]
        and word[i + 2] == word[i + 3]
        and word[i] < word[i + 2]
        for i in range(len(word) - 3)
    )


def main():
    for n in range(0, 11):
        total_partitions = 0
        total_occurrences = 0
        for word in noncrossing_rgfs(n):
            total_partitions += 1
            total_occurrences += occurrence_count(word)
        assert total_partitions == catalan(n), (n, total_partitions, catalan(n))
        expected = comb(2 * n - 5, n - 4) if n >= 4 else 0
        assert total_occurrences == expected, (n, total_occurrences, expected)
    print("PASS: Catalan cardinalities and 1122 totals verified for n=0..10")


if __name__ == "__main__":
    main()
