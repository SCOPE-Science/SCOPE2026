#!/usr/bin/env python3
"""Exact six-letter matching-complex fixed-locus census; Python 3 standard library."""
import csv
import itertools
import os
import sys
from array import array
from collections import Counter

N = 6
PERMS = tuple(itertools.permutations(range(N)))
PID = {p: i for i, p in enumerate(PERMS)}
IDENTITY = PID[tuple(range(N))]
SIZE = len(PERMS)
EDGES = tuple(itertools.combinations(range(N), 2))
EDGE_ID = {e: i for i, e in enumerate(EDGES)}


def multiplication():
    rows = []
    for p in PERMS:
        rows.append(array('H', (PID[tuple(p[q[i]] for i in range(N))]
                                for q in PERMS)))
    inverse = [None] * SIZE
    for i in range(SIZE):
        for j, element in enumerate(rows[i]):
            if element == IDENTITY:
                inverse[i] = j
                break
        assert inverse[i] is not None
    return rows, inverse


def subgroup(generators, mul):
    reached = {IDENTITY}
    queue = [IDENTITY]
    for x in queue:
        for generator in generators:
            y = mul[x][generator]
            if y not in reached:
                reached.add(y)
                queue.append(y)
    return frozenset(reached)


def group_classes(mul, inv):
    representatives = [(frozenset((IDENTITY,)), ())]
    classes = {representatives[0][0]: 0}
    pos = 0
    while pos < len(representatives):
        old_subgroup, old_generators = representatives[pos]
        for x in range(SIZE):
            if x in old_subgroup:
                continue
            gens = old_generators + (x,)
            new_group = subgroup(gens, mul)
            if new_group in classes:
                continue
            class_number = len(representatives)
            for c in range(SIZE):
                inverse_c = inv[c]
                conjugate = frozenset(mul[mul[c][h]][inverse_c]
                                      for h in new_group)
                if conjugate in classes:
                    assert classes[conjugate] == class_number
                classes[conjugate] = class_number
            representatives.append((new_group, gens))
        pos += 1
    assert pos == len(representatives)
    assert len(classes) == 1455 and len(representatives) == 56
    return representatives, classes


def normalizer_order(H, gens, mul, inv):
    count = 0
    for c in range(SIZE):
        # Conjugation preserving all generators and group order preserves H.
        if all(mul[mul[c][x]][inv[c]] in H for x in gens):
            count += 1
    assert SIZE % count == 0
    return count


def fixed_orbit_complex(H, ep):
    available = set(range(len(EDGES)))
    admitted = []
    while available:
        e = min(available)
        orbit = frozenset(ep[g][e] for g in H)
        assert orbit <= available
        available.difference_update(orbit)
        endpoints = [v for z in orbit for v in EDGES[z]]
        if len(endpoints) == len(set(endpoints)):
            admitted.append(tuple(sorted(orbit)))
    # The realization of the orbit complex is precisely the geometric H-fixed set.
    use = [frozenset(v for e in orbit for v in EDGES[e]) for orbit in admitted]
    faces = set()
    for k in range(1, len(use) + 1):
        for comb in itertools.combinations(range(len(use)), k):
            if len(frozenset.union(*(use[i] for i in comb))) == sum(len(use[i]) for i in comb):
                faces.add(frozenset(comb))
    return admitted, faces


def key(face):
    return tuple(sorted(face))


def encode_face(face):
    return '.'.join(map(str, key(face)))


def decode_face(s):
    assert s
    return frozenset(int(v) for v in s.split('.'))


def facets(faces):
    return [f for f in faces if not any(f < g for g in faces)]


def free_pairs(faces):
    fs = facets(faces)
    pairs = []
    for f in fs:
        for v in sorted(f):
            q = f - {v}
            if q and q in faces and sum(q <= g for g in fs) == 1:
                pairs.append((f, q))
    return sorted(pairs, key=lambda z: (-len(z[0]), key(z[0]), key(z[1])))


def collapse(faces):
    current = set(faces)
    steps = []
    while True:
        choices = free_pairs(current)
        if not choices:
            break
        f, q = choices[0]
        assert f in current and q in current
        current.remove(f)
        current.remove(q)
        steps.append((f, q))
    return steps, current


def components(faces):
    vs = {next(iter(f)) for f in faces if len(f) == 1}
    adj = {v: set() for v in vs}
    for f in faces:
        if len(f) == 2:
            a, b = tuple(f)
            adj[a].add(b)
            adj[b].add(a)
    n = 0
    while vs:
        n += 1
        stack = [vs.pop()]
        while stack:
            for neighbor in adj[stack.pop()]:
                if neighbor in vs:
                    vs.remove(neighbor)
                    stack.append(neighbor)
    return n


def classify(faces):
    steps, rest = collapse(faces)
    v = sum(len(f) == 1 for f in rest)
    e = sum(len(f) == 2 for f in rest)
    t = sum(len(f) == 3 for f in rest)
    assert not any(len(f) > 3 for f in rest)
    c = components(rest)
    if (v, e, t, c) == (0, 0, 0, 0):
        name = 'empty'
    elif e == 0 and t == 0 and c == v == 3:
        name = 'three_points'
    elif (v, e, t, c) == (1, 0, 0, 1):
        name = 'contractible'
    elif (v, e, t, c) == (15, 30, 0, 1):
        name = 'wedge_16_circles'
    else:
        raise AssertionError(('unclassified', (v,e,t,c), rest))
    return name, steps, rest



