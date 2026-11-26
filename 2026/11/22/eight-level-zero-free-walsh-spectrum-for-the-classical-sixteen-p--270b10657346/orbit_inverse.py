"""Exact affine-orbit convolution certificate for the SQS(16) inverse.

Python 3.10+ standard library. Only 8 * 140 orbit transitions are counted.
"""
from fractions import Fraction
from itertools import combinations

points = range(16)
one = (1 << 16) - 1


def linear(a):
    return sum(((a & x).bit_count() % 2) << x for x in points)


forms = [linear(a) for a in points]
blocks = {
    (forms[a] ^ (e * one)) & (forms[b] ^ (f * one))
    for a, b in combinations(range(1, 16), 2)
    for e in (0, 1)
    for f in (0, 1)
}
assert len(blocks) == 140
affine_weight8 = {h ^ (e * one) for h in forms[1:] for e in (0, 1)}
types = [0, 4, 6, 8, -8, 10, 12, 16]


def orbit(word):
    weight = word.bit_count()
    if weight == 8 and word not in affine_weight8:
        weight = -8
    return types.index(weight)


x, y, z, t = [forms[1 << i] for i in range(4)]
q, b = x & y, (x & y) ^ (z & t)
representatives = [0, q, b, x, q ^ z, b ^ one, q ^ one, one]
assert [orbit(h) for h in representatives] == list(range(8))
matrix = []
for h in representatives:
    row = [0] * 8
    for block in blocks:
        row[orbit(h ^ block)] += 1
    matrix.append(row)
assert matrix == [
    [0,140,0,0,0,0,0,0],
    [1,36,64,3,36,0,0,0],
    [0,20,45,0,60,15,0,0],
    [0,14,0,0,112,0,14,0],
    [0,6,32,4,60,32,6,0],
    [0,0,15,0,60,45,20,0],
    [0,0,0,3,36,64,36,1],
    [0,0,0,0,0,0,140,0],
]
values = [-255,24,-9,25,-3,7,0,-415]
assert [sum(a*b for a,b in zip(row,values)) for row in matrix] == [3360]+[0]*7
sizes = [1,140,448,30,840,448,140,1]
assert sum(sizes) == 2048
assert all(sizes[i]*matrix[i][j] == sizes[j]*matrix[j][i] for i in range(8) for j in range(8))
assert Fraction(sum(abs(a)*n for a,n in zip(values,sizes)),3360) == Fraction(3617,840)
for row in matrix:
    print(row)
print('3360 times inverse on the eight orbits:', values)
print('endpoint norm:', Fraction(3617,840))
