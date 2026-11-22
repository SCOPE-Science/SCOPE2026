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

# Reproduction and verification limits

The exact proof is in `RESULT.md`. Reproduce the supplementary computations using `python CHECK.py` with NumPy and SymPy; the script tests the anticommutator, involution identity, formula for the norm of an oblique rank-one reflection, all displayed optimal constructions, and finite complex perturbations. The observed completion string was `THREE_STEP_INVOLUTION_NORM_DIAGNOSTIC_OK 22463`.

The symbolic identity checks are exact; the randomized spectral checks are finite numerical diagnostics with stated tolerances. They do not certify global minimization, which is instead established by the explicit triangular classification and inequality in `RESULT.md`. No independent mathematical audit has been performed. The comparison to the 2023 factorization paper is limited by unavailable full text.
