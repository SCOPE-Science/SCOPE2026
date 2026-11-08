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

# Reproducibility and boundaries

Run `python3 check_extremal.py` in this package. The checker has no third-party dependencies and uses only integer arithmetic and `fractions.Fraction`. It (i) independently builds the signed coordinate-permutation cocycle for every primitive itinerary in dimensions 2 through 12 and lengths 1 through 10, (ii) compares the least eigenvalue-modulus exponent and number of minimizing points to the closed formulas in 110 cases, and (iii) solves 1,440 periodic affine fixed-point systems in exact rationals and verifies the actual branch inequalities and returns. The stated pass message is produced only after all checks complete successfully.

The mathematical result is the all-dimensional theorem and its proof in `RESULT.md`. Verification cases are deliberately finite and neither claim exhaustive coverage for all dimensions nor substitute for the argument using permutation cycles, right-visit distribution and cyclic gap counting. The source's published symbolic-coding result establishes that the primitive words actually correspond to physical primitive periodic points in all dimensions. The earlier three-dimensional special case is excluded from the new-claim domain.
