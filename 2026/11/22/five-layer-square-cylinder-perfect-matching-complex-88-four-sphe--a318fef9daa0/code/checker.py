#!/usr/bin/env python3
"""Self-contained exact computation for the perfect-matching complex of C4 x P5.
No external modules, symbolic packages, random numbers, or network calls.
Run: python3 checker.py
"""
from collections import Counter, defaultdict
from itertools import product
from heapq import heappush, heappop
from hashlib import sha256
import json


def graph():
    vertices = list(product(range(2), range(2), range(5)))
    index = {v: i for i, v in enumerate(vertices)}
    edges = []
    for i, v in enumerate(vertices):
        for direction in range(3):
            if v[direction] + 1 < (2, 2, 5)[direction]:
                w = list(v)
                w[direction] += 1
                edges.append((i, index[tuple(w)]))
    assert len(vertices) == 20 and len(edges) == 36
    return vertices, edges


def complex_of_extendible_matchings(vertices, edges):
    adjacency = [[] for _ in vertices]
    for i, (a, b) in enumerate(edges):
        adjacency[a].append((i, b))
        adjacency[b].append((i, a))
    matchings = []
    def recurse(remaining, edges_so_far):
        if not remaining:
            matchings.append(tuple(sorted(edges_so_far)))
            return
        pivot = (remaining & -remaining).bit_length() - 1
        for e, neighbor in adjacency[pivot]:
            if remaining & (1 << neighbor):
                recurse(remaining ^ (1 << pivot) ^ (1 << neighbor), edges_so_far + (e,))
    recurse((1 << len(vertices)) - 1, ())
    assert len(set(matchings)) == len(matchings) == 450
    faces = {0}
    for matching in matchings:
        subfaces = [0]
        for edge_id in matching:
            subfaces += [face | (1 << edge_id) for face in subfaces]
        faces.update(subfaces)
    assert len(faces) == 183544
    assert max(face.bit_count() for face in faces) == 10
    return matchings, faces


def collapse(faces, vertex_count):
    current = set(faces)
    number_of_covers = {face: 0 for face in current}
    for face in current:
        z = face
        while z:
            one = z & -z
            z -= one
            number_of_covers[face ^ one] += 1
    heap = [(-face.bit_count(), face) for face in current if face and number_of_covers[face] == 1]
    from heapq import heapify
    heapify(heap)
    pairs_digest = sha256()
    pairs = 0
    while heap:
        _, face = heappop(heap)
        if face not in current or number_of_covers[face] != 1:
            continue
        covers = [face | (1 << j) for j in range(vertex_count) if not face & (1 << j) and face | (1 << j) in current]
        assert len(covers) == 1
        coface = covers[0]
        assert coface.bit_count() == face.bit_count() + 1
        pairs_digest.update(f'{face},{coface}\n'.encode('ascii'))
        for removed in (face, coface):
            current.remove(removed)
            z = removed
            while z:
                one = z & -z
                z -= one
                subface = removed ^ one
                if subface in current:
                    number_of_covers[subface] -= 1
                    assert number_of_covers[subface] >= 0
                    if subface and number_of_covers[subface] == 1:
                        heappush(heap, (-subface.bit_count(), subface))
        pairs += 1
    assert pairs == 88171 and len(current) == 7202
    f_vector = [sum(face.bit_count() == i + 1 for face in current) for i in range(5)]
    assert f_vector == [36, 427, 1850, 3129, 1759]
    return current, pairs, pairs_digest.hexdigest(), f_vector


def fundamental_group_elimination(core):
    vertices = sorted(face for face in core if face.bit_count() == 1)
    edges = sorted(face for face in core if face.bit_count() == 2)
    triangles = sorted(face for face in core if face.bit_count() == 3)
    parent = list(range(len(vertices)))
    vi = {v: i for i, v in enumerate(vertices)}
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    killed = set()
    for edge in edges:
        vertices_on_edge = [vi[1 << j] for j in range(edge.bit_length()) if edge & (1 << j)]
        a, b = map(root, vertices_on_edge)
        if a != b:
            parent[a] = b
            killed.add(edge)
    assert len(killed) == 35 and len({root(v) for v in range(36)}) == 1
    steps = []
    progressed = True
    while progressed:
        progressed = False
        for triangle in triangles:
            edges_of_triangle = [triangle ^ (1 << j) for j in range(triangle.bit_length()) if triangle & (1 << j)]
            unknown = [edge for edge in edges_of_triangle if edge not in killed]
            if len(unknown) == 1:
                killed.add(unknown[0])
                steps.append((unknown[0], triangle))
                progressed = True
    assert len(steps) == 392 and len(killed) == len(edges) == 427
    return {'tree_edges': 35, 'triangle_relator_eliminations': len(steps), 'remaining_nontrivial_generators': 0}


def boundary_columns(faces_by_size, k):
    # k-simplex -> (k-1)-simplices; orientation by increasing edge-index order.
    prev = {face: i for i, face in enumerate(faces_by_size[k - 1])}
    columns = {}
    for j, face in enumerate(faces_by_size[k]):
        z = face
        sign = 1
        column = {}
        while z:
            one = z & -z
            z -= one
            column[prev[face ^ one]] = sign
            sign = -sign
        columns[j] = column
    return columns


