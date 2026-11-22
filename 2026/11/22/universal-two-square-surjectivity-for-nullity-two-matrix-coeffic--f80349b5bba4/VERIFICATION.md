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

The accompanying executable `check_square_coeff.py` replays exact-arithmetic consistency checks in matrix dimensions \(7,8,9,12\). For each dimension it tests six random rational targets in each of the five bottom-row cases; all 120 configurations meet the required prescribed bottom rows and rank-\(n-2\) residual condition. The rank-one nilpotent case explicitly verifies \(X^2=N\) by exact multiplication. The successful sentinel is `MATRIX_TWO_SQUARES_NULLITY_TWO_CERTIFICATES_OK`.

The universal proof in RESULT.md is independent of these finite tests. In particular the full-rank-lifting step applies to *every* row-surjective matrix and the rank-one classifications cover *all* quotient types. No externally conducted specialist audit or machine-formalized infinite proof is asserted. Historical-priority completeness is not asserted.
