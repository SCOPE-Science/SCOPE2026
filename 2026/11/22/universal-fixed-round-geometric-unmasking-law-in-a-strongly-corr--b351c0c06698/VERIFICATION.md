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
The accompanying `checker.py` recomputes the Markov mutual-information series, compares the closed one-stage formula to an independent truncated triple-gap sum at moderate parameters, and evaluates the predicted fixed-round asymptotic schedules as \(f\) decreases. Its numerical checks do not prove global minimizer uniqueness or an infinite-size theorem; the mathematical proof is in `RESULT.md`. Requires Python 3, NumPy and SciPy. The primary source [1] was inspected at its path-error and exact-gap equations; the other studies' inspected material and uninspected-full-text limitations are documented in `REVIEW.md`.