def unit_diagonalize(columns):
    # Exact integer elementary column operations only; every removed pivot is ±1.
    cols = {j: dict(col) for j, col in columns.items()}
    rows = defaultdict(dict)
    for j, col in cols.items():
        for i, x in col.items():
            rows[i][j] = x
    pivots = 0
    while True:
        candidate = None
        for j, col in cols.items():
            for i, x in col.items():
                if abs(x) == 1:
                    cost = (len(col)-1) * (len(rows[i])-1)
                    if candidate is None or cost < candidate[0]:
                        candidate = (cost, i, j, x)
                    if candidate[0] == 0:
                        break
            if candidate is not None and candidate[0] == 0:
                break
        if candidate is None:
            break
        _, i, j, sign = candidate
        col = cols[j]
        for jj, value in list(rows[i].items()):
            if jj == j:
                continue
            factor = value * sign
            for ii, coefficient in col.items():
                updated = cols[jj].get(ii, 0) - factor * coefficient
                if updated:
                    cols[jj][ii] = updated
                    rows[ii][jj] = updated
                else:
                    cols[jj].pop(ii, None)
                    rows[ii].pop(jj, None)
            assert i not in cols[jj]
        for ii in col:
            rows[ii].pop(j, None)
        cols.pop(j)
        rows.pop(i, None)
        pivots += 1
    assert all(not col for col in cols.values()), 'Nonunit Smith remainder: cannot certify integral homology'
    return pivots


def boundary_squared_zero(faces_by_size, k):
    if k < 2:
        return
    # Exact check for every oriented k-simplex.
    for face in faces_by_size[k]:
        z = face
        sign = 1
        coefficients = {}
        while z:
            bit = z & -z
            z -= bit
            facet = face ^ bit
            zz = facet
            sign2 = 1
            while zz:
                bit2 = zz & -zz
                zz -= bit2
                sub = facet ^ bit2
                coefficients[sub] = coefficients.get(sub, 0) + sign * sign2
                sign2 = -sign2
            sign = -sign
        assert all(x == 0 for x in coefficients.values())


def induced_symmetry(vertices, edges, k, reflection, reverse):
    vi = {v: i for i, v in enumerate(vertices)}
    ei = {edge: i for i, edge in enumerate(edges)}
    vmap = []
    for a, b, t in vertices:
        if reflection:
            a = 1 - a
        for _ in range(k):
            a, b = 1-b, a
        if reverse:
            t = 4 - t
        vmap.append(vi[a,b,t])
    return [ei[tuple(sorted((vmap[a],vmap[b])))] for a, b in edges]


def trace_top_homology(faces, edge_action):
    # Alternating fixed-face chain trace = Lefschetz number.
    # Since reduced homology is Z^88 in even degree 4 only: tr(H4)=L-1.
    trace = 0
    for face in faces:
        if face == 0:
            continue
        bits = []
        z = face
        image = 0
        while z:
            one = z & -z
            z -= one
            i = one.bit_length()-1
            bits.append(i)
            image |= 1 << edge_action[i]
        if image != face:
            continue
        ordered_images = [edge_action[i] for i in bits]
        inversions = sum(ordered_images[i] > ordered_images[j] for i in range(len(bits)) for j in range(i+1,len(bits)))
        trace += (-1 if (len(bits)-1+inversions) % 2 else 1)
    return trace - 1


def dihedral_characters(faces, vertices, edges):
    traces = {}
    for k, s, h in product(range(4), range(2), range(2)):
        permutation = induced_symmetry(vertices,edges,k,s,h)
        traces[k,s,h] = trace_top_homology(faces, permutation)
    assert [traces[k,s,0] for k,s in product(range(4),range(2))] == [88,8,0,0,0,8,0,0]
    # row index A1,A2,B1,B2,E; column index path-reversal sign + or -
    def d4_character(k,s):
        return (1,(-1)**s,(-1)**k,(-1)**(k+s), (2 if k==0 else -2 if k==2 else 0) if s==0 else 0)
    mult = {}
    for j,name in enumerate(('A1','A2','B1','B2','E')):
        for sign,label in ((1,'+'),(-1,'-')):
            num = sum(traces[k,s,h] * d4_character(k,s)[j] * sign**h for k,s,h in traces)
            assert num % 16 == 0 and num >= 0
            mult[name+label] = num // 16
    assert mult == {'A1+':7,'A1-':6,'A2+':6,'A2-':3,'B1+':9,'B1-':4,'B2+':4,'B2-':5,'E+':10,'E-':12}
    assert sum(mult[x] * (2 if x.startswith('E') else 1) for x in mult) == 88
    return traces,mult


def main():
    vertices, edges = graph()
    matchings, faces = complex_of_extendible_matchings(vertices, edges)
    core, pairs, pair_hash, fvec = collapse(faces, len(edges))
    fg = fundamental_group_elimination(core)
    bydim = {k: sorted(face for face in core if face.bit_count() == k+1) for k in range(5)}
    for k in range(2,5):
        boundary_squared_zero(bydim, k)
    ranks = {}
    for k in (2,3,4):
        ranks[k] = unit_diagonalize(boundary_columns(bydim,k))
    assert ranks == {2:392,3:1458,4:1671}
    assert (fvec[1]-35-ranks[2], fvec[2]-ranks[2]-ranks[3],fvec[3]-ranks[3]-ranks[4],fvec[4]-ranks[4]) == (0,0,0,88)
    traces,mult = dihedral_characters(faces, vertices, edges)
    canonical = [[k,s,traces[k,s,0],traces[k,s,1]] for k,s in product(range(4),range(2))]
    report={'graph':'C4_cartesian_P5','vertices':20,'edges':len(edges),'perfect_matchings':len(matchings),
            'face_count_including_empty':len(faces),'top_dimension':9,
            'elementary_collapse_pairs':pairs,'collapse_pairs_sha256':pair_hash,
            'core_f_vector':fvec,'fundamental_group':fg,'unit_smith_ranks':ranks,
            'reduced_integral_homology':{'H4_rank':88,'all_others_zero':True},
            'top_homology_character_rows_rk_s_h0_h1':canonical,
            'D4_x_C2_rational_multiplicities':mult,'full_symmetry_quotient_rational_H4_rank':mult['A1+']}
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
