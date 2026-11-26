"""Standalone exact certificate for the first strict integer Davenport gap.

Run: python3 verify.py.  No packages or input files are required.
"""
from itertools import combinations_with_replacement, product
from math import gcd


def pair_bound(support):
    return max((b-a)//gcd(-a,b) for a in support for b in support if a < 0 < b)


def is_minimal_zero_sum(seq):
    if len(seq) < 2 or sum(seq) != 0:
        return False
    # A proper nonempty zero-sum subsequence exists iff one exists
    # among the first len(seq)-1 entries, by taking complements.
    sums = {0}
    for x in seq[:-1]:
        added = {s + x for s in sums}
        if 0 in added:
            return False
        sums |= added
    return True


def strict_witnesses(max_diameter):
    witnesses = []
    inspected_zero_sums = 0
    for length in range(2, max_diameter+1):
        for seq in combinations_with_replacement(range(1-max_diameter,max_diameter), length):
            if seq[0] >= 0 or seq[-1] <= 0 or seq[-1] - seq[0] > max_diameter or 0 in seq:
                continue
            if sum(seq):
                continue
            inspected_zero_sums += 1
            if length <= pair_bound(set(seq)):
                continue
            if is_minimal_zero_sum(seq):
                witnesses.append(seq)
    return witnesses, inspected_zero_sums


expected = {(-6,-1,2,2,3), (-3,-2,-2,1,6)}
for diameter in range(2,10):
    witnesses, checked = strict_witnesses(diameter)
    if diameter < 9:
        assert not witnesses, (diameter,witnesses)
    else:
        assert set(witnesses) == expected, witnesses
    print('diameter', diameter, 'zero-sum candidates', checked,
          'strict witnesses', len(witnesses))

support = (-6,-1,2,3)
assert pair_bound(support) == 4
# Classify all irreducible zero-sum multiplicity vectors on this support.
minimal = []
for counts in product(range(10), repeat=4):
    if sum(counts) == 0 or sum(counts)>9:
        continue
    seq = tuple(x for x, multiplicity in zip(support,counts) for _ in range(multiplicity))
    if is_minimal_zero_sum(seq):
        minimal.append((sum(counts),counts))
assert set(minimal) == {
    (3,(0,2,1,0)), (3,(1,0,0,2)), (4,(0,3,0,1)),
    (4,(1,0,3,0)), (5,(1,1,2,1))
}, minimal
# No other nonzero member of the containing diameter-nine interval can
# be adjoined while retaining the pairwise lower bound equal to four.
for x in range(-6,4):
    if x == 0 or x in support:
        continue
    assert pair_bound(set(support)|{x}) > 4, x
print('ALL CHECKS PASSED; five minimal sequence types; unique support up to reflection and zero')
