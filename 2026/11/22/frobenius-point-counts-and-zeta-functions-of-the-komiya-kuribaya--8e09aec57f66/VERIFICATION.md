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

# Verification scope

Run `python verify.py` with `kkcore.py` beside it, plus SymPy for exact integer factorization. The exact determinant support and all seven exceptional incidence tables, along with each of the four generic Frobenius signs, must return `KK_BITANGENT_ZETA_ALL_PRIME_CLASSES_OK`. Run `python verify_bitangents.py` to test each of the 28 binary-quartic square restrictions in the biquadratic coefficient field; the expected result is `ALL 28 BITANGENTS VERIFIED`. Run `python verify_direct.py` to count all rational points on the union independently over the seven specified prime fields.

The proof of the all-prime theorem combines the exact determinant norms with the fact that every Frobenius action is one of four explicitly checked sign changes. All field-extension counts then follow from the resulting order-two Frobenius action. The finite programs reproduce this complete reduction and check the stated tables. A separate outside mathematical audit has not been performed, and the work does not cover characteristics less than seven.
