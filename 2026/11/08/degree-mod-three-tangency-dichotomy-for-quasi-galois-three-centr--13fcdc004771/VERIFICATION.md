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

# Verification
Run `python3 verify.py` with the Python 3 standard library. Its output must contain `GCD_ALL_DEGREES_4_TO_40_OK`, `ORBIT_COUNTS_N_3_TO_8_OK`, and `CERTIFICATE_OK`. It tests the exact rational polynomial gcd of the restricted Fermat equation and its derivative, including the odd-degree leading-coefficient case, and computes finite combinatorial consistency checks. The uniform proof for arbitrary degrees and ambient dimensions is the algebraic argument in RESULT.md; exhaustive checking through degree 40 does not prove it. Full projective monomial transitivity and contact uniqueness are justified geometrically in RESULT.md rather than by floating-point testing. No independent mathematical audit has been performed.
