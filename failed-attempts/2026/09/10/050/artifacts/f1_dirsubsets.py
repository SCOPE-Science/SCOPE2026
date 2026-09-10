"""Fallback attempt F1: direction-restricted D_4(3) — the natural explicit
F-free candidates. Keep only lines from a subset S of directions.
Checks F-freeness + edge density vs 1e-6 N^{5/4}, and records the exponent
(E scales as N^{3/4} for fixed |S|, so asymptotically below N^{5/4}).
stdlib only.
"""
import itertools
import json
from r1_D4_freeness import len4_paths, has_theta

q = 3
k = 4
pts = list(itertools.product(range(q), repeat=k))
p_index = {p: i for i, p in enumerate(pts)}
dirs = [tuple(pow(z, i, q) for i in range(k)) for z in range(q)]
# lines per direction
per_dir = []
for d in dirs:
    seen = set()
    for x in pts:
        line = tuple(sorted(
            p_index[tuple((x[i] + y * d[i]) % q for i in range(k))]
            for y in range(q)))
        seen.add(line)
    per_dir.append(sorted(seen))

nP = len(pts)


def test_subset(S):
    lines = []
    for di in S:
        lines.extend(per_dir[di])
    nL = len(lines)
    N = nP + nL
    adj = [set() for _ in range(N)]
    for li, line in enumerate(lines):
        v = nP + li
        for u in line:
            adj[u].add(v)
            adj[v].add(u)
    E = sum(len(a) for a in adj) // 2
    # full Theta census (PP + LL)
    pp = sum(1 for i in range(nP) for j in range(i + 1, nP)
             if has_theta(adj, i, j))
    LL = list(range(nP, N))
    ll = sum(1 for a in range(len(LL)) for b in range(a + 1, len(LL))
             if has_theta(adj, LL[a], LL[b]))
    return {"S": list(S), "N": N, "E": E,
            "E_over_N54": E / (N ** 1.25),
            "threshold_1em6_N54": 1e-6 * (N ** 1.25),
            "PP_theta": pp, "LL_theta": ll,
            "F_free": (pp == 0 and ll == 0)}


out = []
for r in (2, 3):
    for S in itertools.combinations(range(q), r):
        res = test_subset(S)
        out.append(res)
        print(res)
with open("f1_dirsubsets.json", "w") as f:
    json.dump(out, f, indent=2)
print("wrote f1_dirsubsets.json")
