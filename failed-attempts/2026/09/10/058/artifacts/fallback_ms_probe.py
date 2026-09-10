"""Fallback probe: bulk mean-square QUE error for canonical half-volume a*.
Y_n = (1/Nbulk) sum_{j in I0} X_j^2, X_j = sum_{i<=n/2} psi_j(i)^2 - 1/2.
Also reports n*Y_n (Gaussian heuristic predicts O(1)) and Nbulk/n (KM ~0.30).
Stdlib + numpy only, seeded.
"""
import numpy as np, json

def random_3regular(n, rng, max_try=300):
    assert n % 2 == 0
    for _ in range(max_try):
        stubs = np.repeat(np.arange(n), 3)
        rng.shuffle(stubs)
        A = np.zeros((n, n))
        ok = True
        for k in range(0, 3 * n, 2):
            u, v = int(stubs[k]), int(stubs[k + 1])
            if u == v or A[u, v] == 1:
                ok = False; break
            A[u, v] = A[v, u] = 1.0
        if ok:
            return A
    raise RuntimeError("no simple realization")

rng = np.random.default_rng(20260910)
rec = {}
for n in [200, 400, 800]:
    trials = 4 if n <= 400 else 2
    rows = []
    for t in range(trials):
        A = random_3regular(n, rng)
        w, V = np.linalg.eigh(A)
        m = (w >= -1.0) & (w <= 1.0)
        P = V[:, m] ** 2
        X = P[:n // 2, :].sum(axis=0) - 0.5
        Y = float((X ** 2).mean())
        rows.append({"Y": Y, "nY": n * Y, "Nbulk": int(m.sum())})
    rec[str(n)] = rows
    for r in rows:
        print(f"n={n} Nbulk/n={r['Nbulk']/n:.3f} Y={r['Y']:.6f} nY={r['nY']:.3f}", flush=True)
with open("artifacts_ms_probe.json", "w") as f:
    json.dump(rec, f, indent=1)
# threshold check: bound (log n)^C0/sqrt(n) with C0=6 vs observed Y
import math
for n in [200, 400, 800]:
    for r in rec[str(n)]:
        thr = (math.log(n) ** 6) / math.sqrt(n)
        print(f"n={n} Y={r['Y']:.2e} thr(C0=6)={thr:.2e} hold={r['Y'] <= thr}")
