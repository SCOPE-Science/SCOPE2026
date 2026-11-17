"""Exhaustive vectorized verification for cubic seven-cage majority dynamics.
Requirements: Python 3, NumPy, NetworkX. Run: python verify_independent.py
No external data files are needed.
"""
import collections
import numpy as np
import networkx as nx

N = 24
G = nx.Graph()
G.add_nodes_from(range(N))
for i in range(N):
    G.add_edge(i, (i + 1) % N)
    G.add_edge(i, (i + (-12, 7, -7)[i % 3]) % N)
assert G.number_of_edges() == 36
assert set(dict(G.degree()).values()) == {3}
assert min(len(c) for c in nx.minimum_cycle_basis(G)) == 7
perms = [[mapping[i] for i in range(N)] for mapping in
         nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter()]
assert len(perms) == 32
neighbors = [tuple(G.neighbors(i)) for i in range(N)]


def advance(values):
    result = np.zeros_like(values)
    for i, (a, b, c) in enumerate(neighbors):
        count = ((values >> a) & 1) + ((values >> b) & 1) + ((values >> c) & 1)
        result |= (count >= 2).astype(np.uint32) << i
    return result


def transform(values, permutation):
    result = np.zeros_like(values)
    for i, j in enumerate(permutation):
        result |= ((values >> i) & 1) << j
    return result


fixed, two = [], []
witness = None
hist_fixed = np.zeros(12, dtype=np.int64)
hist_two = np.zeros(12, dtype=np.int64)
consensus_zero = consensus_one = 0
for low in range(0, 1 << N, 1 << 18):
    states = np.arange(low, low + (1 << 18), dtype=np.uint32)
    y = advance(states)
    z = advance(y)
    fixed.extend(states[y == states])
    two.extend(states[(z == states) & (states < y)])
    history = [states, y, z]
    for t in range(3, 14):
        history.append(advance(history[-1]))
    assert np.array_equal(history[13], history[11]), 'F^13=F^11 failed'
    if witness is None:
        differs = np.flatnonzero(history[10] != history[12])
        if len(differs):
            witness = int(states[differs[0]])
    is_fixed = (history[11] == history[12])
    discovered = np.zeros(len(states), dtype=np.bool_)
    for t in range(12):
        first = (history[t] == history[t + 2]) & ~discovered
        hist_fixed[t] += np.count_nonzero(first & is_fixed)
        hist_two[t] += np.count_nonzero(first & ~is_fixed)
        discovered |= first
    assert discovered.all()
    consensus_zero += np.count_nonzero(history[11] == 0)
    consensus_one += np.count_nonzero(history[11] == (1 << N) - 1)
fixed = np.array(fixed, dtype=np.uint32)
two = np.array(two, dtype=np.uint32)
assert len(fixed) == 550 and len(two) == 63715 and witness is not None
assert np.array_equal(advance(fixed), fixed)
partners = advance(two)
assert np.all(advance(partners) == two) and np.all(two < partners)
print('graph vertices=24, edges=36, girth=7, automorphisms=32')
print('exhaustive states checked=16777216')
print('fixed configurations=550, primitive two-cycles=63715')
print('F^13=F^11 holds for every configuration')
print('F^12 != F^10 witness=', witness, 'hex=', format(witness, '06x'))
print('first entry: [time, eventual fixed, eventual two]')
for t in range(12):
    print(t, int(hist_fixed[t]), int(hist_two[t]))
print('total fixed-basin=',sum(hist_fixed),'two-basin=',sum(hist_two))
print('unanimous basin each=',consensus_zero,consensus_one)
assert int(sum(hist_fixed)) == 2091268 and int(sum(hist_two)) == 14685948
assert consensus_zero == consensus_one == 1033256
assert int(hist_two[-1]) == 320 and int(hist_fixed[-1]) == 0
for name, states, others in [('fixed', fixed, None), ('two', two, partners)]:
    canonical = states.copy()
    for perm in perms:
        shifted = transform(states, perm)
        if others is not None:
            shifted = np.minimum(shifted, transform(others, perm))
        canonical = np.minimum(canonical, shifted)
    labels, sizes = np.unique(canonical, return_counts=True)
    counts = dict(sorted(collections.Counter(map(int, sizes)).items()))
    print(name + ' symmetry classes=', len(labels), 'orbit-size histogram=', counts)
    assert sum(size * multiplicity for size, multiplicity in counts.items()) == len(states)
