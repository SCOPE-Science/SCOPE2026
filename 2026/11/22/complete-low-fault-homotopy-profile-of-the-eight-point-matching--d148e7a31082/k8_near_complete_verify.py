#!/usr/bin/env python3
"""Complete finite certificate for matching complexes of K8 with <=3
missing edges. Standalone Python 3; no packages or network access needed.
Run: python3 k8_near_complete_verify.py
"""
from itertools import combinations
from collections import Counter, deque

CASES = [
 ("intact", (), (28, 210, 420, 105), 132),
 ("one_edge", ((0, 1),), (27, 195, 375, 90), 116),
 ("two_incident", ((0, 1), (0, 2)), (26, 180, 330, 75), 100),
 ("two_disjoint", ((0, 1), (2, 3)), (26, 181, 336, 78), 102),
 ("three_star", ((0, 1), (0, 2), (0, 3)), (25, 165, 285, 60), 84),
 ("three_triangle", ((0, 1), (0, 2), (1, 2)), (25, 165, 285, 60), 84),
 ("three_path", ((0, 1), (1, 2), (2, 3)), (25, 166, 291, 63), 86),
 ("three_adjacent_plus_disjoint", ((0, 1), (0, 2), (3, 4)),
  (25, 167, 297, 66), 88),
 ("three_disjoint", ((0, 1), (2, 3), (4, 5)),
  (25, 168, 302, 68), 90),
]

def edge_set(banned):
    return [(i, j) for i in range(8) for j in range(i + 1, 8)
            if (i, j) not in banned]

def complex_faces(edges):
    faces = {0}  # Augmented empty face is represented by zero.
    for size in range(1, 5):
        for ids in combinations(range(len(edges)), size):
            if len({v for j in ids for v in edges[j]}) == 2 * size:
                faces.add(sum(1 << j for j in ids))
    return faces

def check_morse(edges, all_faces):
    remaining = set(all_faces)
    pairs = []
    # Lexicographic sequential toggle matching on the augmented complex.
    # Every available pair consists of two matchings differing by the next
    # graph edge in the lexicographic list.
    for j in range(len(edges)):
        bit = 1 << j
        for lo in sorted(remaining):
            if lo & bit == 0 and lo | bit in remaining:
                hi = lo | bit
                remaining.remove(lo)
                remaining.remove(hi)
                pairs.append((lo, hi))
    assert 2 * len(pairs) + len(remaining) == len(all_faces)
    assert len({z for lo, hi in pairs for z in (lo, hi)}) == 2 * len(pairs)
    assert 0 not in remaining and sum(lo == 0 for lo, hi in pairs) == 1
    paired = set(pairs)
    # Enumerate EVERY codimension-one incidence. Matched incidences point
    # down; all others point up. Topological sorting proves no cycles.
    indegree = {f: 0 for f in all_faces}
    outgoing = {f: [] for f in all_faces}
    hasse_edges = 0
    for hi in all_faces:
        x = hi
        while x:
            b = x & -x
            lo = hi ^ b
            assert lo in all_faces
            u, v = (hi, lo) if (lo, hi) in paired else (lo, hi)
            outgoing[u].append(v)
            indegree[v] += 1
            hasse_edges += 1
            x ^= b
    q = deque(f for f in all_faces if indegree[f] == 0)
    visited = 0
    while q:
        u = q.popleft()
        visited += 1
        for v in outgoing[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    assert visited == len(all_faces), "gradient cycle exists"
    return remaining, pairs, hasse_edges

def signature(ban):
    degree = [0] * 8
    for i, j in ban:
        degree[i] += 1
        degree[j] += 1
    return tuple(sorted((d for d in degree if d), reverse=True))

def check_exhaustive_fault_types():
    complete_edges = edge_set(set())
    for size in (0, 1, 2, 3):
        representatives = [b for _, b, _, _ in CASES if len(b) == size]
        profiles = {signature(b) for b in representatives}
        assert len(profiles) == len(representatives)
        observed = Counter(signature(b) for b in combinations(complete_edges, size))
        assert set(observed) == profiles
        assert sum(observed.values()) == (1, 28, 378, 3276)[size]
        print("fault_orbits", size, "profiles", len(profiles),
              "labeled_fault_sets", sum(observed.values()))

def main():
    check_exhaustive_fault_types()
    for name, banned, expected_f, expected_critical in CASES:
        edges = edge_set(set(banned))
        faces = complex_faces(edges)
        fvector = tuple(sum(f.bit_count() == size for f in faces)
                        for size in range(1, 5))
        assert fvector == expected_f, (name, fvector)
        critical, pairs, incidences = check_morse(edges, faces)
        assert Counter(f.bit_count() - 1 for f in critical) == {2: expected_critical}
        assert fvector[0]-fvector[1]+fvector[2]-fvector[3]-1 == expected_critical
        print(name, "f", fvector, "faces", len(faces), "pairs", len(pairs),
              "critical_2", len(critical), "Hasse_covers", incidences,
              "acyclic", True)
    print("PASS: all fault orbits, faces, acyclic matchings and sphere counts")

if __name__ == '__main__':
    main()
