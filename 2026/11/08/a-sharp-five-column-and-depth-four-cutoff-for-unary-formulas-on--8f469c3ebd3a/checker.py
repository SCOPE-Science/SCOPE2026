"""Exhaustive semantic certificate for one-variable formulas on three-by-m S5 products.

Run with Python 3 (standard library only).  Model components are nonempty supports
of the eight possible binary column triples.  Two modalities are equivalence
relations induced by equal row and equal column, respectively.
"""
from itertools import product

R = 3
ALPHABET = range(1 << R)
worlds = []
index = {}
for support in range(1, 1 << (1 << R)):
    for v in ALPHABET:
        if support & (1 << v):
            for row in range(R):
                index[(support, v, row)] = len(worlds)
                worlds.append((support, v, row))
assert len(worlds) == 3 * 8 * 2**7 == 3072

row_succ = []
column_succ = []
for support, v, row in worlds:
    row_succ.append(tuple(index[(support, u, row)] for u in ALPHABET if support & (1 << u)))
    column_succ.append(tuple(index[(support, v, j)] for j in range(R)))

# Initial color is precisely the truth of the only propositional letter.
labels = [(v >> row) & 1 for support, v, row in worlds]
counts_by_depth = [[len(set(labels[i] for i,(s,_,__) in enumerate(worlds) if s.bit_count() <= m)) for m in range(1,9)]]
for depth in range(1, 6):
    signatures = [
        (labels[i], frozenset(labels[j] for j in row_succ[i]),
                    frozenset(labels[j] for j in column_succ[i]))
        for i in range(len(worlds))
    ]
    identifiers = {signature: number for number, signature in enumerate(set(signatures))}
    new_labels = [identifiers[s] for s in signatures]
    # Refinement must never identify two previously distinct semantic types.
    old_for_new = {}
    for a, b in zip(labels, new_labels):
        if b in old_for_new:
            assert old_for_new[b] == a
        else:
            old_for_new[b] = a
    labels = new_labels
    counts_by_depth.append([len(set(labels[i] for i,(s,_,__) in enumerate(worlds) if s.bit_count() <= m)) for m in range(1,9)])

EXPECTED = (
    (2,2,2,2,2,2,2,2),
    (4,8,8,8,8,8,8,8),
    (4,28,60,64,64,64,64,64),
    (4,28,88,136,140,140,140,140),
    (4,28,88,146,164,164,164,164),
    (4,28,88,146,164,164,164,164),
)
assert tuple(map(tuple,counts_by_depth)) == EXPECTED, counts_by_depth
# Last round witnesses a fixed point of the finite bisimulation refinement.
assert counts_by_depth[4] == counts_by_depth[5]
print('THREE_ROW_S5_PROFILE_OK',len(worlds),'states,',len(range(1,256)),'supports')
for depth,row in enumerate(EXPECTED):
    print(depth,*row)
