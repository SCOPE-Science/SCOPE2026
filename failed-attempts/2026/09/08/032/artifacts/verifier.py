"""Independent verifier for the theta-vs-Hoffman strictness witness (stdlib + numpy only).
Checks: cubic/connected/triangle-free (exact integer), h from spectrum (recomputed),
primal X feasibility for theta(complement) -> certified lower bound, exact alpha by
branch-and-bound replay, alpha-set independence, sandwich h <= theta_LB <= alpha.
Exit 0 on PASS, nonzero on FAIL."""
import json, sys
import numpy as np

W = json.load(open("output/artifacts/witness_RTF_seed77.json"))
A = np.array(W["adj"], dtype=int)
X = np.array(W["X"])
n = A.shape[0]
assert A.shape == (18, 18), A.shape
assert (A == A.T).all() and (np.diag(A) == 0).all()
assert set(np.unique(A)) <= {0, 1}
assert bool((A.sum(1) == 3).all()), "not cubic"
seen = {0}; st = [0]
while st:
    u = st.pop()
    for v in np.where(A[u])[0].tolist():
        if v not in seen:
            seen.add(v); st.append(v)
assert len(seen) == 18, "disconnected"
for i in range(n):
    for j in range(i + 1, n):
        if A[i, j]:
            assert not np.logical_and(A[i], A[j]).any(), "triangle at %d-%d" % (i, j)
print("graph checks: cubic/connected/triangle-free OK")

w = np.linalg.eigvalsh(A.astype(float))
lmin = float(w[0]); h = 1 + 3 / (-lmin)
assert abs(h - W["h"]) < 1e-9, (h, W["h"])
assert abs(lmin - W["lmin"]) < 1e-9
print("h recomputed = %.10f (lmin=%.10f) matches claim" % (h, lmin))

for i in range(n):
    for j in range(n):
        if i != j and A[i, j] == 0:
            assert abs(X[i, j]) < 1e-9, (i, j, X[i, j])
m = float(np.linalg.eigvalsh((X + X.T) / 2)[0])
tr = float(np.trace(X)); s = float(X.sum())
assert m >= -1e-9, m
assert abs(tr - 1) < 1e-9, tr
assert abs(s - W["theta_lb"]) < 1e-9, (s, W["theta_lb"])
print("primal feasible: sum=%.10f psdmin=%.2e trace=%.12f" % (s, m, tr))
print("certified theta(complement) - h >= %.10f" % (s - h))
assert s - h >= 0.12, "gap margin check"

adj = [0] * n
for i in range(n):
    mm = 0
    for j in range(n):
        if A[i, j]:
            mm |= 1 << j
    adj[i] = mm
best = [0]
def bb(cand, cur):
    if cand == 0:
        best[0] = max(best[0], cur); return
    if cur + bin(cand).count("1") <= best[0]:
        return
    c = cand; v = -1; bd = -1
    while c:
        lsb = c & -c; u = lsb.bit_length() - 1
        d = bin(adj[u] & cand).count("1")
        if d > bd:
            bd = d; v = u
        c ^= lsb
    bb(cand & ~((1 << v) | adj[v]), cur + 1)
    bb(cand & ~(1 << v), cur)
bb((1 << n) - 1, 0)
assert best[0] == W["alpha"] == 8, (best[0], W["alpha"])
sset = [i for i in range(n) if (W["alpha_set"] >> i) & 1]
assert len(sset) == 8 and all(A[i, j] == 0 for a, i in enumerate(sset) for j in sset[a + 1:])
print("alpha replayed = 8; witness independent set", sset)
assert h - 1e-9 <= s <= 8 + 1e-9
print("sandwich h <= theta_LB <= alpha holds")
print("VERIFIER PASS")
