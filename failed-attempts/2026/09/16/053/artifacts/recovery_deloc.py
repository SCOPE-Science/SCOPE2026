"""Bounded recovery/plausibility test: delocalization trend for 1D real-symmetric band matrices.
Builds periodic band matrices (Gaussian entries, variance ~1/W inside band), full
eigendecomposition at small N, records max_k ||psi_k||_inf^2 * N (O(1) = delocalized).
This tests plausibility only; it cannot prove optimal local laws / QUE / rigidity.
"""
import numpy as np

def band_goe(n, w, rng):
    # 1D periodic band: |i-j| <= w/2 mod n, variance 1/w (off-diag), 2/w diag scaled for symmetry
    h = np.zeros((n, n))
    hw = w // 2
    for i in range(n):
        for d in range(hw + 1):
            j = (i + d) % n
            if d == 0:
                h[i, j] = rng.normal(0, np.sqrt(2.0 / w))
            else:
                v = rng.normal(0, np.sqrt(1.0 / w))
                h[i, j] = v
                h[j, i] = v
    return h

def stats_for(n, w, nsamples=4, seed=0):
    rng = np.random.default_rng(seed)
    out = []
    for s in range(nsamples):
        h = band_goe(n, w, rng)
        vals, vecs = np.linalg.eigh(h)
        # vecs columns are eigenvectors; inf-norm squared
        inf2 = np.max(np.abs(vecs) ** 2, axis=0)  # per eigenvector
        scaled = inf2 * n  # O(1) if delocalized
        bulk_mask = np.abs(vals) < 1.0
        edge_mask = np.abs(vals) > 1.5
        rec = {
            "w": w, "sample": s,
            "max_scaled_all": float(np.max(scaled)),
            "mean_scaled_all": float(np.mean(scaled)),
            "max_scaled_bulk": float(np.max(scaled[bulk_mask])) if bulk_mask.any() else float("nan"),
            "max_scaled_edge": float(np.max(scaled[edge_mask])) if edge_mask.any() else float("nan"),
            "n_edge": int(edge_mask.sum()),
        }
        out.append(rec)
    return out

if __name__ == "__main__":
    n = 400
    lines = [f"N={n}; metric = max_k ||psi_k||_inf^2 * N (delocalized ~ O(1); localized ~ N/W)"]
    for w in [40, 120, 250]:
        recs = stats_for(n, w)
        for r in recs:
            lines.append(str(r))
        m_all = np.mean([r["max_scaled_all"] for r in recs])
        m_edge = np.nanmean([r["max_scaled_edge"] for r in recs])
        lines.append(f"W={w}: mean over samples of max_scaled_all={m_all:.2f}, of max_scaled_edge={m_edge:.2f}")
    txt = "\n".join(lines)
    print(txt)
    with open("recovery_deloc_results.txt", "w") as f:
        f.write(txt + "\n")
