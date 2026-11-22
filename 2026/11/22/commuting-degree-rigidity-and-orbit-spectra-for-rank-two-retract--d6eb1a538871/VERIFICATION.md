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

The algebraic proof is in `RESULT.md`. `verify_retractions.py` is a standalone Python 3 checker using prime-field arithmetic and explicit multiplication of squarefree monomial basis elements. It independently enumerates all possible endomorphism generator images in the cases \((d,q)=(2,3)\) and \((2,5)\), checks all square relations, tests idempotence and computes image dimensions. It then checks every parametrized rank-two retraction and all pairs in the cases \((2,3),(2,5),(3,3)\), including direct comparison of compositions and of the predicted graph degrees.

The expected final checker line is `ODD_SQUAREZERO_RANK_TWO_RETRACTION_CHECKS_PASSED`. These are finite reproducibility checks, not exhaustive checks for arbitrary parameter values or for prime-power fields of nonprime order. The proof does not use a computational infinity claim.
