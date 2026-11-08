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

# Reproduction of the sharp random-crossing benchmark

Run `python3 check.py` using Python 3 without optional third-party modules. The program integrates the explicit nonnegative spectral-error formulas by adaptive Simpson integration with splits at the avoided-crossing scale and checks the analytic uniform-density identities, positivity of coupled levels, and convergence directions across representative moment orders. In this package it returned `PASS: 55 deterministic quadrature and algebra checks.`

Mathematical verification rests on the five-step analytic proof in `RESULT.md`: exact diagonalization; dominated-convergence constants for moments away from the critical exponent; crossing-localized logarithmic estimates at the critical exponent; coupled-level rescaling with integrable tails; and direct uniform-density integration. In particular, finite numerical tests are not used as a proof of any all-density or infinite-limit claim.

The resulting classification is conditional on bounded density and a strictly positive continuous value at the crossing, exact shared-parameter coupling and rank-one (not full cluster) projectors. No independent validation or external certification is represented.
