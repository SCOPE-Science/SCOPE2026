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

The all-size structural premise is checked by a direct mathematical proof identifying each admissible ideal/filter one-point extension with an order ideal of a doubled finite poset. The exact finite cutoff is checked by `checker.py`, using solely standard-library Python \(\ge3.10\), against `collision_pairs.json`.

The checker generates exactly \(1,1,2,5,16,63,318,2045\) isomorphism classes at sizes zero through seven; calculates for each class its whole rank polynomial in two independent ways; and confirms no collision through six, six pairwise collisions at seven, 2,045 distinct two-coordinate profiles at seven, and the complete cover-list/coefficients certificate. Its actual terminal output is in `verification_output.txt`. It does not enumerate posets of order greater than seven, nor prove any claim outside that domain. Independent mathematical audit is not performed.
