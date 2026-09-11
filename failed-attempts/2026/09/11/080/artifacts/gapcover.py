import math
import numpy as np

# Zero in on the persistent gap near (0.421,0.434): is it a TRUE gap of the
# quasiperiodic limit? Use the gap-labelling + coexistence idea:
# a true gap is open for ALL phases th. Scan nth phases at q=987 and check
# whether some phase puts an eigenvalue inside (0.4215,0.4335).
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
    for q in [377, 610, 987]:
        for nth in [24, 96]:
            lo, hi = 0.4215, 0.4335
            inside_any = False
            cover_count = 0
            for j in range(nth):
                w = spec(q, j / nth)
                inside = w[(w > lo) & (w < hi)]
                if len(inside):
                    inside_any = True
                    cover_count += 1
            print(f"q={q} nth={nth}: phases_with_eig_in_({lo},{hi}): {cover_count}/{nth} "
                  f"-> {'NOT a true gap (covered)' if inside_any else 'candidate TRUE gap'}")
            # also scan the whole [0.1,0.6] window: maximal sub-interval avoided by ALL phases
            grid = np.linspace(0.1, 0.6, 20001)
            covered = np.zeros(len(grid), dtype=bool)
            for j in range(nth):
                w = spec(q, j / nth)
                idx = np.searchsorted(w, grid)
                idxm = np.clip(idx - 1, 0, len(w) - 1)
                idxp = np.clip(idx, 0, len(w) - 1)
                dist = np.minimum(np.abs(grid - w[idxm]), np.abs(grid - w[idxp]))
                covered |= (dist < 0.5 / q)
            runs = []
            i = 0
            n = len(grid)
            while i < n:
                if not covered[i]:
                    j = i
                    while j + 1 < n and not covered[j + 1]:
                        j += 1
                    runs.append((grid[i], grid[j]))
                    i = j + 1
                else:
                    i += 1
            runs.sort(key=lambda r: -(r[1] - r[0]))
            print(f"   max avoided runs: " +
                  ", ".join(f"({a:.4f},{b:.4f},w={b-a:.4f})" for a, b in runs[:8]))
