#!/usr/bin/env python3
"""Independent Python verification of the 4-cube matching-deletion shattering table.

Standard library only.  Enumerates independent sets directly rather than
using maximal-clique enumeration, and tests all traces as set intersections.
Run: python3 check_matching_profiles.py
"""
from collections import Counter
from itertools import permutations

N = 16
EDGES = tuple(sorted((u, u ^ (1 << j)) for u in range(N) for j in range(4)
                     if u < (u ^ (1 << j))))
NEIGHBORS = [set() for _ in range(N)]
for a, b in EDGES:
    NEIGHBORS[a].add(b)
    NEIGHBORS[b].add(a)


def all_matchings(unmatched, edges=()):
    if not unmatched:
        yield tuple(sorted(edges))
        return
    u = min(unmatched)
    for v in sorted(NEIGHBORS[u] & unmatched):
        yield from all_matchings(unmatched - {u, v}, edges + ((u, v),))


def group_actions():
    for order in permutations(range(4)):
        for offset in range(N):
            yield tuple(offset ^ sum(((u >> j) & 1) << order[j]
                                     for j in range(4)) for u in range(N))


def act_matching(matching, action):
    return tuple(sorted(tuple(sorted((action[a], action[b])))
                        for a, b in matching))


def statistics(matching):
    retained_edges = set(EDGES) - set(matching)
    neighbors = [0] * N
    for a, b in retained_edges:
        neighbors[a] |= 1 << b
        neighbors[b] |= 1 << a
    independent = [False] * (1 << N)
    independent[0] = True
    for s in range(1, 1 << N):
        bit = s & -s
        v = bit.bit_length() - 1
        independent[s] = independent[s ^ bit] and not (neighbors[v] & (s ^ bit))
    concepts = [s for s in range(1 << N) if independent[s] and all(
        neighbors[v] & s for v in range(N) if not (s >> v & 1))]
    count_concepts = Counter(s.bit_count() for s in concepts)
    face_set = set()
    for support in range(1 << N):
        k = support.bit_count()
        if k >= 7 or (1 << k) > len(concepts) or not independent[support]:
            continue
        if len({concept & support for concept in concepts}) == 1 << k:
            face_set.add(support)
    polynomial = tuple(Counter(s.bit_count() for s in face_set)[k]
                       for k in range(7))
    facets = [s for s in face_set if all((s | (1 << v)) not in face_set
               for v in range(N) if not (s >> v & 1))]
    facet_poly = tuple(Counter(s.bit_count() for s in facets)[k]
                       for k in range(7))
    return polynomial, facet_poly, tuple(sorted(count_concepts.items()))


EXPECTED = (
    (4, (1,16,96,256,256,0,0), (0,0,0,0,256,0,0), ((4,16),(6,16),(8,4))),
    (48, (1,16,96,240,168,0,0), (0,0,0,24,168,0,0), ((4,6),(5,8),(6,20),(7,4),(8,2))),
    (24, (1,16,96,224,88,0,0), (0,0,0,64,88,0,0), ((4,4),(6,40),(8,2))),
    (48, (1,16,96,232,120,0,0), (0,0,0,24,120,0,0), ((5,16),(6,32),(8,2))),
    (96, (1,16,96,240,169,0,0), (0,0,0,16,169,0,0), ((4,1),(5,16),(6,30),(8,2))),
    (12, (1,16,96,256,256,0,0), (0,0,0,0,256,0,0), ((4,8),(6,32),(8,2))),
    (32, (1,16,96,248,209,36,0), (0,0,0,12,77,36,0), ((4,1),(5,36),(6,22),(8,2))),
    (8, (1,16,96,272,296,48,0), (0,0,0,0,128,48,0), ((4,4),(5,48),(6,16),(8,2))),
)


def main():
    all_m = set(all_matchings(frozenset(range(N))))
    assert len(all_m) == 272
    actions = tuple(group_actions())
    assert len(actions) == 384
    pending = set(all_m)
    orbit_total = 0
    for i, (size, polynomial, facets, concept_sizes) in enumerate(EXPECTED, 1):
        representative = min(pending)
        orbit = {act_matching(representative, action) for action in actions}
        assert len(orbit) == size and orbit <= pending
        pending -= orbit
        orbit_total += len(orbit)
        data = statistics(representative)
        assert data == (polynomial, facets, concept_sizes), (i, data)
        print(f"orbit={i} size={size} face={polynomial} facets={facets}")
    assert not pending and orbit_total == 272
    assert sum(size for size, p, f, c in EXPECTED if p[5]) == 40
    assert sum(size for size, p, f, c in EXPECTED if sum(x>0 for x in f)==1) == 16
    print("PYTHON_Q4_MATCHING_SHATTER_PASS matchings=272 orbits=8 vc5=40 pure=16")


if __name__ == "__main__":
    main()
