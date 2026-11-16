"""Independent exact certificate check using shifted attack masks and low-bit elimination."""
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


def enumerate_queens(n):
    mask = (1 << n) - 1
    placements = []

    def rec(cols, left, right, columns):
        if len(columns) == n:
            placements.append(tuple(columns))
            return
        available = mask & ~(cols | left | right)
        while available:
            bit = available & -available
            available ^= bit
            columns.append(bit.bit_length() - 1)
            rec(cols | bit, ((left | bit) << 1) & mask,
                ((right | bit) >> 1) & mask, columns)
            columns.pop()

    rec(0, 0, 0, [])
    return placements


def independent_pair_bits(permutation):
    n = len(permutation)
    b = 0
    pair_id = 0
    for i in range(n):
        for j in range(i + 1, n):
            ci, cj = permutation[i], permutation[j]
            # Reverse ordered columns: a deliberately different basis encoding.
            pos = (pair_id * n * (n - 1)
                   + cj * (n - 1) + ci - (ci > cj))
            b ^= 1 << pos
            pair_id += 1
    return b


def rank_lower_pivot(rows):
    basis = {}
    for bits in rows:
        while bits:
            low = bits & -bits
            if low not in basis:
                basis[low] = bits
                break
            bits ^= basis[low]
    return len(basis)


def replay_high_pivots(n, placements, pivot_sequence):
    # Verify the explicitly stored pivot witness against exact row bytes.
    basis = {}
    assert len(pivot_sequence) == len(placements)
    for p, expected in zip(placements, pivot_sequence):
        x = 0
        for i, j in combinations(range(n), 2):
            a, b = p[i], p[j]
            row_pair = i * (2*n-i-1)//2 + j-i-1
            position = row_pair*n*(n-1)+a*(n-1)+b-int(b>a)
            x ^= 1 << position
        while x:
            col = x.bit_length() - 1
            if col not in basis:
                assert col == expected, (n, col, expected)
                basis[col] = x
                break
            x ^= basis[col]
        else:
            raise AssertionError('Unexpected dependent row')
    return len(basis)


def run():
    certificate = json.loads((Path(__file__).resolve().parent / 'rank_certificate.json').read_text())
    summaries = []
    for n in range(7, 13):
        placements = enumerate_queens(n)
        expected = certificate['observations'][n - 4]
        assert len(placements) == expected['solutions']
        if n <= 11:
            rank = rank_lower_pivot(independent_pair_bits(p) for p in placements)
            assert rank == len(placements)
            assert replay_high_pivots(n, placements, certificate['certificate'][str(n)]) == rank
            summaries.append({'n':n, 'configurations':len(placements),
                              'rank_over_GF2':rank})
        else:
            assert len(placements) == 14200
            summaries.append({'n': n, 'configurations': len(placements),
                              'upper_rank_over_R': 66*12*11})
    used = Counter((i, p[i], j, p[j]) for p in enumerate_queens(11)
                   for i in range(11) for j in range(i+1, 11))
    assert len(used) == 5280
    assert min(used.values()) == 2
    assert 1 not in used.values()
    return {'verified': True, 'cases': summaries,
            'used_queen_pairs_at_11':len(used),
            'minimum_pair_completions_at_11':min(used.values())}


if __name__ == '__main__':
    print(json.dumps(run(), separators=(',', ':')))
