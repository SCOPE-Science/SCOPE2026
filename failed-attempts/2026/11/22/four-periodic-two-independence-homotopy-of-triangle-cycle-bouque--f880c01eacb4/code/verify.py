#!/usr/bin/env python3
"""Reproducible finite checks for triangle-cycle two-independence complexes.
Requires Python 3 standard library only; see RESULT.md for the uniform proof.
"""
from collections import Counter, deque


def vertices_edges(n):
    assert n >= 3
    # 0,...,n-1 is the cycle; n,n+1 are two triangle vertices.
    edges = {(min(i, (i + 1) % n), max(i, (i + 1) % n)) for i in range(n)}
    edges.update(((0, n), (0, n + 1), (n, n + 1)))
    return n + 2, tuple(sorted(edges))


def admissible_faces(n):
    nv, edges = vertices_edges(n)
    neighbors = [0] * nv
    for u, v in edges:
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u
    # A subset has components with at most two vertices iff every
    # selected vertex has at most one selected neighbour.
    result = []
    for mask in range(1 << nv):
        if all(not ((mask >> v) & 1) or (mask & neighbors[v]).bit_count() <= 1
               for v in range(nv)):
            result.append(mask)
    return result


def toggle_in_family(family, vertex, pairs):
    bit = 1 << vertex
    unpaired = set(family)
    for f in sorted(family):
        if not (f & bit) and f in unpaired and (f | bit) in unpaired:
            pairs.append((f, f | bit))
            unpaired.remove(f)
            unpaired.remove(f | bit)
    return unpaired


def make_matching(n, faces):
    a, b = n, n + 1
    family = set(faces)
    pairs = []
    # First toggle vertex a in the entire augmented face poset.
    family = toggle_in_family(family, a, pairs)
    group = {'b':set(), 'left':set(), 'right':set()}
    for f in family:
        assert not(f & (1 << a)) and f & 1
        neighbours = [x for x in (b, 1, n - 1) if f & (1 << x)]
        assert len(neighbours) == 1, (n, f, neighbours)
        tag = 'b' if neighbours[0] == b else ('left' if neighbours[0] == 1 else 'right')
        group[tag].add(f)
    # The three residual fibers are disjoint shifted path 2-independence complexes.
    path = {
        'b': list(range(2, n - 1)),
        'left':list(range(3, n - 1)),
        'right':list(range(2, n - 2)),
    }
    if n == 3:
        path['left'] = []
        path['right'] = []
    critical = set()
    for tag in ('b', 'left', 'right'):
        fam = group[tag]
        for p in path[tag][::4]:
            fam = toggle_in_family(fam, p, pairs)
        critical.update(fam)
    assert len(pairs)*2 + len(critical) == len(faces)
    return pairs, critical


def acyclicity(n, faces, pairs):
    nv = n+2
    face_set = set(faces)
    upper = dict(pairs)
    in_degree = {f: 0 for f in faces}
    outgoing = {f: [] for f in faces}
    covers = 0
    for hi in faces:
        bits = hi
        while bits:
            bit = bits & -bits
            lo = hi ^ bit
            assert lo in face_set
            if upper.get(lo) == hi: u,v = lo, hi
            else: u,v = hi,lo
            outgoing[u].append(v)
            in_degree[v] += 1
            covers += 1
            bits -= bit
    queue = deque(f for f in faces if in_degree[f] == 0)
    count = 0
    while queue:
        f = queue.popleft()
        count += 1
        for v in outgoing[f]:
            in_degree[v]-=1
            if in_degree[v] == 0:
                queue.append(v)
    return count == len(faces), covers



def mod2_betti(n, faces):
    """Direct simplicial boundary ranks over F2, independent of Morse reduction."""
    levels = {}
    for face in faces:
        levels.setdefault(face.bit_count(), []).append(face)
    ranks = {0: 0}
    for size in sorted(levels):
        if size == 0:
            continue
        lows = levels.get(size - 1, [])
        if size == 1:
            ranks[size] = 1 if levels[size] else 0
            continue
        index = {face: i for i, face in enumerate(lows)}
        pivots = {}
        for hi in levels[size]:
            col = 0
            bits = hi
            while bits:
                bit = bits & -bits
                col ^= 1 << index[hi ^ bit]
                bits -= bit
            while col:
                lead = col.bit_length()-1
                if lead not in pivots:
                    pivots[lead] = col
                    break
                col ^= pivots[lead]
        ranks[size] = len(pivots)
    out = {}
    for size in sorted(levels):
        if size == 0:continue
        b = len(levels[size]) - ranks.get(size,0) - ranks.get(size+1,0)
        assert b >= 0
        if b:out[size-1] = b
    return out


def prediction(n):
    k,r=divmod(n,4)
    if r == 3:return (2*k+1,3)
    if r == 0:return (2*k-1,2)
    if r == 1:return None
    return (2*k+1,1)


def run(n_lo=3, n_hi=16):
    assert 3 <= n_lo <= n_hi
    for n in range(n_lo, n_hi+1):
        faces = admissible_faces(n)
        pairs, critical = make_matching(n, faces)
        # Independently generate the matching by a single global sequence of
        # element toggles. This checks that the three-fiber description
        # reproduces the ordinary sequential construction, not only counts.
        remaining = set(faces)
        other_pairs = []
        for vertex in [n] + list(range(n)) + [n + 1]:
            remaining = toggle_in_family(remaining, vertex, other_pairs)
        assert set(other_pairs) == set(pairs) and remaining == critical, n
        cnt = Counter(f.bit_count()-1 for f in critical)
        pred=prediction(n)
        assert cnt == (Counter({pred[0]:pred[1]}) if pred else Counter()), (n,cnt,pred)
        # Small-instance homology check uses the original simplicial
        # differentials, not the constructed matching.
        if n <= 10:
            independent_betti = mod2_betti(n, faces)
            assert independent_betti == ({pred[0]: pred[1]} if pred else {}), n
        acyclic, cover_count = acyclicity(n, faces, pairs)
        assert acyclic, n
        euler = sum((-1)**(f.bit_count()-1) for f in faces if f) - 1
        assert euler == (pred[1]*((-1)**pred[0]) if pred else 0)
        print(f'n={n}: faces_with_empty={len(faces)}; pairs={len(pairs)}; '
              f'covers={cover_count}; critical={sorted(cnt.items())}; '
              f'acyclic=yes; pivot_methods_agree=yes; reduced_euler={euler}; '
              f'mod2_chain_check={"yes" if n <= 10 else "not_run"}')
    print('PASS: exhaustive checks of each claimed finite instance')

if __name__ == '__main__':
    run()
