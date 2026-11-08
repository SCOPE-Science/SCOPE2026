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

# Reproducibility

Use Python 3 to run `python verify.py` in this directory; the checker has no external dependencies. It constructs the integer-polynomial-scaled reduced star and triangle transition matrices, verifies that every row sums to its common positive denominator, computes the exact four-transient-state Cramer numerators/denominators for one and two updates per graph, and tests the difference identities against their fully listed coefficient polynomials by comparing every integer coefficient. It then constructs the full, unreduced eight-configuration birth–death chain independently and verifies the formulas at 40 exact rational values. Success prints `IDENTITY_OK 1`, `IDENTITY_OK 2`, `EIGHT_STATE_OK` and `VERIFY_OK`.

The rational-point tests are consistency checks, not a substitute for an all-fitness argument. The symbolic coefficient identity is an exhaustive finite verification of the specified polynomial equation; the proof additionally explains why its denominators are nonzero for all positive fitness and uses all-positive polynomial factors to infer the signs for every positive nonneutral fitness. No experimental claim about dwell lengths at least three, stochastic switching, phase-randomized starts, or independent external auditing is made.
