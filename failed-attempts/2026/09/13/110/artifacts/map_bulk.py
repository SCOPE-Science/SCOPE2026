"""Support/spectrum map for lane-1731: bulk (Brown proxy) vs s_min (spectrum proxy)."""
import numpy as np

ev = np.load("output/artifacts/ev_lane1731_N700.npy")
print("n =", ev.size)
x = ev.real
y = ev.imag
print("Re range:", x.min(), x.max(), " Im range:", y.min(), y.max())
print("frac Im==0 (tol 1e-9):", float(np.mean(np.abs(y) < 1e-9)))
print("frac |Im|<0.05:", float(np.mean(np.abs(y) < 0.05)))
# box occupancy on [-4,4]^2 with 0.5 boxes -> hole search
B = 0.5
gx = np.floor((x + 4) / B).astype(int)
gy = np.floor((y + 4) / B).astype(int)
occ = {}
for a, b in zip(gx, gy):
    if 0 <= a < 16 and 0 <= b < 16:
        occ[(a, b)] = occ.get((a, b), 0) + 1
empty = [(a, b) for a in range(16) for b in range(16) if (a, b) not in occ]
print("empty boxes (center):", [(round(-4 + (a + .5) * B, 2), round(-4 + (b + .5) * B, 2)) for a, b in empty])
# low-count boxes
low = sorted(occ.items(), key=lambda kv: kv[1])[:12]
print("lowest-count boxes:", [((round(-4 + (a + .5) * B, 2), round(-4 + (b + .5) * B, 2)), c) for (a, b), c in low])
# radial profile in annuli
edges = [0, .1, .25, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 8]
r = np.abs(ev)
for lo, hi in zip(edges[:-1], edges[1:]):
    print(f"annulus [{lo},{hi}):", int(np.sum((r >= lo) & (r < hi))))
