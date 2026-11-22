#!/usr/bin/env python3
"""Recompute exact discrete-Morse certificates for five-cut Möbius ladders."""
import collections
import hashlib
import itertools
import json


def graph_neighbors(n):
    size = 2*n
    return tuple((1 << ((v-1) % size)) |
                 (1 << ((v+1) % size)) |
                 (1 << ((v+n) % size)) for v in range(size))


def connected(mask, neighbors):
    seen = mask & -mask
    while True:
        nxt = seen
        for v, neighborhood in enumerate(neighbors):
            if (seen >> v) & 1:
                nxt |= neighborhood & mask
        if nxt == seen:
            return seen == mask
        seen = nxt


def faces_by_facets(n):
    size = 2*n
    full = (1 << size)-1
    adj = graph_neighbors(n)
    disconnected = []
    for vertices in itertools.combinations(range(size), 5):
        mask = sum(1 << v for v in vertices)
        if not connected(mask, adj):
            disconnected.append(mask)
    faces = {0}
    for removed in disconnected:
        facet = full ^ removed
        face = facet
        while face:
            faces.add(face)
            face = (face - 1) & facet
    return faces, disconnected


def check_independent_face_rule(n, faces, disconnected):
    # Directly test the defining existential complement criterion for every mask.
    size = 2*n
    full = (1 << size)-1
    disconnected_set = set(disconnected)
    for face in range(1 << size):
        complement = full ^ face
        expect = False
        sub = complement
        while sub:
            if sub.bit_count() == 5 and sub in disconnected_set:
                expect = True
                break
            sub = (sub-1) & complement
        assert (face in faces) == expect, (n, face)


def lexicographic_matching(n, faces):
    nonempty = faces - {0}
    unavailable = set()
    pairs = []
    for vertex in range(2*n):
        bit = 1 << vertex
        for lower in sorted(nonempty):
            upper = lower | bit
            if (lower & bit) or lower in unavailable:
                continue
            if upper not in nonempty or upper in unavailable:
                continue
            pairs.append((lower, upper))
            unavailable.add(lower)
            unavailable.add(upper)
    return pairs, nonempty - unavailable


def verify_hasse_acyclic(faces, pairs):
    # Reverse each matched edge of the ordinary upper-to-lower Hasse DAG.
    nodes = faces - {0}
    vertices = sorted(nodes)
    index = {face: i for i, face in enumerate(vertices)}
    matching = set(pairs)
    outgoing = [[] for _ in vertices]
    indegree = [0] * len(vertices)
    directed_edges = 0
    for upper in vertices:
        bits = upper
        while bits:
            one = bits & -bits
            lower = upper ^ one
            bits ^= one
            if lower == 0:
                continue
            assert lower in index
            if (lower, upper) in matching:
                src, dest = lower, upper
            else:
                src, dest = upper, lower
            i = index[src]
            j = index[dest]
            outgoing[i].append(j)
            indegree[j] += 1
            directed_edges += 1
    queue = collections.deque(i for i, degree in enumerate(indegree) if degree == 0)
    visited = 0
    while queue:
        i = queue.popleft()
        visited += 1
        for j in outgoing[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                queue.append(j)
    assert visited == len(vertices), (visited, len(vertices))
    return directed_edges, visited



def mod_two_homology(faces):
    """Independently reduce the ordinary simplicial boundary maps over F_2."""
    by_degree = collections.defaultdict(list)
    for simplex in faces:
        if simplex:
            by_degree[simplex.bit_count()-1].append(simplex)
    ranks = {}
    for degree in range(1, max(by_degree)+1):
        previous = {simplex:i for i,simplex in enumerate(by_degree[degree-1])}
        pivots = {}
        for simplex in by_degree[degree]:
            boundary = 0
            bits = simplex
            while bits:
                one = bits & -bits
                bits -= one
                boundary ^= 1 << previous[simplex ^ one]
            while boundary:
                pivot = boundary.bit_length()-1
                if pivot not in pivots:
                    pivots[pivot] = boundary
                    break
                boundary ^= pivots[pivot]
        ranks[degree] = len(pivots)
    return {degree:len(by_degree[degree])-ranks.get(degree,0)
            -ranks.get(degree+1,0)-(degree == 0)
            for degree in sorted(by_degree)}

def verify(n):
    faces, disconnected = faces_by_facets(n)
    check_independent_face_rule(n, faces, disconnected)
    pairs, critical = lexicographic_matching(n, faces)
    assert len(faces)-1 == 2*len(pairs)+len(critical)
    edge_count, visited = verify_hasse_acyclic(faces, pairs)
    dimensions = collections.Counter(f.bit_count()-1 for f in faces if f)
    crit = collections.Counter(f.bit_count()-1 for f in critical)
    d = 1 if n == 4 else 2*n-6
    expected_top = {4:1, 5:41, 6:216, 7:582, 8:1213}[n]
    assert dict(crit) == {0:1,d:expected_top}
    assert len(faces) == {4:33, 5:523, 6:3176, 7:14766, 8:62851}[n]
    reduced_chi = -1 + sum(((-1)**q)*count for q,count in dimensions.items())
    assert reduced_chi == ((-1)**d)*expected_top
    mod2 = mod_two_homology(faces)
    assert mod2 == {degree:(expected_top if degree == d else 0)
                    for degree in sorted(dimensions)}
    return {
        'n':n, 'graph_vertices':2*n, 'disconnected_five_sets':len(disconnected),
        'simplices_including_empty':len(faces),
        'face_vector':{str(k): dimensions[k] for k in sorted(dimensions)},
        'matched_pairs':len(pairs), 'critical_cells':{str(k):crit[k] for k in sorted(crit)},
        'oriented_hasse_edges':edge_count, 'dag_vertices_visited':visited,
        'reduced_euler_characteristic':reduced_chi,
        'mod2_reduced_betti':{str(k): v for k,v in mod2.items()},
        'homotopy':'wedge of %d spheres in degree %d'%(expected_top,d)
    }

if __name__ == '__main__':
    records = [verify(n) for n in (4,5,6,7,8)]
    for record in records:
        print(json.dumps(record,sort_keys=True,ensure_ascii=False))
    print('ALL FIVE EXACT MATCHING AND DAG CHECKS PASSED')
