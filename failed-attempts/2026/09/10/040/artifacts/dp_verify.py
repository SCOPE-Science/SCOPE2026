"""Exact DP verification of one-point and two-point barrier probabilities
for the idealized Gaussian tree model of the gamma=1 uniform envelope.

Model: S_0 = C, S_k = C + N(0, k*sigma2), sigma2 = ln2 (branching RW).
Event E_K = {min_{k<=K} S_k >= 0, S_K in [K*sigma2 - C, K*sigma2 + Cp]}.
Computes P1(K), q_j(z) = P_z(survive j->K + terminal), P2(j,K) = E[1 q(Z_j)^2],
shell weights and s-energy sums. Validates:
  (a) P1(K) ~ c0 K^{-q} 2^{-K/2}  (fit q; expect q = 1/2),
  (b) shell sum S_s(K) = sum_j 2^{js} w_j R_j, w_j = 4*2^{-2j} (pair fraction),
      R_j = P2(j,K)/P1(K)^2, bounded in K iff s < 3/2.
Forward/backward propagation on uniform grid with exact Gaussian kernel.
Stdlib + numpy only.
"""
import json
import numpy as np

SIGMA2 = np.log(2.0)
C = 2.0
CP = 2.0

def build_grid(K, dx=0.05, lo_pad=3.0, hi_pad=8.0):
    hi = K * SIGMA2 + hi_pad
    lo = -lo_pad
    n = int(np.ceil((hi - lo) / dx)) + 1
    xs = lo + dx * np.arange(n)
    return xs, dx

def kernel(sigma, dx, trunc=7.0):
    r = int(np.ceil(trunc * sigma / dx))
    off = np.arange(-r, r + 1) * dx
    k = np.exp(-off ** 2 / (2 * sigma ** 2))
    k /= k.sum()
    return k

def forward(p0, K, ker, xs, dx):
    sigma = np.sqrt(SIGMA2)
    import numpy as _np
    p = p0.copy()
    snaps = {0: p.copy()}
    alive = xs >= 0
    for k in range(1, K + 1):
        p = _np.convolve(p, ker, mode="same")
        p[~alive] *= 0.0
        snaps[k] = p.copy()
    return snaps

def terminal_mask(xs, K):
    ctr = K * SIGMA2
    return (xs >= ctr - C) & (xs <= ctr + CP)

def backward(K, ker, xs, dx, tmask):
    n = len(xs)
    alive = xs >= 0
    v = np.where(tmask, 1.0, 0.0)
    qs = {K: v.copy()}
    for k in range(K - 1, -1, -1):
        # v_k(x) = sum_y ker(y-x) alive(y) v_{k+1}(y); convolution symmetric
        v = np.convolve(v * alive, ker, mode="same")
        qs[k] = v.copy()
    return qs

def run(K, dx=0.05):
    xs, dx = build_grid(K, dx)
    ker = kernel(np.sqrt(SIGMA2), dx)
    p0 = np.zeros_like(xs)
    p0[np.argmin(np.abs(xs - C))] = 1.0 / dx
    snaps = forward(p0, K, ker, xs, dx)
    tmask = terminal_mask(xs, K)
    P1 = float((snaps[K] * tmask).sum() * dx)
    qs = backward(K, ker, xs, dx, tmask)
    P2 = {}
    for j in range(0, K + 1):
        pj = snaps[j]
        q = qs[j]
        P2[j] = float((pj * q * q).sum() * dx)
    return {"K": K, "P1": P1, "P2": P2, "dx": dx}

def shell_table(res, s_list):
    K = res["K"]
    P1 = res["P1"]
    rows = []
    for j in range(0, K + 1):
        R = res["P2"][j] / P1 ** 2
        w = 4.0 * 2.0 ** (-2 * j)
        rows.append({"j": j, "R": R, "w": w,
                     "ratio_over_2pow": R / 2.0 ** j})
    out = {}
    for s in s_list:
        tot = sum((2.0 ** (r["j"] * s)) * r["w"] * r["R"] for r in rows)
        out[str(s)] = tot
    return rows, out

def main():
    print("== one-point fit ==")
    one = {}
    for K in [10, 15, 20, 25, 30, 40]:
        r = run(K)
        one[K] = r["P1"]
        scaled = r["P1"] * 2 ** (K / 2.0)
        print(f"K={K}: P1={r['P1']:.6e}  P1*2^(K/2)={scaled:.6e}  *sqrt(K)={scaled*np.sqrt(K):.6f}")
    print("\n(q=1/2 check: P1*2^(K/2)*sqrt(K) -> const)")
    print("\n== two-point ratio R_j / 2^j (expect poly-bounded in j) ==")
    res = run(30)
    rows, es = shell_table(res, [1.0, 1.3, 1.4, 1.49, 1.51, 1.6])
    for r in rows[::3]:
        print(f"j={r['j']:3d}: R={r['R']:.4e}  R/2^j={r['ratio_over_2pow']:.4e}")
    print("\n== energy sums S_s(K=30) ==")
    for s, v in es.items():
        print(f"s={s}: S={v:.6e}")
    print("\n== energy sums vs K (bounded iff s<1.5) ==")
    estab = {}
    for K in [15, 20, 25, 30]:
        r = run(K)
        _, e = shell_table(r, [1.0, 1.4, 1.49, 1.6])
        estab[K] = e
        print(f"K={K}: " + "  ".join(f"s={s}:{v:.4e}" for s, v in e.items()))
    # diagonal check
    K = 30
    EN_factor = 2 ** (1.5 * K) * one[K]  # E[N]/nQ^... just log
    with open("output/artifacts/dp_verify.json", "w") as f:
        json.dump({"one_point": {str(k): v for k, v in one.items()},
                   "energy_vs_K": {str(k): v for k, v in estab.items()},
                   "shells_K30": rows, "S_s_K30": es}, f, indent=1)
    print("\nwrote output/artifacts/dp_verify.json")

if __name__ == "__main__":
    main()
