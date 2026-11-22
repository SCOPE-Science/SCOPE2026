#!/usr/bin/env python3
"""Exact, self-contained verification of the triangular-prism forest-orbit result.

Enumerates a finite simplicial quotient after barycentric subdivision. All
arithmetic is over the integers; zero tests and unit operations are exact.
"""
from collections import Counter, defaultdict
from itertools import permutations

# C3 square K2: two triangles joined by a matching.
EDGES = tuple(sorted(
    [tuple(sorted((i, (i + 1) % 3))) for i in range(3)]
    + [tuple(sorted((i + 3, (i + 1) % 3 + 3))) for i in range(3)]
    + [(i, i + 3) for i in range(3)]
))
assert len(EDGES) == 9 and len(set(EDGES)) == 9
EDGE_ID = {edge: i for i, edge in enumerate(EDGES)}


def automorphisms():
    ans = []
    for p in permutations(range(3)):
        for exchange in (0, 1):
            vertices = {i + 3 * side: p[i] + 3 * (side ^ exchange)
                        for i in range(3) for side in range(2)}
            mapping = tuple(EDGE_ID[tuple(sorted((vertices[a], vertices[b])))]
                            for a, b in EDGES)
            ans.append(mapping)
    assert len(ans) == len(set(ans)) == 12
    return tuple(ans)

GROUP = automorphisms()
# Independent brute-force check that the displayed twelve permutations are all
# automorphisms, rather than a proper subgroup of the full symmetry group.
edge_set = set(EDGES)
full_vertex_aut = [p for p in permutations(range(6))
                   if {tuple(sorted((p[a], p[b]))) for a, b in EDGES} == edge_set]
assert len(full_vertex_aut) == 12



def is_forest(mask):
    parent = list(range(6))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for j, (a, b) in enumerate(EDGES):
        if mask & (1 << j):
            a, b = root(a), root(b)
            if a == b:
                return False
            parent[a] = b
    return True

FACES = tuple(f for f in range(1, 1 << len(EDGES)) if is_forest(f))
FACESET = set(FACES)
FACECOUNT = Counter(f.bit_count() for f in FACES)
assert tuple(FACECOUNT[d] for d in range(1, 6)) == (9, 36, 82, 111, 75)
TRANSFORM = {f: tuple(sum(1 << permutation[i] for i in range(9) if f & (1 << i))
                      for permutation in GROUP) for f in FACES}


def canonical(chain):
    return min(tuple(TRANSFORM[mask][i] for mask in chain) for i in range(12))


def orbit_flags():
    layers = []
    active = {(f,) for f in FACES}
    while active:
        representatives = sorted({canonical(c) for c in active})
        layers.append(representatives)
        if len(layers) == 5:
            break
        # Every orbit of extensions has a representative extending a
        # canonical prefix, because the group acts on the entire flag.
        active = set()
        for flag in representatives:
            top = flag[-1]
            for extended in FACES:
                if extended != top and (extended & top) == top:
                    active.add(canonical(flag + (extended,)))
    assert tuple(map(len, layers)) == (41, 405, 1339, 1722, 750)
    for layer in layers:
        for flag in layer:
            ranks = tuple(m.bit_count() for m in flag)
            assert ranks == tuple(sorted(set(ranks)))
    return layers

FLAGS = orbit_flags()
LOOKUP = [{flag: index for index, flag in enumerate(layer)} for layer in FLAGS]
DIM = [len(layer) for layer in FLAGS]


