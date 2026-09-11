import math
import numpy as np

# Refined: for fixed phase th, scan q up to 987; find persistent gaps covering
# subintervals of [0.1,0.6]: gaps whose (a,b) overlap-range persists across q.
# Simpler: at q=987, take phases th in fine grid; union of spectra; find E-intervals
# covered by NO eigenvalue for any th -> true gaps.
lam = 3.0
alpha = (math.sqrt(5) - 1) / 2

def spec(q, th):
    p = int(round(q * alpha))
    d = np.array([2 * lam * math.cos(2 * math.pi * (th + k * p / q)) for k in range(q)])
    off = np.ones(q - 1)
    M = np.diag(d) + np.diag(off, 1) + np.diag(off, -1)
    M[0, q - 1] = 1.0
    M[q - 1, 0] = 1.0
    return np.sort(np.linalg.eigvalsh(M))

if __name__ == "__main__":
    import sys
    q = int(sys.argv[1]) if len(sys.argv) > 1 else 610
    ngrid = 4001
    grid = np.linspace(0.05, 0.65, ngrid)
    covered = np.zeros(ngrid, dtype=bool)
    nth = 24
    for j in range(nth):
        th = j / nth
        w = spec(q, th)
        idx = np.searchsorted(w, grid)
        idxm = np.clip(idx - 1, 0, len(w) - 1)
        idxp = np.clip(idx, 0, len(w) - 1)
        dist = np.minimum(np.abs(grid - w[idxm]), np.abs(grid - w[idxp]))
        tol = 0.5 / q
        covered |= (dist < tol)
    # find maximal uncovered runs
    runs = []
    i = 0
    while i < ngrid:
        if not covered[i]:
            j = i
            while j + 1 < ngrid and not covered[j + 1]:
                j += 1
            runs.append((grid[i], grid[j]))
            i = j + 1
        else:
            i += 1
    print(f"q={q} nth={nth}: {len(runs)} uncovered runs in [0.05,0.65]:")
    for a, b in sorted(runs, key=lambda r: -(r[1] - r[0]))[:25]:
        print(f"   ({a:.5f},{b:.5f}) width={b-a:.5f}")
