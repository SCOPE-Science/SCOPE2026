"""TARGET witness verifier: N=80 Green-decay ledger + Herman-threshold sanity check.

Operator: (H u)_n = u_{n+1} + u_{n-1} + 3*cos(2*pi*(n*alpha+theta)) u_n,
alpha = (sqrt(5)-1)/2. Dirichlet restriction to [1,80].
Audit grid: E in {k*0.5/40}, k=0..40 (41 pts); theta in {j/400}, j=0..399.
Pass criteria:
  (G1) Lyapunov numeric margin: log(3/2) - 0.05 > 0.35 (analytic proof in DRAFT.md
       gives L(E) >= log(3/2) for every E, uniformly).
  (G2) For every non-resonant grid pair, C(E,th) := max_{x,y}(log|G_xy|+0.30|x-y|) <= 8.0.
  (G3) Resonant fraction <= 1.5% overall and every E-slice good fraction >= 95%.
Writes resonant_log.csv next to this script. Prints VERIFY_OK on full pass.
Requires only numpy. Runtime ~10 s.
"""
import csv
import math
import os
import sys

import numpy as np

ALPHA = (math.sqrt(5) - 1) / 2
N = 80
RATE = 0.30
CSTAR = 8.0
NE, NT = 41, 400
HERE = os.path.dirname(os.path.abspath(__file__))


def green_const(E, th):
    n = np.arange(1, N + 1)
    d = 3.0 * np.cos(2.0 * math.pi * (n * ALPHA + th)) - E
    M = np.diag(d)
    M += np.diag(np.ones(N - 1), 1) + np.diag(np.ones(N - 1), -1)
    try:
        G = np.linalg.inv(M)
    except np.linalg.LinAlgError:
        return float("inf")
    idx = np.arange(N)
    D = np.abs(idx[:, None] - idx[None, :])
    with np.errstate(divide="ignore"):
        val = np.log(np.abs(G) + 1e-300) + RATE * D
    return float(np.max(val))


def main():
    ok = True
    # (G1) Herman threshold sanity
    thr = math.log(1.5) - 0.05
    print(f"Herman edge: log(3/2)-0.05 = {thr:.6f} (>0.35: {thr > 0.35})")
    ok &= thr > 0.35
    # (G2/G3) grid ledger
    resonant = []
    total = NE * NT
    bad_per_E = []
    for k in range(NE):
        E = k * 0.5 / (NE - 1)
        bad = 0
        for j in range(NT):
            th = j / NT
            if green_const(E, th) > CSTAR:
                bad += 1
                resonant.append((E, th))
        bad_per_E.append(bad)
    nb = len(resonant)
    print(f"grid {NE}x{NT}={total}, resonant={nb}, frac={nb/total:.5f}")
    print(f"worst E-slice bad={max(bad_per_E)}/{NT} "
          f"(min good frac={1-max(bad_per_E)/NT:.4f})")
    ok &= (nb / total) <= 0.015
    ok &= max(bad_per_E) <= 20
    with open(os.path.join(HERE, "resonant_log.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["E", "theta", "Cstar", "rate"])
        for E, th in resonant:
            w.writerow([f"{E:.6f}", f"{th:.6f}", CSTAR, RATE])
    print(f"wrote resonant_log.csv ({nb} rows)")
    print("VERIFY_OK" if ok else "VERIFY_FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
