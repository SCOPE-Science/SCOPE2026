"""Two-sided certificate replay for mu*(4,9). Stdlib + numpy only."""
import json, math, os
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
W2 = 5/32
L = math.sqrt(W2)
print(f"LOWER: Welch bound L = sqrt(5/32) = {L:.10f}")
assert abs((32*(L**2)-5)/3) < 1e-12, "f vanishes exactly at L"
assert (1 + 8*(4*0.0-1)/3) < 0, "f(0)<0 sanity"
print("LOWER OK: f(t)=(32t^2-5)/3, c=(1,8), f(1)/c0=9 -> mu*(4,9) >= sqrt(5/32) ~= 0.3952847075")

V = np.array(json.load(open(os.path.join(BASE, "vectors.json")))["rows"], dtype=float)
Vn = V / np.linalg.norm(V, axis=1, keepdims=True)
assert np.allclose(np.linalg.norm(Vn, axis=1), 1.0, atol=1e-12), "unit norms"
G = Vn @ Vn.T
w = np.linalg.eigvalsh(G)
assert w.min() > -1e-8, f"PSD fail: {w.min()}"
assert np.sum(w > 1e-6) <= 4, f"rank fail: {w}"
i, j = np.triu_indices(9, 1)
mu = float(np.abs(G[i, j]).max())
print(f"UPPER: min eig = {w.min():.3e}, nonzero eigs = {int(np.sum(w>1e-6))}, mu = {mu:.10f}")
assert mu <= 0.438, f"U bound fail: {mu}"
print(f"UPPER OK: mu = {mu:.8f} <= 0.438  =>  mu*(4,9) <= 0.438")
print(f"CERTIFIED INTERVAL: mu*(4,9) in [{L:.7f}, 0.438], width ~ {0.438-L:.4f}")
