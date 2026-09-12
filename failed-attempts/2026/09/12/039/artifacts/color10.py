"""DSATUR branch-and-bound 10-colouring of the block-intersection graph (57 vertices).
Writes 10-partitions if found. Deterministic, stdlib only."""
import itertools, sys, time

A = [
    ((0, 1, 4), (0, 2, 9), (0, 5, 11)),
    ((0, 1, 4), (0, 2, 12), (0, 5, 13)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 10)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 13)),
]
V = 19
which = int(sys.argv[1]) if len(sys.argv) > 1 else 0
K = 10
TIMELIM = float(sys.argv[2]) if len(sys.argv) > 2 else 600


def develop(fam):
    blocks = set()
    for t in fam:
        for s in range(V):
            blocks.add(frozenset((x + s) % V for x in t))
    return sorted(blocks)


blocks = develop(A[which])
m = len(blocks)
assert m == 57
# adjacency: share a point
adj = [set() for _ in range(m)]
deg = [0] * m
for i in range(m):
    for j in range(i + 1, m):
        if blocks[i] & blocks[j]:
            adj[i].add(j)
            adj[j].add(i)
print(f"A{which+1}: edges={sum(len(a) for a in adj)//2}", flush=True)

color = [-1] * m
order = sorted(range(m), key=lambda i: -len(adj[i]))
# symmetry break: fix max-degree vertex to color 0? DSATUR picks adaptively; instead
# order vertices statically by degree and try colors in order with forward checking.
# Use degeneracy: color in fixed order with pruning; K=10 needs full search though.
# Better: recursive with saturation selection.

deadline = time.time() + TIMELIM
nodes = [0]
found = [None]


def select():
    best, bestkey = -1, None
    for i in range(m):
        if color[i] < 0:
            used = {color[j] for j in adj[i] if color[j] >= 0}
            key = (len(used), len(adj[i]))
            if bestkey is None or key > bestkey:
                best, bestkey = i, key
    return best


def dfs(ncolored):
    nodes[0] += 1
    if found[0] is not None or time.time() > deadline:
        return True
    if ncolored == m:
        found[0] = list(color)
        return True
    v = select()
    used = {color[j] for j in adj[v] if color[j] >= 0}
    for c in range(K):
        if c in used:
            continue
        color[v] = c
        if dfs(ncolored + 1):
            if found[0] is not None:
                return True
        color[v] = -1
    return False


# iterative: pick first vertex fixed to 0 to break color symmetry
v0 = max(range(m), key=lambda i: len(adj[i]))
color[v0] = 0
t0 = time.time()
dfs(1)
print(f"done t={time.time()-t0:.1f}s nodes={nodes[0]} found={found[0] is not None}", flush=True)
if found[0] is not None:
    classes = [[] for _ in range(K)]
    for i, c in enumerate(found[0]):
        classes[c].append(sorted(blocks[i]))
    # verify
    for cl in classes:
        seen = set()
        for b in cl:
            for x in b:
                assert x not in seen, "not a partial parallel class"
                seen.add(x)
    assert sum(len(c) for c in classes) == 57
    print("class sizes:", sorted(len(c) for c in classes))
    with open(f"partition_A{which+1}.txt", "w") as fh:
        for ci, cl in enumerate(classes):
            fh.write(f"class {ci} ({len(cl)} blocks):\n")
            for b in cl:
                fh.write("  " + repr(b) + "\n")
