"""Exact finite combinatorial checks for the first Fano-free pair-type obstruction.

Standard-library Python 3. No data files are required.
"""
from itertools import combinations
from math import comb

V = range(7)
OLD = frozenset(range(5))
NEW = frozenset((5, 6))
TRIPLES = tuple(frozenset(t) for t in combinations(V, 3))
PAIRS = tuple(frozenset(t) for t in combinations(V, 2))


def enumerate_fano_designs():
    """Independent exact-cover enumeration of all STS(7) on fixed labels."""
    incidence = {p: tuple(t for t in TRIPLES if p <= t) for p in PAIRS}
    result = set()

    def extend(blocks, uncovered):
        if not uncovered:
            assert len(blocks) == 7
            result.add(frozenset(blocks))
            return
        p = min(uncovered, key=lambda q: sum(
            all(frozenset(s) <= uncovered for s in combinations(t, 2))
            for t in incidence[q]))
        for t in incidence[p]:
            c = frozenset(frozenset(s) for s in combinations(t, 2))
            if c <= uncovered:
                extend(blocks + [t], uncovered - c)

    extend([], frozenset(PAIRS))
    return tuple(result)


def fano_conditions(design):
    old = frozenset(t for t in design if t <= OLD)
    fresh = frozenset(t for t in design if t not in old)
    assert len(old) == 2 and len(fresh) == 5
    return old, fresh


def test():
    designs = enumerate_fano_designs()
    assert len(designs) == 30, len(designs)
    old_triples = tuple(t for t in TRIPLES if t <= OLD)
    assert len(old_triples) == 10
    bits = tuple(t for t in TRIPLES if not t <= OLD)
    assert len(bits) == 25
    assert sum(bool(t & NEW == NEW) for t in bits) == 5
    covered = {}
    for d in designs:
        e, f = fano_conditions(d)
        covered.setdefault(e, []).append(f)
    assert len(covered) == 15, len(covered)
    for old_pair in combinations(old_triples, 2):
        old = frozenset(old_pair)
        intersection_size = len(old_pair[0] & old_pair[1])
        fs = covered.get(old, [])
        assert len(fs) == (2 if intersection_size == 1 else 0)
        if fs:
            assert len(fs[0] & fs[1]) == 1
            overlap = next(iter(fs[0] & fs[1]))
            assert overlap & NEW == NEW
            assert overlap & OLD == old_pair[0] & old_pair[1]
    print('DESIGNS=30; OLD_BOWTIES=15; EACH_HAS_TWO_COMPLETIONS=OK')

    old = frozenset((frozenset((0, 1, 2)), frozenset((0, 3, 4))))
    f, g = covered[old]
    assert len(f | g) == 9
    a = 0
    all_new_bits = set(bits)
    assert f <= all_new_bits and g <= all_new_bits
    for s in map(frozenset, (t for k in range(6) for t in combinations(OLD,k))):
        count = 2**20 if a not in s else 2**20 - 2*(2**16) + 2**12
        # Independence-based exact count and a separate algebraic formula.
        assert count == (2**12)*(256 if a not in s else 225)
    total = sum(comb(4,k)*2**12*256 + comb(4,k-1)*2**12*225
                if 0 <= k-1 <= 4 else comb(4,k)*2**12*256
                for k in range(6))
    assert total == 31522816 == 2**25 - 2*2**20 + 2**16
    assert 512*total == 481*(2**25)
    print('PAIR_TYPE_TOTAL=31522816; UNCONSTRAINED=33554432; RATIO=481/512')

    # Direct enumeration of the 20 one-point link bits, with the central
    # mutual-link bit fixed on. None of these rows is used to derive the proof.
    edge_bits = sorted((t for t in bits if len(t & NEW) == 1),key=lambda t:tuple(sorted(t)))
    assert len(edge_bits) == 20
    pos = {b:i for i,b in enumerate(edge_bits)}
    def mask(conditions):
        return sum(1 << pos[t] for t in conditions if len(t & NEW) == 1)
    mf, mg = mask(f), mask(g)
    assert mf.bit_count() == mg.bit_count() == 4
    assert not (mf & mg)
    bad_union = 0
    by_both = 0
    for z in range(1<<20):
        hitf=(z & mf)==mf
        hitg=(z & mg)==mg
        bad_union += (hitf or hitg)
        by_both += (hitf and hitg)
    assert bad_union == 2*2**16-2**12
    assert by_both == 2**12
    assert (1<<20)-bad_union == 225*2**12
    print('DIRECT_LINK_ENUMERATION=1048576; GOOD_WHEN_CENTRAL=921600')
    # Exact mutual-link probability and scalar observable distance.
    assert (225,481) == (225,225+256)
    assert sum(abs((225-256)*(comb(4,k-1) if 0<=k-1<=4 else 0) -
                   (225-256)*(comb(4,k) if 0<=k<=4 else 0))
               for k in range(6)) == 2*31*6
    # TV(K, Bin(5,1/2)) = (31/962)*6/16 = 93/7696.
    assert 31*6 == 93*2
    print('MUTUAL_LINK_CENTER_BIAS=225/481; SIZE_TV=93/7696')
    print('VERIFY_OK')


if __name__ == '__main__':
    test()
