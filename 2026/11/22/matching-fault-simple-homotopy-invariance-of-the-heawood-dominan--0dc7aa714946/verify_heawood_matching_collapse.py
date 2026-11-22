#!/usr/bin/env python3
"""Exact self-contained certificates for matching faults in the Heawood dominance complex.

No third-party dependencies. Incidence, automorphisms, orbit covers,
finite face posets, relative elementary collapses and the intact
six-sphere discrete Morse model are all reconstructed from definitions.
"""
from collections import Counter, deque
from itertools import permutations

N = 14
ALL = (1 << N) - 1
D = {0, 1, 3}
EDGES = tuple(sorted((i, 7 + j) for i in range(7)
                     for j in range(7) if (j - i) % 7 in D))
assert len(EDGES) == 21
EDGEMAP = {e: k for k, e in enumerate(EDGES)}
ADJ = [0] * N
for a, b in EDGES:
    ADJ[a] |= 1 << b
    ADJ[b] |= 1 << a
assert all(x.bit_count() == 3 for x in ADJ)


def face_set(missing_edges):
    """Closed-neighborhood dominance criterion for the edge-deleted graph."""
    adj = ADJ.copy()
    for j, (a, b) in enumerate(EDGES):
        if missing_edges & (1 << j):
            adj[a] ^= 1 << b
            adj[b] ^= 1 << a
    return {s for s in range(1 << N)
            if all(adj[v] & (ALL ^ s) for v in range(N) if s & (1 << v))}


def all_matchings():
    matches = {0}
    for k, (a, b) in enumerate(EDGES):
        new = set()
        for mask in matches:
            if all((a not in EDGES[j] and b not in EDGES[j])
                   for j in range(len(EDGES)) if mask & (1 << j)):
                new.add(mask | (1 << k))
        matches |= new
    return matches


def all_automorphisms():
    line_sets = [frozenset(i for i in range(7) if (j-i) % 7 in D)
                 for j in range(7)]
    line_lookup = {s: j for j, s in enumerate(line_sets)}
    collineations = []
    for p in permutations(range(7)):
        if all(frozenset(p[i] for i in line) in line_lookup
               for line in line_sets):
            mapped_lines = tuple(7 + line_lookup[frozenset(p[i] for i in line)]
                                 for line in line_sets)
            collineations.append(tuple(p) + mapped_lines)
    assert len(collineations) == 168
    polarity = tuple(7 + (-i) % 7 for i in range(7)) + tuple((-j) % 7 for j in range(7))
    perms = collineations + [tuple(polarity[p[v]] for v in range(N))
                            for p in collineations]
    assert len(set(perms)) == 336
    aut = []
    for p in perms:
        edge_perm = tuple(EDGEMAP[tuple(sorted((p[a], p[b])))]
                          for a, b in EDGES)
        assert len(set(edge_perm)) == 21
        aut.append(edge_perm)
    assert len(set(aut)) == 336
    return aut


def permute_matching(mask, perm):
    out = 0
    while mask:
        bit = mask & -mask
        mask -= bit
        out |= 1 << perm[bit.bit_length()-1]
    return out


def relative_collapse(larger, smaller):
    """Give an explicit free-face matching for larger -> smaller.

    For every s outside the target subcomplex, no coface of s lies inside
    the target. Thus one remaining immediate coface is a genuine free face.
    Each removal is of two simplices differing by one vertex.
    """
    assert smaller <= larger and 0 in smaller
    diff = larger - smaller
    upper = {s: set() for s in diff}
    lower = {s: set() for s in diff}
    for s in diff:
        for v in range(N):
            t = s | (1 << v)
            if t != s and t in diff:
                upper[s].add(t)
                lower[t].add(s)
    ready = deque(sorted((s for s in diff if len(upper[s]) == 1),
                         key=lambda s: (s.bit_count(), s)))
    remaining = set(diff)
    steps = 0
    while ready:
        s = ready.popleft()
        if s not in remaining or len(upper[s]) != 1:
            continue
        t = next(iter(upper[s]))
        assert t in remaining and (t ^ s).bit_count() == 1
        # A free codimension-one face cannot have other (non-immediate)
        # cofaces: adding any further vertex would create another
        # immediate coface of the smaller simplex.
        remaining.remove(s)
        remaining.remove(t)
        for z in (s, t):
            for r in lower[z]:
                upper[r].remove(z)
                if len(upper[r]) == 1:
                    ready.append(r)
            for r in upper[z]:
                lower[r].remove(z)
        steps += 1
    return len(diff), steps, len(remaining)


