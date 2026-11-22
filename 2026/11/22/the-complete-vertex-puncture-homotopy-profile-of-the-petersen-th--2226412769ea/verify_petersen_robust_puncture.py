"""Exhaustive finite proof checker for a Petersen robust-clique puncture.

Standard Python 3 only. All simplices and directed Hasse covers are reconstructed.
"""
from itertools import combinations
from collections import Counter, deque
import random

VERTICES = list(combinations(range(5), 2))
ADJ = [set(j for j, b in enumerate(VERTICES)
           if i != j and set(a).isdisjoint(b))
       for i, a in enumerate(VERTICES)]
assert len(VERTICES) == 10 and sum(map(len, ADJ)) == 30
assert all(i in ADJ[j] for i in range(10) for j in ADJ[i])

# A simplex has no independent triple in the Petersen graph.
FULL = set()
for size in range(1, 11):
    for s in combinations(range(10), size):
        if all(any(y in ADJ[x] for x, y in combinations(t, 2))
               for t in combinations(s, 3)):
            FULL.add(s)
assert all(tuple(x for x in face if x != v) in FULL
           for face in FULL for v in face if len(face) > 1)


def coreduction(faces):
    """Pair a cell with its sole remaining boundary cell, else mark critical.

    Choices are reproducible, not mathematical assumptions; acyclicity is
    checked independently on *every* full face-poset cover below.
    """
    rng = random.Random(0)
    active = set(faces)
    boundaries = {f: {f[:i] + f[i+1:] for i in range(len(f))
                      if len(f) > 1} for f in faces}
    coboundaries = {f: set() for f in faces}
    for f, boundary in boundaries.items():
        for g in boundary:
            assert g in faces
            coboundaries[g].add(f)
    boundary_count = {f: len(boundaries[f]) for f in faces}
    pairs, critical = [], []
    while active:
        available = [f for f in active if boundary_count[f] == 1]
        if available:
            smallest = min(map(len, available))
            upper = rng.choice(sorted(f for f in available if len(f) == smallest))
            lower = next(g for g in boundaries[upper] if g in active)
            removed = (upper, lower)
            pairs.append((lower, upper))
        else:
            smallest = min(map(len, active))
            face = rng.choice(sorted(f for f in active if len(f) == smallest))
            removed = (face,)
            critical.append(face)
        for f in removed:
            active.remove(f)
            for upper in coboundaries[f]:
                boundary_count[upper] -= 1
    return pairs, critical


def verify_acyclic(faces, pairs, critical):
    """Full Hasse DAG: match arrows up, all other arrows down."""
    assert len(faces) == 2*len(pairs) + len(critical)
    matched = {(lower, upper) for lower, upper in pairs}
    used = [f for p in pairs for f in p] + critical
    assert len(used) == len(faces) and set(used) == faces
    outgoing = {f: [] for f in faces}
    indeg = {f: 0 for f in faces}
    covers = 0
    for upper in faces:
        for i in range(len(upper)):
            if len(upper) < 2:
                continue
            lower = upper[:i] + upper[i+1:]
            assert lower in faces
            if (lower, upper) in matched:
                src, dst = lower, upper
            else:
                src, dst = upper, lower
            outgoing[src].append(dst)
            indeg[dst] += 1
            covers += 1
    queue = deque(f for f in faces if indeg[f] == 0)
    seen = 0
    while queue:
        face = queue.popleft()
        seen += 1
        for nxt in outgoing[face]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                queue.append(nxt)
    assert seen == len(faces), 'cycle in directed Hasse graph'
    return covers


def betti_mod2(faces):
    """Separate boundary rank computation over F2, using integer bitsets."""
    layers = {}
    for f in faces:
        layers.setdefault(len(f)-1, []).append(f)
    for k in layers:
        layers[k].sort()
    dims = range(max(layers)+1)
    ranks = {}
    for k in dims:
        if k == 0:
            ranks[k] = 0
            continue
        lower = {f:i for i, f in enumerate(layers[k-1])}
        pivot = {}
        for upper in layers[k]:
            bits = 0
            for j in range(len(upper)):
                bits ^= 1 << lower[upper[:j]+upper[j+1:]]
            while bits:
                p = bits.bit_length()-1
                if p in pivot:
                    bits ^= pivot[p]
                else:
                    pivot[p] = bits
                    break
        ranks[k] = len(pivot)
    return {k: len(layers[k]) - ranks[k] - ranks.get(k+1, 0) - (1 if k==0 else 0)
            for k in dims}


def check(name, faces, want_faces, want_pairs, want_critical, want_covers):
    assert len(faces) == want_faces
    pairs, critical = coreduction(faces)
    assert len(pairs) == want_pairs
    assert dict(Counter(len(f)-1 for f in critical)) == want_critical
    covers = verify_acyclic(faces, pairs, critical)
    assert covers == want_covers, (name, covers, want_covers)
    betti = {d:b for d,b in betti_mod2(faces).items() if b}
    expected = {d:m for d,m in want_critical.items() if d>0}
    assert betti == expected, (name, betti, expected)
    print(f'{name}: faces={len(faces)} pairs={len(pairs)} covers={covers} '
          f'critical={dict(sorted(want_critical.items()))} mod2_betti={betti}')


# Vertex-transitivity follows from the S5 action on unordered pairs.
DELETE = {face for face in FULL if 0 not in face}
LINK = {tuple(x for x in face if x != 0) for face in FULL
        if 0 in face and len(face) > 1}
assert len(FULL) == len(DELETE) + len(LINK) + 1
assert all(f in DELETE for f in LINK)

if __name__ == '__main__':
    # Hasse-cover constants are checked against independently rebuilt covers.
    check('full', FULL, 232, 111, {0:1, 3:9}, 720)
    check('deletion', DELETE, 159, 77, {0:1, 3:4}, 471)
    check('link', LINK, 72, 33, {0:1, 2:5}, 168)
    print('PETERSEN_ROBUST_PUNCTURE_VERIFY_OK')
