#!/usr/bin/env python3
"""Exact finite evidence for the labelled random circle-graph MTP2 threshold.

Two genuinely different exhaustive generators agree: (a) multiset endpoint
words; (b) perfect matchings with each pair assigned a chord label.
Only finite enumerations are checked; the all-size theorem is analytic.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def edge_list(n):
    return list(combinations(range(n), 2))


def crossing_signature(chords, n):
    """chords[label] is a pair of endpoints in cyclic order."""
    edges = edge_list(n)
    bits = 0
    for idx, (a, b) in enumerate(edges):
        x, y = sorted(chords[a])
        u, v = sorted(chords[b])
        if (x < u < y) != (x < v < y):
            bits |= 1 << idx
    return bits


def word_law(n):
    """Uniform random multiset endpoint word with first letter 0.

    For each event invariant under circular rotations, this conditional
    sample space has exactly the same law as the unrestricted sample space.
    """
    c = Counter()
    capacities = [1] + [2] * (n - 1)
    prefix = [0]
    def rec():
        if len(prefix) == 2 * n:
            ends = [[] for _ in range(n)]
            for pos, label in enumerate(prefix):
                ends[label].append(pos)
            c[crossing_signature(ends, n)] += 1
            return
        for label in range(n):
            if capacities[label] > 0:
                capacities[label] -= 1
                prefix.append(label)
                rec()
                prefix.pop()
                capacities[label] += 1
    rec()
    assert sum(c.values()) == factorial(2*n - 1) // (2**(n-1))
    return c


def matching_law(n):
    """Uniform perfect matching on [2n], then uniform labels on pairs."""
    c = Counter()
    def match(rest, pairs):
        if not rest:
            for order in permutations(pairs):
                c[crossing_signature(order, n)] += 1
            return
        first, *tail = rest
        for j, other in enumerate(tail):
            match(tail[:j] + tail[j+1:], pairs+[(first,other)])
    match(list(range(2*n)), [])
    assert sum(c.values()) == factorial(2*n) // (2**n)
    return c


def normalize(c):
    return {key: Fraction(value, sum(c.values())) for key, value in c.items()}


def fkg_check(p, n):
    m = 1 << len(edge_list(n))
    return [ (x,y) for x in range(m) for y in range(m)
             if p.get(x|y,0)*p.get(x&y,0) < p.get(x,0)*p.get(y,0)]


def cov(p, m1, m2):
    first = sum(w for g,w in p.items() if g&m1 == m1)
    second = sum(w for g,w in p.items() if g&m2 == m2)
    both = sum(w for g,w in p.items() if g&m1==m1 and g&m2==m2)
    return both - first*second


def main():
    laws = {}
    checks = 0
    for n in (1, 2, 3, 4, 5):
        a,b=word_law(n),matching_law(n)
        pa,pb=normalize(a),normalize(b)
        assert pa == pb, (n,pa,pb)
        laws[n]=pa
        checks+=len(pa)
        print(f'n={n}: {len(pa)} labelled graph patterns; exact independent enumeration agreed')
    p3=laws[3]
    assert p3[0]==Fraction(1,3)
    assert all(p3[1<<i]==Fraction(2,15) for i in range(3))
    assert all(p3[7^(1<<i)]==Fraction(1,15) for i in range(3))
    assert p3[7]==Fraction(1,15)
    assert fkg_check(p3,3)==[]
    assert fkg_check(laws[2],2)==[]
    assert fkg_check(laws[1],1)==[]
    checks+= (8*8 + 2*2 + 1)
    p4=laws[4]
    # Ordered edge bits: 01,02,03,12,13,23.
    assert p4[0]==Fraction(2,15)
    assert p4[1]==p4[32]==Fraction(2,45)
    assert p4[33]==Fraction(4,315)
    lhs=p4[0]*p4[33]
    rhs=p4[1]*p4[32]
    assert lhs < rhs and lhs/rhs==Fraction(6,7)
    assert cov(p4,1,32)==0
    assert cov(p3,1,2)==Fraction(1,45)
    checks+=6
    # Projectively consistent induced graphs: restrict the first four labels.
    restrict={edge:i for i,edge in enumerate(edge_list(5))}
    map4=[restrict[e] for e in edge_list(4)]
    p5project=Counter()
    for state,prob in laws[5].items():
        bit=sum(((state>>j)&1)<<i for i,j in enumerate(map4))
        p5project[bit]+=prob
    assert dict(p5project)==p4
    checks+=len(p4)
    print(f'3-chord FKG all pairs: PASS. 4-chord strict defect lhs={lhs}, rhs={rhs}, ratio={lhs/rhs}.')
    print('Shared-edge indicator covariance = 1/45; disjoint-edge covariance = 0.')
    print(f'5-to-4 chord consistency: PASS. Assertions/exact pattern checks >= {checks}.')


if __name__ == '__main__':
    main()
