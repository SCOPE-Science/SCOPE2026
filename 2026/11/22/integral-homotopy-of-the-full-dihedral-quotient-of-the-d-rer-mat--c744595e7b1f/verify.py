#!/usr/bin/env python3
"""Exact chain and fundamental-group verification for a matching-complex orbit space.

Requires only the Python standard library. Rebuilds all cells from graph definitions.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations


def graph_and_symmetry():
    n = 6
    edge_set = set()
    def add(u, v):
        edge_set.add(tuple(sorted((u, v))))
    for i in range(n):
        add(i, (i + 1) % n)
        add(i, n + i)
        add(n + i, n + (i + 2) % n)
    edges = sorted(edge_set)
    assert len(edges) == 18
    index = {e: j for j, e in enumerate(edges)}
    transforms = []
    for sign in (1, -1):
        for shift in range(n):
            def vertex(v):
                return (v // n) * n + (sign * (v % n) + shift) % n
            p = tuple(index[tuple(sorted((vertex(u), vertex(v))))]
                      for u, v in edges)
            assert len(set(p)) == 18
            transforms.append(p)
    assert len(set(transforms)) == 12
    # The six inner vertices are exactly those participating in triangles.
    triangles = [set((a, b, c)) for a, b, c in combinations(range(12), 3)
                 if all(tuple(sorted(e)) in edge_set
                        for e in ((a, b), (b, c), (a, c)))]
    assert triangles == [{6, 8, 10}, {7, 9, 11}]
    return edges, transforms


def matching_faces(edges):
    faces = {}
    for k in range(1, 7):
        for combo in combinations(range(18), k):
            if len({v for i in combo for v in edges[i]}) == 2 * k:
                faces[sum(1 << i for i in combo)] = k
    assert Counter(k-1 for k in faces.values()) == {
        0: 18, 1: 117, 2: 334, 3: 402, 4: 156, 5: 10}
    return faces


def fundamental_group_is_trivial(edges, faces):
    # Fundamental group presentation of the 2-skeleton, using a maximal tree.
    V = sorted(f for f in faces if faces[f] == 1)
    assert len(V) == 18
    simplices = {k: [] for k in (2, 3)}
    for f, k in faces.items():
        if k in simplices:
            simplices[k].append(tuple(i for i in range(18) if f >> i & 1))
    edge_pairs = sorted(simplices[2])
    parent = list(range(18))
    def root(i):
        while i != parent[i]:
            i = parent[i]
        return i
    tree = set()
    for u, v in edge_pairs:
        a, b = root(u), root(v)
        if a != b:
            parent[a] = b
            tree.add((u, v))
    assert len(tree) == 17
    gens = {e: i+1 for i, e in enumerate(e for e in edge_pairs if e not in tree)}
    assert len(gens) == 100
    def word_edge(u, v):
        g = gens.get(tuple(sorted((u, v))), 0)
        return [] if not g else [g if u < v else -g]
    def reduced(w):
        st = []
        for x in w:
            if st and st[-1] == -x:
                st.pop()
            else:
                st.append(x)
        return st
    rels = [reduced(word_edge(a,b)+word_edge(b,c)+word_edge(c,a))
            for a,b,c in simplices[3]]
    remaining = set(gens.values())
    eliminated = 0
    while remaining:
        pivot = None
        for ridx, word in enumerate(rels):
            for pos, x in enumerate(word):
                if abs(x) in remaining and sum(abs(z)==abs(x) for z in word)==1:
                    pivot = ridx, pos, x
                    break
            if pivot:
                break
        assert pivot is not None, 'uneliminated fundamental group generators'
        ridx, pos, letter = pivot
        rel = rels[ridx]
        # A (signed generator) B = 1, hence signed generator = A^-1 B^-1.
        a, b = rel[:pos], rel[pos+1:]
        replacement = reduced([-x for x in a[::-1]] + [-x for x in b[::-1]])
        if letter < 0:
            replacement = [-x for x in replacement[::-1]]
        g = abs(letter)
        for i, word in enumerate(rels):
            if i == ridx:
                continue
            expanded = []
            for x in word:
                if abs(x) == g:
                    expanded.extend(replacement if x > 0 else [-y for y in replacement[::-1]])
                else:
                    expanded.append(x)
            rels[i] = reduced(expanded)
        rels[ridx] = []
        remaining.remove(g)
        eliminated += 1
    assert eliminated == 100 and all(not r for r in rels)
    return eliminated


def orbit_flag_cells(faces, transforms):
    end = {}
    flags = []
    for f in sorted(faces, key=lambda x: (faces[x], x)):
        fs = [(f,)]
        sub = (f - 1) & f
        while sub:
            if sub in end:
                fs.extend(w+(f,) for w in end[sub])
            sub = (sub - 1) & f
        end[f] = fs
        flags.extend(fs)
    assert len(flags) == 166087
    actions = [{f: sum(1 << p[i] for i in range(18) if f >> i & 1)
                for f in faces} for p in transforms]
    orbit = {}
    cells = []
    for flag in flags:
        if flag in orbit:
            continue
        idx = len(cells)
        cells.append(flag)
        for action in actions:
            moved = tuple(action[f] for f in flag)
            if moved in orbit:
                assert orbit[moved] == idx
            orbit[moved] = idx
    assert len(cells) == 14313
    assert Counter(len(f)-1 for f in cells) == {
        0: 117, 1: 1219, 2: 3949, 3: 5338, 4: 3090, 5: 600}
    bounds, upper = [], defaultdict(set)
    for cid, flag in enumerate(cells):
        bd = []
        if len(flag) > 1:
            for j in range(len(flag)):
                subflag = flag[:j] + flag[j+1:]
                fid = orbit[subflag]
                assert fid not in bd
                bd.append(fid)
                upper[fid].add(cid)
        bounds.append(bd)
    return cells, bounds, upper


def collapse(cells, boundary, upper):
    alive = bytearray([1]) * len(cells)
    upper = {i: set(v) for i, v in upper.items()}
    queue = deque(i for i in range(len(cells)) if len(upper.get(i, ())) == 1)
    count = 0
    while queue:
        a = queue.popleft()
        if not alive[a] or len(upper.get(a, ())) != 1:
            continue
        b = next(iter(upper[a]))
        assert alive[b] and len(cells[b]) == len(cells[a])+1
        # A free face has no other (not necessarily immediate) coface.
        assert not upper.get(b, ())
        for c in (a, b):
            for f in boundary[c]:
                upper[f].discard(c)
                if len(upper[f]) == 1:
                    queue.append(f)
            alive[c] = 0
        count += 1
    remaining = {i for i, a in enumerate(alive) if a}
    assert count == 6411 and len(remaining) == 1491
    assert Counter(len(cells[i])-1 for i in remaining) == {
        0: 68, 1: 396, 2: 677, 3: 350}
    return remaining


def quotient_pi1_is_trivial(cells, boundary, alive):
    """Tietze-eliminate a maximal-tree presentation of the quotient 2-skeleton."""
    vertices = sorted(c for c in alive if len(cells[c]) == 1)
    edges = sorted(c for c in alive if len(cells[c]) == 2)
    triangles = sorted(c for c in alive if len(cells[c]) == 3)
    assert (len(vertices), len(edges), len(triangles)) == (68, 396, 677)
    parent = {v: v for v in vertices}
    def root(i):
        while i != parent[i]:
            i = parent[i]
        return i
    tree = set()
    for e in edges:
        v, w = boundary[e]
        assert v in alive and w in alive
        a, b = root(v), root(w)
        if a != b:
            parent[a] = b
            tree.add(e)
    assert len(tree) == len(vertices) - 1
    gens = {e: i+1 for i, e in enumerate(e for e in edges if e not in tree)}
    assert len(gens) == 329
    def reduced(word):
        stack = []
        for x in word:
            if stack and stack[-1] == -x:
                stack.pop()
            else:
                stack.append(x)
        return stack
    rels = []
    for t in triangles:
        # Boundary of (low,mid,high): +(mid,high) -(low,high) +(low,mid)
        upper, long, lower = boundary[t]
        rels.append([g for g in (gens.get(lower,0),gens.get(upper,0),
                                 -gens.get(long,0)) if g])
    remaining = set(gens.values())
    eliminated = 0
    while remaining:
        pivot = None
        for ridx, word in enumerate(rels):
            for j, letter in enumerate(word):
                if abs(letter) in remaining and sum(abs(x)==abs(letter) for x in word)==1:
                    pivot = ridx, j, letter
                    break
            if pivot:
                break
        assert pivot is not None, 'residual quotient pi1 presentation'
        ridx, j, letter = pivot
        word = rels[ridx]
        lhs, rhs = word[:j], word[j+1:]
        replacement = reduced([-x for x in lhs[::-1]]+[-x for x in rhs[::-1]])
        if letter < 0:
            replacement = [-x for x in replacement[::-1]]
        for k, old in enumerate(rels):
            if k == ridx:
                continue
            expanded = []
            for x in old:
                if abs(x) == abs(letter):
                    expanded.extend(replacement if x > 0 else [-y for y in replacement[::-1]])
                else:
                    expanded.append(x)
            rels[k] = reduced(expanded)
        rels[ridx] = []
        remaining.remove(abs(letter))
        eliminated += 1
    assert eliminated == 329 and all(not r for r in rels)
    return eliminated


def unit_reduce(cells, boundary, alive):
    cols = {}
    for c in alive:
        if len(cells[c]) > 1:
            cols[c] = {a: (-1)**j for j, a in enumerate(boundary[c]) if a in alive}
    def assert_square_zero():
        for c in alive:
            if len(cells[c]) <= 2:
                continue
            total = Counter()
            for a, coeff in cols[c].items():
                for i, coeff2 in cols[a].items():
                    total[i] += coeff * coeff2
            assert not any(total.values()), c
    assert_square_zero()
    count = Counter()
    for d in range(1, 6):
        while True:
            pivot = next(((a, b, v)
                for b in sorted(alive) if len(cells[b]) == d+1
                for a, v in cols[b].items() if a in alive and abs(v)==1), None)
            if pivot is None:
                break
            a, b, v = pivot
            for c in list(cols):
                if c not in alive or c in (a, b) or len(cells[c]) != d+1:
                    continue
                factor = cols[c].get(a, 0)*v
                if factor == 0:
                    continue
                for i, w in cols[b].items():
                    new = cols[c].get(i, 0) - factor*w
                    if new:
                        cols[c][i] = new
                    else:
                        cols[c].pop(i, None)
            for c in list(cols):
                if c in alive and c not in (a, b) and len(cells[c]) == d+2:
                    cols[c].pop(b, None)
            cols.pop(a, None)
            cols.pop(b, None)
            alive.remove(a)
            alive.remove(b)
            count[d] += 1
    assert_square_zero()
    assert count == {1:67, 2:329, 3:348}
    assert Counter(len(cells[i])-1 for i in alive) == {0:1, 3:2}
    assert all(not cols.get(i) for i in alive)
    return count


def main():
    edges, transformations = graph_and_symmetry()
    faces = matching_faces(edges)
    tree_elims = fundamental_group_is_trivial(edges, faces)
    cells, boundary, cofaces = orbit_flag_cells(faces, transformations)
    active = collapse(cells, boundary, cofaces)
    quotient_elims = quotient_pi1_is_trivial(cells, boundary, active)
    reductions = unit_reduce(cells, boundary, active)
    print('graph_edges=18 matching_faces=1037 orbit_cells=14313')
    print('original_pi1_generator_eliminations=' + str(tree_elims))
    print('quotient_pi1_generator_eliminations=' + str(quotient_elims))
    print('elementary_collapse_pairs=6411 integral_unit_pairs=' + str(sum(reductions.values())))
    print('homology_Z_in_degree_0_and_Z2_in_degree_3_no_other_homology')
    print('DURER_DIHEDRAL_ORBIT_HOMOTOPY_OK')


if __name__ == '__main__':
    main()
