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

The proof is analytic and includes the exact geometry, CDF quadrature and coarea saddle residue. `CHECKER.py` executes independent polygon-hull perimeter comparisons (160 Haar-normal examples), Monte Carlo against the deterministic CDF, and numerical checks for the logarithmic residue and endpoint coefficients. It requires Python 3, NumPy and SciPy. The deterministic numerical estimate of the log coefficient from symmetric windows \(10^{-2}\) and \(10^{-4}\) is approximately \(1.24679962\); the exact expression is approximately \(1.24767573\). These checks do not establish the mathematical limit or historical priority, which rest on the accompanying proof and literature discussion. No independent mathematical audit has been performed.
