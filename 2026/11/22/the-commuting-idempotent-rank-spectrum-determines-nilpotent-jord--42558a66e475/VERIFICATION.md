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

Run `python verify.py` with Python 3 and no third-party dependencies. The checker constructs Jordan representatives, directly enumerates all candidate idempotent matrices over the indicated small prime fields, independently checks commutation and ranks, compares with the Gaussian forward formula, and applies the triangular inverse recurrence.

Exhaustive matrix tests cover every Jordan partition and all matrices of dimensions 1–4 over the two-element field, and dimensions 1–3 over the three-element field. The symbolic coefficient formula plus exact inverse is also checked for all partitions through dimension 22 at field-cardinality parameters 2, 3, 4, 5; these latter checks are not direct field matrix enumerations. Expected terminal marker: `JORDAN_IDEMPOTENT_RECONSTRUCTION_VERIFIED`.

Proof dependency: an idempotent commuting with the fixed nilpotent corresponds to an ordered invariant direct sum, and the module automorphism-group quotient yields the exact profile weights. The coefficient argument in RESULT.md is the all-dimensional proof; the finite computation is only corroboration. No external or independent audit has been performed.
