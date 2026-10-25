"""Independent finite Morse and chain checks for the ordinary independence complex."""
from collections import Counter, defaultdict, deque

N = 11
ORDER = (1, 4, 5, 2, 0, 6, 8, 7, 9, 10, 3)

def face_sets():
    adj = [0] * N
    def add(a, b):
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    for i in range(5):
        add(i, (i + 1) % 5)
        add(5 + i, (i + 1) % 5)
        add(5 + i, (i - 1) % 5)
        add(10, 5 + i)
    faces = {mask for mask in range(1, 1 << N)
             if all(not (mask & adj[v]) for v in range(N)
                    if mask & (1 << v))}
    two = {mask for mask in range(1, 1 << N)
           if all((mask & adj[v]).bit_count() <= 1 for v in range(N)
                  if mask & (1 << v))}
    return faces, two


def toggle_matching(faces):
    # Each pair differs by the insertion of a vertex from the stated order.
    remaining = set(faces)
    pairs = []
    for v in ORDER:
        for f in sorted(faces):
            g = f | (1 << v)
            if f in remaining and not (f & (1 << v)) and g in remaining:
                remaining.remove(f)
                remaining.remove(g)
                pairs.append((f, g))
    return pairs, remaining


def check_acyclic(faces, pairs):
    paired = set(pairs)
    out = defaultdict(list)
    indeg = {f: 0 for f in faces}
    covers = 0
    for upper in faces:
        for v in range(N):
            if upper & (1 << v):
                lower = upper ^ (1 << v)
                if lower == 0:
                    continue
                assert lower in faces
                # Matched incidence is oriented upward, all other incidences downward.
                src, dst = (lower, upper) if (lower, upper) in paired else (upper, lower)
                out[src].append(dst)
                indeg[dst] += 1
                covers += 1
    q = deque(f for f, d in indeg.items() if d == 0)
    visited = 0
    while q:
        f = q.popleft()
        visited += 1
        for g in out[f]:
            indeg[g] -= 1
            if indeg[g] == 0:
                q.append(g)
    assert visited == len(faces), (visited, len(faces))
    return covers


def boundary_ranks_mod2(faces):
    bydim = defaultdict(list)
    for f in faces:
        bydim[f.bit_count() - 1].append(f)
    ranks = {}
    for d in range(1, max(bydim) + 1):
        lows = {f: i for i, f in enumerate(sorted(bydim[d - 1]))}
        pivots = {}
        for upper in sorted(bydim[d]):
            column = 0
            for v in range(N):
                if upper & (1 << v):
                    column ^= 1 << lows[upper ^ (1 << v)]
            while column:
                i = column.bit_length() - 1
                if i not in pivots:
                    pivots[i] = column
                    break
                column ^= pivots[i]
        ranks[d] = len(pivots)
    counts = {d: len(bydim[d]) for d in bydim}
    homology = {d: counts[d] - ranks.get(d, 0) - ranks.get(d + 1, 0)
                for d in counts}
    return counts, ranks, homology


def main():
    ordinary, two = face_sets()
    assert len(ordinary) == 102 and len(two) == 312
    pairs, critical = toggle_matching(ordinary)
    assert len(pairs) == 50
    assert critical == {2, 1033}, critical
    covers = check_acyclic(ordinary, pairs)
    assert covers > 0
    counts, ranks, b = boundary_ranks_mod2(ordinary)
    counts2, ranks2, b2 = boundary_ranks_mod2(two)
    assert counts == {0: 11, 1: 35, 2: 40, 3: 15, 4: 1}
    assert counts2 == {0: 11, 1: 55, 2: 110, 3: 95, 4: 36, 5: 5}
    assert {d: v for d, v in b.items() if d > 0 and v} == {2: 1}
    assert {d: v for d, v in b2.items() if d > 0 and v} == {2: 1}
    print('ordinary independence: 102 nonempty faces; 50 matching pairs')
    print(f'acyclic complete Hasse orientation: {covers} cover relations')
    print('critical masks: [2] (vertex), [1033] (2-cell)')
    print('Morse CW type: one 0-cell, one 2-cell, hence S^2')
    print('independent mod-2 reduced homology: rank 1 in degree 2 for both complexes')
    print('ordinary homotopy and homology cross-check: VERIFIED')

if __name__ == '__main__':
    main()
