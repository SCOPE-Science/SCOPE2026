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

# Reproduction

From the folder containing this file, run `python3 verify.py` with Python 3; no external packages or data files are needed. The checker generates symmetric and pseudo-symmetric numerical semigroups by complementary Frobenius pairs and independently checks all small-F cases by unrestricted membership-bit enumeration. It exhausts all relevant special-gap masks for the specified ordinary semigroup, proves three-factor noncoverage, verifies an explicit four-factor intersection, then counts all shortest decompositions by two separate combination algorithms.

Expected essential output: `CLASSIFICATION_OK 56`, `INCLUSION_EXCLUSION_OK 56`, and `FROBENIUS_SIGNATURES {(24, 25, 26, 27): 28, (24, 26, 27, 27): 28}`. The direct checker also prints `VERIFY_OK`, `H28_THREE_FACTOR_MAX (8788, 13, 14)` and four witness coverage sets.

These are exhaustive *finite* checks. The equivalence of the enumerated pair choices with all irreducible numerical semigroups follows from the proven symmetric/pseudo-symmetric characterization; machine output does not supply independent expert verification or a general theorem for arbitrary multiplicity.
