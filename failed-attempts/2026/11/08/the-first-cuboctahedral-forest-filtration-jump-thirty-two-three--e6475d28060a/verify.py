#!/usr/bin/env python3
"""Reproduce the cuboctahedral two-stage forest-complex homotopy calculation.

Python 3.9+ standard library. All graph data, face predicates, finite matchings,
acyclicity tests and independent mod-two boundary ranks are recomputed here.
"""
import json
from collections import Counter, deque

CUBE_EDGES = tuple(sorted((x, x ^ (1 << bit)) for x in range(8)
                          for bit in range(3) if x < (x ^ (1 << bit))))
N = len(CUBE_EDGES)
assert N == 12
ADJ = tuple(sum((1 << j) for j, other in enumerate(CUBE_EDGES)
                if i != j and (u in other or v in other))
            for i, (u, v) in enumerate(CUBE_EDGES))
assert all(x.bit_count() == 4 for x in ADJ)
assert sum(x.bit_count() for x in ADJ) // 2 == 24

def degree_predicate(mask, level):
    return all((mask & ADJ[i]).bit_count() <= level
               for i in range(N) if mask & (1 << i))

def component_predicate(mask, bound):
    """Independent graph traversal; membership iff all components <= bound."""
    seen = 0
    for start in range(N):
        bit = 1 << start
        if not mask & bit or seen & bit:
            continue
        size = 0
        stack = [start]
        seen |= bit
        while stack:
            v = stack.pop()
            size += 1
            if size > bound:
                return False
            nbr = ADJ[v] & mask & ~seen
            while nbr:
                nxt = nbr & -nbr
                nbr -= nxt
                seen |= nxt
                stack.append(nxt.bit_length() - 1)
    return True

def faces(level):
    p = {m for m in range(1 << N) if degree_predicate(m, level)}
    q = {m for m in range(1 << N) if component_predicate(m, level + 1)}
    assert p == q
    assert 0 in p
    return p

def critical_faces(face_set, vertex_order):
    """Staged element matching on the augmented face poset."""
    remaining = set(face_set)
    partners = {}
    for i in vertex_order:
        bit = 1 << i
        for lower in range(1 << N):
            if lower & bit or lower not in remaining:
                continue
            upper = lower | bit
            if upper in remaining:
                remaining.remove(lower)
                remaining.remove(upper)
                partners[lower] = upper
                partners[upper] = lower
    assert len(partners) + len(remaining) == len(face_set)
    return partners, remaining

