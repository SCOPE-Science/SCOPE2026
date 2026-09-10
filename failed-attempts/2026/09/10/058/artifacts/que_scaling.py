"""Bounded QUE-error scaling test, random 3-regular graphs.
Stdlib + numpy only. Seeded. Configuration model + simple-graph retry.
Measures for bulk eigenvectors (eigval in [-1,1]):
  E_half(j) = |sum_{i<n/2} psi_j(i)^2 - 1/2|   (canonical half-volume, sum-zero a*)
  E_rand(j) = |sum_i a(i) psi_j(i)^2| for 4 random sign vectors (sum zero)
  E_L1approx = proxy for sup over a via max over sampled a's.
Reports max over j in I0 per graph, averaged over trials.
Also checks sup-norm for contrast.
"""
import numpy as np, json

def random_3regular(n, rng, max_try=200):
    assert n % 2 == 0
    for _ in range(max_try):
        stubs = np.repeat(np.arange(n), 3)
        rng.shuffle(stubs)
        A = np.zeros((n, n), dtype=float)
        ok = True
        for k in range(0, 3 * n, 2):
            u, v = int(stubs[k]), int(stubs[k+1])
            if u == v or A[u, v] == 1:
                ok = False; break
            A[u, v] = A[v, u] = 1.0
        if ok:
            return A
    raise RuntimeError("no simple realization")

def que_stats(A, rng, nsign=4):
    n = A.shape[0]
    w, V = np.linalg.eigh(A)
    mask = (w >= -1.0) & (w <= 1.0)
    idx = np.where(mask)[0]
    P = V[:, idx] ** 2  # n x m
    m = len(idx)
    if m == 0:
        return None
    half = np.abs(P[:n//2, :].sum(axis=0) - 0.5)
    # random zero-sum sign observables
    er = half.copy()
    for _ in range(nsign):
        a = rng.choice([-1.0, 1.0], size=n)
        a -= a.mean()  # exactly zero-sum (values +-1 shifted); still bounded by 2
        e = np.abs(a @ P)
        er = np.maximum(er, e)
    supn = np.sqrt(n) * np.abs(V[:, idx]).max(axis=0)
    return dict(m=int(m), max_half=float(half.max()), mean_half=float(half.mean()),
                max_samp=float(er.max()), max_sup=float(supn.max()))

rng = np.random.default_rng(643)
out = {}
for n in [100, 200, 400, 800]:
    trials = 6 if n <= 400 else 3
    rows = []
    for t in range(trials):
        A = random_3regular(n, rng)
        rows.append(que_stats(A, rng))
    mh = float(np.mean([r["max_half"] for r in rows]))
    ms = float(np.mean([r["max_samp"] for r in rows]))
    mm = float(np.mean([r["m"] for r in rows]))
    out[str(n)] = dict(trials=trials, mean_max_half=mh, mean_max_samp=ms, mean_m=mm,
                       rows=rows)
    print(f"n={n} trials={trials} <m>={mm:.1f} meanMaxHalf={mh:.4f} meanMaxSamp={ms:.4f}", flush=True)

# fit power law meanMaxHalf ~ C n^{-gamma} using endpoints
import math
ns = sorted(int(k) for k in out)
ys = [out[str(n)]["mean_max_half"] for n in ns]
x0, x1, y0, y1 = math.log(ns[0]), math.log(ns[-1]), math.log(ys[0]), math.log(ys[-1])
gamma = -(y1 - y0) / (x1 - x0)
print(f"endpoint fitted decay gamma={gamma:.3f} (target per-vector rate alpha=1/4)")
print(json.dumps({k: {kk: v[kk] for kk in ("trials","mean_max_half","mean_max_samp","mean_m")} for k, v in out.items()}, indent=1))
with open("artifacts_que_scaling.json", "w") as f:
    json.dump(out, f, indent=1)
