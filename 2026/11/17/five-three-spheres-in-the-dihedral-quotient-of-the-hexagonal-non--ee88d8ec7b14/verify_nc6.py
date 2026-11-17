#!/usr/bin/env python3
"""Integral cellular verification for the dihedral orbit of the six-point
noncrossing-partition proper order complex. No external dependencies.

Run: python3 verify_nc6.py
"""
from collections import Counter, defaultdict
from itertools import combinations

N = 6


def partitions(n):
    """Set partitions in canonical restricted-growth-string order."""
    def extend(values, largest):
        if len(values) == n:
            yield tuple(tuple(i for i, x in enumerate(values) if x == k)
                        for k in range(largest + 1))
            return
        for k in range(largest + 2):
            yield from extend(values + [k], max(k, largest))
    yield from extend([0], 0)


def is_noncrossing(p):
    block = {j: i for i, b in enumerate(p) for j in b}
    return not any(block[a] == block[c] and block[b] == block[d]
                   and block[a] != block[b]
                   for a, b, c, d in combinations(range(N), 4))

full = [p for p in partitions(N) if is_noncrossing(p)]
assert len(full) == 132
P = sorted((p for p in full if 1 < len(p) < N),
           key=lambda p: (N - len(p), p))
assert len(P) == 130
index = {p: i for i, p in enumerate(P)}
rank = [N - len(p) for p in P]
assert Counter(rank) == {1: 15, 2: 50, 3: 50, 4: 15}
block_index = [{v: i for i, b in enumerate(p) for v in b} for p in P]


def finer(i, j):
    if rank[i] >= rank[j]:
        return False
    a, b = block_index[i], block_index[j]
    return all(a[x] != a[y] or b[x] == b[y]
               for x, y in combinations(range(N), 2))

above = [[j for j in range(len(P)) if finer(i, j)]
         for i in range(len(P))]
group = [tuple((a + s * i) % N for i in range(N))
         for a in range(N) for s in (1, -1)]
assert len(set(group)) == 12


def transform(p, g):
    return tuple(sorted(tuple(sorted(g[x] for x in b)) for b in p))

perms = [tuple(index[transform(p, g)] for p in P) for g in group]
assert all(sorted(perm) == list(range(len(P))) for perm in perms)


def canonical(chain):
    return min(tuple(g[x] for x in chain) for g in perms)

# Both reflection classes fix vertices: the reflections i->-i and i->1-i.
for reflection in (1, 3):
    assert group[reflection][0] in (0, 1)
    assert any(perm[i] == i for i in range(len(P))
               for perm in [perms[reflection]])

chains = []

def walk(chain):
    chains.append(tuple(chain))
    for j in above[chain[-1]]:
        walk(chain + [j])

for i in range(len(P)):
    walk([i])
assert len(chains) == 4621
cells = {k: sorted({canonical(c) for c in chains if len(c) == k + 1})
         for k in range(4)}
counts = tuple(len(cells[k]) for k in range(4))
assert counts == (22, 114, 204, 116), counts
assert sum((-1)**k*counts[k] for k in range(4)) == -4
# Check Burnside's lemma separately, on the actual chains, not on cell keys.
for k in range(4):
    ch = [c for c in chains if len(c) == k + 1]
    fixed_total = sum(sum(all(perm[i] == i for i in c) for c in ch)
                      for perm in perms)
    assert fixed_total == len(group) * counts[k]

cell_id = {k: {c: i for i, c in enumerate(cells[k])}
           for k in range(4)}
differential = {}
for k in (1, 2, 3):
    differential[k] = []
    for c in cells[k]:
        col = defaultdict(int)
        for i in range(len(c)):
            col[cell_id[k-1][canonical(c[:i] + c[i+1:])]] += (-1)**i
        differential[k].append({i: v for i, v in col.items() if v})


def compose(a, b):
    for col in a:
        out = defaultdict(int)
        for j, v in col.items():
            for i, w in b[j].items():
                out[i] += v*w
        assert all(v == 0 for v in out.values())

for k in (2, 3):
    compose(differential[k], differential[k-1])

# Exact integral cancellation of unit boundary pivots.  The chain-group basis
# changes are elementary unimodular transformations; this is not a claim of
# simplicial collapse.  Its only topological use is the homology calculation.
alive = {k: set(range(counts[k])) for k in range(4)}
cols = {k: {j: dict(col) for j, col in enumerate(differential[k])}
        for k in differential}
rows = {k: defaultdict(dict) for k in differential}
for k in cols:
    for j, col in cols[k].items():
        for i, v in col.items():
            rows[k][i][j] = v
pivots = Counter()
for k in (1, 2, 3):
    while True:
        pivot = next(((i, j, v) for i, row in rows[k].items()
                      if i in alive[k-1] for j, v in row.items()
                      if j in alive[k] and abs(v) == 1), None)
        if pivot is None:
            break
        i, j, unit = pivot
        row, column = dict(rows[k][i]), dict(cols[k][j])
        for other, a in row.items():
            if other == j:
                continue
            factor = a // unit
            for ii, b in column.items():
                new = cols[k][other].get(ii, 0) - factor*b
                if new:
                    cols[k][other][ii] = new
                    rows[k][ii][other] = new
                else:
                    cols[k][other].pop(ii, None)
                    rows[k][ii].pop(other, None)
        for ii in column:
            rows[k][ii].pop(j, None)
        for other in row:
            cols[k][other].pop(i, None)
        del cols[k][j]
        rows[k].pop(i, None)
        if k + 1 in cols:
            for other in list(rows[k+1].get(j, {})):
                cols[k+1][other].pop(j, None)
            rows[k+1].pop(j, None)
        if k - 1 in cols:
            for ii in list(cols[k-1].get(i, {})):
                rows[k-1][ii].pop(i, None)
            cols[k-1].pop(i, None)
        alive[k].remove(j)
        alive[k-1].remove(i)
        pivots[k] += 1
    assert all(not c for c in cols[k].values())
    if k < 3:
        assert all(not col or set(col).issubset(alive[k])
                   for col in cols[k+1].values())
assert tuple(pivots[k] for k in (1, 2, 3)) == (21, 93, 111)
assert tuple(len(alive[k]) for k in range(4)) == (1, 0, 0, 5)
assert sum(len(c) for matrix in cols.values() for c in matrix.values()) == 0
print('noncrossing partitions (including bounds):', len(full))
print('proper noncrossing partitions:', len(P))
print('ordinary order-complex cells before quotient:', len(chains))
print('dihedral orbit cells in degrees 0 to 3:', counts)
print('boundary compositions: zero')
print('unit integral cancellations in degrees 1 to 3:',
      tuple(pivots[k] for k in (1, 2, 3)))
print('remaining chain modules in degrees 0 to 3:',
      tuple(len(alive[k]) for k in range(4)))
print('all remaining differentials: zero')
print('reflection classes: invariant partition vertices found')
print('PASS')