def checked_dag(face_set, partners):
    """Orient matched cover edges upward and all others downward."""
    out = {f: [] for f in face_set}
    indegree = {f: 0 for f in face_set}
    incidences = 0
    for upper in face_set:
        bits = upper
        while bits:
            bit = bits & -bits
            bits -= bit
            lower = upper ^ bit
            if lower not in face_set:
                assert lower == 0
                continue
            a, b = ((lower, upper) if partners.get(lower) == upper
                    else (upper, lower))
            out[a].append(b)
            indegree[b] += 1
            incidences += 1
    queue = deque(f for f in face_set if indegree[f] == 0)
    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for child in out[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    assert visited == len(face_set), (visited, len(face_set))
    return incidences

def unreduced_boundary_ranks_mod2(face_set):
    by_dim = {d: sorted(f for f in face_set if f.bit_count() == d + 1)
              for d in range(max(m.bit_count() for m in face_set))}
    # Integral oriented boundary reduces to the incidence matrix mod two.
    ranks = {0: 0}
    for d in range(1, len(by_dim)):
        idx = {f: j for j, f in enumerate(by_dim[d - 1])}
        pivots = {}
        for upper in by_dim[d]:
            bits = upper
            vec = 0
            while bits:
                bit = bits & -bits
                bits -= bit
                vec ^= 1 << idx[upper ^ bit]
            while vec:
                p = vec.bit_length() - 1
                if p not in pivots:
                    pivots[p] = vec
                    break
                vec ^= pivots[p]
        ranks[d] = len(pivots)
    betti = {d: len(by_dim[d]) - ranks[d] - ranks.get(d + 1, 0)
             for d in by_dim}
    betti[0] -= 1
    return ranks, {d: b for d, b in betti.items() if b != 0}

ORDERS = {
    0: [list(range(N)), list(range(N - 1, -1, -1))],
    1: [[5,2,9,1,8,3,10,7,0,11,4,6],
        [9,0,7,4,8,10,1,11,2,3,5,6]],
}
EXPECTED = {
    0: dict(face_count=108, facets={2:8, 3:9},
            f_vector=[12,42,44,9], critical={2:4},
            matched_pairs=52, incidences=264, betti={2:4}),
    1: dict(face_count=456, facets={3:45, 4:36},
            f_vector=[12,66,164,177,36], critical={3:32},
            matched_pairs=212, incidences=1524, betti={3:32}),
}

def relative_mod2_betti(larger, smaller):
    """Direct quotient-chain computation for a simplicial pair (larger,smaller)."""
    assert smaller <= larger
    bydim = {d: sorted(f for f in larger-smaller if f.bit_count()==d+1)
             for d in range(max(m.bit_count() for m in larger))}
    ranks = {0:0}
    for d in range(1,len(bydim)):
        indices = {f:j for j,f in enumerate(bydim[d-1])}
        pivots={}
        for upper in bydim[d]:
            col=0
            bits=upper
            while bits:
                bit=bits&-bits;bits-=bit
                low=upper^bit
                if low in indices:col ^= 1<<indices[low]
            while col:
                pivot=col.bit_length()-1
                if pivot not in pivots:
                    pivots[pivot]=col;break
                col ^= pivots[pivot]
        ranks[d]=len(pivots)
    return {d:len(bydim[d])-ranks[d]-ranks.get(d+1,0)
            for d in bydim if len(bydim[d])-ranks[d]-ranks.get(d+1,0)}

def run():
    report = dict(cube_edges=[list(e) for e in CUBE_EDGES],
                  line_graph_vertices=N, line_graph_edges=24,
                  levels={})
    for k in (0, 1):
        fs = faces(k)
        fvec = [sum(f.bit_count()==i+1 for f in fs)
                for i in range(max(m.bit_count() for m in fs))]
        facet = Counter(m.bit_count()-1 for m in fs
                        if all((m | (1 << i)) not in fs
                               for i in range(N) if not m & (1 << i)))
        target = EXPECTED[k]
        assert len(fs) == target['face_count']
        assert fvec == target['f_vector']
        assert dict(facet) == target['facets']
        matchings = []
        for order in ORDERS[k]:
            partners, crit = critical_faces(fs, order)
            incidences = checked_dag(fs, partners)
            hist = Counter(m.bit_count()-1 for m in crit)
            assert dict(hist) == target['critical']
            assert len(partners)//2 == target['matched_pairs']
            assert incidences == target['incidences']
            assert 0 in partners  # empty face paired with a zero-cell
            partner = partners[0]
            assert partner.bit_count() == 1
            # Deleting the augmented empty-face pair leaves one critical
            # zero-cell and the same high-dimensional critical cells.
            ordinary_fs = fs - {0}
            ordinary_partners = {a:b for a,b in partners.items()
                                 if a not in (0,partner) and b not in (0,partner)}
            assert checked_dag(ordinary_fs, ordinary_partners) < incidences
            actual = Counter(m.bit_count()-1 for m in crit)
            actual[0] += 1
            assert actual[0] == 1
            matchings.append({'order':order, 'matched_pairs_augmented':len(partners)//2,
                              'critical_augmented':dict(sorted(hist.items())),
                              'critical_ordinary':dict(sorted(actual.items())),
                              'Hasse_incidences_augmented':incidences,
                              'critical_masks_augmented':sorted(crit)})
        ranks, betti = unreduced_boundary_ranks_mod2(fs)
        assert betti == target['betti'], (k,betti)
        report['levels'][str(k)] = {
            'face_count_including_empty':len(fs),
            'f_vector':fvec,
            'facet_dimension_counts':dict(sorted(facet.items())),
            'direct_mod2_boundary_ranks':ranks,
            'direct_reduced_mod2_betti':betti,
            'matchings':matchings,
        }
    report['relative_reduced_mod2_betti'] = relative_mod2_betti(faces(1),faces(0))
    assert report['relative_reduced_mod2_betti'] == {3:36}
    report['conclusion'] = ('F_0(L(Q_3)) is a wedge of four 2-spheres; '
                            'F_1(L(Q_3)) is a wedge of 32 3-spheres; '
                            'the cofibre F_1/F_0 is a wedge of 36 3-spheres.')
    print(json.dumps(report, sort_keys=True, indent=2))
    print('CUBOCTAHEDRAL_FOREST_FILTRATION_JUMP_VERIFIED')

if __name__ == '__main__':
    run()
