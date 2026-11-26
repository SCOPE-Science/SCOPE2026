#!/usr/bin/env python3
"""Exact reproducible computation for the perfect-matching complex of a (2,2,3) hexagon.

Each triangle is described in the integer basis of a unit triangular lattice.
The graph is the dual adjacency graph of the triangular cells in the hexagon.
Only Python's standard library is used.
"""
import json
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations


def honeycomb(a, b, c):
    # Vertices in the triangular-lattice basis, in positive boundary order.
    polygon = ((0, 0), (a, 0), (a, b), (a-c, b+c), (-c, b+c), (-c, c))
    def interior(x, y):
        return all((q[0]-p[0])*(y-p[1])-(q[1]-p[1])*(x-p[0]) >= 0
                   for p, q in zip(polygon, polygon[1:] + polygon[:1]))
    triangles = []
    # A lattice triangle has either vertices (i,j),(i+1,j),(i,j+1),
    # or (i+1,j+1),(i+1,j),(i,j+1).
    for i in range(-c-1, a+2):
        for j in range(-1, b+c+2):
            for vertex_set in (((i,j), (i+1,j), (i,j+1)),
                               ((i+1,j+1), (i+1,j), (i,j+1))):
                triangle = tuple(sorted(vertex_set))
                sx = sum(v[0] for v in triangle)
                sy = sum(v[1] for v in triangle)
                if interior(Fraction(sx, 3), Fraction(sy, 3)):
                    triangles.append(triangle)
    assert len(triangles) == 2 * (a*b + a*c + b*c)
    by_side = defaultdict(list)
    for index, triangle in enumerate(triangles):
        for side in combinations(triangle, 2):
            by_side[side].append(index)
    edges = []
    for incident in by_side.values():
        assert len(incident) in (1, 2)
        if len(incident) == 2:
            edges.append(tuple(sorted(incident)))
    return triangles, tuple(sorted(edges))


def enumerate_perfect_matchings(vertices, edges):
    adj = [[] for _ in range(vertices)]
    for edge_id, (u, v) in enumerate(edges):
        adj[u].append((v, edge_id))
        adj[v].append((u, edge_id))
    matchings = []
    def walk(uncovered, selected):
        if not uncovered:
            matchings.append(tuple(sorted(selected)))
            return
        v = min((v for v in range(vertices) if (uncovered >> v) & 1),
                key=lambda x: sum((uncovered >> w) & 1 for w, _ in adj[x]))
        for w, edge_id in adj[v]:
            if (uncovered >> w) & 1:
                walk(uncovered & ~(1 << v) & ~(1 << w), selected + (edge_id,))
    walk((1 << vertices)-1, ())
    assert len(matchings) == len(set(matchings))
    for matching in matchings:
        covered = set()
        for e in matching:
            assert not covered.intersection(edges[e])
            covered.update(edges[e])
        assert len(covered) == vertices
    return tuple(sorted(matchings))


def bipartite_matching_count(vertices, edges):
    adj = [[] for _ in range(vertices)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    color = [-1]*vertices
    for root in range(vertices):
        if color[root] != -1: continue
        color[root] = 0
        fringe = [root]
        for v in fringe:
            for w in adj[v]:
                if color[w] == -1:
                    color[w] = 1-color[v]
                    fringe.append(w)
                else: assert color[w] == 1-color[v]
    left = [v for v in range(vertices) if color[v] == 0]
    right = [v for v in range(vertices) if color[v] == 1]
    assert len(left) == len(right)
    r_index = {v: i for i, v in enumerate(right)}
    options = [sum(1 << r_index[v] for v in adj[u]) for u in left]
    @lru_cache(None)
    def count(i, used):
        if i == len(left): return int(used.bit_count() == len(right))
        total = 0
        possible = options[i] & ~used
        while possible:
            bit = possible & -possible
            possible ^= bit
            total += count(i+1, used | bit)
        return total
    return count(0, 0)


def macmahon(a,b,c):
    answer = Fraction(1)
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                answer *= Fraction(i+j+k-1, i+j+k-2)
    assert answer.denominator == 1
    return int(answer)


def face_set(matchings):
    faces = set()
    for matching in matchings:
        subsets = [0]
        for edge_id in matching:
            bit = 1 << edge_id
            subsets += [s | bit for s in subsets]
        faces.update(subsets)
    return faces


def analyse(a, b, c, do_morse=False):
    tris, edges = honeycomb(a,b,c)
    pm = enumerate_perfect_matchings(len(tris), edges)
    assert len(pm) == macmahon(a,b,c) == bipartite_matching_count(len(tris),edges)
    faces = face_set(pm)
    # Counting the face vector independently of Morse pairing is an Euler check.
    f_vector = Counter(face.bit_count()-1 for face in faces)
    euler_reduced = sum((-1)**dim * count for dim, count in f_vector.items() if dim >= 0) - 1
    report = dict(side_lengths=[a,b,c], graph_vertices=len(tris), graph_edges=len(edges),
                  perfect_matchings=len(pm), augmented_faces=len(faces),
                  face_vector={str(k):f_vector[k] for k in sorted(f_vector)},
                  reduced_euler_characteristic=euler_reduced)
    if do_morse:
        # Successive element pairings: for each pivot e, match F with F+e
        # if both are still present. The standard element-pairing theorem
        # proves acyclicity of their union, including when F is empty.
        stage = []
        original = len(faces)
        for e in range(len(edges)):
            bit = 1 << e
            matched = set()
            for face in faces:
                if (face & bit) == 0 and (face | bit) in faces:
                    matched.add(face)
                    matched.add(face | bit)
            assert len(matched) % 2 == 0
            pairs = len(matched)//2
            faces.difference_update(matched)
            stage.append(dict(pivot=e, pairs=pairs, remaining=len(faces)))
        critical = sorted(faces)
        assert original == sum(2 * x['pairs'] for x in stage) + len(critical)
        report.update(matching_pairs=sum(x['pairs'] for x in stage),
                      matching_stage_counts=stage,
                      critical_face_masks=critical,
                      critical_edge_indices=[[i for i in range(len(edges)) if (mask>>i)&1]
                                             for mask in critical],
                      critical_dimensions=[mask.bit_count()-1 for mask in critical])
    return report


def main():
    control = analyse(2, 2, 2)
    assert (control['graph_vertices'], control['graph_edges'], control['perfect_matchings'],
            control['augmented_faces']) == (24,30,20,66370)
    report = analyse(2, 2, 3, do_morse=True)
    assert (report['graph_vertices'],report['graph_edges'],report['perfect_matchings'],
            report['augmented_faces']) == (32,41,50,2517788)
    assert report['critical_dimensions'] == [4,4]
    assert report['reduced_euler_characteristic'] == 2
    assert report['critical_face_masks'] == [34361841666, 137440068610]
    assert report['matching_pairs'] == 1258893
    print(json.dumps({'validation':'HONEYCOMB_2_2_3_TWO_4_SPHERES_OK',
                      'control_H_2_2_2':control,
                      'H_2_2_3':report},sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
