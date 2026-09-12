import collections, time, math, sys
import numpy as np

def has_crossing(grid):
    n = grid.shape[0]
    visited = np.zeros_like(grid, dtype=bool)
    from collections import deque
    q = deque()
    for r in range(n):
        if grid[r, 0]:
            visited[r, 0] = True
            q.append((r, 0))
    while q:
        r, c = q.popleft()
        if c == n - 1:
            return True
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < n and 0 <= cc < n and not visited[rr, cc] and grid[rr, cc]:
                visited[rr, cc] = True
                q.append((rr, cc))
    return False

def estimate(n, trials=4000, seed=0):
    rng = np.random.default_rng(seed)
    cross = 0
    piv_center = 0
    piv_rand_sum = 0
    cx, cy = n // 2, n // 2
    for t in range(trials):
        g = rng.random((n, n)) < 0.5
        c0 = has_crossing(g)
        cross += c0
        g2 = g.copy(); g2[cx, cy] = not g2[cx, cy]
        if has_crossing(g2) != c0:
            piv_center += 1
        ix = int(rng.integers(0, n)); iy = int(rng.integers(0, n))
        g3 = g.copy(); g3[ix, iy] = not g3[ix, iy]
        if has_crossing(g3) != c0:
            piv_rand_sum += 1
    p = cross / trials
    var = p * (1 - p)
    pc = piv_center / trials
    avg_inf = piv_rand_sum / trials
    N = n * n
    sumInf = N * avg_inf
    osss = var / sumInf if sumInf > 0 else float('nan')
    claimed = 0.02 * n ** -0.5
    witness = 1.0 / n
    return dict(n=n, p=p, var=var, center_piv=pc, avg_inf=avg_inf,
                sumInf=sumInf, osss=osss, claimed=claimed, witness=witness)

if __name__ == "__main__":
    for n, tr in [(8, 6000), (16, 5000), (32, 3000), (48, 1500)]:
        t0 = time.time()
        d = estimate(n, tr)
        print(d, f"trials={tr} time={time.time()-t0:.1f}s", flush=True)
