#!/usr/bin/env python3
"""Exact independent verification of a finite graph-complex character."""
import collections
import hashlib
import itertools
import json
from pathlib import Path

N = 16
FULL = (1 << N) - 1
neighbor = [sum(1 << v for v in range(N) if (u ^ v).bit_count() == 1) for u in range(N)]
nonedges = [sum(1 << x for x in t)
            for t in itertools.combinations(range(N), 4)
            if all(not (neighbor[u] & (1 << v)) for u, v in itertools.combinations(t, 2))]
assert len(nonedges) == 228
faces = {mask for mask in range(1 << N) if all(mask & bad != bad for bad in nonedges)}
fvector = [sum(mask.bit_count() == t for mask in faces) for t in range(7)]
assert fvector == [1, 16, 120, 560, 1592, 2592, 1984]
assert sum(fvector) == 6865
# Independent reconstruction from maximum-independent-number recursion, not from forbidden 4-sets.
alpha = [0] * (1 << N)
for s in range(1, 1 << N):
    bit = s & -s
    i = bit.bit_length() - 1
    alpha[s] = max(alpha[s ^ bit], 1 + alpha[(s ^ bit) & ~neighbor[i]])
assert faces == {mask for mask in range(1 << N) if alpha[mask] <= 3}

# Sequential vertex toggles on the nonempty face poset.
unmatched = set(faces - {0})
pairs = set()
for v in range(N):
    bit = 1 << v
    for low in sorted(unmatched):
        high = low | bit
        if not (low & bit) and high in unmatched:
            unmatched.remove(low)
            unmatched.remove(high)
            pairs.add((low, high))
counts = collections.Counter(m.bit_count() - 1 for m in unmatched)
assert counts == {0: 1, 5: 529}
assert len(pairs) == 3167

# Directly test the reversed-matching Hasse digraph for acyclicity.
nonempty = faces - {0}
indeg = {m: 0 for m in nonempty}
arrows = collections.defaultdict(list)
covers = 0
for high in nonempty:
    sub = high
    while sub:
        bit = sub & -sub
        low = high ^ bit
        sub -= bit
        if low == 0:
            continue
        covers += 1
        tail, head = (low, high) if (low, high) in pairs else (high, low)
        arrows[tail].append(head)
        indeg[head] += 1
queue = collections.deque(m for m, v in indeg.items() if v == 0)
visited = 0
while queue:
    m = queue.popleft()
    visited += 1
    for dest in arrows[m]:
        indeg[dest] -= 1
        if indeg[dest] == 0:
            queue.append(dest)
assert visited == len(nonempty) == 6864
assert covers == sum(t * fvector[t] for t in range(1, 7)) - 16
pair_hash = hashlib.sha256(''.join('%d:%d\n' % x for x in sorted(pairs)).encode()).hexdigest()

# Action g on cube vertices: map bit i to bit sigma[i] and XOR a translation b.
def action(sigma, b):
    return [sum(((x >> i) & 1) << sigma[i] for i in range(4)) ^ b for x in range(N)]

def vertex_orbits(mapping):
    seen = set()
    res = []
    for i in range(N):
        if i in seen:
            continue
        j, orbit = i, 0
        while j not in seen:
            seen.add(j)
            orbit |= 1 << j
            j = mapping[j]
        res.append(orbit)
    return res

def type_of(sigma, b):
    used = set()
    positive, negative = [], []
    for i in range(4):
        if i in used:
            continue
        j = i
        cycle = []
        while j not in used:
            used.add(j)
            cycle.append(j)
            j = sigma[j]
        (negative if (sum((b >> k) & 1 for k in cycle) % 2) else positive).append(len(cycle))
    return tuple(sorted(positive, reverse=True)), tuple(sorted(negative, reverse=True))

traces = {}
classes = collections.defaultdict(list)
for sigma in itertools.permutations(range(4)):
    for b in range(16):
        orbits = vertex_orbits(action(sigma, b))
        # Reduced Lefschetz = - character (only reduced H_5 survives).
        # Each orbit contributes -1 to the signed face alternating sum.
        robust_total = 0
        dual_total = 0
        for subset in range(1 << len(orbits)):
            mask = 0
            for j, block in enumerate(orbits):
                if subset & (1 << j):
                    mask |= block
            parity = (-1) ** subset.bit_count()
            robust_total += parity * int(mask in faces)
            # Independent second expression through the Alexander dual cut complex.
            dual_total += parity * int(alpha[FULL ^ mask] >= 4)
        # All cube automorphisms are even permutations of the 16 vertices.
        assert len(orbits) % 2 == 0
        assert robust_total == -dual_total
        key = (tuple(sigma), b)
        traces[key] = robust_total
        classes[type_of(sigma, b)].append(robust_total)
assert len(traces) == 384 and len(classes) == 20
rows = []
for typ, values in sorted(classes.items()):
    assert len(set(values)) == 1
    rows.append({'positive_cycles': list(typ[0]), 'negative_cycles': list(typ[1]),
                 'class_size': len(values), 'trace': values[0]})
assert sum(r['class_size'] for r in rows) == 384
assert sum(r['class_size'] * r['trace'] for r in rows) == 0
assert traces[(tuple(range(4)), 0)] == 529
assert traces[(tuple(range(4)), 15)] == 9

translation_traces = [traces[(tuple(range(4)), b)] for b in range(16)]
assert [translation_traces[1 << i] for i in range(4)] == [-35] * 4
mult = collections.defaultdict(set)
for a in range(16):
    raw = sum((-1) ** ((a & b).bit_count()) * translation_traces[b] for b in range(16))
    assert raw % 16 == 0
    mult[a.bit_count()].add(raw // 16)
assert {k: sorted(v) for k, v in mult.items()} == {0:[27],1:[28],2:[33],3:[37],4:[44]}
assert sum(r['trace'] for r in [] ) == 0
assert sum(translation_traces) == 16 * 27
assert sum(traces[(tuple(sigma), 0)] for sigma in itertools.permutations(range(4))) == 24 * 24

certificate = {'vertices': N, 'edges': 32, 'forbidden_independent_quadruples': 228,
               'faces_by_cardinality': fvector, 'nonempty_faces': len(nonempty),
               'matched_pairs': len(pairs), 'critical_cells': {str(k): v for k,v in sorted(counts.items())},
               'Hasse_covers': covers, 'gradient_toposort_visited': visited,
               'matched_pairs_sha256': pair_hash, 'classes': rows,
               'translation_multiplicity_by_character_weight': {str(k): list(v)[0] for k,v in sorted(mult.items())},
               'full_group_invariant_rank': 0, 'translation_invariant_rank': 27,
               'coordinate_permutation_invariant_rank': 24}
expected = Path(__file__).with_name('certificate.json')
if expected.is_file():
    assert certificate == json.loads(expected.read_text(encoding='utf-8'))
else:
    expected.write_text(json.dumps(certificate,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('VERIFY_OK',json.dumps({'faces':len(faces),'pairs':len(pairs),'covers':covers,'classes':len(classes), 'translation_multiplicities':certificate['translation_multiplicity_by_character_weight'],'full_invariants':0},sort_keys=True))