def independent_barycentric_invariants(H, ep):
    """Compute fixed-locus Euler/component data from invariant faces, not edge-orbits."""
    original_faces = []
    for k in (1, 2, 3):
        for seq in itertools.combinations(range(len(EDGES)), k):
            endpoints = [v for z in seq for v in EDGES[z]]
            if len(endpoints) == len(set(endpoints)):
                original_faces.append(frozenset(seq))
    assert len(original_faces) == 75
    fixed_faces = [f for f in original_faces if all(
        frozenset(ep[g][v] for v in f) == f for g in H)]
    comparable_pairs = [(i, j) for i in range(len(fixed_faces))
                        for j in range(i+1, len(fixed_faces))
                        if fixed_faces[i] < fixed_faces[j] or fixed_faces[j] < fixed_faces[i]]
    triples = sum(1 for i in range(len(fixed_faces))
                  for j in range(len(fixed_faces))
                  for k in range(len(fixed_faces))
                  if fixed_faces[i] < fixed_faces[j] < fixed_faces[k])
    chi = len(fixed_faces) - len(comparable_pairs) + triples
    parent = list(range(len(fixed_faces)))
    def root(a):
        while parent[a] != a:
            a = parent[a]
        return a
    for i,j in comparable_pairs:
        parent[root(i)] = root(j)
    comps = len({root(i) for i in range(len(fixed_faces))})
    return chi, comps

def census():
    mul, inv = multiplication()
    reps, all_subgroups = group_classes(mul, inv)
    ep = [[EDGE_ID[tuple(sorted((p[a], p[b])))] for a, b in EDGES]
          for p in PERMS]
    expected_data = []
    type_counts = Counter()
    seen_class_count = Counter(all_subgroups.values())
    for i, (H, gens) in enumerate(reps):
        assert len(H) * (SIZE // len(H)) == SIZE
        normalizer = normalizer_order(H, gens, mul, inv)
        assert seen_class_count[i] == SIZE // normalizer
        orbit, faces = fixed_orbit_complex(H, ep)
        name, pairs, rest = classify(faces)
        independently_expected = {
            'wedge_16_circles': (-15, 1),
            'contractible': (1, 1),
            'three_points': (3, 3),
            'empty': (0, 0),
        }
        assert independent_barycentric_invariants(H, ep) == independently_expected[name]
        if i == 0:
            assert len(orbit) == 15 and len(faces) == 75
        elif name == 'wedge_16_circles':
            raise AssertionError('ambient type for proper subgroup')
        type_counts[name] += seen_class_count[i]
        expected_data.append({
            'class_index': str(i),
            'group_order': str(len(H)),
            'conjugacy_count': str(seen_class_count[i]),
            'generators': ','.join(map(str, gens)),
            'orbit_edges': ';'.join('.'.join(map(str, z)) for z in orbit),
            'face_count': str(len(faces)),
            'homotopy_type': name,
            'collapse_pairs': ';'.join(encode_face(f)+'>'+encode_face(q) for f,q in pairs),
            'residual_faces': ';'.join(encode_face(f) for f in sorted(rest, key=lambda x:(len(x),key(x)))),
        })
    assert type_counts == {'wedge_16_circles': 1,
                            'contractible': 1140,
                            'three_points': 80,
                            'empty': 234}, type_counts
    assert sum(type_counts.values()) == 1455
    # Independent global check: redo orbit and Morse construction for every
    # labeled subgroup, not merely representatives. No class result is reused.
    all_counts = Counter()
    for H in all_subgroups:
        _, faces = fixed_orbit_complex(H, ep)
        category, _, _ = classify(faces)
        all_counts[category] += 1
    assert all_counts == type_counts
    return expected_data, type_counts


def check_certificate(rows, filename):
    with open(filename, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        actual = list(reader)
    assert actual == rows, 'Certificate differs from complete regenerated enumeration'
    # Replaying each recorded elementary collapse independently of choice policy.
    for r in actual:
        orb = [tuple(map(int, s.split('.'))) for s in r['orbit_edges'].split(';') if s]
        used = [frozenset(v for e in orbit for v in EDGES[e]) for orbit in orb]
        fs = set()
        for k in range(1, len(orb)+1):
            for ss in itertools.combinations(range(len(orb)), k):
                if len(frozenset.union(*(used[j] for j in ss))) == sum(map(len, (used[j] for j in ss))):
                    fs.add(frozenset(ss))
        for step in r['collapse_pairs'].split(';'):
            if not step:
                continue
            p, q = (decode_face(s) for s in step.split('>'))
            assert (p, q) in free_pairs(fs), 'Invalid elementary collapse'
            fs.remove(p)
            fs.remove(q)
        remaining = ';'.join(encode_face(f) for f in sorted(fs, key=lambda x: (len(x), key(x))))
        assert remaining == r['residual_faces']
    print('MATCHING_K6_SUBGROUP_FIXED_SPACE_CENSUS_PASS',
          'subgroups=1455', 'conjugacy_classes=56',
          'circles=1', 'contractible=1140', 'three_points=80', 'empty=234')


if __name__ == '__main__':
    rows, counts = census()
    columns = list(rows[0])
    if len(sys.argv) == 3 and sys.argv[1] == '--write-certificate':
        with open(sys.argv[2], 'w', encoding='utf-8', newline='') as fp:
            writer = csv.DictWriter(fp, fieldnames=columns, lineterminator='\n')
            writer.writeheader()
            writer.writerows(rows)
        check_certificate(rows, sys.argv[2])
    else:
        file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'm6_subgroup_census.csv')
        check_certificate(rows, file)
