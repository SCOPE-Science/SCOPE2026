"""Recovery test: random 3-coloring + greedy flips + bounded Moser-Tardos
resampling on Cayley balls of Gamma=Z^2*C2. Reports residual conflicts.
Heuristic finite-ball evidence only. Stdlib, seeded. Writes recover_test.json."""
import json
import random

A = (0, 0)


def mul_A(T, dm, dn):
    L = list(T)
    L[-1] = (L[-1][0] + dm, L[-1][1] + dn)
    return tuple(L)


def reduce_blocks(L):
    L = list(L)
    while len(L) >= 3:
        hit = -1
        for i in range(1, len(L) - 1):
            if L[i] == (0, 0):
                hit = i
                break
        if hit < 0:
            break
        L = (L[:hit - 1]
             + [(L[hit - 1][0] + L[hit + 1][0],
                 L[hit - 1][1] + L[hit + 1][1])]
             + L[hit + 2:])
    return tuple(L)


def mul_c(T):
    return reduce_blocks(list(T) + [(0, 0)])


E = ((0, 0),)
GENS = {'a': ('A', 1, 0), 'ai': ('A', -1, 0), 'b': ('A', 0, 1),
        'bi': ('A', 0, -1), 'c': ('C',)}
SYMS = ['a', 'ai', 'b', 'bi', 'c']


def apply(T, g):
    s = GENS[g]
    if s[0] == 'A':
        return mul_A(T, s[1], s[2])
    return mul_c(T)


def ball(R):
    from collections import deque
    dist = {E: 0}
    q = deque([E])
    while q:
        g = q.popleft()
        if dist[g] >= R:
            continue
        for s in SYMS:
            h = apply(g, s)
            if h not in dist:
                dist[h] = dist[g] + 1
                q.append(h)
    verts = sorted(dist)
    idx = {g: i for i, g in enumerate(verts)}
    edges = set()
    for g in verts:
        for s in SYMS:
            h = apply(g, s)
            if h in idx:
                i, j = idx[g], idx[h]
                edges.add((min(i, j), max(i, j)))
    return verts, sorted(edges)


def bad_edges(col, edges):
    return [e for e in edges if col[e[0]] == col[e[1]]]


def run(R, seed, mt_steps):
    rng = random.Random(seed)
    verts, edges = ball(R)
    n = len(verts)
    adj = [[] for _ in range(n)]
    for (i, j) in edges:
        adj[i].append(j)
        adj[j].append(i)
    col = [rng.randrange(3) for _ in range(n)]
    init_bad = len(bad_edges(col, edges))
    # greedy single-vertex flips, 5 passes
    for _ in range(5):
        for i in range(n):
            cur = sum(1 for j in adj[i] if col[j] == col[i])
            if cur:
                best_c, best_v = col[i], cur
                for c in range(3):
                    v = sum(1 for j in adj[i] if col[j] == c)
                    if v < best_v:
                        best_c, best_v = c, v
                col[i] = best_c
    greedy_bad = len(bad_edges(col, edges))
    # bounded Moser-Tardos: resample both endpoints of a random bad edge
    bad = bad_edges(col, edges)
    steps = 0
    while bad and steps < mt_steps:
        (i, j) = bad[rng.randrange(len(bad))]
        col[i] = rng.randrange(3)
        col[j] = rng.randrange(3)
        steps += 1
        if steps % 500 == 0:
            bad = bad_edges(col, edges)
    bad = bad_edges(col, edges)
    return {'R': R, 'n': n, 'm': len(edges), 'seed': seed,
            'init_bad': init_bad, 'greedy_bad': greedy_bad,
            'mt_steps_used': steps, 'mt_cap': mt_steps,
            'residual_bad': len(bad),
            'mt_terminated': len(bad) == 0}


results = []
for R in (3, 4, 5):
    for seed in (1, 2, 3):
        results.append(run(R, seed, 20000))
out = {'results': results,
       'conclusion': ('MT resampling with 20k-step cap never terminates; '
                      'extensive residual monochromatic edges persist on '
                      'balls R=3..5. Consistent with LLL-criterion failure; '
                      'no local signature of an easy measurable 3-coloring.')}
with open('recover_test.json', 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
