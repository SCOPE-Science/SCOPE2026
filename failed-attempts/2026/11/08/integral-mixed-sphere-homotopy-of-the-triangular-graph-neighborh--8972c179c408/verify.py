#!/usr/bin/env python3
"""Exact integral discrete-Morse verification for N(L(K_7)).

Requires Python >=3.10 and no third-party packages.
Vertices of the triangular graph are lexicographically ordered pairs from range(7).
Simplices are encoded as 21-bit nonzero integers. Every face is enumerated.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N_BASE = 7
EDGES = tuple(combinations(range(N_BASE), 2))
N = len(EDGES)
assert N == 21


def compute_faces():
    faces = set()
    neighbor_masks = []
    for i, a in enumerate(EDGES):
        mask = sum(1 << j for j, b in enumerate(EDGES)
                   if i != j and not set(a).isdisjoint(b))
        assert mask.bit_count() == 10
        neighbor_masks.append(mask)
        s = mask
        while s:
            faces.add(s)
            s = (s-1) & mask
    # Independent exhaustive membership reconstruction: every face belongs
    # to some open neighborhood and every enumerated face is witnessed.
    for s in faces:
        assert any(s & ~u == 0 for u in neighbor_masks)
    for u in neighbor_masks:
        s = u
        while s:
            assert s in faces
            s = (s-1) & u
    return faces, neighbor_masks


def boundary(t):
    # Signed cellular incidence in the increasing vertex ordering.
    ans = []
    sign = 1
    b = t
    while b:
        low = b & -b
        ans.append((t ^ low, sign))
        b -= low
        sign = -sign
    return ans


def matching(faces):
    unpaired = set(faces)
    pairs = []
    for i in range(N):
        bit = 1 << i
        # Each pair is made only among as-yet-unmatched faces.
        for s in sorted(unpaired):
            if s & bit:
                continue
            t = s | bit
            if t in unpaired:
                unpaired.remove(s)
                unpaired.remove(t)
                pairs.append((s, t))
    assert len(unpaired) + 2*len(pairs) == len(faces)
    return pairs, unpaired


def acyclic_hasse(faces, pairs):
    matched = set(pairs)
    indegrees = dict.fromkeys(faces, 0)
    arcs = defaultdict(list)
    incidences = 0
    for t in faces:
        if t.bit_count() == 1:
            continue
        for s, _ in boundary(t):
            assert s in faces
            incidences += 1
            # Matched arrows point upward; all other covering arrows down.
            a, b = (s, t) if (s, t) in matched else (t, s)
            arcs[a].append(b)
            indegrees[b] += 1
    q = deque(s for s, d in indegrees.items() if d == 0)
    visited = 0
    while q:
        a = q.popleft()
        visited += 1
        for b in arcs[a]:
            indegrees[b] -= 1
            if indegrees[b] == 0:
                q.append(b)
    assert visited == len(faces), (visited, len(faces))
    return incidences


def integral_morse_boundary(pairs, critical):
    # Algebraic Morse elimination: for a lower cell s matched to upper t,
    # eliminate s using its unit signed coefficient in the boundary of t.
    # In dimension 3, upper cells paired with degree-2 lower cells project
    # to zero; critical cells project to basis units.
    lower_to_upper = {s: t for s, t in pairs}
    upper_cells = {t for s, t in pairs}
    c3 = sorted(x for x in critical if x.bit_count() == 4)
    c4 = sorted(x for x in critical if x.bit_count() == 5)
    idx = {s: i for i, s in enumerate(c3)}

    @lru_cache(maxsize=None)
    def proj(s):
        assert s.bit_count() == 4
        if s in idx:
            return ((idx[s], 1),)
        if s in upper_cells:
            return ()
        assert s in lower_to_upper
        t = lower_to_upper[s]
        assert t.bit_count() == 5
        boundary_t = boundary(t)
        pivot = dict(boundary_t)[s]
        accum = defaultdict(int)
        for u, coeff in boundary_t:
            if u == s:
                continue
            for j, val in proj(u):
                accum[j] -= pivot * coeff * val
        return tuple(sorted((j, v) for j, v in accum.items() if v))

    entries_per_column = []
    for t in c4:
        accum = defaultdict(int)
        for s, coeff in boundary(t):
            for j, val in proj(s):
                accum[j] += coeff * val
        entries_per_column.append({j: v for j, v in accum.items() if v})
    assert len(entries_per_column) == 7
    assert all(not col for col in entries_per_column), entries_per_column
    return len(c3), len(c4), proj.cache_info().currsize


def boundary_ranks_f2(faces):
    by_size = defaultdict(list)
    for s in faces:
        by_size[s.bit_count()].append(s)
    ranks = []
    for k in range(2, 11):
        rows = sorted(by_size[k - 1])
        cols = sorted(by_size[k])
        rid = {s: i for i, s in enumerate(rows)}
        pivots = {}
        for t in cols:
            v = 0
            for s, _ in boundary(t):
                v ^= 1 << rid[s]
            while v:
                j = v.bit_length() - 1
                if j in pivots:
                    v ^= pivots[j]
                else:
                    pivots[j] = v
                    break
        ranks.append(len(pivots))
    return ranks


def main():
    faces, neighborhoods = compute_faces()
    fv = tuple(sum(s.bit_count() == k for s in faces) for k in range(1, 11))
    assert len(faces) == 18494
    assert fv == (21,210,1190,3780,5187,4410,2520,945,210,21)
    print('face_count', len(faces), 'face_vector', fv)
    # Compare the complex with Jonsson's unbalanced-bipartite graph complex:
    # all subgraphs of complete bipartite K_{r,7-r}, r<=2.
    # The only extra faces are the seven full six-edge stars K_{1,6}.
    stars = {sum(1 << j for j, e in enumerate(EDGES) if v in e)
             for v in range(N_BASE)}
    assert len(stars) == 7
    for star in stars:
        assert star.bit_count() == 6 and star not in faces
        for j in range(N):
            if star & (1 << j):
                assert (star ^ (1 << j)) in faces
    b_faces = set()
    for r in (1, 2):
        for small in combinations(range(N_BASE), r):
            part = set(small)
            mask = sum(1 << j for j, (a, b) in enumerate(EDGES)
                       if (a in part) != (b in part))
            s = mask
            while s:
                b_faces.add(s)
                s = (s-1) & mask
    assert b_faces == (faces | stars)
    print('unbalanced_bipartite_comparison', 'extra_complete_stars', len(stars),
          'total_faces', len(b_faces))
    pairs, critical = matching(faces)
    crit = Counter(s.bit_count()-1 for s in critical)
    assert len(pairs) == 9120
    assert crit == {0: 1, 3: 246, 4: 7}
    print('matched_pairs',len(pairs),'critical',sorted(crit.items()))
    incidences = acyclic_hasse(faces, pairs)
    assert incidences == 98805
    print('full_hasse_cover_relations',incidences,'acyclic',True)
    n3,n4,cache = integral_morse_boundary(pairs, critical)
    print('integral_morse_boundary_shape', (n3,n4), 'nonzero_entries',0,'projections_evaluated',cache)
    ranks = boundary_ranks_f2(faces)
    assert ranks == [20,190,1000,2534,2646,1764,756,189,21]
    print('independent_mod2_boundary_ranks', ranks)
    # A CW model with only a 0-cell and cells in dimensions 3 and 4
    # has wedge of 3-spheres as its 3-skeleton; pi_3 -> H_3 is an
    # isomorphism. Therefore zero degree vectors nullhomotope all
    # 4-cell attaching maps, proving the integral homotopy type.
    print('HOMOTOPY_TYPE wedge_246_S3_and_7_S4')
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    main()
