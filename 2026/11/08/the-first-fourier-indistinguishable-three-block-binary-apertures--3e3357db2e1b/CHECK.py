#!/usr/bin/env python3
"""Exact exhaustive verification of the first three-run aperiodic phase collision.

No third-party packages required. Every positive five-part composition is generated.
The two correlation implementations use independent integer algorithms.
"""
from collections import defaultdict
from itertools import combinations
from math import comb

EXPECTED = {5:(1,1),6:(3,3),7:(9,9),8:(19,19),
            9:(38,38),10:(66,66),11:(110,110),12:(170,169)}
EXCEPTIONAL = frozenset(('101111110011','100111011111'))

def correlation_by_pairs(w):
    ones = [i for i,v in enumerate(w) if v == '1']
    return tuple(sum((i+d) in ones for i in ones) for d in range(len(w)))

def correlation_by_bits(w):
    mask = sum((1 << i) for i,v in enumerate(w) if v == '1')
    return tuple((mask & (mask >> d)).bit_count() for d in range(len(w)))

def all_three_run(n):
    for a,b,c,d in combinations(range(1,n),4):
        yield '1'*a+'0'*(b-a)+'1'*(c-b)+'0'*(d-c)+'1'*(n-d)

def verify():
    total = 0
    for n,(orbit_count,signature_count) in EXPECTED.items():
        groups = defaultdict(set)
        seen_words = set()
        for w in all_three_run(n):
            assert len(w) == n and w.count('1') >= 3
            assert w[0] == '1' and w[-1] == '1'
            assert sum(w[i] != w[i-1] for i in range(1,n)) == 4
            assert w not in seen_words
            seen_words.add(w)
            c1 = correlation_by_pairs(w)
            c2 = correlation_by_bits(w)
            assert c1 == c2
            assert c1[0] == w.count('1') and c1[-1] == 1
            canonical = min(w,w[::-1])
            groups[c1].add(canonical)
            total += 1
        assert len(seen_words) == comb(n-1,4)
        classes = set().union(*groups.values())
        assert len(classes) == orbit_count
        assert len(groups) == signature_count
        ambiguous = [set(v) for v in groups.values() if len(v)>1]
        if n < 12:
            assert not ambiguous
        else:
            assert len(ambiguous)==1 and ambiguous[0] == EXCEPTIONAL
        print('span',n,'words',len(seen_words),'reflection_classes',
              len(classes),'spectra',len(groups),'ambiguous_fibers',len(ambiguous))
    assert total == sum(comb(n-1,4) for n in range(5,13)) == 792
    a,b=sorted(EXCEPTIONAL)
    assert a != b and a != b[::-1]
    assert correlation_by_bits(a) == correlation_by_bits(b)
    print('CHECK_OK exact_three_run_words=792 first_span=12 exceptional_unoriented_pair=1')

if __name__ == '__main__':
    verify()
