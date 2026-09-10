"""Corrected tilted-pair certificate for lane-599 TARGET (two-sided tube).
Pair mass E[v_j^2] is the EXACT conditional pair mass (subtree independence);
no division by the shared tilt. Upper barrier S_k - k ln2 <= Cup.
Writes output/artifacts/tilted_certificate.json. Stdlib + numpy.
"""
import json
import numpy as np

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dp_verify import build_grid, kernel, terminal_mask

SIGMA2 = np.log(2.0)
C = 2.0
CP = 2.0

def run_correct(K, upper=5.0, dx=0.05):
    xs, dx = build_grid(K, dx)
    ker = kernel(np.sqrt(SIGMA2), dx)
    alive_lo = xs >= 0
    p = np.zeros_like(xs)
    p[np.argmin(np.abs(xs - C))] = 1.0 / dx
    snaps = {0: p.copy()}
    for k in range(1, K + 1):
        p = np.convolve(p * alive_lo, ker, mode="same") * alive_lo
        if upper is not None:
            p[xs > k * SIGMA2 + upper] *= 0.0
        snaps[k] = p.copy()
    tmask = terminal_mask(xs, K)
    tiltK = np.exp(xs - K * SIGMA2 / 2.0)
    Mmean = float((snaps[K] * tmask * tiltK).sum() * dx)
    v = np.where(tmask, tiltK, 0.0)
    qs = {K: v.copy()}
    for k in range(K - 1, -1, -1):
        v = np.convolve(v * alive_lo, ker, mode="same") * alive_lo
        if upper is not None:
            v[xs > k * SIGMA2 + upper] *= 0.0
        qs[k] = v.copy()
    R = {j: float((snaps[j] * qs[j] * qs[j]).sum() * dx) / Mmean ** 2
         for j in range(K + 1)}
    return Mmean, R

def main():
    rec = {}
    for K in [10, 15, 20, 25, 30, 40]:
        Mm, R = run_correct(K, 5.0)
        E = {s: sum((2.0 ** (j * s)) * 4 ** (-j) * R[j] for j in range(K + 1))
             for s in [1.0, 1.4, 1.49, 1.6]}
        rec[str(K)] = {"Mmean": Mm, "R_over_sqrt2pow_max":
                        max(v / 2 ** (j / 2) for j, v in R.items()),
                        "energy": {str(k): v for k, v in E.items()}}
        print(f'K={K} M={Mm:.3f} R*/2^(j/2)max={rec[str(K)]["R_over_sqrt2pow_max"]:.3f} ' +
              ' '.join(f's={s}:{v:.2f}' for s, v in E.items()), flush=True)
    with open("output/artifacts/tilted_certificate.json", "w") as f:
        json.dump(rec, f, indent=1)
    print("wrote output/artifacts/tilted_certificate.json")

if __name__ == "__main__":
    main()
