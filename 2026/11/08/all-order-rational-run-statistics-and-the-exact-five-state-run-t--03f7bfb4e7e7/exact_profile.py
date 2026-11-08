#!/usr/bin/env python3
"""Exact factor and successive-run frequencies for a specified binary Toeplitz word.

This is standalone; Python 3 standard library only. The Toeplitz pattern is a
mathematical input. Rational arithmetic is used at every step.
"""
from fractions import Fraction as F
from functools import lru_cache

PATTERN = '01?0?10??'
HOLE_RANK = {2: 0, 4: 1, 7: 2, 8: 3}
ONE = F(2, 5)
PAIR = {'00': F(3, 10), '01': F(3, 10),
        '10': F(3, 10), '11': F(1, 10)}
EXPECTED = (
    (0, 9, 12, 0, 6),
    (9, 0, 12, 6, 0),
    (12, 12, 8, 2, 2),
    (0, 6, 2, 0, 1),
    (6, 0, 2, 1, 0),
)

# The nine-residue conditioning equations for the base measures.
assert 9 * ONE == 2 + 4 * ONE
assert 9 * PAIR['11'] == 2 * ONE + PAIR['11']
assert PAIR['10'] == ONE - PAIR['11']
assert PAIR['01'] == ONE - PAIR['11']
assert sum(PAIR.values(), F(0)) == 1

@lru_cache(None)
def factor_frequency(word):
    """Exact natural frequency of the word in the Toeplitz fixed point."""
    if not word:
        return F(1)
    if len(word) == 1:
        return ONE if word == '1' else 1 - ONE
    if len(word) == 2:
        return PAIR[word]
    total = F(0)
    for r in range(9):
        hole_letters = []
        hole_indices = []
        consistent = True
        for offset, target in enumerate(word):
            block, position = divmod(r + offset, 9)
            fixed_symbol = PATTERN[position]
            if fixed_symbol != '?':
                if fixed_symbol != target:
                    consistent = False
                    break
            else:
                hole_letters.append(target)
                hole_indices.append(4 * block + HOLE_RANK[position])
        if not consistent:
            continue
        assert hole_indices == list(range(hole_indices[0], hole_indices[0] + len(hole_indices))) if hole_indices else True
        assert len(hole_letters) < len(word), ('nondecreasing recurrence', r, word)
        total += factor_frequency(''.join(hole_letters))
    return total / 9


def successive_run_density(a, b):
    if a > 5 or b > 5 or a < 1 or b < 1:
        return F(0)
    return factor_frequency('1' + '0' * (a - 1) + '1' + '0' * (b - 1) + '1')


def main():
    matrix = [[successive_run_density(a, b) for b in range(1, 6)] for a in range(1, 6)]
    normalized = [[v / ONE for v in row] for row in matrix]
    expected = [[F(c, 108) for c in row] for row in EXPECTED]
    assert normalized == expected, (normalized, expected)
    assert sum(map(sum, normalized), F(0)) == 1
    assert normalized == [list(row) for row in zip(*normalized)]
    marginal = list(map(sum, normalized))
    assert marginal == [F(1, 4), F(1, 4), F(1, 3), F(1, 12), F(1, 12)]
    assert sum(F(i+1)*marginal[i] for i in range(5)) == F(5, 2)
    # Verify the nontrivial base+short-window formulas used in the argument.
    assert [factor_frequency(w) for w in ('101', '100', '1001', '1000', '0001', '0000')] == [F(1,10), F(1,5), F(2,15), F(1,15), F(1,15), F(1,30)]
    for n in range(1, 24):
        for w_int in range(min(1<<n, 16)):
            v = f'{w_int:0{n}b}'
            assert 0 <= factor_frequency(v) <= 1
    print('EXACT_RUN_PROFILE_OK')
    print('five_by_five_numerators_denominator_108:', EXPECTED)
    print('marginals:', marginal)
    print('mean_length:', F(5,2))
    print('cache_words:', factor_frequency.cache_info().currsize)

if __name__ == '__main__':
    main()
