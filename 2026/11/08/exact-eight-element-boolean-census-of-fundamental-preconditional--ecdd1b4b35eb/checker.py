"""Exhaustive certificate for the F-preconditional census on P({0,1,2}).

Python >= 3.9, standard library only. Lists each admissible row under the
necessary local axioms, tests every resulting operation against the original
five preconditional laws, and applies the full six-element atom-permutation
group. This is finite exhaustive enumeration, not a theorem prover.
"""
from itertools import product, permutations
from collections import Counter

N = 3
TOP = (1 << N) - 1
V = range(TOP + 1)
def sub(a):
    return [x for x in V if x & a == x]

def rows(a):
    xs = sub(a)
    opts = []
    for x in xs:
        if a == TOP:
            opts.append([x])                 # P1 and P2
        elif a == 0 or x == a:
            opts.append([TOP])               # conditional identity
        elif x == 0:
            opts.append([z for z in V if (a & z) == 0])  # semi
        else:
            opts.append([z for z in V if (x & z) == x])  # P2
    out = []
    for v in product(*opts):
        f = dict(zip(xs, v))
        if any((f[x] & f[y]) != f[x]
               for x in xs for y in xs if (x & y) == x):
            continue                         # P4 isotonicity
        if any((f[f[y] & a] & f[y]) != f[f[y] & a]
               for y in xs):
            continue                         # P5 with inner antecedent a
        out.append(f)
    return out

ROW = {a: rows(a) for a in V}
assert [len(ROW[a]) for a in V] == [1, 4, 4, 13, 4, 13, 13, 1]

# Necessary and sufficient P5 constraints for proper nested antecedents.
# Every pair of distinct two-element antecedents is incomparable.
models_T = 0
models_F = []
for atom_rows in product(*(ROW[a] for a in (1, 2, 4))):
    f = {0: ROW[0][0], TOP: ROW[TOP][0],
         **dict(zip((1, 2, 4), atom_rows))}
    allowed = {}
    for d in (3, 5, 6):
        allowed[d] = [g for g in ROW[d]
                      if all((g[f[x][y] & d] & f[x][y]) == g[f[x][y] & d]
                             for x in (1, 2, 4) if (x & d) == x
                             for y in sub(x))]
    for d3, d5, d6 in product(allowed[3], allowed[5], allowed[6]):
        f[3], f[5], f[6] = d3, d5, d6
        op = tuple(f[a][a & b] for a in V for b in V)
        arrow = lambda a, b: op[8*a+b]
        # Independent replay from the five P1--P5 axioms themselves.
        assert all((arrow(7, a) & a) == arrow(7, a) for a in V)
        assert all((a & b & arrow(a, b)) == (a & b) for a in V for b in V)
        assert all((arrow(a, b) & arrow(a, a & b)) == arrow(a, b)
                   for a in V for b in V)
        assert all((arrow(a, b & c) & arrow(a, b)) == arrow(a, b & c)
                   for a in V for b in V for c in V)
        assert all((arrow(a, arrow(a & b, c)) & arrow(a & b, c))
                   == arrow(a, arrow(a & b, c))
                   for a in V for b in V for c in V)
        assert all(arrow(a, a) == TOP and (a & arrow(a, 0)) == 0 for a in V)
        models_T += 1
        if all((a & arrow(arrow(a, 0), 0)) == a for a in V):
            models_F.append(op)

assert models_T == 7820
assert len(models_F) == 1021

# Extract the unique reflexive symmetric graph from each negation.
def graph_edges(op):
    return tuple((i, j) for i in range(N) for j in range(i + 1, N)
                 if not (op[8*(1 << i)] & (1 << j)))

by_graph = Counter(graph_edges(op) for op in models_F)
by_edge_count = Counter()
for edge_set, count in by_graph.items():
    by_edge_count[len(edge_set)] += count
assert dict(by_edge_count) == {0: 1, 1: 48, 2: 243, 3: 729}
assert sorted(by_graph.values()) == [1, 16, 16, 16, 81, 81, 81, 729]

# Orbit-count certificate by full atom relabeling S_3.
def mask_map(p):
    return tuple(sum(1 << p[i] for i in range(N) if a & (1 << i)) for a in V)

def conjugate(op, m):
    q = [0] * 64
    for a in V:
        for b in V:
            q[8*m[a] + m[b]] = m[op[8*a+b]]
    return tuple(q)

G = [(p, mask_map(p)) for p in permutations(range(N))]
fixed = {p: sum(conjugate(op, m) == op for op in models_F) for p, m in G}
fixed_by_order = Counter()
for p, count in fixed.items():
    if p == (0,1,2): kind = 'identity'
    elif all(p[p[p[i]]] == i for i in range(N)) and p != (0,1,2) and any(p[p[i]] != i for i in range(N)):
        kind = '3cycle'
    else: kind = 'transposition'
    fixed_by_order[kind] += count
assert fixed_by_order == {'identity': 1021, 'transposition': 123, '3cycle': 20}
canon = {min(conjugate(op, m) for _, m in G) for op in models_F}
assert len(canon) == 194 == sum(fixed.values()) // 6
orbit_hist = Counter()
for op in canon:
    orbit_hist[len({conjugate(op, m) for _, m in G})] += 1
assert orbit_hist == {1: 4, 2: 3, 3: 37, 6: 150}
print('F_PRECONDITIONAL_BOOLEAN3_OK',
      'T=',models_T, 'F=',len(models_F),
      'negation_graphs=',len(by_graph),
      'edge_count_fibres=',dict(sorted(by_edge_count.items())),
      'isomorphism_classes=',len(canon),
      'orbit_sizes=',dict(sorted(orbit_hist.items())))
