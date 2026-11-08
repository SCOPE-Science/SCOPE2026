"""Exact finite-period certificate for a two-dimensional border-collision map.
Run with Python 3.9+; uses only the standard library.
This finite certificate accompanies an analytic upper-bound proof.
"""
from fractions import Fraction as Q
from itertools import product

Z = Q(0)
O = Q(1)
A = {
    'L': ((Q(1), O), (Q(7, 4), Z)),
    'R': ((Q(-7, 4), O), (Q(-3, 5), Z)),
}
b = (O, Z)
I = ((O, Z), (Z, O))

def matmul(U, V):
    return tuple(tuple(sum(U[i][k] * V[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))

def matvec(U, v):
    return tuple(sum(U[i][j] * v[j] for j in range(2)) for i in range(2))

def add(u, v):
    return (u[0] + v[0], u[1] + v[1])

def det(U):
    return U[0][0] * U[1][1] - U[0][1] * U[1][0]

def minus_I(U):
    return ((O-U[0][0], -U[0][1]), (-U[1][0], O-U[1][1]))

def plus_I(U):
    return ((O+U[0][0], U[0][1]), (U[1][0], O+U[1][1]))

def solve(U, v):
    d = det(U)
    assert d != 0, 'singular return: needs separate treatment'
    return ((U[1][1] * v[0] - U[0][1] * v[1]) / d,
            (-U[1][0] * v[0] + U[0][0] * v[1]) / d)

def iterate(word):
    M, c = I, (Z, Z)
    for letter in word:
        M = matmul(A[letter], M)
        c = add(matvec(A[letter], c), b)
    root = solve(minus_I(M), c)
    pts = []
    v = root
    for letter in word:
        pts.append(v)
        assert (letter == 'L' and v[0] < 0) or (letter == 'R' and v[0] > 0)
        v = add(matvec(A[letter], v), b)
    assert v == root
    return root, pts, M

def minperiod(word):
    for k in (1, 2, 4):
        if all(word[j] == word[(j + k) % 4] for j in range(4)):
            return k
    raise AssertionError

def necklace(word):
    return min(word[j:] + word[:j] for j in range(4))

EXPECTED = {
    'LLLL': (Q(-4, 7), Q(-959, 256), 1),
    'RRRR': (Q(20, 67), Q(-259089, 160000), 1),
    'LRLR': (Q(-3, 11), Q(-143, 400), 2),
    'LLLR': (Q(-440, 799), Q(799, 320), 4),
    'LLRR': (Q(-1348, 2571), Q(-2571, 1600), 4),
    'LRRR': (Q(-3867, 8396), Q(2099, 2000), 4),
}
STABILITY = {
    'LLLR': (Q(-377,80), Q(-1029,320), Q(-2217,320)),
    'LLRR': (Q(1187,320), Q(441,400), Q(9299,1600)),
    'LRRR': (Q(-171,400), Q(-189,500), Q(389,2000)),
}

all_points = set()
count = {1: 0, 2: 0, 4: 0}
necklaces = {}
for tup in product('LR', repeat=4):
    word = ''.join(tup)
    root, pts, M = iterate(word)
    assert root not in all_points, f'non-unique assigned root for {word}'
    all_points.add(root)
    d = minperiod(word)
    assert all(pts[j] == pts[(j+d)%4] for j in range(4))
    count[d] += 1
    necklaces.setdefault(necklace(word), []).append(word)
    if word in EXPECTED:
        x, determinant, period = EXPECTED[word]
        assert root[0] == x
        assert det(minus_I(M)) == determinant
        assert d == period
    if word in STABILITY:
        trace, determ, val = STABILITY[word]
        assert M[0][0] + M[1][1] == trace
        assert det(M) == determ
        assert det(plus_I(M)) == val
        if word == 'LRRR':
            assert det(minus_I(M)) > 0 and val > 0 and O - determ > 0
        if word == 'LLLR':
            assert val < 0 and determ < 0
        if word == 'LLRR':
            assert det(minus_I(M)) < 0 and trace > 0 and determ > 0

assert set(necklaces) == set(EXPECTED)
assert {w:len(v) for w,v in necklaces.items()} == {
    'LLLL': 1, 'RRRR': 1, 'LRLR': 2, 'LLLR': 4, 'LLRR': 4, 'LRRR': 4}
assert count == {1: 2, 2: 2, 4: 12}, count
assert len(all_points) == 16
assert Q(1) > abs(Q(1) + Q(-7,4))
assert Q(-7,4) < -abs(Q(1) + Q(3,5))
print('EXACT_16_WORD_CENSUS_OK')
print('PERIODS_2_2_12_OK')
print('MONODROMY_AND_HYPERBOLICITY_OK')
