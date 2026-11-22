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

# Verification of the finite transformation calculation

Extract `check.py` and `check-output.txt` into the same directory, then run `python3 check.py`. The checker requires only Python's standard library and prints deterministic lines. It enumerates every function in 29 independent rank-two sandwich configurations for two through six points, evaluates the sandwich product directly, constructs the full commuting relation on star-idempotents, checks all constant and rank-two neighbor lists and compares the matrix-power traces of the unsigned incidence Gram matrix for every power from one through the ambient degree. Its final line must be `PASS total configurations=29` and its complete output must match `check-output.txt`.

The exhaustive finite computations support, but cannot prove, the formulas for all degrees. The unrestricted proof is the rank-two idempotence classification, exact pairwise commutation calculation, explicit incidence Gram diagonalization and degree-separation argument in RESULT.md. In particular, the checker does not independently enumerate the full graph automorphism group; that assertion is supplied by the mathematical proof.

No outside independent audit, certification, or validation is asserted.
