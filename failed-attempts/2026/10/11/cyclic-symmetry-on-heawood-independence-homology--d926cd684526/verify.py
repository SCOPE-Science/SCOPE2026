#!/usr/bin/env python3
import json
from collections import deque
from itertools import combinations

N = 14
ROTATION_ORDER = 7


def heawood_edges():
    edges = set()
    for line in range(7):
        for delta in (0, 1, 3):
            point = (line + delta) % 7
            edges.add(tuple(sorted((point, 7 + line))))
    return sorted(edges)


def rotate_vertex(v, k):
    if v < 7:
        return (v + k) % 7
    return 7 + ((v - 7 + k) % 7)


def independent_faces(edges):
    edge_set = set(edges)
    faces = []
    for mask in range(1, 1 << N):
        vertices = [v for v in range(N) if (mask >> v) & 1]
        if all(tuple(sorted((a, b))) not in edge_set for a, b in combinations(vertices, 2)):
            faces.append(mask)
    return faces


def staged_toggle_matching(faces):
    unmatched = set(faces)
    pairs = []
    for vertex in range(N):
        bit = 1 << vertex
        for lower in sorted(tuple(unmatched)):
            if lower & bit:
                continue
            upper = lower | bit
            if upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                pairs.append((lower, upper))
    return pairs, sorted(unmatched)


def verify_hasse_acyclic(faces, pairs):
    index = {face: i for i, face in enumerate(faces)}
    face_set = set(faces)
    matched = set(pairs)
    adjacency = [[] for _ in faces]
    indegree = [0] * len(faces)
    covers = 0
    for upper in faces:
        for vertex in range(N):
            if not ((upper >> vertex) & 1):
                continue
            lower = upper & ~(1 << vertex)
            if lower == 0 or lower not in face_set:
                continue
            covers += 1
            if (lower, upper) in matched:
                source, target = index[lower], index[upper]
            else:
                source, target = index[upper], index[lower]
            adjacency[source].append(target)
            indegree[target] += 1
    queue = deque(i for i, d in enumerate(indegree) if d == 0)
    seen = 0
    while queue:
        node = queue.popleft()
        seen += 1
        for target in adjacency[node]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    return seen == len(faces), covers


def signed_chain_trace(faces, k):
    trace = {}
    for face in faces:
        vertices = [v for v in range(N) if (face >> v) & 1]
        image = [rotate_vertex(v, k) for v in vertices]
        image_mask = sum(1 << v for v in image)
        if image_mask != face:
            continue
        position = {v: i for i, v in enumerate(vertices)}
        permutation = [position[v] for v in image]
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(len(permutation))
            for j in range(i + 1, len(permutation))
        )
        sign = -1 if inversions % 2 else 1
        dimension = len(vertices) - 1
        trace[dimension] = trace.get(dimension, 0) + sign
    return trace


def main():
    edges = heawood_edges()
    assert len(edges) == 21
    degrees = [0] * N
    for a, b in edges:
        degrees[a] += 1
        degrees[b] += 1
    assert degrees == [3] * N

    edge_set = set(edges)
    for k in range(ROTATION_ORDER):
        rotated = {tuple(sorted((rotate_vertex(a, k), rotate_vertex(b, k)))) for a, b in edges}
        assert rotated == edge_set
    assert all(rotate_vertex(v, 7) == v for v in range(N))
    assert any(rotate_vertex(v, 1) != v for v in range(N))

    faces = independent_faces(edges)
    face_vector = {}
    for face in faces:
        dimension = face.bit_count() - 1
        face_vector[dimension] = face_vector.get(dimension, 0) + 1
    assert len(faces) == 457
    assert [face_vector[d] for d in range(7)] == [14, 70, 154, 147, 56, 14, 2]

    pairs, critical = staged_toggle_matching(faces)
    critical_vector = {}
    for face in critical:
        dimension = face.bit_count() - 1
        critical_vector[dimension] = critical_vector.get(dimension, 0) + 1
    assert len(pairs) == 225
    assert critical_vector == {0: 1, 3: 6}
    acyclic, covers = verify_hasse_acyclic(faces, pairs)
    assert acyclic
    assert covers == 1568

    lefschetz = []
    h3_character = []
    chain_traces = []
    for k in range(ROTATION_ORDER):
        trace = signed_chain_trace(faces, k)
        L = sum(((-1) ** d) * value for d, value in trace.items())
        # The Morse calculation proves that only H_0 and H_3 are nonzero.
        h3_trace = 1 - L
        chain_traces.append({str(d): trace[d] for d in sorted(trace)})
        lefschetz.append(L)
        h3_character.append(h3_trace)
    assert lefschetz == [-5, 2, 2, 2, 2, 2, 2]
    assert h3_character == [6, -1, -1, -1, -1, -1, -1]

    summary = {
        "vertices": N,
        "edges": len(edges),
        "nonempty_faces": len(faces),
        "face_vector": [face_vector[d] for d in range(7)],
        "hasse_covers": covers,
        "matching_pairs": len(pairs),
        "critical_cells": {str(d): critical_vector[d] for d in sorted(critical_vector)},
        "chain_traces": chain_traces,
        "lefschetz_numbers": lefschetz,
        "H3_character": h3_character,
    }
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
