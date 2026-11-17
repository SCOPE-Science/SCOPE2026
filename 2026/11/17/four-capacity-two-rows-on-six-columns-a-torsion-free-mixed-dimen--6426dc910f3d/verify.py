#!/usr/bin/env python3
"""Exact finite certificate for the four-row, six-column capacity-two multiple chessboard complex.
Usage: python verify.py (requires sympy >= 1.12). No network access or input files required.
"""
from collections import Counter, defaultdict, deque
from itertools import product
from sympy import ZZ, zeros
from sympy.matrices.normalforms import smith_normal_form

ROWS, COLS, CAP = 4, 6, 2
PIVOTS = (11, 13, 0, 1, 15, 3, 6, 5, 20, 9, 12, 8, 21, 16, 4, 22, 10, 14, 18, 19, 23, 17, 2, 7)


def faces():
    layers = defaultdict(set)
    for a in product(range(ROWS + 1), repeat=COLS):
        counts = [0] * ROWS
        mask = 0
        for j, x in enumerate(a):
            if x:
                counts[x - 1] += 1
                if counts[x - 1] > CAP:
                    break
                mask |= 1 << (j * ROWS + x - 1)
        else:
            layers[mask.bit_count()].add(mask)
    return {k: tuple(sorted(v)) for k, v in layers.items()}


def boundary(mask):
    ans = {}
    x, i = mask, 0
    while x:
        bit = x & -x
        x -= bit
        ans[mask ^ bit] = 1 if not (i % 2) else -1
        i += 1
    return ans


def make_matching(F):
    # Sequential elementary pivot matchings, except for the empty face.
    remaining = set().union(*[set(v) for v in F.values()]) - {0}
    matched = {}
    for v in PIVOTS:
        b = 1 << v
        for x in sorted(remaining):
            if not (x & b) and x | b in remaining:
                remaining.remove(x)
                remaining.remove(x | b)
                matched[x] = x | b
    return matched, remaining


def acyclic(F, matched):
    all_faces = set().union(*[set(v) for v in F.values()]) - {0}
    index = {x: i for i, x in enumerate(sorted(all_faces))}
    indeg = [0] * len(index)
    graph = [[] for _ in index]
    covers = 0
    for hi in all_faces:
        x = hi
        while x:
            bit = x & -x
            x -= bit
            lo = hi ^ bit
            if lo == 0:
                continue
            if matched.get(lo) == hi:
                src, dst = lo, hi
            else:
                src, dst = hi, lo
            graph[index[src]].append(index[dst])
            indeg[index[dst]] += 1
            covers += 1
    queue = deque(i for i, d in enumerate(indeg) if d == 0)
    seen = 0
    while queue:
        i = queue.popleft()
        seen += 1
        for j in graph[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                queue.append(j)
    assert seen == len(index), ('cyclic matching', seen, len(index))
    return len(index), covers


def morse_boundary(matched, critical):
    crit4 = sorted(x for x in critical if x.bit_count() == 5)
    crit5 = sorted(x for x in critical if x.bit_count() == 6)
    paired = {lo: hi for lo, hi in matched.items() if lo.bit_count() == 5}
    cache, active = {}, set()

    def expand(x):
        # Projection along the dimension-(4,5) gradient matching.
        if x in cache:
            return cache[x]
        if x not in paired:
            return {x: 1}
        assert x not in active
        active.add(x)
        bd = boundary(paired[x])
        incidence = bd.pop(x)
        out = {}
        for y, c in bd.items():
            for z, w in expand(y).items():
                out[z] = out.get(z, 0) - incidence * c * w
        active.remove(x)
        cache[x] = {k: v for k, v in out.items() if v}
        return cache[x]

    row_id = {x: i for i, x in enumerate(crit4)}
    mat = zeros(len(crit4), len(crit5))
    for j, top in enumerate(crit5):
        for lo, c in boundary(top).items():
            for k, v in expand(lo).items():
                if k in row_id:
                    mat[row_id[k], j] += c * v
    diag_mat = smith_normal_form(mat, domain=ZZ)
    diag = [int(diag_mat[i, i]) for i in range(min(diag_mat.shape))]
    assert sorted(abs(x) for x in diag) == [0] * 5 + [1] * 8, diag
    return mat, diag


def finite_field_ranks(F, p):
    ranks = {0: 0}
    for degree in range(1, 7):
        lower = {x: i for i, x in enumerate(F[degree - 1])}
        pivots = {}
        for x in F[degree]:
            if p == 2:
                v = 0
                for y in boundary(x):
                    v ^= 1 << lower[y]
                while v:
                    bit = v.bit_length() - 1
                    if bit in pivots:
                        v ^= pivots[bit]
                    else:
                        pivots[bit] = v
                        break
            else:
                vec = {lower[y]: c % p for y, c in boundary(x).items()}
                while vec:
                    bit = max(vec)
                    if bit in pivots:
                        coeff = vec[bit]
                        for z, c in pivots[bit].items():
                            w = (vec.get(z, 0) - coeff * c) % p
                            if w: vec[z] = w
                            else: vec.pop(z, None)
                    else:
                        inv = pow(vec[bit], -1, p)
                        pivots[bit] = {z: c * inv % p for z, c in vec.items()}
                        break
        ranks[degree] = len(pivots)
    betti = {d - 1: len(F[d]) - ranks[d] - ranks.get(d + 1, 0) for d in range(1, 7)}
    assert betti == {0: 0, 1: 0, 2: 0, 3: 0, 4: 88, 5: 5}, betti
    return ranks, betti


def main():
    F = faces()
    fv = [len(F[d]) for d in range(1, 7)]
    assert fv == [24, 240, 1200, 3060, 3600, 1440]
    matched, critical = make_matching(F)
    types = dict(sorted(Counter(x.bit_count() - 1 for x in critical).items()))
    assert len(matched) == 4727
    assert types == {0: 1, 4: 96, 5: 13}, types
    n, covers = acyclic(F, matched)
    assert n == 9564
    M, diag = morse_boundary(matched, critical)
    for p in [2, 3, 5]:
        ranks, betti = finite_field_ranks(F, p)
        print(f'field={p} boundary_ranks={[ranks[k] for k in range(1, 7)]} betti={betti}')
    print('f_vector=', fv)
    print('nonempty_faces=', n, 'matching_pairs=', len(matched), 'hasse_covers=', covers)
    print('critical_cells=', types)
    print('morse_matrix_shape=', M.shape, 'nonzero_entries=', sum(int(x != 0) for x in M))
    print('morse_smith_diagonal=', diag)
    print('homotopy=88 S^4 wedge 5 S^5')
    print('CHESSBOARD_4X6_CAP2_MORSE_PASS')


if __name__ == '__main__':
    main()
