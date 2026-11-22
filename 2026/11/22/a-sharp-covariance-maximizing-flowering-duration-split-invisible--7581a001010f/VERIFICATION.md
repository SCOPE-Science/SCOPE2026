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
# Verification of the mathematical claim

The analytical proof partitions the total duration into three ranges using the center distance, and derives the exact covariance expression within the feasible middle range. No computer enumeration is used as a substitute for the global proof.

The package includes self-contained `checker.py` with deterministic pseudorandom seeds. It checks circular intervals by independently splitting wrapped arcs into segments; compares direct intersection length with the predicted formula over 50,000 random parameter choices; tests optimality and covariance gain over 10,000 middle-band choices; and checks the exact rational witness using Python's `fractions.Fraction`. Invoke `python3 checker.py`; all tests must terminate without an assertion failure.

Limitations: floating-point geometry comparisons are numerical and supplementary. The exact fraction witness is not a proof of all-parameter uniqueness. The proof relies on precisely two species, one shared uniform phase, proper contiguous circular arcs and fixed centers. No field or external independent scientific validation is asserted.
