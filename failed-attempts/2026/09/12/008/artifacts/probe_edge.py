"""Decisive probe: edge/corner pivotality vs claimed floor (triangular site, p=1/2).

Routes R1 (OSSS total) and R2-bulk (central pivotal) are already rate-blocked.
This tests the last elementary rescue: max_i Inf_i via boundary cells.
NOT the Voronoi target model; diagnostic of scaling shapes only.
"""
import time
from collections import deque
import numpy as np

NBS = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, -1))

def has_crossing(grid):
    n = grid.shape[0]
    visited = np.zeros_like(grid, dtype=bool)
    q = deque()
    for r in range(n):
        if grid[r, 0]:
            visited[r, 0] = True
            q.append((r, 0))
    while q:
        r, c = q.popleft()
        if c == n - 1:
            return True
        for dr, dc in NBS:
            rr, cc = r + dr, c + dc
            if 0 <= rr < n and 0 <= cc < n and grid[rr, cc] and not visited[rr, cc]:
                visited[rr, cc] = True
                q.append((rr, cc))
    return False

def estimate(n, trials, seed):
    rng = np.random.default_rng(seed)
    pts = {
        "center": (n // 2, n // 2),
        "edge_mid_left": (n // 2, 0),
        "edge_mid_top": (0, n // 2),
        "corner": (0, 0),
    }
    piv = {k: 0 for k in pts}
    for _ in range(trials):
        g = rng.random((n, n)) < 0.5
        c0 = has_crossing(g)
        for k, (ix, iy) in pts.items():
            g2 = g.copy()
            g2[ix, iy] = not g2[ix, iy]
            piv[k] += (has_crossing(g2) != c0)
    out = {k: v / trials for k, v in piv.items()}
    out["claimed"] = 0.02 * n ** -0.5
    out["n"] = n
    return out

if __name__ == "__main__":
    for n, tr, sd in [(16, 4000, 11), (32, 2000, 12), (48, 1200, 13)]:
        t0 = time.time()
        print(estimate(n, tr, sd), f"time={time.time()-t0:.1f}s", flush=True)
