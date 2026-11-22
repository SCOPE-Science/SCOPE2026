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

The standalone `checker.py` requires Python 3 and no third-party modules. Run `python checker.py` in the directory containing this file. The deterministic checks cover the odd Fourier spectrum, closed-form finite variance/deletion second moment, Euler-product transform and all numerical constants; seeded simulations additionally compare geometric counts against the exact formulas. The script's assertions passed, including negative mixed-covariance sign checks for the squared deletion response. Monte Carlo is not a proof of the general limit.

The mathematical proof relies on exact geometric conditional probabilities, Hoeffding orthogonality, joint finite-frequency central limit theory, an \(L^2\)-tail bound and independent Gaussian integrations. It does not construct a machine-formal proof or claim independent review. Historical-priority limitations are stated in the associated review.
