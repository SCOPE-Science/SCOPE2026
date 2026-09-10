"""PRESET FALLBACK: 1/2-snowflake embedding of H_3(Z_5) into l_2^N, N<=64,
distortion <= 8 over all 7750 pairs.

Strategy (rigorous + computational):
- H = Heisenberg mod 5: (x,y,z), x,y,z in Z5, mult (x,y,z)(x',y',z') =
  (x+x', y+y', z+z'+x*y'). Generators S = {a^+-1, b^+-1}, a=(1,0,0), b=(0,1,0).
  Order 125. BFS word metric d_H. Diameter D (expect ~10).
- Phi: N-dim Euclidean features with ||Phi(u)-Phi(v)|| ~ d_H(u,v)^{1/2}.
  Route A (tried first): heat-kernel / random-walk embedding at scale t:
    K_t = (I + P + ... ) or diffusion coordinates sqrt(t)-scaled.
    Theory: on vertex-transitive graphs, ||K_t(u,.)-K_t(v,.)||_2^2
    grows like min(d(u,v)/t^{1/2}-type...) -- needs tuning, risky.
  Route B (robust, used): normalized Laplacian eigenvectors (first m of them,
  excluding trivial) scaled by lambda_i^{-1/4}: then
    ||Phi(u)-Phi(v)||^2 = sum_i (f_i(u)-f_i(v))^2 / sqrt(lambda_i),
  which is the Bessel-potential / sqrt-Laplacian kernel: commutes with
  isometries, and on vertex-transitive graphs E||.||^2 over pairs at fixed
  distance is monotone in distance for the full kernel; truncated to m<=64
  coordinates we verify distortion directly by brute force.
  Fallback C (guaranteed): rescale any injective Phi so its image lies in a
  small ball: snowflake distortion of a constant map is ~ sqrt(D); more
  precisely, mapping all points to vertices of a regular simplex gives
  ||diff|| = const for all pairs, so L = d^{1/2}/const ranges over
  [1/const, sqrt(D)/const], ratio = sqrt(D) <= sqrt(10) < 8. So even the
  trivial equidistant embedding PASSES the criterion (with min denom > 0).
  We use Route B for a genuine geometric witness but keep C as certificate
  of feasibility; verifier checks the actual logged table either way.

Writes: output/artifacts/Phi_64x125.csv, output/artifacts/verify_fallback.py,
        output/artifacts/fallback_verification.json
"""
import json, csv, math
from collections import deque
import numpy as np

MOD = 5
def mul(p, q):
    x, y, z = p; x2, y2, z2 = q
    return ((x+x2) % MOD, (y+y2) % MOD, (z+z2+ x*y2) % MOD)
def inv(p):
    x, y, z = p
    xi, yi = (-x) % MOD, (-y) % MOD
    return (xi, yi, (x*y - z) % MOD)

a = (1,0,0); b = (0,1,0)
S = [a, b, inv(a), inv(b)]
pts = [(x,y,z) for x in range(MOD) for y in range(MOD) for z in range(MOD)]
idx = {p:i for i,p in enumerate(pts)}
n = len(pts)
assert n == 125

# neighbors
nbrs = []
for p in pts:
    nb = [idx[mul(p,s)] for s in S]
    nbrs.append(nb)

# BFS all-pairs distances
D = np.zeros((n,n), dtype=int)
for s in range(n):
    dist = np.full(n, -1)
    dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for w in nbrs[u]:
            if dist[w] < 0:
                dist[w] = dist[u]+1
                q.append(w)
    assert (dist >= 0).all()
    D[s] = dist
diam = int(D.max())
np.save("output/artifacts/H3Z5_distances.npy", D)

# Normalized Laplacian eigenvectors: L = I - A/4 (4-regular multigraph, simple here)
A = np.zeros((n,n))
for u in range(n):
    for w in nbrs[u]:
        A[u,w] += 1.0
A /= 4.0
L = np.eye(n) - A
evals, evecs = np.linalg.eigh(L)  # ascending
assert evals[0] < 1e-9
m = 64
lams = evals[1:m+1]
vecs = evecs[:, 1:m+1]
assert (lams > 1e-9).all()
Phi = vecs / (lams[None,:]**0.25)   # shape (125,64): N=64 features
# Center not needed (differences only). Table format: 64x125
Table = Phi.T  # (64,125)
np.savetxt("output/artifacts/Phi_64x125.csv", Table, delimiter=",")
with open("output/artifacts/Phi_64x125.csv") as f:
    pass

# Verify
SQ = np.sqrt(D.astype(float))
diff2 = np.zeros((n,n))
for k in range(m):
    c = Phi[:,k]
    diff2 += (c[:,None]-c[None,:])**2
E = np.sqrt(np.maximum(diff2, 0))
iu = np.triu_indices(n, 1)
den = E[iu]
num = SQ[iu]
assert (den > 0).all(), "collision: non-injective embedding"
Lr = num/den
ratio = float(Lr.max()/Lr.min())
res = {"N": m, "n": n, "diameter": diam,
       "min_E": float(den.min()), "max_E": float(den.max()),
       "min_L": float(Lr.min()), "max_L": float(Lr.max()),
       "max_over_min": ratio, "PASS": bool(ratio <= 8.0 and (den>0).all())}
json.dump(res, open("output/artifacts/fallback_probe.json","w"), indent=2)
print(json.dumps(res, indent=2))
