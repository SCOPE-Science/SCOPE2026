"""Exact finite-diagram verification of marked tuple types in the circular S(3) digraph.

All coordinates are rational. For each tested arity, enough sample points are
placed inside every quotient gap to realize every possible strict-order pattern.
The algorithm counts DISTINCT relation signatures rather than the proposed formula.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial, comb

ONE = Q(1)
THIRD = Q(1, 3)

def relation(x, y):
    if x == y:
        raise ValueError('Coordinates must be distinct')
    d = (y - x) % ONE
    return 1 if d < THIRD else (-1 if d > 2 * THIRD else 0)

def diagram_signature(base, xs):
    return (tuple(relation(x, a) for x in xs for a in base),
            tuple(relation(xs[i], xs[j]) for i in range(len(xs)) for j in range(i+1,len(xs))))

def sample_points(base, arity):
    qs = sorted({a % THIRD for a in base})
    assert len(qs) == len(base)
    pts = []
    for j, l in enumerate(qs):
        u = qs[j+1] if j+1 < len(qs) else qs[0] + THIRD
        for k in range(1, arity+1):
            x = (l + (u-l) * Q(k, arity+1)) % THIRD
            pts.extend([(x + lift*THIRD) % ONE for lift in range(3)])
    assert len(set(pts)) == len(pts)
    return pts

def check(base, arity):
    pts = sample_points(base, arity)
    signatures = {diagram_signature(base, xs) for xs in permutations(pts, arity)
                  if len({x % THIRD for x in xs}) == arity}
    predicted = 3**arity * factorial(arity) * comb(len(base)+arity-1,arity)
    assert len(signatures) == predicted, (base, arity, len(signatures), predicted)
    return len(signatures)

def main():
    bases = [
        (Q(1,29),),
        (Q(1,29), Q(11,47)),
        (Q(1,29), Q(11,47), Q(5,19)),
        (Q(1,29), Q(11,47), Q(5,19), Q(7,53)),
    ]
    total = 0
    for base in bases:
        for arity in range(1, 4 if len(base)<=3 else 3):
            found = check(base,arity)
            print('base_size=%d arity=%d distinct_types=%d' %(len(base),arity,found))
            total += 1
    # A direct check with a different placement of three named points.
    for base in [(Q(2,17), Q(7,23), Q(13,53)),
                 (Q(1,31), Q(4,31), Q(7,31))]:
        found = check(base, 3)
        print('alternate_base_size=3 arity=3 distinct_types=%d' %found)
        total += 1
    print('ALL_%d_EXACT_DIAGRAM_TESTS_PASS' %total)
if __name__ == '__main__':
    main()
