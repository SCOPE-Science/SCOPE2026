"""Route R1: anchor scale + test the only explicit published algebraic candidate.

Conlon D_k(q) (arXiv:2011.11064, Thm 2): D_4(q) is bipartite P ankle L,
|P|=|L|=q^4, E=q^5, and any two vertices in P have <= 2 paths of length 4
between them (one-sided: NO guarantee for pairs in L, nor full
Theta_{4,4,4}-freeness). This script checks, for q=2,3:
  (a) edge density constant E/N^{5/4},
  (b) Theta_{4,4,4} (3 pairwise internally-disjoint length-4 paths)
      with endpoints both in P (must be 0 by Thm 2) vs both in L
      (may be nonzero -> NOT fully F-free -> cannot serve as A_n).
Bipartite + even path length => endpoints always on the same side.
stdlib only.
"""
import itertools
import json


def build_D4(q):
    pts = list(itertools.product(range(q), repeat=4))
    p_index = {p: i for i, p in enumerate(pts)}
    dirs = [tuple(pow(z, i, q) for i in range(4)) for z in range(q)]
    lines = []
    seen = set()
    for d in dirs:
        for x in pts:
            line = tuple(sorted(
                p_index[tuple((x[i] + y * d[i]) % q for i in range(4))]
                for y in range(q)))
            if line not in seen:
                seen.add(line)
                lines.append(line)
    nP, nL = len(pts), len(lines)
    N = nP + nL
    adj = [set() for _ in range(N)]
    for li, line in enumerate(lines):
        v = nP + li
        for u in line:
            adj[u].add(v)
            adj[v].add(u)
    return adj, nP, nL


def len4_paths(adj, s, t):
    out = []
    for a in adj[s]:
        if a == t:
            continue
        for b in adj[a]:
            if b == s or b == t:
                continue
            for c in adj[b]:
                if c == a or c == s:
                    continue
                if t in adj[c]:
                    vs = (s, a, b, c, t)
                    if len(set(vs)) == 5:
                        out.append(vs)
    return out


def has_theta(adj, s, t):
    paths = len4_paths(adj, s, t)
    if len(paths) < 3:
        return False
    for combo in itertools.combinations(range(len(paths)), 3):
        used = set()
        ok = True
        for idx in combo:
            internal = set(paths[idx][1:-1])
            if internal & used:
                ok = False
                break
            used |= internal
        if ok:
            return True
    return False


def side_count(adj, verts):
    n = 0
    ex = None
    for i in range(len(verts)):
        for j in range(i + 1, len(verts)):
            if has_theta(adj, verts[i], verts[j]):
                n += 1
                if ex is None:
                    ex = (verts[i], verts[j])
    return n, ex


res = {}
for q in (2, 3):
    adj, nP, nL = build_D4(q)
    N = nP + nL
    E = sum(len(a) for a in adj) // 2
    pp, exPP = side_count(adj, list(range(nP)))
    ll, exLL = side_count(adj, list(range(nP, N)))
    res[q] = {
        "N": N, "E": E,
        "E_over_N54": E / (N ** 1.25),
        "PP_theta_pairs": pp, "PP_example": exPP,
        "LL_theta_pairs": ll, "LL_example": exLL,
    }
    print(q, res[q])

with open("r1_D4_freeness.json", "w") as f:
    json.dump(res, f, indent=2)
print("wrote r1_D4_freeness.json")
