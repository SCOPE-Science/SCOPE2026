#!/usr/bin/env python3
"""Exact, dependency-free certificate for a ternary single-deletion list-two code."""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product

ALPHABET = '012'
WORDS4 = tuple(map(''.join, product(ALPHABET, repeat=4)))
WORDS3 = tuple(map(''.join, product(ALPHABET, repeat=3)))
CODE = '''0000 0011 0022 0120 0121 0210 1001 1022 1100 1110 1111
1122 1201 2000 2002 2102 2112 2201 2211 2220 2222'''.split()

def deletion_shadow(word):
    return frozenset(word[:i] + word[i + 1:] for i in range(len(word)))

def output_weight(y):
    if y[0] == y[1] == y[2]:
        return Fraction(5, 8)
    if y[0] == y[1] or y[1] == y[2]:
        return Fraction(3, 8)
    return Fraction(1, 4)

def input_slack(w):
    if len(set(w)) == 1:
        return Fraction(3, 8)
    if w[0] == w[1] and w[2] == w[3] and w[0] != w[2]:
        return Fraction(1, 4)
    return Fraction(0)

assert len(WORDS4) == 81 and len(WORDS3) == 27
assert len(CODE) == len(set(CODE)) == 21
assert all(w in WORDS4 for w in CODE)

# All 81 four-letter words satisfy the dual inequality.
sums = {
    w: sum((output_weight(y) for y in deletion_shadow(w)), Fraction(0))
       + input_slack(w)
    for w in WORDS4
}
assert all(v >= 1 for v in sums.values())
assert Counter(sums.values()) == {Fraction(1): 51, Fraction(9, 8): 12,
                                 Fraction(5, 4): 18}
assert sum(map(output_weight, WORDS3), Fraction(0)) == Fraction(75, 8)
assert sum(map(input_slack, WORDS4), Fraction(0)) == Fraction(21, 8)
upper = 2 * sum(map(output_weight, WORDS3), Fraction(0)) + sum(
    map(input_slack, WORDS4), Fraction(0))
assert upper == Fraction(171, 8) and upper < 22

# A full ten-orbit check independently verifies the finite reduction.
remaining = set(WORDS4)
orbits = []
while remaining:
    representative = min(remaining)
    orbit = set()
    for p in permutations(ALPHABET):
        sigma = dict(zip(ALPHABET, p))
        image = ''.join(sigma[c] for c in representative)
        orbit.add(image)
        orbit.add(image[::-1])
    assert orbit <= remaining
    assert {sums[w] for w in orbit} == {sums[representative]}
    remaining.difference_update(orbit)
    orbits.append((representative, len(orbit), sums[representative]))
assert len(orbits) == 10 and sum(m for _, m, _ in orbits) == 81

# Every received three-letter word has exactly two possible transmitted words.
loads = Counter(y for w in CODE for y in deletion_shadow(w))
assert len(loads) == 27 and all(loads[y] == 2 for y in WORDS3)
assert sum(loads.values()) == 54

# The length-four code is not the union of two uniquely decodable codes.
a, b, c = '0120', '0121', '0210'
assert all(w in CODE for w in (a, b, c))
assert deletion_shadow(a) & deletion_shadow(b)
assert deletion_shadow(b) & deletion_shadow(c)
assert deletion_shadow(c) & deletion_shadow(a)
assert not (deletion_shadow(a) & deletion_shadow(b) & deletion_shadow(c))

print('Alphabet: 3; block length: 4; exactly one deletion; list bound: 2')
print('Input words: 81; output words: 27')
print('Dual inequality: verified for all 81 input words')
print('Dual values: 1 (51), 9/8 (12), 5/4 (18)')
print('Sum output weights: 75/8; sum input slacks: 21/8')
print('Upper bound: 171/8, hence at most 21 codewords')
print('Finite symmetry orbits (representative, size, dual value):')
for rep, size, value in orbits:
    print(' ', rep, size, value)
print('Witness: 21 distinct words; all 27 received words have load exactly 2')
print('Conflict triangle: 0120, 0121, 0210; triple intersection empty')
print('Final exact optimum: 21')