def check_intact_sphere():
    """A full acyclic two-critical-cell matching on the intact face poset."""
    faces = face_set(0)
    assert len(faces) == 8851
    unmatched = set(faces)
    pairings = []
    for v in range(14):
        bit = 1 << v
        for s in sorted(unmatched):
            t = s | bit
            if s in unmatched and not (s & bit) and t in unmatched:
                unmatched.remove(s)
                unmatched.remove(t)
                pairings.append((s, t))
    # The empty face and its paired vertex give the ordinary base point.
    assert pairings[0] == (0, 1)
    nonempty_pairs = pairings[1:]
    critical = unmatched | {1}
    assert len(nonempty_pairs) == 4424
    assert critical == {1, sum(1 << i for i in range(7, 14))}, critical
    matched = {(s, t) for s, t in nonempty_pairs}
    nodes = faces - {0}
    outgoing = {s: [] for s in nodes}
    indegree = {s: 0 for s in nodes}
    incidences = 0
    for t in nodes:
        for v in range(N):
            if t & (1 << v):
                s = t ^ (1 << v)
                if not s: continue
                if (s, t) in matched:
                    outgoing[s].append(t)
                    indegree[t] += 1
                else:
                    outgoing[t].append(s)
                    indegree[s] += 1
                incidences += 1
    assert incidences == 52304
    ready = deque(s for s, n in indegree.items() if n == 0)
    seen = 0
    while ready:
        s = ready.popleft()
        seen += 1
        for t in outgoing[s]:
            indegree[t] -= 1
            if indegree[t] == 0:
                ready.append(t)
    assert seen == len(nodes) == 8850, (seen, len(nodes))
    print('BASE: 8851 augmented faces, 4424 ordinary matched pairs, two critical cells dimensions 0 and 6')
    print('BASE: directed Hasse poset acyclic, 8850 nodes, 52304 incidences')


def check_cycle_contrast():
    """Show that graph-edge deletion invariance is not universal."""
    def ordinary_euler_for(n, edges):
        adj = [0] * n
        for a, b in edges:
            adj[a] |= 1 << b
            adj[b] |= 1 << a
        full = (1 << n) - 1
        return sum((-1) ** (s.bit_count() - 1)
                   for s in range(1, 1 << n)
                   if all(adj[v] & (full ^ s)
                          for v in range(n) if s & (1 << v)))
    path = [(i, i+1) for i in range(6)]
    assert ordinary_euler_for(7, path + [(0, 6)]) == 0
    assert ordinary_euler_for(7, path) == 2
    print('BOUNDARY: deleting one edge from the 7-cycle changes dominance Euler characteristic from 0 to 2')


def main():
    check_cycle_contrast()
    check_intact_sphere()
    matchings = all_matchings()
    assert len(matchings) == 3462
    full_matchings = [m for m in matchings if m.bit_count() == 7]
    unextendible = sum(not any((m & ~full) == 0 for full in full_matchings)
                       for m in matchings)
    assert unextendible == 1260
    hist = Counter(m.bit_count() for m in matchings)
    assert dict(sorted(hist.items())) == {0: 1, 1: 21, 2: 168, 3: 644,
                                         4: 1218, 5: 1050, 6: 336, 7: 24}
    aut = all_automorphisms()
    unseen = matchings.copy()
    representatives = []
    orbit_coverage = set()
    while unseen:
        rep = min(unseen)
        orbit = {permute_matching(rep, p) for p in aut}
        assert orbit <= matchings
        assert not (orbit & orbit_coverage)
        unseen -= orbit
        orbit_coverage |= orbit
        representatives.append((rep, len(orbit)))
    assert orbit_coverage == matchings
    assert len(representatives) == 30
    orbit_hist = Counter(rep.bit_count() for rep, _ in representatives)
    assert dict(sorted(orbit_hist.items())) == {0: 1, 1: 1, 2: 2,
                                                3: 6, 4: 8, 5: 7, 6: 4, 7: 1}
    cache = {}
    def f(mask):
        if mask not in cache:
            cache[mask] = face_set(mask)
        return cache[mask]
    count = 0
    count_by_size = Counter()
    total_pairs = 0
    for mask, orbit_size in representatives:
        for k in range(len(EDGES)):
            if mask & (1 << k):
                target = f(mask)
                source = f(mask ^ (1 << k))
                # More edge deletions: weaker domination, hence fewer faces.
                size, steps, remaining = relative_collapse(source, target)
                assert remaining == 0 and size == 2 * steps, (mask, k, size, steps, remaining)
                count += 1
                total_pairs += steps
                count_by_size[mask.bit_count()] += 1
    assert count == 121
    assert dict(sorted(count_by_size.items())) == {1:1,2:4,3:18,4:32,5:35,6:24,7:7}
    print('AUTOMORPHISMS: 168 Fano collineations; full graph automorphisms 336')
    print('MATCHINGS: 3462, including 1260 nonextendible matchings; size counts:', dict(sorted(hist.items())))
    print('ORBITS: 30, counts by size:', dict(sorted(orbit_hist.items())))
    print('COLLAPSE CERTIFICATES: 121 relative one-edge transitions checked; all differences reduced to zero')
    print('CERTIFICATE PAIRS: total', total_pairs, 'relative elementary pairs across representatives')
    print('CONCLUSION: every matching-deletion step induces a simple-homotopy equivalence')

if __name__ == '__main__':
    main()
