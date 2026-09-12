"""Fast heuristic 10-colouring: greedy over random orders + tabu/simulated annealing."""
import itertools, random, sys, time

A = [
    ((0, 1, 4), (0, 2, 9), (0, 5, 11)),
    ((0, 1, 4), (0, 2, 12), (0, 5, 13)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 10)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 13)),
]
V = 19
which = int(sys.argv[1]) if len(sys.argv) > 1 else 0
K = 10
BUDGET = float(sys.argv[2]) if len(sys.argv) > 2 else 120


def develop(fam):
    blocks = set()
    for t in fam:
        for s in range(V):
            blocks.add(frozenset((x + s) % V for x in t))
    return sorted(blocks)


blocks = develop(A[which])
m = len(blocks)
adj = [set() for _ in range(m)]
for i in range(m):
    for j in range(i + 1, m):
        if blocks[i] & blocks[j]:
            adj[i].add(j)
            adj[j].add(i)

random.seed(12345)
t0 = time.time()


def greedy(order):
    color = [-1] * m
    for v in order:
        used = {color[j] for j in adj[v] if color[j] >= 0}
        for c in range(K):
            if c not in used:
                color[v] = c
                break
        if color[v] < 0:
            return None, order
    return color, order


# 1) greedy over many random + degree orders
verts = list(range(m))
best = None
tries = 0
while time.time() - t0 < BUDGET / 3:
    tries += 1
    r = random.random()
    if r < 0.4:
        order = sorted(verts, key=lambda i: (random.random(), -len(adj[i])))
    elif r < 0.7:
        order = verts[:]
        random.shuffle(order)
    else:
        # saturation-like randomized
        order = sorted(verts, key=lambda i: -len(adj[i]))
        # random perturbation: swap chunks
        for _ in range(5):
            a, b = random.randrange(m), random.randrange(m)
            order[a], order[b] = order[b], order[a]
    c, _ = greedy(order)
    if c is not None:
        best = c
        break
print(f"greedy tries={tries} found={best is not None}", flush=True)

# 2) simulated annealing on conflicts with K colors
if best is None:
    color = [random.randrange(K) for _ in range(m)]
    # conflict count
    def nconf(color):
        n = 0
        for i in range(m):
            ci = color[i]
            for j in adj[i]:
                if j > i and color[j] == ci:
                    n += 1
        return n

    cur = nconf(color)
    print("init conflicts:", cur, flush=True)
    T = 2.0
    it = 0
    while time.time() - t0 < BUDGET:
        it += 1
        T = max(0.05, 2.0 * (1 - (time.time() - t0) / BUDGET))
        v = random.randrange(m)
        old = color[v]
        # pick conflicting vertex preferentially
        new = random.randrange(K)
        if new == old:
            continue
        delta = 0
        for j in adj[v]:
            if color[j] == new:
                delta += 1
            if color[j] == old:
                delta -= 1
        if delta <= 0 or random.random() < 2.718281828 ** (-delta / T):
            color[v] = new
            cur += delta
            if cur == 0:
                best = list(color)
                break
    print(f"SA iters={it} final_conf={cur} found={best is not None}", flush=True)

if best is not None:
    classes = [[] for _ in range(K)]
    for i, c in enumerate(best):
        classes[c].append(sorted(blocks[i]))
    for cl in classes:
        seen = set()
        for b in cl:
            for x in b:
                assert x not in seen
                seen.add(x)
    assert sum(len(c) for c in classes) == 57
    print("class sizes:", sorted(len(c) for c in classes))
    with open(f"partition_A{which+1}.txt", "w") as fh:
        for ci, cl in enumerate(classes):
            fh.write(f"class {ci} ({len(cl)} blocks):\n")
            for b in cl:
                fh.write("  " + repr(b) + "\n")
else:
    print("NO 10-PARTITION FOUND (heuristic, not a proof)")
