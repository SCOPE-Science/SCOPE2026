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

Execute `python3 verify_double_six_coinvariants.py` (standard library only). It checks exactly 27 line classes, 36 root-pair double-sixes, all 21 Picard-kernel basis vectors, an exact determinant of absolute value 65536, the modulo-four diagonal, a rank-15 equivariant pair map, and all eleven Frobenius permutations. The final output must be `DOUBLE_SIX_FROBENIUS_COINVARIANTS_VERIFIED_OK`.

The mathematical proof uses a complete list of 72 roots and conjugacy types, an exact determinant upper bound together with modular divisibility lower bounds, and an explicit equivariant surjection. It does not infer an infinite statement from finite-field sampling. No independent scientific audit has been performed. The computation concerns the stated six-point blow-up family, not arbitrary cubic-surface Galois actions.