def burnside_flag_orbits():
    totals = [0] * 5
    for i in range(len(GROUP)):
        fixed = {f for f in FACES if TRANSFORM[f][i] == f}
        counts = {}
        for f in FACES:
            if f not in fixed:
                continue
            cur = [1, 0, 0, 0, 0]
            x = (f - 1) & f
            while x:
                if x in fixed:
                    for j in range(1, 5):
                        cur[j] += counts[x][j - 1]
                x = (x - 1) & f
            counts[f] = cur
            for j in range(5):
                totals[j] += cur[j]
    assert all(t % 12 == 0 for t in totals)
    assert [t // 12 for t in totals] == DIM
    return totals


def boundaries():
    rows, cols = [], []
    for dimension in range(1, 5):
        r, c = defaultdict(dict), defaultdict(dict)
        for j, flag in enumerate(FLAGS[dimension]):
            for k in range(dimension + 1):
                boundary_face = canonical(flag[:k] + flag[k+1:])
                i = LOOKUP[dimension-1][boundary_face]
                assert j not in r[i]
                v = (-1) ** k
                r[i][j] = v
                c[j][i] = v
        rows.append(r)
        cols.append(c)
    return rows, cols


def check_chain_complex(cols):
    for d in range(3):
        for j, terms in cols[d+1].items():
            accumulation = defaultdict(int)
            for middle, v in terms.items():
                for low, w in cols[d][middle].items():
                    accumulation[low] += v * w
            assert all(v == 0 for v in accumulation.values()), (d, j)


def reduce_integral_complex(rows, cols):
    # Each unit pivot splits an acyclic 2-term direct summand over Z.
    dimensions = DIM[:]
    cancelled = []
    for d in range(4, 0, -1):
        rr, cc = rows[d-1], cols[d-1]
        steps = 0
        while True:
            pivot = None
            for r, row in rr.items():
                for c, value in row.items():
                    if abs(value) == 1:
                        cost = (len(row)-1) * (len(cc[c])-1)
                        if pivot is None or cost < pivot[0]:
                            pivot = (cost, r, c, value)
                        if cost == 0:
                            break
                if pivot is not None and pivot[0] == 0:
                    break
            if pivot is None:
                break
            _, r, c, value = pivot
            column = list(cc[c].items())
            row = list(rr[r].items())
            for j, t in row:
                if j == c:
                    continue
                factor = t * value  # value^{-1} = value for +/- 1
                for i, u in column:
                    if i == r:
                        continue
                    new = rr[i].get(j, 0) - factor * u
                    if new:
                        rr[i][j] = new
                        cc[j][i] = new
                    else:
                        rr[i].pop(j, None)
                        cc[j].pop(i, None)
            for i, _ in column:
                rr[i].pop(c, None)
            for j, _ in row:
                cc[j].pop(r, None)
            del rr[r]
            del cc[c]
            # Adjacent differential entries are removed in the new
            # integral bases. Chain-complex identities make the
            # corresponding eliminated maps vanish automatically.
            if d < 4:
                for j in list(rows[d].get(c, {})):
                    cols[d][j].pop(c, None)
                rows[d].pop(c, None)
            if d > 1:
                for i in list(cols[d-2].get(r, {})):
                    rows[d-2][i].pop(r, None)
                cols[d-2].pop(r, None)
            dimensions[d] -= 1
            dimensions[d-1] -= 1
            steps += 1
        check_chain_complex(cols)
        cancelled.append(steps)
    assert cancelled == [748, 974, 365, 40], cancelled
    assert dimensions == [1, 0, 0, 0, 2], dimensions
    assert all(not any(col.values()) for degree in cols for col in degree.values())
    return cancelled, dimensions


def fundamental_group_presentation():
    lookup0, lookup1 = LOOKUP[0], LOOKUP[1]
    parent = list(range(DIM[0]))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    tree = set()
    for (a, b), edge in lookup1.items():
        va, vb = lookup0[canonical((a,))], lookup0[canonical((b,))]
        assert va != vb
        ra, rb = root(va), root(vb)
        if ra != rb:
            parent[ra] = rb
            tree.add(edge)
    assert len(tree) == DIM[0]-1
    generators = {j: k+1 for k, j in enumerate(x for x in range(DIM[1]) if x not in tree)}
    assert len(generators) == 365

    def edge(a, b):
        return lookup1[canonical((a, b))]
    def freely_reduce(word):
        result = []
        for x in word:
            if result and result[-1] == -x:
                result.pop()
            else:
                result.append(x)
        return result

    relations = []
    for a, b, c in FLAGS[2]:
        rel = []
        for x, y, sign in ((a, b, +1), (b, c, +1), (a, c, -1)):
            gen = generators.get(edge(x, y))
            if gen:
                rel.append(sign * gen)
        rel = freely_reduce(rel)
        if rel:
            relations.append(rel)
    total_generators = len(generators)
    eliminations = 0
    while True:
        relations = [freely_reduce(r) for r in relations]
        relations = [r for r in relations if r]
        frequencies = Counter(abs(x) for word in relations for x in word)
        best = None
        for i, word in enumerate(relations):
            for x in word:
                gen = abs(x)
                if sum(abs(t) == gen for t in word) > 1:
                    continue
                score = ((frequencies[gen]-1) * (len(word)-1), len(word), i, gen)
                if best is None or score < best:
                    best = score
        if best is None:
            break
        _, _, index, gen = best
        word = relations[index]
        pos = next(j for j, x in enumerate(word) if abs(x) == gen)
        sign = word[pos] > 0
        seq = word[pos+1:] + word[:pos]
        substitute = [-x for x in seq[::-1]]
        if not sign:
            substitute = [-x for x in substitute[::-1]]
        verify = word[:pos] + (substitute if sign else [-x for x in substitute[::-1]]) + word[pos+1:]
        assert not freely_reduce(verify)
        new_relations = []
        for k, rel in enumerate(relations):
            if k == index:
                continue
            out = []
            for x in rel:
                if x == gen:
                    out.extend(substitute)
                elif x == -gen:
                    out.extend([-y for y in substitute[::-1]])
                else:
                    out.append(x)
            if out:
                new_relations.append(freely_reduce(out))
        relations = new_relations
        eliminations += 1
    assert eliminations == total_generators == 365
    assert not any(relations), (eliminations, relations[:4])
    return eliminations


def main():
    print('FOREST_FACES', *(FACECOUNT[d] for d in range(1, 6)))
    assert len(GROUP) == 12
    print('AUTOMORPHISMS', len(GROUP))
    sums = burnside_flag_orbits()
    print('BURNSIDE_FIXED_FLAG_TOTALS', *sums)
    print('ORBIT_CELL_COUNTS', *DIM)
    rows, cols = boundaries()
    print('BOUNDARY_NONZEROS', *(sum(len(c) for c in degree.values()) for degree in cols))
    check_chain_complex(cols)
    print('CHAIN_IDENTITIES', 'PASS')
    cancellations, survivors = reduce_integral_complex(rows, cols)
    print('INTEGRAL_UNIT_CANCELLATIONS_DESCENDING', *cancellations)
    print('RESIDUAL_CHAIN_RANKS', *survivors)
    print('PI1_TIETZE_ELIMINATIONS', fundamental_group_presentation())
    print('PRISM_FOREST_FULL_QUOTIENT_WEDGE_TWO_S4_OK')

if __name__ == '__main__':
    main()
