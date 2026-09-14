"""Large-deviation resonant-count: empirical delocalization-side threshold.

For H on T_K, delocalization follows if the expected number of epsilon-resonant
sites at distance n grows exponentially: K^n * P(|V-E| < tau_n) with
tau_n = t * sqrt(K) * (typical boundary amplitude factor)... The ASW criterion
reduces to: g_eff(E) := 4 g rho(E) > 1 => resonant proliferation.
We directly simulate: for K in {64,128,256,512}, E-grid, estimate single-site
resonance probability p = P(|V-E| < t*sqrt(K)*C) via MC, and report
n=1 growth factor K*p vs the two candidate laws 4g rho(E)*C' and 2e g rho(E)*C'.
This tests the CONSTANT on the delocalization side, where popdyn FM only gives
the localization side. Writes JSON to argv[1].
"""
import json
import sys

import numpy as np

GRID = np.linspace(-1.0, 1.0, 20001)
CDF = (15.0 / 16.0) * (GRID - 2 * GRID ** 3 / 3 + GRID ** 5 / 5 + 8.0 / 15.0)
CDF /= CDF[-1]


def rho_fn(x):
    x = np.asarray(x)
    return (15.0 / 16.0) * (1.0 - x ** 2) ** 2 * (np.abs(x) < 1.0)


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else None
    rng = np.random.default_rng(7)
    g = 1.0
    Nmc = 400000
    Vsamp = np.interp(rng.random(Nmc), CDF, GRID)
    rows = []
    for K in [64, 128, 256, 512]:
        t = g / (K * np.log(K))
        tau = t * np.sqrt(K)  # resonant window scale (C=1)
        for E in [0.5, 0.6, 0.65, 0.696, 0.72, 0.745, 0.78, 0.85]:
            p = float(np.mean(np.abs(Vsamp - E) < tau))
            Kp = K * p
            rE = float(rho_fn(E))
            # predicted Kp under density approx: K * 2*tau*rho(E) = 2g rho/lnK *...:
            pred = float(K * 2 * tau * rE)
            rows.append({"K": K, "E": E, "rhoE": rE, "tau": float(tau),
                         "K_times_p": Kp, "density_pred": pred,
                         "ratio": Kp / pred if pred > 0 else None,
                         "four_g_rho": 4 * g * rE,
                         "twoe_g_rho": 2 * np.e * g * rE})
            print(f"K={K} E={E:.3f} Kp={Kp:.4f} pred={pred:.4f} "
                  f"ratio={Kp/pred:.3f} 4grho={4*g*rE:.3f} 2egrho={2*np.e*g*rE:.3f}",
                  flush=True)
    out = {"rows": rows,
           "note": ("Kp>1 proliferates resonances; density law Kp~2g rho sqrt(K)/lnK; "
                    "constant adjudication comes from the refined ASW rate, see DRAFT.")}
    if out_path:
        with open(out_path, "w") as f:
            json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
