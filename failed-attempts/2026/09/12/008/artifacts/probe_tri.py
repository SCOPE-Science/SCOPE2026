"""Recovery-test proxy: triangular-lattice SITE percolation at p=1/2 (exactly critical).

NOT the Voronoi target model. Purpose: diagnose the scaling shapes of the
billed template (total influence exponent, OSSS-implied floor exponent) to test
whether an elementary route can reach the claimed 0.02 n^{-1/2} floor.
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
    cross = 0
    piv_c = 0
    piv_r = 0
    cx = cy = n // 2
    for _ in range(trials):
        g = rng.random((n, n)) < 0.5
        c0 = has_crossing(g)
        cross += c0
        g2 = g.copy()
        g2[cx, cy] = not g2[cx, cy]
        piv_c += (has_crossing(g2) != c0)
        ix = int(rng.integers(0, n))
        iy = int(rng.integers(0, n))
        g3 = g.copy()
        g3[ix, iy] = not g3[ix, iy]
        piv_r += (has_crossing(g3) != c0)
    p = cross / trials
    var = p * (1 - p)
    avg_inf = piv_r / trials
    sum_inf = n * n * avg_inf
    osss = var / sum_inf if sum_inf > 0 else float("nan")
    ss_shape = sum_inf ** 2 / (n * n) if sum_inf > 0 else float("nan")
    return dict(n=n, trials=trials, p=round(p, 4), var=round(var, 5),
                center_piv=round(piv_c / trials, 6),
                sumInf=round(sum_inf, 4),
                osss_floor=round(osss, 6),
                ss_shape=round(ss_shape, 6),
                claimed=round(0.02 * n ** -0.5, 6),
                witness=round(1.0 / n, 6))

if __name__ == "__main__":
    rows = []
    for n, tr, sd in [(8, 8000, 1), (12, 6000, 2), (16, 5000, 3),
                      (24, 3000, 4), (32, 2000, 5), (48, 1200, 6)]:
        t0 = time.time()
        d = estimate(n, tr, sd)
        rows.append(d)
        print(d, f"time={time.time()-t0:.1f}s", flush=True)
    xs = np.log([r["n"] for r in rows])
    ys = np.log([r["sumInf"] for r in rows])
    slope = float(np.polyfit(xs, ys, 1)[0])
    print(f"EXPONENT_FIT sumInf ~ n^{slope:.3f} (exact four-arm scaling predicts 0.75)",
          flush=True)
    for r in rows:
        print(f"n={r['n']}: osss={r['osss_floor']} ss_shape={r['ss_shape']} "
              f"claimed={r['claimed']} witness={r['witness']} var={r['var']}",
              flush=True)
