"""Exact, standard-library verification of small ordinary-semigroup decomposition lengths.
Run: python3 verify.py.  No external data or packages are required.
"""
from functools import lru_cache

@lru_cache(None)
def irreducible_gaps(F):
    """All gap masks for irreducible numerical semigroups of Frobenius F.

    Bit n corresponds to positive integer n.  The reflection criterion
    generates every symmetric/pseudosymmetric candidate; sums test closure.
    """
    assert F >= 1
    pairs = [(i, F-i) for i in range(1, (F+1)//2)]
    output = set()
    for choice in range(1 << len(pairs)):
        included = set()
        for j, (a, b) in enumerate(pairs):
            included.add(a if (choice >> j) & 1 else b)
        if any(a+b <= F and a+b not in included
               for a in included for b in included):
            continue
        gaps = ((1 << (F+1))-2) ^ sum(1 << v for v in included)
        output.add(gaps)
    return tuple(sorted(output))

def masks_for_m(m):
    special = tuple(range((m+1)//2, m))
    masks = set()
    for F in special:
        for gaps in irreducible_gaps(F):
            mask = sum(1 << j for j, v in enumerate(special)
                       if (gaps >> v) & 1)
            if mask:
                masks.add(mask)
    return special, tuple(sorted(masks))

def exact_minimum(m):
    special, masks = masks_for_m(m)
    target = (1 << len(special))-1
    # Attainable unions of gap masks using exactly j components.
    reachable = {0}
    for j in range(1, m+1):
        reachable = {u | v for u in reachable for v in masks}
        if target in reachable:
            return j
    raise AssertionError('A cover must exist')

def reachable(gens, limit):
    s = [False]*(limit+1)
    s[0] = True
    for n in range(1, limit+1):
        s[n] = any(n >= a and s[n-a] for a in gens)
    return s

def test_witness():
    generators = [
        (13,14,15,16,17,18,19,20,21,22,23,25),
        (2,27),
        (4,15,17),
        (7,11,15,17,19,23),
    ]
    expected_F = (24,25,26,27)
    rows = [reachable(g, 100) for g in generators]
    for g, F, s in zip(generators, expected_F, rows):
        assert not s[F]
        # A positive interval of length min(g) past F proves conductor F+1.
        assert all(s[n] for n in range(F+1, F+min(g)+1))
        genus = sum(not s[n] for n in range(1,F+1))
        assert genus == (F+1)//2 if F%2 else genus == F//2+1
    assert all(all(s[n] for s in rows) == (n == 0 or n >= 28)
               for n in range(101))
    special = range(14,28)
    masks = [{n for n in special if not s[n]} for s in rows]
    assert set.union(*masks) == set(special)
    assert all(any(n not in set.union(*(masks[:i]+masks[i+1:]))
                   for n in masks[i]) for i in range(4))
    return masks

def independent_small_F_test():
    # This separate exhaustive membership-bit enumeration does not rely on
    # pair-assignment completeness and checks the critical classification.
    for F in range(1,14):
        observed = set()
        for bits in range(1 << (F-1)):
            included = {n for n in range(1,F) if (bits >> (n-1)) & 1}
            if any(a+b <= F and a+b not in included
                   for a in included for b in included):
                continue
            genus = F - len(included)
            if genus != ((F+1)//2 if F%2 else F//2+1):
                continue
            observed.add(((1 << (F+1))-2) ^ sum(1 << n for n in included))
        assert observed == set(irreducible_gaps(F)), (F, len(observed))

def audit_noncoverage(m, k, expected_mask_count, expected_max_union):
    special, masks = masks_for_m(m)
    assert len(masks) == expected_mask_count, (m, len(masks))
    reachable = {0}
    for _ in range(k):
        reachable = {a|b for a in reachable for b in masks}
    maximum = max(x.bit_count() for x in reachable)
    assert maximum == expected_max_union, (m, maximum)
    assert ((1 << len(special))-1) not in reachable
    return len(reachable), maximum, len(special)

if __name__ == '__main__':
    independent_small_F_test()
    expected = {
        **{m:1 for m in range(2,4)},
        **{m:2 for m in range(4,7)},
        **{m:3 for m in range(7,13)},
        **{m:4 for m in range(13,25)},
        **{m:5 for m in range(25,28)},
        28:4, 29:5, 30:4, 31:4, 32:4,
    }
    for m in range(2,33):
        actual = exact_minimum(m)
        assert actual == expected[m], (m,actual,expected[m])
    coverage27 = audit_noncoverage(27,4,118,12)
    coverage28 = audit_noncoverage(28,3,163,13)
    witness = test_witness()
    print('VERIFY_OK')
    print('LAMBDA_2_TO_32',','.join(str(expected[m]) for m in range(2,33)))
    print('H27_FOUR_FACTOR_MAX',coverage27)
    print('H28_THREE_FACTOR_MAX',coverage28)
    print('H28_WITNESS_GAP_COVERS',*[sorted(t) for t in witness],sep='\n')

# The following independent searches certify the *new* four-component census.
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb

def shortest_decompositions_H28():
    """Enumerate every unordered four-element irreducible decomposition."""
    special = tuple(range(14,28))
    full = (1 << len(special))-1
    by_mask = defaultdict(list)
    for F in range(14,28):
        for gaps in irreducible_gaps(F):
            mask = sum(1 << j for j, a in enumerate(special)
                       if gaps >> a & 1)
            if mask:
                by_mask[mask].append((F, gaps))
    assert sum(map(len, by_mask.values())) == 285
    assert len(by_mask) == 163

    # Method A: pair-joining explicit enumeration; increasing mask indices
    # count unordered sets only once.  Product expands genuinely distinct
    # irreducible semigroups sharing a special-gap mask.
    masks = sorted(by_mask)
    pair_unions = defaultdict(list)
    for i,j in combinations(range(len(masks)),2):
        pair_unions[masks[i] | masks[j]].append((i,j))
    signatures = Counter()
    all_four = []
    for u, pairs_left in pair_unions.items():
        need = full ^ u
        v = need
        while True:
            for k,l in pair_unions.get(v, ()):
                for i,j in pairs_left:
                    if j < k:
                        for selections in product(by_mask[masks[i]],
                                                  by_mask[masks[j]],
                                                  by_mask[masks[k]],
                                                  by_mask[masks[l]]):
                            assert len(set(selections)) == 4
                            signatures[tuple(sorted(F for F,_ in selections))] += 1
                            all_four.append(selections)
            if v == full:
                break
            v = (v+1) | need
    assert len(all_four) == 56
    assert signatures == {
        (24,25,26,27):28,
        (24,26,27,27):28,
    }, signatures

    # Method B: a different algorithm: subset zeta transform followed by
    # inclusion-exclusion on the special-gap universe.  Choose(C(U),4)
    # counts *unordered* selections of four distinct irreducibles whose
    # missing-gap masks lie inside U.  Moebius inversion keeps precisely
    # selections whose masks together cover the entire universe.
    count_by_mask = Counter({mask:len(rows) for mask,rows in by_mask.items()})
    inside = [count_by_mask[u] for u in range(1<<len(special))]
    for j in range(len(special)):
        for u in range(1<<len(special)):
            if u >> j & 1:
                inside[u] += inside[u^(1<<j)]
    total = sum((-1)**(len(special)-u.bit_count()) *
                comb(inside[u],4) for u in range(1<<len(special))
                if inside[u]>=4)
    assert total == 56, total

    # Explicit parameter classification of all 56: seven A masks with
    # exactly two F=24 realizations, one F=26 C, a two-choice F=27 D,
    # and a two-choice B (F=25 or F=27).
    A = [(24,), (15,24), (17,24), (15,17,24), (14,24),
         (14,15,24), (14,19,24)]
    B = [(25,(15,17,19,21,23,25)),
         (27,(15,17,19,21,23,25,27))]
    C = (26,(14,18,22,26))
    D = [(27,(16,20,27)),(27,(15,16,20,27))]
    def number(F, missing):
        mask = sum(1<<(v-14) for v in missing)
        return sum(int(ff==F) for ff,_ in by_mask[mask])
    assert all(number(24,x)==2 for x in A)
    assert all(number(*x)==1 for x in B)
    assert number(*C)==1
    assert all(number(*x)==1 for x in D)
    assert 7*2*2*2 == len(all_four)
    for a in A:
        for b in B:
            for d in D:
                assert set(a)|set(b[1])|set(C[1])|set(d[1]) == set(special)
    print('CLASSIFICATION_OK',len(all_four))
    print('FROBENIUS_SIGNATURES',dict(sorted(signatures.items())))
    print('INCLUSION_EXCLUSION_OK',total)

if __name__ == '__main__':
    shortest_decompositions_H28()
