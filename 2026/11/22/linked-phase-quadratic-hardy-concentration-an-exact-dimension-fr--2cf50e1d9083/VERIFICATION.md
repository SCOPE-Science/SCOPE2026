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

## Reproducibility
Execute `python check.py` with Python 3, `sympy` and `numpy`. It checks the exact six-dimensional block, exchange-symmetry decomposition, characteristic factors, root intervals using rational arithmetic and a certified enclosure for \(\pi\), and entire normalized Gram spectra for complex dimensions \(3,4,5,8\). A separate seeded Gaussian simulation checks direct integration of the original two real-part inequalities in dimension three.

The exact proof of universal dimension-independence is the Gaussian–Dirichlet moment cancellation and phase symmetry, not the finite dimensional tests. The randomized check has finite-sample error and cannot independently establish the theorem. No independent review has been performed.
