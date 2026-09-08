"""Vectorized Betti census: all 2^15 labeled graphs on 6 vertices.
Hochster: b(Z_K) = 1 + sum_{J nonempty} (tilde b0(K_J) + tilde b1(K_J)),
tilde b0 = comp-1, tilde b1 = E-V+comp. Connectivity via full-mask comp.
Stdlib+numpy only."""
import numpy as np, json

N = 6
EDGES = [(i, j) for i in range(N) for j in range(i+1, N)]
M = len(EMDGES_) if False else len(EDGES)
NG = 1 << M  # 32768
G = ((np.arange(NG)[:, None] >> np.arange(M)) & 1).astype(np.int64)  # 32768x15
EMASK = np.array([(1 << i) | (1 << j) for (i, j) in EDGES])

# neighbor bitmasks per graph: NBM[g,i]
NBM = np.zeros((NG, N), dtype=np.int64)
for e, (i, j) in enumerate(EDGES):
    NBM[:, i] |= (G[:, e] << j)
    NBM[:, j] |= (G[:, e] << i)
A = ((NBM[:, :, None] >> np.arange(N)) & 1).astype(np.int64)  # 32768x6x6
APLUS = A.copy()
for i in range(N):
    APLUS[:, i, i] = 1
APLUS = APLUS.astype(bool)

def comps_for_mask(J):
    inJ = np.array([(J >> i) & 1 for i in range(N)], dtype=bool)
    V = int(inJ.sum())
    L = np.where(inJ[None, :], np.arange(N)[None, :], 99).astype(np.int64)
    for _ in range(N):
        cand = np.where(APLUS, L[:, None, :], 99)
        L = cand.min(axis=2)
        L = np.where(inJ[None, :], L, 99)
    # count distinct labels among nodes in J
    Ls = L.copy()
    # distinct count per row over masked entries
    out = np.zeros(NG, dtype=np.int64)
    for v in range(N):
        if inJ[v]:
            out += ((L == v).sum(axis=1) > 0).astype(np.int64)
    return out, V

b = np.ones(NG, dtype=np.int64)
conn = np.zeros(NG, dtype=bool)
for J in range(1, 64):
    einJ = ((EMASK & ~J) == 0)
    E = G @ einJ.astype(np.int64)
    comp, V = comps_for_mask(J)
    b += E - V + 2 * comp - 1
    if J == 63:
        conn = (comp == 1)

bc = b[conn]
alle = (G * np.array([1 if True else 0 for _ in range(M)])).sum(axis=1)
print("connected count:", int(conn.sum()))
print("max b (connected):", int(bc.max()))
print("min b (connected):", int(bc.min()))
idx = np.where(conn & (b == bc.max()))[0]
print("num labeled maximizers:", len(idx))
# edge counts among maximizers
print("edges of maximizers:", sorted(set(int(G[i].sum()) for i in idx)))
# distribution of b values (connected)
vals, counts = np.unique(bc, return_counts=True)
print("b-value histogram (connected):", list(zip(vals.tolist(), counts.tolist())))
# top two distinct values -> gap
s = sorted(set(bc.tolist()), reverse=True)
print("top values:", s[:4])
# save maximizer adjacency bitmasks + one representative edge list
rep = int(idx[0])
print("rep idx:", rep, "edges:", [EDGES[e] for e in range(M) if (rep >> e) & 1])
json.dump({"max_b": int(bc.max()), "runner_up": s[1], "gap": s[0]-s[1],
           "n_max_labeled": len(idx),
           "max_edge_count": sorted(set(int(G[i].sum()) for i in idx)),
           "rep_idx": rep,
           "rep_edges": [EDGES[e] for e in range(M) if (rep >> e) & 1],
           "hist": list(zip(vals.tolist(), counts.tolist()))},
          open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-162/output/artifacts/graph_census.json", "w"))
