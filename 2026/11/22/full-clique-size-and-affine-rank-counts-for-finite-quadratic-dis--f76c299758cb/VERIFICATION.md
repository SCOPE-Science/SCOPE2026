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

The `CHECK.py` file is standalone Python 3 using standard-library arithmetic only. It enumerates ordered small cliques from the defining squared-distance condition, measures linear dependence by explicit row reduction, and separately predicts counts from the stated orbit quotient and finite quadratic zero counts. It covers 102 prime-field cases with odd primes 3, 5 and 7 plus 16 cases over the proper extension field of order 9; executed output was `EQUILATERAL_COUNT_OK 102` and `EXTENSION_FIELD_F9_OK 16`.

The proof is an infinite deduction from the forced Gram matrix, classification of nondegenerate finite quadratic forms, Witt extension, finite orthogonal group orders, and Gauss sums. The checks only test small cases; the research is not independently externally audited.
