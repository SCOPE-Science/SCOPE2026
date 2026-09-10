"""Replay-verifier for the emergent obstruction certificate. Stdlib+numpy only. Prints VERIFY_OK on success."""
import json, math, itertools, sys
from collections import deque
sys.path.insert(0, "output/artifacts")
from delayer_strategy import load, build, simulate, delayer_move, consistent

adj = load(); n, edges, emap = build(adj)
m = len(edges)
tau = [0]*n; tau[0] = 1

# 1. Graph: 60 vertices, 3-regular, simple, undirected
assert n == 60, n
assert m == 90, m
for u in range(n):
    assert len(adj[u]) == 3 and u not in adj[u] and len(set(adj[u])) == 3
    for v in adj[u]:
        assert u in adj[v]
print("[1] graph: 60 vertices, 3-regular, simple, symmetric OK; edges =", m)

# 2. Ramanujan spectrum (recomputed): lambda* <= 2*sqrt(2)
import numpy as np
A = np.zeros((n, n))
for u in range(n):
    for v in adj[u]:
        A[u, v] = 1.0
w = np.sort(np.linalg.eigvalsh(A))
lam = max(abs(x) for x in w if abs(x - 3) > 1e-6)
assert lam <= 2*math.sqrt(2), lam
assert abs((w**2).sum() - 180.0) < 1e-6  # tr A^2 = n*d
print(f"[2] Ramanujan OK: lambda*={lam:.6f} <= 2sqrt2={2*math.sqrt(2):.6f}; trA^2={(w**2).sum():.2f}")

# 3. Exact small-set edge-boundaries: k=1 ->3, k=2 ->4, k=3 ->5, k=4 ->4
def eb(S):
    S = set(S); b = 0
    for u in S:
        for v in adj[u]:
            if v not in S: b += 1
    return b
expect = {1: 3, 2: 4, 3: 5, 4: 4}
for k, e in expect.items():
    best = min(eb(S) for S in itertools.combinations(range(n), k))
    assert best == e, (k, best, e)
    print(f"[3] exact min edge-boundary k={k}: {best} OK")

# 4. Trap certificate: for EVERY edge, 5-query trap prover holds naive Delayer to score 4
ndead = 0
for (uu, vv) in edges:
    xu = [x for x in adj[uu] if x != vv]; xv = [x for x in adj[vv] if x != uu]
    e = lambda a, b: emap[(min(a,b), max(a,b))]
    o = [e(uu,xu[0]), e(uu,xu[1]), e(vv,xv[0]), e(vv,xv[1]), e(uu,vv)]
    vals = {o[0]:0, o[1]:0, o[2]:1^tau[uu]^tau[vv], o[3]:0}
    s, tr = simulate(n, adj, emap, edges, tau, o, lambda ei,a,u: vals.get(ei,0))
    assert s == 4, ((uu,vv), s)
    # legality: every '*' was a legal deferral; game ended in genuine clause falsification
    assign = {}; unset = set(range(m))
    for (ei, mv, val) in tr:
        assert delayer_move(n, adj, emap, edges, tau, assign, unset, ei) == mv, (ei, mv)
        assign[ei] = val if mv == '*' else mv
        unset.discard(ei)
    assert not consistent(n, adj, emap, edges, tau, assign, unset)
    # confirm a fully-assigned vertex with wrong parity exists
    uset = set(unset); rem = list(tau)
    for ei, val in assign.items():
        u, v = edges[ei]; rem[u] ^= val; rem[v] ^= val
    bad = [x for x in range(n) if all(emap[(min(x,v),max(x,v))] not in uset for v in adj[x]) and (rem[x]&1)]
    assert bad, "no falsified clause"
    ndead += 1
print(f"[4] trap certificate OK: score=4 on all {ndead}/90 edges, each ending in falsified vertex clause")

# 5. Conversion arithmetic: width 9 cannot yield length 4096
V = 90; w0 = 3; w = 9
bsw = math.exp((w-w0)**2/(16*V))
assert bsw < 1.2, bsw
assert 2**w == 512 < 4096
need = math.sqrt(math.log(4096)*16*V) + w0
assert need > 57, need
print(f"[5] conversion impossibility OK: BSW(w9)->{bsw:.4f}; 2^9=512<4096; width needed for 4096 via BSW>={need:.1f}")
print("VERIFY_OK")
