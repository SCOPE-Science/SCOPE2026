---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

The analytic proof and exact scope are in `RESULT.md`. Run `python checker.py` with SciPy available. Fixed random seeds reproduce four Monte Carlo cases of \(30{,}000\) paths each; each case compares an empirical mean and Laplace transform to independent special-function expressions, verifies the gamma-mean integral representation, and checks the first-jump survival bound. A separate grid checks strict mean monotonicity and the correct mean asymptotic lower bound. The actual run completed all assertions and printed `all supplementary checks passed`.

For \((a,\lambda,c,h,s)=(1.8,1.5,0.6,12,2)\): exact \(\mathbb E\tau_h=0.7077264877658449\), exact \(\mathbb E[e^{-s\tau_h}]=0.4223846030236965\), empirical mean \(0.7070100491\), empirical transform \(0.4235243265\). The rigorous coupling upper bound is \(0.06\); empirical first-leaching failure frequency was \(0.0563\).

Finite stochastic simulations do not establish a theorem for arbitrary parameters; only the analytic generator proof does. There was no independent audit, no field data, and no claimed external certification.
