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

The claim is supported by a four-part symbolic and geometric proof in RESULT.md. Run `python check_fixed.py` with Python 3 and SymPy installed. The script checks the order-three transformation, blow-up coordinate formulas, denominator-cleared ideal identities, discriminant and resultant, special-fiber Groebner/nilpotence relations, reduction of the derivative and sample rational supports in six prime characteristics. Its successful terminal marker is `M05_C3_INTEGRAL_FIXED_SCHEME_CHECKED`.

The algebraic proof, not finite enumeration, establishes the global fixed scheme, finite flatness, characteristic-three Hilbert function and formal non-linearizability in all characteristics. There is no external or independent proof audit. The result does not determine the quotient singularity and is limited to the split surface and the indicated permutation.
