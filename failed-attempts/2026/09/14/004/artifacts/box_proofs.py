"""Finite minimal-element verification of I^(m) subset I^r for (3,2) and (4,3).
Descent lemma: if a feasible for m (all minimal-cover sums >= m) has a_v >= m+1,
then a - e_v is still feasible (covers through v had sum >= a_v >= m+1). Hence every
minimal feasible exponent lies in {0..m}^10, and every feasible dominates a minimal one.
So checking box minimals suffices. Membership in I^r = domination by an r-edge product."""
import numpy as np, itertools, json, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1804/output/artifacts')
from petersen_core import EDGES, all_minimal_covers

covers = all_minimal_covers()
A = np.array([[(m >> v) & 1 for v in range(10)] for m in covers], dtype=np.int64)  # 15x10
E = np.array(EDGES, dtype=np.int64)  # 15x2
print("covers:", A.shape, "edges:", E.shape, flush=True)

def edge_gens(r):
    """All exponent vectors of r-edge products (with repetition), deduplicated."""
    gens = set()
    for combo in itertools.combinations_with_replacement(range(len(E)), r):
        g = [0]*10
        for e in combo:
            g[E[e][0]] += 1; g[E[e][1]] += 1
        gens.add(tuple(g))
    return np.array(sorted(gens), dtype=np.int64)

def verify(m, r, chunksize=1 << 20):
    B = m + 1  # coordinate bound for minimals
    N = B ** 10
    G = edge_gens(r)
    print(f"(m,r)=({m},{r}): box {B}^10={N}, I^{r} gens={len(G)}", flush=True)
    divs = np.array([B ** k for k in range(10)], dtype=np.int64)
    n_feas_box = 0; minimals = []
    for start in range(0, N, chunksize):
        idx = np.arange(start, min(start + chunksize, N), dtype=np.int64)
        X = ((idx[:, None] // divs[None, :]) % B).astype(np.int64)  # (C,10)
        S = X @ A.T  # (C,15) cover sums
        feas = S.min(axis=1) >= m
        n_feas_box += int(feas.sum())
        F = X[feas]; SF = S[feas]
        # minimality: a-e_v infeasible for all v with a_v>0  <=>  exists cover through v with sum == m
        has_wit = np.zeros((len(F), 10), dtype=bool)
        for v in range(10):
            tryv = F[:, v] > 0
            # witness cover C containing v with SF == m
            W = ((SF == m) & (A[None, :, v] == 1)).any(axis=1)
            has_wit[:, v] = W
        ismin = np.array([bool((~has_wit[i][F[i] > 0]).sum() == 0) for i in range(len(F))])
        minimals.extend([tuple(map(int, F[i])) for i in np.nonzero(ismin)[0]])
        print(f"  chunk {start//chunksize}: feas-cumsum={n_feas_box}, minimals-cumsum={len(minimals)}", flush=True)
    print(f"minimals in box: {len(minimals)}", flush=True)
    # membership: each minimal dominates some gen
    M = np.array(sorted(minimals), dtype=np.int64)
    bad = []
    wit = {}
    for i in range(0, len(M), 2048):
        Mb = M[i:i+2048]
        # Mb (k,10), G (g,10): dominates iff (Mb[:,None,:] >= G[None,:,:]).all(axis=2).any(axis=1)
        D = (Mb[:, None, :] >= G[None, :, :]).all(axis=2)
        ok = D.any(axis=1)
        for j in np.nonzero(~ok)[0]:
            bad.append(tuple(map(int, Mb[j])))
        for j in np.nonzero(ok)[0]:
            wit[tuple(map(int, Mb[j]))] = tuple(map(int, G[int(np.nonzero(D[j])[0][0])]))
    print(f"failures (minimal in I^({m}) not in I^{r}): {len(bad)}", flush=True)
    return minimals, wit, bad

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else '32'
    if which == '32':
        minimals, wit, bad = verify(3, 2)
        json.dump({'minimals': [list(a) for a in sorted(minimals)],
                   'witness': {str(k): list(v) for k, v in wit.items()},
                   'failures': [list(a) for a in bad]},
                  open('contain32_certificate.json', 'w'))
        print("saved contain32_certificate.json")
    elif which == '43':
        minimals, wit, bad = verify(4, 3)
        json.dump({'minimals': [list(a) for a in sorted(minimals)],
                   'witness': {str(k): list(v) for k, v in wit.items()},
                   'failures': [list(a) for a in bad]},
                  open('contain43_certificate.json', 'w'))
        print("saved contain43_certificate.json")
