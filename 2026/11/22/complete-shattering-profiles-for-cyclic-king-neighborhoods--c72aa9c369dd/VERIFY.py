"""Exact finite certificate for three-by-three translated cyclic windows.

Standard-library Python 3. The accompanying theorem explains why these
finite orbit and trace tests suffice for all side lengths at least three.
"""
from collections import Counter
from itertools import combinations


def windows(m, n):
    return tuple(frozenset(((x + a) % m) * n + ((y + b) % n)
               for a in (-1, 0, 1) for b in (-1, 0, 1))
                 for x in range(m) for y in range(n))


def trace_masks(support, boxes):
    return frozenset(sum((1 << j) for j, p in enumerate(support) if p in box)
                     for box in boxes)


def shattered(support, boxes):
    return len(trace_masks(support, boxes)) == (1 << len(support))


def anchor_profiles(m, n):
    boxes = windows(m, n)
    pts = tuple(x*n + y for x in range(3) for y in range(3))
    out = {}
    for mask in range(512):
        s = tuple(pts[j] for j in range(9) if mask & (1 << j))
        out[mask] = trace_masks(s, boxes)
    return out


def profile_shattered(mask, trace_set):
    return len(trace_set) == (1 << mask.bit_count())


def orbit_of(s, m, n):
    pts = tuple(divmod(x, n) for x in s)
    return frozenset(tuple(sorted(((x + a) % m)*n+(y+b) % n
                      for x, y in pts))
                     for a in range(m) for b in range(n))


def enumerate_shattered(m, n):
    boxes = windows(m, n)
    candidates = {()}
    for b in boxes:
        bb = sorted(b)
        for k in range(1, len(bb) + 1):
            candidates.update(combinations(bb, k))
    accepted = {s for s in candidates if shattered(s, boxes)}
    counts = Counter(map(len, accepted))
    # Completeness: any shattered nonempty S has the all-one trace,
    # hence is contained in one box and is among the candidates.
    orb = Counter()
    seen = set()
    for s in sorted(accepted, key=lambda x: (len(x), x)):
        if not s or s in seen:
            continue
        o = orbit_of(s, m, n)
        assert o <= accepted
        orb[len(s), len(o)] += 1
        seen.update(o)
    assert seen == accepted - {()}
    triples = {s for s in accepted if len(s) == 3}
    pair_covered = {p for t in triples for p in combinations(t, 2)}
    maximal_pairs = {s for s in accepted if len(s) == 2} - pair_covered
    return counts, orb, accepted, maximal_pairs


def d4_and_translate(m, n, template):
    # Eight reflected and rotated local motifs, embedded in a cyclic window.
    pts = [tuple(p) for p in template]
    out = set()
    for reflection in (False, True):
        for quarterturns in range(4):
            q = [(-x if reflection else x, y) for x, y in pts]
            for _ in range(quarterturns):
                q = [(-y, x) for x, y in q]
            for a in range(m):
                for b in range(n):
                    out.add(tuple(sorted(((x + a) % m)*n + ((y+b) % n)
                                  for x, y in q)))
    return out


def main():
    # Complete local census, not Monte Carlo testing.
    bases = {
        (3, 3): ([1], {}),
        (3, 4): ([1, 12], {(1, 12): 1}),
        (3, 5): ([1, 15, 45], {(1, 15): 1, (2, 15): 3}),
        (3, 6): ([1, 18, 108], {(1, 18): 1, (2, 18): 6}),
        (4, 4): ([1, 16, 120, 288], {(1, 16): 1, (2, 8): 3,
                                     (2, 16): 6, (3, 16): 18}),
        (4, 5): ([1, 20, 190, 420], {(1, 20): 1, (2, 10): 1,
                                     (2, 20): 9, (3, 20): 21}),
        (5, 5): ([1, 25, 300, 300], {(1, 25): 1, (2, 25): 12,
                                     (3, 25): 12})
    }
    for (m, n), (expected, expected_orbits) in bases.items():
        counts, orbitcounts, _, _ = enumerate_shattered(m, n)
        assert [counts[k] for k in range(len(expected))] == expected
        assert not any(k >= len(expected) for k in counts)
        assert orbitcounts == expected_orbits, (m, n, orbitcounts)
        print('BASE', m, n, expected, dict(orbitcounts))

    # In one dimension a 3-window intersects another 3-window only
    # at relative center displacements -2,-1,0,1,2 (on a cycle >=5).
    # New centers outside these produce ONLY the empty trace.
    pairs = [((3,6),(3,7)), ((4,5),(4,6)), ((4,5),(4,8)),
             ((5,5),(5,6)), ((5,5),(6,5)), ((5,5),(6,6)),
             ((5,5),(7,8))]
    profiles = {p: anchor_profiles(*p) for pair in pairs for p in pair}
    for a,b in pairs:
        pa,pb = profiles[a],profiles[b]
        for mask in range(512):
            ta,tb=pa[mask],pb[mask]
            assert ta - {0} == tb - {0}, (a,b,mask,'nonzero')
            assert profile_shattered(mask,ta)==profile_shattered(mask,tb), (a,b,mask)
        print('PROFILE_STABLE', a, b, '512/512')
    # The only potential new shattering from a longer period would be
    # adding the empty trace to a support with all nonempty traces.
    for base in ((3,6),(4,5),(5,5)):
        p=profiles[base]
        critical = []
        for mask, traces in p.items():
            k=mask.bit_count()
            if k and set(range(1, 1<<k))<=traces and 0 not in traces:
                critical.append(mask)
        assert critical==[], (base,critical)
        print('EMPTY_TRACE_OBSTRUCTION_ABSENT',base,'512/512')

    # Main structural assertion: all shattered triples on >=5 x >=5
    # are precisely the dihedral translates of three local motifs.
    motifs=( ((0,0),(0,2),(1,1)),
             ((0,0),(0,2),(2,1)),
             ((0,1),(1,0),(2,2)) )
    counts, orbs, accepted, maximal_pairs=enumerate_shattered(7,7)
    expected_triples=set().union(*(d4_and_translate(7,7,t) for t in motifs))
    actual_triples={s for s in accepted if len(s)==3}
    assert len(expected_triples)==12*49 and expected_triples==actual_triples
    assert counts==Counter({0:1,1:49,2:12*49,3:12*49})
    assert len(maximal_pairs)==4*49
    assert len({tuple(sorted(s)) for s in maximal_pairs})==4*49
    print('TRIPLE_MOTIFS',len(actual_triples),'MAXIMAL_PAIRS',len(maximal_pairs))

    # Independent direct finite boards, not used for all-size induction.
    for m,n in ((3,7),(3,8),(4,6),(4,7),(5,6),(5,7),(6,6),(6,7),(7,7)):
        counts, _, _, maximal_pairs = enumerate_shattered(m,n)
        if m==3:
            expected=[1,3*n,18*n]
        elif m==4:
            expected=[1,4*n,38*n,84*n]
        else:
            expected=[1,m*n,12*m*n,12*m*n]
            assert len(maximal_pairs)==4*m*n
        assert [counts[k] for k in range(len(expected))] == expected
        assert max(counts)==len(expected)-1
        print('DIRECT',m,n,expected)
    print('ALL_CYCLIC_KING_SHATTERING_CHECKS_PASS')

if __name__=='__main__':
    main()
