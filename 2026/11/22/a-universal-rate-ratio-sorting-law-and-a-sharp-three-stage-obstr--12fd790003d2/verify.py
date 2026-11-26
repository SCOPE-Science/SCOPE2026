"""Exact finite check for the local and global three-transition obstruction."""

from fractions import Fraction as Q
from itertools import permutations
from math import prod


def transient(r):
    """Transient probability matrix at t=log(2) via partial fractions."""
    T = [[Q(0) for j in range(3)] for i in range(3)]
    for j in range(3):
        for i in range(j, 3):
            T[i][j] = prod(r[j:i]) * sum(
                Q(1, 2**r[k] * prod(r[l] - r[k] for l in range(j, i + 1) if l != k))
                for k in range(j, i + 1)
            )
        assert sum(T[i][j] for i in range(3)) <= 1
    assert all(x >= 0 for row in T for x in row)
    return T


blocks = {key: transient(r) for key, r in {
    'A': (4, 1, 2), 'B': (1, 4, 3), 'C': (8, 1, 2),
}.items()}

numerators = {
    'A': (48, [[3, 0, 0], [28, 24, 0], [10, 12, 12]]),
    'B': (48, [[24, 0, 0], [7, 3, 0], [8, 12, 6]]),
    'C': (1792, [[7, 0, 0], [1016, 896, 0], [428, 448, 448]]),
}
for letter, (d, rows) in numerators.items():
    assert blocks[letter] == [[Q(x, d) for x in row] for row in rows]


def completion(sequence):
    state = [Q(1), Q(0), Q(0)]
    for letter in sequence:
        state = [sum(x * z for x, z in zip(row, state)) for row in blocks[letter]]
    return 1 - sum(state)


assert completion('AB') == Q(569, 768)
assert completion('BA') == Q(324, 768)
assert completion('AB') - completion('BA') == Q(245, 768)
table = {''.join(word): completion(word) for word in permutations('ABC')}
assert table == {k: Q(v, 1376256) for k, v in dict(
    ABC=1231672, ACB=1198687, BAC=902392,
    BCA=938120, CAB=1218287, CBA=1277532,
).items()}
assert table['CAB'] - table['CBA'] == Q(-59245, 1376256)
assert all(table['CBA'] > value for key, value in table.items() if key != 'CBA')
print('PASS: exact transient matrices, two local swap signs, and both unique optima')
