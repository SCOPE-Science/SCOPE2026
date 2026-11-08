"""Finite exact checks supporting the branching-word and spherical shift formulas.
All calculations use the Python standard library and rational arithmetic.
These computations are not a proof of infinite-dimensional assertions.
"""
from fractions import Fraction
from math import floor

COUNT = 0

def ck(condition):
    global COUNT
    assert condition
    COUNT += 1


def mechanical(d, j):
    return ((j + 1) * d).__floor__() - (j * d).__floor__()

# Balanced-word identity at rational test slopes.
for den in range(1, 11):
    for num in range(den + 1):
        d = Fraction(num, den)
        for start in range(0, 19):
            for length in range(1, 19):
                actual = sum(mechanical(d, j) for j in range(start, start + length))
                exact = ((start + length) * d).__floor__() - (start * d).__floor__()
                ck(actual == exact)
                ck(abs(Fraction(actual) - length * d) < 1 or length * d == actual)

# Spherical finite-tree formulas, with exact norm squares.
for pattern in ([1, 1, 1, 1], [2, 2, 2, 2], [1, 2, 1, 2], [2, 1, 1, 2], [2, 2, 1, 2]):
    layers = [[()]]
    children = {}
    for b in pattern:
        layer = []
        for v in layers[-1]:
            kids = [v + (j,) for j in range(b)]
            children[v] = kids
            layer.extend(kids)
        layers.append(layer)
    B = 1
    for n, layer in enumerate(layers):
        if n:
            B *= pattern[n-1]
        ck(len(layer) == B)
        for z in [Fraction(0), Fraction(1,2), Fraction(1), Fraction(3,2)]:
            # level-constant values x_v=z^n/B_n satisfy Sx=z*x away from the last level
            coeffs = {}
            prod = 1
            for ell, vs in enumerate(layers):
                if ell:
                    prod *= pattern[ell - 1]
                for v in vs:
                    coeffs[v] = z ** ell / prod
            for v in [u for vs in layers[:-1] for u in vs]:
                ck(sum(coeffs[u] for u in children[v]) == z * coeffs[v])
        ck(len(layer) * Fraction(1, B)**2 == Fraction(1, B))

# Constructed edit intervals are disjoint; check finite concrete windows.
triples = [(Fraction(0), Fraction(1,2), Fraction(1)),
           (Fraction(1,3), Fraction(2,3), Fraction(1)),
           (Fraction(0), Fraction(1), Fraction(1))]
for a, c, b in triples:
    intervals = [(40, 6), (120, 11), (250, 19)]
    def bit(j):
        for start, L in intervals:
            if start <= j < start + L:
                return mechanical(b, j - start)
            if start + L <= j < start + 2*L:
                return mechanical(a, j - start - L)
        return mechanical(c, j)
    for start, length in intervals:
        upper = sum(bit(j) for j in range(start, start+length))
        lower = sum(bit(j) for j in range(start+length, start+2*length))
        ck(abs(Fraction(upper) - b*length) < 1 or upper == b*length)
        ck(abs(Fraction(lower) - a*length) < 1 or lower == a*length)
    for j in range(0, 330):
        ck(bit(j) in (0, 1))
print('EXACT_SPHERICAL_TREE_CHECK_OK', COUNT)
