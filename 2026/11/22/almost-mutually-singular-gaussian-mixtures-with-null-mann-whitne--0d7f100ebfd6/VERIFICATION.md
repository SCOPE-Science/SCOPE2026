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

# Verification record

The proof uses exact Gaussian comparison identities and a measurable-set total-variation inequality for every positive width. `verify.py` checks numerical quadrature and closed formulas at representative values and prints the count of assertions passed. Its finite checks do not certify infinite quantification, which is proved symbolically in `RESULT.md`. The original test's large-sample non-consistency conclusion follows from the published bivariate central limit theorem at each fixed positive width and the exact null-effect identities, not from finite-sample simulation. No independent mathematical audit or external certification has been performed.
