#!/usr/bin/env python3
"""Independent coefficient-by-coefficient GF(2) enumeration, no bit-polynomial library."""
from collections import Counter
from itertools import product

def main():
    joint = Counter()
    counts = [[0] * 8 for _ in range(4)]
    condition_counts = Counter()
    for v in product((0, 1), repeat=8):
        a, b, c, d, e, f, g, h = v
        # B=[[a,b],[c,d]], C=[[e,f],[g,h]]
        t0, t1 = a ^ d, e ^ h
        d0 = (a & d) ^ (b & c)
        d1 = (a & h) ^ (d & e) ^ (b & g) ^ (c & f)
        d2 = (e & h) ^ (f & g)
        delta = (d0, d1, d2)
        unit = delta in ((1,0,0), (0,1,0), (0,0,1))
        zero = delta == (0,0,0)
        root_one = delta == (t0 ^ 1, t1, 0)
        root_u = delta == (0, t0, t1 ^ 1)
        strong = not zero and not unit and not root_one and not root_u
        ent = 2 if d2 else (1 if (t1 or d1) else 0)
        joint[ent, strong] += 1
        counts[t0 + 2*t1][d0 + 2*d1 + 4*d2] += 1
        if zero: condition_counts['det_zero'] += 1
        elif unit: condition_counts['det_unit'] += 1
        elif root_one: condition_counts['unit_root_1'] += 1
        elif root_u: condition_counts['unit_root_u'] += 1
        else: condition_counts['strong'] += 1
    assert joint == {(0,False):40,(1,False):102,(1,True):18,
                     (2,False):42,(2,True):54}, joint
    assert condition_counts == {'det_zero':64,'det_unit':84,
                                'unit_root_1':18,'unit_root_u':18,
                                'strong':72}, condition_counts
    assert counts == [
        [10,10,6,6,10,10,6,6],
        [18,2,6,6,6,6,18,2],
        [18,6,6,18,2,6,6,2],
        [18,6,18,6,6,2,6,2],
    ], counts
    print('All 256 independent coefficient tests passed.')
    print('Trace/determinant coefficient multiplicity matrix:', counts)
    print('Mutually exclusive rejection categories:', sorted(condition_counts.items()))
    print('Entropy/strong-transitivity counts:', sorted(joint.items()))

if __name__ == '__main__':
    main()
