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

# Verification notes

`checker.py` uses an independent multinomial-composition evaluation, not the proposed polynomial formula, to verify 54 exact rational moment comparisons. It symbolically checks the pair-smoothing identity and phase derivative; checks 100 ordered transition thresholds; exhausts 4,472 rational-simplex grid points for dimensions two through four at eight rational inverse-probability values; and checks 23 different two-coordinate splits at the exceptional parameter \(t=5\). All assertions passed on the packaged source.

The universal proof is the algebraic moment expansion plus pair perturbations, followed by the monotone crossing argument in `RESULT.md`. The checker does not establish the infinite-dimensional claim by enumeration and does not verify publication uniqueness. No independent mathematical audit has been performed.
