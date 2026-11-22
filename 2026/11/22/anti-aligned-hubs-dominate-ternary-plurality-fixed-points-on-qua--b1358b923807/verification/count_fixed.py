"""Exact all-page-size recurrence for ternary plurality fixed configurations.

No third-party modules. Run `python verification/count_fixed.py`.
"""
from collections import defaultdict

PAGE_EQUAL = ((0, 0), (1, 1), (1, 2), (2, 1), (2, 2))
PAGE_UNEQUAL = ((0, 0), (0, 1), (0, 2), (1, 1), (2, 1), (2, 2))


def keeps(incumbent, counts):
    maximum = max(counts)
    winners = [i for i in range(3) if counts[i] == maximum]
    return len(winners) != 1 or winners[0] == incumbent


def sector(pages, hub_left, hub_right, number_of_pages):
    # Keys are ordered counts for the three colors on each of the two outer shores.
    counts = {(0, 0, 0, 0, 0, 0): 1}
    for _ in range(number_of_pages):
        following = defaultdict(int)
        for key, ways in counts.items():
            for left, right in pages:
                successor = list(key)
                successor[left] += 1
                successor[3 + right] += 1
                following[tuple(successor)] += ways
        counts = following
    result = 0
    for histogram, ways in counts.items():
        l = list(histogram[:3]); r = list(histogram[3:])
        l[hub_right] += 1; r[hub_left] += 1
        if keeps(hub_left, l) and keeps(hub_right, r):
            result += ways
    assert sum(counts.values()) == len(pages) ** number_of_pages
    return result


def fixed_counts(m):
    if m < 1:
        raise ValueError('A quadrilateral book has at least one page')
    a = sector(PAGE_EQUAL, 0, 0, m)
    b = sector(PAGE_UNEQUAL, 0, 1, m)
    return a, b, 3 * a + 6 * b


if __name__ == '__main__':
    expected = [
        (5, 4, 39), (13, 9, 93), (61, 58, 531),
        (293, 705, 5109), (1001, 2996, 20979),
        (4885, 19446, 131331), (22765, 152426, 982851),
        (88485, 811901, 5136861), (421369, 5036368, 31482315),
        (1999493, 35037414, 216222963),
    ]
    for m, triple in enumerate(expected, start=1):
        got = fixed_counts(m)
        assert got == triple, (m, got, triple)
        print(m, *got)
    print('EXACT_COUNTS_OK')
