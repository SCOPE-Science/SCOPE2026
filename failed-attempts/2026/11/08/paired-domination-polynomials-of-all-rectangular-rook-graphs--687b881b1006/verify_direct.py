"""Direct adjacency-and-matching enumeration of paired dominating rook placements.

Uses no line-graph component-parity theorem or generating-function coefficients.
Run with Python 3.9+; standard library only.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
import json


def direct_counts(m, n):
    squares = [(i, j) for i in range(m) for j in range(n)]
    counts = Counter()
    for k in range(2, m * n + 1, 2):
        for subset in combinations(range(m * n), k):
            chosen = [squares[q] for q in subset]
            chosen_set = set(chosen)
            if any((i, j) not in chosen_set and
                   not any(i == a or j == b for a, b in chosen)
                   for i in range(m) for j in range(n)):
                continue
            adj = [tuple(j for j in range(k) if i != j and
                         (chosen[i][0] == chosen[j][0] or
                          chosen[i][1] == chosen[j][1]))
                   for i in range(k)]

            @lru_cache(None)
            def has_matching(mask):
                if not mask:
                    return True
                low = mask & -mask
                i = low.bit_length() - 1
                rem = mask ^ low
                return any(rem & (1 << j) and
                           has_matching(rem ^ (1 << j)) for j in adj[i])

            if has_matching((1 << k) - 1):
                counts[k] += 1
    return dict(sorted(counts.items()))


if __name__ == '__main__':
    expected = {
        (2, 2): {2: 4, 4: 1},
        (2, 3): {2: 3, 4: 15, 6: 1},
        (2, 4): {2: 4, 4: 62, 6: 28, 8: 1},
        (3, 3): {4: 81, 6: 84, 8: 9},
        (3, 4): {4: 129, 6: 840, 8: 495, 10: 66, 12: 1},
        (3, 5): {4: 210, 6: 3655, 8: 6300, 10: 3003, 12: 455, 14: 15},
        (4, 4): {4: 80, 6: 4464, 8: 12150, 10: 7992, 12: 1820,
                 14: 120, 16: 1},
    }
    for shape, want in expected.items():
        got = direct_counts(*shape)
        assert got == want, (shape, got, want)
        print(json.dumps({'board': list(shape), 'coefficients': got,
                          'direct_perfect_matching': 'PASS'}, sort_keys=True))
    print('DIRECT_PASS: all seven board polynomials match.')
