"""Batch A experiments for lane-20324 target (7-regular non-bipartite Ramanujan infinitude).

A1: Exhaustive small-order census (n=8: K8; n=10: complements of 2-regular graphs).
A2: Signing search on K8: one-sided (MSS) vs two-sided (Bilu-Linial-type) feasibility;
    plus an explicit one-sided-good / two-sided-bad certificate signing.
A3: Random 7-regular graphs: exact two-sided Ramanujan frequency vs n
    (tests whether the probabilistic route can give infinitude).
"""
import json
import math
import random
import numpy as np
import networkx as nx

BOUND7 = 2 * math.sqrt(6)
TOL = 1e-9
rng = random.Random(20260915)
np.random.seed(20260915)

results = {"bound_7": BOUND7}


def spec(G):
    return np.sort(np.linalg.eigvalsh(nx.to_numpy_array(G, dtype=float)))


def ram_status(G, d=7):
    """Return dict with connected / regular / nonbipartite / one-sided / two-sided Ramanujan flags."""
    w = spec(G)
    conn = nx.is_connected(G)
    top_mult_1 = bool(np.sum(w > d - 1e-6) == 1)
    nontrivial = w[w < d - 1e-6]
    lam2 = float(nontrivial[-1]) if len(nontrivial) else None
    lamn = float(w[0])
    one_sided = bool(lam2 is not None and lam2 <= BOUND7 + 1e-7)
    two_sided = bool(one_sided and abs(lamn) <= BOUND7 + 1e-7)
    nonbip = bool(abs(lamn + d) > 1e-6)  # connected regular: bipartite <=> lam_n == -d
    return {"connected": bool(conn), "top_simple": top_mult_1, "lambda2": lam2,
            "lambda_n": lamn, "nonbipartite": nonbip,
            "one_sided_Ram": one_sided, "two_sided_Ram": two_sided}


# ---------------- A1: small census ----------------
A1 = {}
A1["K8"] = ram_status(nx.complete_graph(8))
# 7-regular on 10 vertices <=> complement of 2-regular <=> cycle-type partitions of 10 (parts>=3)
parts_list = [[10], [7, 3], [6, 4], [5, 5], [4, 3, 3]]
A1["n10"] = []
for parts in parts_list:
    H = nx.Graph()
    v = 0
    for L in parts:
        cyc = list(range(v, v + L))
        H.add_edges_from((cyc[i], cyc[(i + 1) % L]) for i in range(L))
        v += L
    G = nx.complement(H)
    assert all(d == 7 for _, d in G.degree())
    st = ram_status(G)
    st["complement_cycle_type"] = parts
    A1["n10"].append(st)
results["A1_small_census"] = A1

# ---------------- A2: signings of K8 ----------------
A = nx.to_numpy_array(nx.complete_graph(8), dtype=float)
iu = np.triu_indices(8, 1)
m = len(iu[0])


def spec_of_sign(s):
    As = np.zeros((8, 8))
    As[iu] = s
    As[(iu[1], iu[0])] = s
    w = np.linalg.eigvalsh(As)
    return w


def radius(s):
    w = spec_of_sign(s)
    return float(max(w[-1], -w[0])), float(w[-1]), float(w[0])


best_two = (1e9, None)   # spectral radius
best_one = (1e9, None)   # lambda max
cert = None              # one-sided good but two-sided bad
N_RAND = 40000
for _ in range(N_RAND):
    s = np.random.choice([-1.0, 1.0], size=m)
    rho, lmax, lmin = radius(s)
    if rho < best_two[0]:
        best_two = (rho, s.copy())
    if lmax < best_one[0]:
        best_one = (lmax, s.copy())
    if cert is None and lmax <= BOUND7 + 1e-9 and (-lmin) > BOUND7 + 1e-9:
        cert = {"lmax": lmax, "lmin": lmin,
                "signing_rows": (np.where(np.eye(8) == 0, 0, 0) is None) and None or None,
                }


def local_search(s0, objective, passes=6):
    s = s0.copy()
    cur, _, _ = radius(s)
    if objective == "one":
        cur = radius(s)[1]
    for _ in range(passes):
        improved = False
        order = list(range(m))
        rng.shuffle(order)
        for j in order:
            s[j] *= -1.0
            r, lmax, _ = radius(s)
            val = lmax if objective == "one" else r
            if val < cur - 1e-12:
                cur = val
                improved = True
            else:
                s[j] *= -1.0
        if not improved:
            break
    r, lmax, lmin = radius(s)
    return s, r, lmax, lmin


for start, obj in [("two", "two")] * 12 + [("one", "one")] * 6:
    s0 = np.random.choice([-1.0, 1.0], size=m)
    s, r, lmax, lmin = local_search(s0, obj)
    if r < best_two[0]:
        best_two = (r, s.copy())
    if lmax < best_one[0]:
        best_one = (lmax, s.copy())
    if cert is None and lmax <= BOUND7 + 1e-9 and (-lmin) > BOUND7 + 1e-9:
        pass  # already have one

# rebuild a clean certificate signing explicitly (deterministic rescan)
cert_mat = None
for t in range(200000):
    s = np.random.choice([-1.0, 1.0], size=m)
    r, lmax, lmin = radius(s)
    if lmax <= BOUND7 + 1e-9 and (-lmin) > BOUND7 + 1e-9:
        As = np.zeros((8, 8))
        As[iu] = s
        As[(iu[1], iu[0])] = s
        cert_mat = {"seed_draw": t, "lmax": lmax, "lmin": lmin,
                    "matrix": [[float(x) for x in row] for row in As]}
        break

results["A2_signings_K8"] = {
    "n_random": N_RAND,
    "best_spectral_radius": best_two[0],
    "best_spectral_radius_le_bound": bool(best_two[0] <= BOUND7 + 1e-9),
    "best_one_sided_lmax": best_one[0],
    "one_sided_feasible": bool(best_one[0] <= BOUND7 + 1e-9),
    "certificate_one_sided_good_two_sided_bad": cert_mat,
}

# ---------------- A3: random 7-regular, Ramanujan frequency vs n ----------------
A3 = {}
for n, trials in [(16, 300), (40, 150), (100, 60), (200, 25), (500, 10)]:
    twos = 0
    ones = 0
    nonb = 0
    vals = []
    for t in range(trials):
        G = nx.random_regular_graph(7, n, seed=1000000 + n * 1000 + t)
        st = ram_status(G)
        vals.append(max(st["lambda2"], abs(st["lambda_n"])))
        twos += st["two_sided_Ram"]
        ones += st["one_sided_Ram"]
        nonb += st["nonbipartite"]
    vals = np.array(vals)
    A3[str(n)] = {"trials": trials, "two_sided_frac": twos / trials,
                  "one_sided_frac": ones / trials, "nonbip_frac": nonb / trials,
                  "mean_max": float(vals.mean()), "min_max": float(vals.min()),
                  "max_max": float(vals.max())}
results["A3_random_freq"] = A3

with open("output/artifacts/exp_results.json", "w") as f:
    json.dump(results, f, indent=1)
print(json.dumps({k: (v if k != "A2_signings_K8" else {kk: vv for kk, vv in v.items() if kk != "certificate_one_sided_good_two_sided_bad"})
                  for k, v in results.items()}, indent=1))
print("CERT:", json.dumps({k: v for k, v in (cert_mat or {}).items() if k != "matrix"}))
print("BOUND:", BOUND7)
