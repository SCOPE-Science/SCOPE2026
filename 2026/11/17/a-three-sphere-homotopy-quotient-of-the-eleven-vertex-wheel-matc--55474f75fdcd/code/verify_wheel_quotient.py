#!/usr/bin/env python3
"""Exact cellular homology of the dihedral orbit of the eleven-vertex wheel matching complex.

Requires Python 3.9+ and SymPy (tested with the local installed release).
Uses integer Smith normal form, not floating-point ranks.
"""
from itertools import combinations
from collections import defaultdict
import hashlib
import json
from sympy import zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 10


def wheel_edges():
    return [tuple(sorted((i, (i + 1) % N))) for i in range(N)] + [tuple(sorted((i, N))) for i in range(N)]


def all_matchings(edges):
    result = []
    for k in range(1, 6):
        for subset in combinations(range(20), k):
            if len({v for j in subset for v in edges[j]}) == 2 * k:
                result.append(subset)
    return result


def group_edge_maps(edges):
    index = {e: j for j, e in enumerate(edges)}
    transformations = []
    for sign in (1, -1):
        for shift in range(N):
            mapping = tuple(index[tuple(sorted((N if x == N else (sign * x + shift) % N,
                                                N if y == N else (sign * y + shift) % N)))]
                            for x, y in edges)
            transformations.append(mapping)
    assert len(set(transformations)) == 20
    return transformations


def compute():
    edges = wheel_edges()
    faces = all_matchings(edges)
    assert len(faces) == len(set(faces))
    faces_by_size = defaultdict(list)
    for face in faces:
        faces_by_size[len(face)].append(face)
    maps = group_edge_maps(edges)

    chains = []
    def extend(chain):
        chains.append(chain)
        low = chain[-1]
        ls = set(low)
        for k in range(len(low) + 1, 6):
            for face in faces_by_size[k]:
                if ls.issubset(face):
                    extend(chain + (face,))
    for face in faces:
        extend((face,))

    def translate(chain, edge_map):
        return tuple(tuple(sorted(edge_map[j] for j in face)) for face in chain)

    # Orbit cells of order-complex flags; increasing ranks eliminate inversions.
    orbit_index = {}
    representatives = []
    cell_layers = defaultdict(list)
    for chain in chains:
        if chain in orbit_index:
            continue
        cell_id = len(representatives)
        representatives.append(chain)
        cell_layers[len(chain) - 1].append(cell_id)
        for edge_map in maps:
            image = translate(chain, edge_map)
            if image in orbit_index:
                assert orbit_index[image] == cell_id
            orbit_index[image] = cell_id
    assert len(orbit_index) == len(chains)

    # Independent Burnside check: fixed flags, not just orbit-representative totals.
    burnside = {}
    for d in range(5):
        level = [chain for chain in chains if len(chain) == d + 1]
        fixed_sum = sum(sum(translate(chain, emap) == chain for chain in level)
                        for emap in maps)
        assert fixed_sum % 20 == 0
        burnside[d] = fixed_sum // 20
        assert burnside[d] == len(cell_layers[d])

    # Boundary of rank-ordered face chains has integer signs (-1)^omitted_position.
    local_indices = {d: {i: j for j, i in enumerate(cell_layers[d])}
                     for d in range(5)}
    boundaries = {}
    sparse = {}
    for d in range(1, 5):
        rows, cols = len(cell_layers[d-1]), len(cell_layers[d])
        matrix = zeros(rows, cols)
        columns = []
        for j, cid in enumerate(cell_layers[d]):
            chain = representatives[cid]
            column = defaultdict(int)
            for i in range(len(chain)):
                lower = chain[:i] + chain[i+1:]
                row = local_indices[d - 1][orbit_index[lower]]
                matrix[row, j] += (-1) ** i
                column[row] += (-1) ** i
            columns.append(dict(column))
        boundaries[d] = matrix
        sparse[d] = columns

    # Independently verify boundary squared = 0 over Z, coefficient-by-coefficient.
    for d in range(2, 5):
        for column in sparse[d]:
            twice = defaultdict(int)
            for middle, coeff in column.items():
                for lower, second_coeff in sparse[d - 1][middle].items():
                    twice[lower] += coeff * second_coeff
            assert all(value == 0 for value in twice.values()), (d, column)

    smith = {}
    ranks = {0: 0, 5: 0}
    matrix_digests = {}
    for d in range(1, 5):
        mat = boundaries[d]
        # Canonical row-major signed integer data hash, including dimensions.
        encoded = json.dumps({'shape': [mat.rows, mat.cols],
                              'entries': [int(mat[i, j]) for i in range(mat.rows)
                                          for j in range(mat.cols)]},
                             separators=(',', ':')).encode('utf-8')
        matrix_digests[d] = hashlib.sha256(encoded).hexdigest()
        diagonal = smith_normal_form(mat, domain=ZZ)
        invariants = [abs(int(diagonal[i, i])) for i in range(min(mat.shape))
                      if diagonal[i, i] != 0]
        ranks[d] = len(invariants)
        smith[d] = {'rank': ranks[d],
                    'nonunit_invariant_factors': [x for x in invariants if x != 1]}
        assert all(i == 1 for i in invariants), (d, smith[d])
    counts = [len(cell_layers[d]) for d in range(5)]
    betti = [counts[d] - ranks[d] - ranks[d+1] for d in range(5)]
    assert counts == [43,343,882,894,312]
    assert [ranks[d] for d in range(1, 5)] == [42,301,581,312]
    assert betti == [1,0,0,1,0]
    print('graph: wheel W_11, rim 10, group D_10 order 20')
    print('matching faces by cardinality:', [len(faces_by_size[k]) for k in range(1,6)])
    print('quotient flag-cell counts dimensions 0..4:', counts)
    print('independent Burnside counts dimensions 0..4:', [burnside[d] for d in range(5)])
    print('boundary-squared identities: all zero over integers')
    for d in range(1, 5):
        print('integer Smith B_%d: rank %d; nonunit factors %s; matrix SHA256 %s' %
              (d, smith[d]['rank'], smith[d]['nonunit_invariant_factors'],matrix_digests[d]))
    print('integral Betti ranks dimensions 0..4:', betti)
    print('integral homology torsion: none (every nonzero Smith factor is 1)')
    print('RESULT: PASS')

if __name__ == '__main__':
    compute()
