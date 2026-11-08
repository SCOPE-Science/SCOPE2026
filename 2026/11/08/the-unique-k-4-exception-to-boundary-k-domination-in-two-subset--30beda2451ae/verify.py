"""Reproduce the boundary k-domination census for two-subset Kneser graphs.

Only standard-library Python is needed.  The finite census checks k=2,3;
the general mathematical theorem requires the accompanying proof.
"""
from itertools import combinations
from math import comb, factorial


def edge_list(n):
    return list(combinations(range(n), 2))


def expected(k):
    n = 2*k + 3
    a = comb(n, 3)*factorial(2*k)//(2**k*factorial(k))
    return a, a + (comb(9, 4) if k == 3 else 0)


def classify_family(D, n, k):
    ds = [0]*n
    for a,b in D:
        ds[a] += 1
        ds[b] += 1
    if sorted(ds) == [1]*(2*k) + [2]*3:
        high = {i for i,x in enumerate(ds) if x == 2}
        if all(tuple(sorted(p)) in D for p in combinations(high,2)):
            return 'triangle_and_matching'
    if k == 3 and sorted(ds) == [0]*5 + [3]*4:
        high = {i for i,x in enumerate(ds) if x == 3}
        if all(tuple(sorted(p)) in D for p in combinations(high,2)):
            return 'K4'
    return 'other'


def literal(D, E, k, variant):
    S = set(D)
    for e in E:
        disjoint = sum(e[0] not in f and e[1] not in f for f in S)
        if variant == 'open_outside' and e not in S and disjoint < k:
            return False
        if variant == 'closed_all' and disjoint + (e in S) < k:
            return False
        if variant == 'open_all' and disjoint < k:
            return False
    return True


def test(k):
    n = 2*k+3
    E = edge_list(n)
    expected_tuple, expected_ordinary = expected(k)
    counts = {'triangle_and_matching': 0, 'K4':0, 'other':0}
    variants = {'open_outside':0,'closed_all':0,'open_all':0}
    smaller = 0
    for family in combinations(E, k+2):
        if literal(family, E, k, 'open_outside'):
            smaller += 1
    assert smaller == 0, (k, smaller)
    for family in combinations(E, k+3):
        # Independent literal definition; no degree-sum shortcut in this enumeration.
        if literal(family, E, k, 'open_outside'):
            typ = classify_family(family, n, k)
            counts[typ] += 1
            assert typ != 'other', (k, family)
            for mode in variants:
                if literal(family,E,k,mode):
                    variants[mode] += 1
    assert counts['triangle_and_matching'] == expected_tuple, (k, counts, expected_tuple)
    assert counts['K4'] == (comb(9,4) if k==3 else 0)
    assert variants['open_outside'] == expected_ordinary
    assert variants['closed_all'] == expected_tuple
    assert variants['open_all'] == expected_tuple
    print('EXHAUSTIVE_OK', 'k',k, 'n',n, 'candidate_k_plus_2',comb(len(E),k+2),
          'candidate_k_plus_3',comb(len(E),k+3),
          'types',counts,'variant_counts',variants)


def constructive_checks():
    for k in range(2,15):
        n=2*k+3
        tri=[(0,1),(0,2),(1,2)]
        D=tri+[(3+2*i,4+2*i) for i in range(k)]
        assert literal(D,edge_list(n),k,'open_all')
        assert literal(D,edge_list(n),k,'closed_all')
        assert literal(D,edge_list(n),k,'open_outside')
        if k==3:
            H=list(combinations(range(4),2))
            assert literal(H,edge_list(n),k,'open_outside')
            assert not literal(H,edge_list(n),k,'closed_all')
            assert not literal(H,edge_list(n),k,'open_all')
    print('CONSTRUCTIONS_OK','k=2..14','exception_K4_verified=PASS')

if __name__ == '__main__':
    test(2)
    test(3)
    constructive_checks()
    print('VERIFY_OK exhaustive_k=2,3 minimum_classification=PASS all_three_variants=PASS exceptional_K4=PASS')
