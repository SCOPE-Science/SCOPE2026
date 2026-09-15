"""Bounded recovery test: finite-time Lyapunov exponents for the most resonant
one-dimensional reduction at small coupling.

Model: (Hu)_n = u_{n-1}+u_{n+1} + lam*2cos(2*pi*(theta+n*omega)) u_n.
omega_res = truncated tower-Liouville constant (beta_1 = +infinity);
omega_dc  = golden mean (Diophantine control).
Question tested: does tailoring to the strongest resonance produce any
Lyapunov-positivity signature at small lam that could kill ac via Kotani?
Expected analysis outcome: LE ~ O(lam^2) -> 0 for BOTH frequencies, i.e. the
LE/Kotani route cannot distinguish the resonant case and cannot exclude ac.
Vectorized over the energy grid; transfer matrices renormalized periodically.
"""
import json
import numpy as np

L_TRUNC = float(sum(2.0 ** (-m) for m in (2, 4, 16)))  # ~0.312515
OM_RES = L_TRUNC % 1.0
OM_DC = (5 ** 0.5 - 1) / 2


def finite_time_le(omega, lam, Es, N=150000, theta=0.1, renorm=500):
    E = np.asarray(Es, dtype=float)
    Q = np.zeros((2, 2, E.size))
    Q[0, 0, :] = 1.0
    Q[1, 1, :] = 1.0
    acc = np.zeros(E.size)
    for j in range(1, N + 1):
        ph = (theta + j * omega) % 1.0
        a = E - lam * 2.0 * np.cos(2 * np.pi * ph)
        n0 = a * Q[0] - Q[1]
        n1 = Q[0].copy()
        Q[0] = n0
        Q[1] = n1
        if j % renorm == 0:
            nrm = np.sqrt((Q ** 2).sum(axis=(0, 1)))
            nrm[nrm == 0.0] = 1.0
            Q /= nrm
            acc += np.log(nrm)
    return acc / N


def main():
    Es = np.linspace(-1.8, 1.8, 17).tolist()
    out = {"omega_res": OM_RES, "omega_dc": OM_DC, "N": 150000, "Es": Es, "rows": []}
    for lam in (0.2, 0.1, 0.05, 0.02):
        le_r = finite_time_le(OM_RES, lam, Es)
        le_d = finite_time_le(OM_DC, lam, Es)
        row = {"lam": lam,
               "res_max": float(le_r.max()), "res_mean": float(le_r.mean()),
               "dc_max": float(le_d.max()), "dc_mean": float(le_d.mean())}
        out["rows"].append(row)
        print(row)
    with open("output/artifacts/le_scan.json", "w") as f:
        json.dump(out, f, indent=1)
    print("wrote output/artifacts/le_scan.json")


if __name__ == "__main__":
    main()
