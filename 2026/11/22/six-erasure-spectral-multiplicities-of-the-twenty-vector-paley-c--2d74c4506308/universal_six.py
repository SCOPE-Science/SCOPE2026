"""Exact six-coordinate skew-sign spectrum classifier, exhaustive modulo switching.

Requires Python 3 standard library only. Run: python universal_six.py
"""
from collections import Counter
from itertools import combinations

TYPES = {(0,1):120, (3,9):240, (4,1):360,
         (5,25):144, (6,49):120, (6,81):40}


def pfaffian(matrix, indices):
    if not indices:
        return 1
    i, *tail = indices
    return sum(((-1) ** j) * matrix[i][partner] *
               pfaffian(matrix, tail[:j] + tail[j + 1:])
               for j, partner in enumerate(tail))


def signature(matrix):
    fours = [pfaffian(matrix, list(J)) ** 2 for J in combinations(range(6), 4)]
    assert set(fours) <= {1, 9}
    k = fours.count(9)
    b = pfaffian(matrix, list(range(6))) ** 2
    return k, b


def acyclic_five(s):
    # First vertex dominates every other one after switching.
    # Check that the remaining 5-vertex tournament is transitive.
    indegree = {i: sum(s[j][i] == 1 for j in range(1,6) if j != i)
                for i in range(1,6)}
    return sorted(indegree.values()) == [0,1,2,3,4]


def all_signatures():
    out = Counter()
    transitive = 0
    for mask in range(1 << 10):
        s = [[0] * 6 for _ in range(6)]
        for j in range(1, 6):
            s[0][j], s[j][0] = 1, -1
        for bit, (i, j) in enumerate(combinations(range(1, 6), 2)):
            v = 1 if mask >> bit & 1 else -1
            s[i][j], s[j][i] = v, -v
        label = signature(s)
        out[label] += 1
        is_transitive = acyclic_five(s)
        assert (label == (0,1)) == is_transitive
        transitive += is_transitive
    assert transitive == 120
    return out


if __name__ == '__main__':
    obs = all_signatures()
    assert obs == TYPES, (obs, TYPES)
    assert sum(obs.values()) == 1024
    for (k, b), number in sorted(obs.items()):
        print(f'k={k}, pfaffian_squared={b}, char_square_coeff={15+8*k}, normalized_pattern_count={number}')
    print('PASS: all 1024 switching-normalized skew sign patterns.')
