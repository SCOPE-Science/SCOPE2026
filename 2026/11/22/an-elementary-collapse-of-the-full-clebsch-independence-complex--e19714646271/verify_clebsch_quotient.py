#!/usr/bin/env python3
"""Exact verifier for the folded-five-cube independence-complex quotient.

Usage: python3 verify_clebsch_quotient.py collapse_certificate.json
Requires Python 3.10+ standard library only.
"""
import itertools
import json
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path


def verify(certificate_path):
    cert = json.loads(Path(certificate_path).read_text(encoding='utf-8'))
    vertices = tuple(x for x in range(32) if x.bit_count() % 2 == 0)
    assert len(vertices) == 16
    vertex_index = {x: i for i, x in enumerate(vertices)}
    graph_edges = {(i, j) for i in range(16) for j in range(i + 1, 16)
                   if (vertices[i] ^ vertices[j]).bit_count() == 4}
    assert len(graph_edges) == 40
    neighborhoods = [{j for j in range(16) if tuple(sorted((i, j))) in graph_edges}
                     for i in range(16)]
    assert all(len(s) == 5 for s in neighborhoods)
    assert all(len(neighborhoods[i] & neighborhoods[j]) ==
               (0 if (i, j) in graph_edges else 2)
               for i in range(16) for j in range(i + 1, 16))
    # Distinct nonneighbors of zero are identified by their two zero-neighbors.
    assert len({frozenset(neighborhoods[0] & neighborhoods[i])
                for i in range(1, 16) if i not in neighborhoods[0]}) == 10

    faces = tuple(m for m in range(1, 1 << 16)
                  if not any(m >> i & 1 and m >> j & 1 for i, j in graph_edges))
    face_set = set(faces)
    assert len(faces) == 392
    assert Counter(m.bit_count() for m in faces) == {1: 16, 2: 80, 3: 160, 4: 120, 5: 16}

    def moved(x, perm):
        return sum(((x >> i) & 1) << perm[i] for i in range(5))

    # This explicit affine group contains all graph automorphisms: its order
    # reaches the 16*(5!) bound from a vertex and its five neighbors.
    all_maps = set()
    for perm in itertools.permutations(range(5)):
        for t in vertices:
            vm = tuple(vertex_index[moved(x, perm) ^ t] for x in vertices)
            all_maps.add(vm)
    assert len(all_maps) == 1920
    for vm in all_maps:
        assert all(tuple(sorted((vm[i], vm[j]))) in graph_edges
                   for i, j in graph_edges)

    def face_image(face, vm):
        result = 0
        while face:
            bit = face & -face
            i = bit.bit_length() - 1
            result |= 1 << vm[i]
            face ^= bit
        return result

    # Four translations generate the even-weight translations; four adjacent
    # swaps generate the five-coordinate permutation group.
    generators = []
    for k in range(1, 5):
        delta = (1 << 0) | (1 << k)
        generators.append(tuple(vertex_index[v ^ delta] for v in vertices))
    for k in range(4):
        p = list(range(5))
        p[k], p[k + 1] = p[k + 1], p[k]
        generators.append(tuple(vertex_index[moved(v, p)] for v in vertices))
    assert len(generators) == 8 and all(g in all_maps for g in generators)
    image_maps = [{f: face_image(f, g) for f in faces} for g in generators]
    assert all(set(im.values()) == face_set for im in image_maps)

    @lru_cache(maxsize=None)
    def ending_at(top):
        output = [(top,)]
        sub = (top - 1) & top
        while sub:
            output.extend(prefix + (top,) for prefix in ending_at(sub))
            sub = (sub - 1) & top
        return tuple(output)

    flags = tuple(flag for top in faces for flag in ending_at(top))
    assert len(flags) == 19992 and len(set(flags)) == len(flags)
    lookup = {f: i for i, f in enumerate(flags)}
    orbit_numbers = [-1] * len(flags)
    representatives = []
    for i, flag in enumerate(flags):
        if orbit_numbers[i] >= 0:
            continue
        cell_id = len(representatives)
        representatives.append(flag)
        stack = [flag]
        orbit_numbers[i] = cell_id
        while stack:
            f = stack.pop()
            for im in image_maps:
                nxt = tuple(im[x] for x in f)
                index = lookup[nxt]
                if orbit_numbers[index] == -1:
                    orbit_numbers[index] = cell_id
                    stack.append(nxt)
    assert all(i >= 0 for i in orbit_numbers)
    assert len(representatives) == 39
    assert Counter(len(f) - 1 for f in representatives) == {0: 6, 1: 13, 2: 13, 3: 6, 4: 1}
    assert [[hex(x) for x in f] for f in representatives] == cert['cell_representatives']

    def face_orbit(flag):
        return orbit_numbers[lookup[flag]]

    boundary = [tuple(face_orbit(flag[:j] + flag[j + 1:])
                      for j in range(len(flag))) if len(flag) > 1 else ()
                for flag in representatives]
    # Each quotient cell has distinct proper codimension-one faces, because
    # deleting distinct chain positions leaves distinct face-rank signatures.
    assert all(len(set(ds)) == len(ds) for ds in boundary)
    assert all(len(representatives[j]) == len(representatives[i]) - 1
               for i, ds in enumerate(boundary) for j in ds)

    # Boundary^2=0 with induced flag ordering.
    for i, ds in enumerate(boundary):
        if len(ds) <= 1:
            continue
        terms = defaultdict(int)
        for k, face in enumerate(ds):
            for r, subface in enumerate(boundary[face]):
                terms[subface] += (-1) ** (k + r)
        assert not any(terms.values()), ('boundary squared', i, dict(terms))

    # For every elementary collapse, certify that the indicated face is
    # contained in exactly one remaining codimension-one coface. This gives
    # a genuine free-face pair in the finite regular quotient CW complex.
    active = set(range(len(representatives)))
    assert len(cert['collapse_pairs']) == 19
    for step, (face, coface) in enumerate(cert['collapse_pairs'], start=1):
        assert face in active and coface in active, ('inactive pair', step)
        assert face in boundary[coface], ('not incident', step)
        assert len(representatives[coface]) == len(representatives[face]) + 1
        containing = [c for c in active if face in boundary[c]]
        assert containing == [coface], ('not free', step, containing)
        # Check remaining active cells are closed under taking faces before
        # and after every deletion, so each is a legitimate elementary collapse.
        assert all(all(f in active for f in boundary[c]) for c in active)
        active.remove(face)
        active.remove(coface)
        assert all(all(f in active for f in boundary[c]) for c in active)
    assert active == {cert['survivor']}
    assert len(representatives[cert['survivor']]) == 1
    assert cert['raw_flags'] == len(flags)
    assert cert['cell_counts'] == {str(k): v for k, v in
                                   sorted(Counter(len(f)-1 for f in representatives).items())}
    print('CLEBSCH_FULL_SYMMETRY_QUOTIENT_19_COLLAPSES_PASS')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 verify_clebsch_quotient.py collapse_certificate.json')
    verify(sys.argv[1])
