"""One-scale Hilbert/expander check (TARGET route R2, proxy level).
Builds a concrete 3-regular expander, certifies classical gap eta = 1-lam2/d,
computes all-pairs word-metric stats via BFS, and evaluates the distortion-template
numbers D >= sqrt(eta*Abar) [Hilbert-Poincare] and D >= sqrt(E[d(Zt,Z0)^2]/(M^2 t)).
Stdlib + numpy only. Writes output/artifacts/one_scale_check.json
"""
import json, collections, random
import numpy as np

random.seed(607); np.random.seed(607)
n, d = 200, 3

def random_regular(n, d):
    assert (n*d) % 2 == 0
    while True:
        stubs = list(range(n))*d
        random.shuffle(stubs)
        E = set()
        ok = True
        for i in range(0, len(stubs), 2):
            u, v = stubs[i], stubs[i+1]
            if u == v or (u, v) in E or (v, u) in E:
                ok = False; break
            E.add((u, v))
        if not ok:
            continue
        adj = [set() for _ in range(n)]
        for u, v in E:
            adj[u].add(v); adj[v].add(u)
        if any(len(a) != d for a in adj):
            continue
        # connected?
        seen = {0}; q = collections.deque([0])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in seen:
                    seen.add(w); q.append(w)
        if len(seen) == n:
            return adj

adj = random_regular(n, d)
A = np.zeros((n, n))
for u in range(n):
    for w in adj[u]:
        A[u, w] = 1.0
evals = np.linalg.eigvalsh(A)
lam2 = float(sorted(evals, reverse=True)[1])
eta = 1.0 - lam2/d

# BFS all-pairs
from collections import deque
Dmat = np.zeros((n, n), dtype=int)
for s in range(n):
    dist = [-1]*n; dist[s] = 0; q = deque([s])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if dist[w] < 0:
                dist[w] = dist[u]+1; q.append(w)
    Dmat[s] = dist
D2 = Dmat.astype(float)**2
Abar = float(D2[np.eye(n) == 0].mean())  # avg squared distance over ordered u!=v incl all pairs
Abar_all = float(D2.mean())
# radius bound: half pairs at distance >= r0?
import math
r0 = math.floor(math.log(n/4, d-1))
frac_far = float((Dmat >= r0).mean())

hilb_lb = math.sqrt(eta*Abar_all)
# Markov-template at mixing time t = ceil(log(4 sqrt(n))/eta)
t = math.ceil(math.log(4*math.sqrt(n))/eta)
markov_number = math.sqrt((0.75*Abar_all)/t)  # = D*M lower bound numerator: D >= number/M

out = {
    "n": n, "d": d, "lam2": lam2, "eta": eta,
    "avg_sq_dist_all": Abar_all, "avg_sq_dist_offdiag": Abar,
    "r0_floor_log": r0, "frac_pairs_dist_ge_r0": frac_far,
    "hilbert_distortion_lb_sqrt_eta_Abar": hilb_lb,
    "mixing_t": t, "markov_numeratorsqrt_0_75Abar_over_t": markov_number,
    "note": "Proxy one-scale level only; NOT the named Mendel-Naor levels.",
}
with open("output/artifacts/one_scale_check.json", "w") as f:
    json.dump(out, f, indent=2)
print(json.dumps(out, indent=2))
