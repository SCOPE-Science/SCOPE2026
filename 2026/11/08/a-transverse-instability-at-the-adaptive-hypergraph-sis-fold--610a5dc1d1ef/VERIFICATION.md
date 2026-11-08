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

The reproducible `fold_check.py` performs exact symbolic rational verification of the stationary fold, the matrix entries and the eigenvalues at the reported parameter set. It also computes three nearby pairs of positive equilibria and tests that each has an eigenvalue of modulus greater than one. Those numerical examples supplement, rather than replace, the analytic continuity and implicit-function arguments in `RESULT.md`. No stochastic model, global attractor classification or independent review is certified.
