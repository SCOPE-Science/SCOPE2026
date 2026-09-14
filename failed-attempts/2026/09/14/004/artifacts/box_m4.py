"""Combined m=4 box: enumerate minimal elements of I^(4) once, test vs I^2 and I^3 gens.
Box {0..4}^10 = 9765625. Chunked numpy. Saves certificate."""
import numpy as np, itertools, json, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1804/output/artifacts')
from petersen_core import EDGES, all_minimal_covers
covers = all_minimal_covers()
A = np.array([[(m >> v) & 1 for v in range(10)] for m in covers], dtype=np.int64)
E = np.array(EDGES, dtype=np.int64)
def edge_gens(r):
    gens = set()
    for combo in itertools.combinations_with_replacement(range(len(E)), r):
        g = [0]*10
        for e in combo:
            g[E[e][0]] += 1; g[E[e][1]] += 1
        gens.add(tuple(g))
    return np.array(sorted(gens), dtype=np.int64)
G2 = edge_gens(2); G3 = edge_gens(3)
print("I^2 gens:", len(G2), "I^3 gens:", len(G3), flush=True)
M = 4; B = 5; N = B**10
divs = np.array([B**k for k in range(10)], dtype=np.int64)
minimals = []
nfeas = 0
CH = 1 << 20
for start in range(0, N, CH):
    idx = np.arange(start, min(start+CH, N), dtype=np.int64)
    X = ((idx[:, None] // divs[None, :]) % B).astype(np.int64)
    S = X @ A.T
    feas = S.min(axis=1) >= M
    nfeas += int(feas.sum())
    F = X[feas]; SF = S[feas]
    ismin = np.ones(len(F), dtype=bool)
    for v in range(10):
        W = ((SF == M) & (A[None, :, v] == 1)).any(axis=1)
        ismin &= (~(F[:, v] > 0) | W)
    minimals.extend([tuple(map(int, F[i])) for i in np.nonzero(ismin)[0]])
    print(f"chunk {start//CH}: feas={nfeas} minimals={len(minimals)}", flush=True)
print("TOTAL minimals:", len(minimals), flush=True)
Mb = np.array(sorted(minimals), dtype=np.int64)
def test(G, name):
    bad = []
    for i in range(0, len(Mb), 1024):
        D = (Mb[i:i+1024, None, :] >= G[None, :, :]).all(axis=2)
        ok = D.any(axis=1)
        for j in np.nonzero(~ok)[0]:
            bad.append(tuple(map(int, Mb[i+j])))
    print(f"{name}: failures={len(bad)}", flush=True)
    for b in bad[:10]:
        print("  fail:", b, "deg", sum(b), flush=True)
    return bad
bad2 = test(G2, "I^(4) vs I^2")
bad3 = test(G3, "I^(4) vs I^3")
json.dump({'minimals': [list(a) for a in sorted(minimals)],
           'fail_vs_I2': [list(a) for a in bad2],
           'fail_vs_I3': [list(a) for a in bad3]},
          open('contain4_certificate.json', 'w'))
print("saved.", flush=True)
