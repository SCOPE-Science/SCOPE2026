#!/usr/bin/env python3
"""Reproducible finite stress test for the signed-divisor continuity criterion.

Finite stress tests support, but do not prove, the arbitrary-rank theorem.
"""
from itertools import product

def leq(x, y):
    return all(a == 0 or (a*b > 0 and abs(a) <= abs(b)) for a,b in zip(x,y))

def affine(matrix, shift, x):
    return tuple(c+sum(a*t for a,t in zip(row,x)) for row,c in zip(matrix,shift))

def proposed(matrix, shift):
    return all((sum(a != 0 for a in row) == 0) or
               (c == 0 and sum(a != 0 for a in row) == 1)
               for row,c in zip(matrix,shift))

def check():
    vectors = list(product(range(-2,3), repeat=2))
    comparable = [(x,y) for x in vectors for y in vectors if leq(x,y)]
    checked = 0
    for entries in product((-1,0,1), repeat=4):
        matrix = (entries[:2], entries[2:])
        for shift in product((-1,0,1), repeat=2):
            actual = all(leq(affine(matrix,shift,x),affine(matrix,shift,y))
                         for x,y in comparable)
            predicted = proposed(matrix,shift)
            assert actual == predicted, (matrix,shift,actual,predicted)
            checked += 1
    # A natural join-monoid substitution that is injective algebraically
    # but not continuous in its group completion.
    mix = ((1,0),(1,1))
    assert not proposed(mix,(0,0))
    assert leq((0,-1),(1,-1))
    assert not leq(affine(mix,(0,0),(0,-1)),affine(mix,(0,0),(1,-1)))
    print(f'PASS {checked} affine 2x2 integer models; {len(comparable)} comparable domain pairs each')
    print('PASS explicit injective monoid-map discontinuity witness')
if __name__ == '__main__':
    check()
