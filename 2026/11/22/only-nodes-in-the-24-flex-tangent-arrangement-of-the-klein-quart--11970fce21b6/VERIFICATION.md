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

Run `python3 VERIFY.py`. It checks every rational point of the projective plane over the field with 29 elements, identifies the 24 rational flexes from the complete intersection of the Klein quartic with its normalized Hessian, verifies the gradients are nonzero and normalized tangent lines distinct, and checks all 276 line pairs have distinct intersection points with multiplicity exactly two. It prints `KLEIN_FLEX_TANGENT_NODAL_ARRANGEMENT_OK` on success. It also performs supporting calculations at primes 43 and 71.

The mathematical argument uses good reduction at 29 to transport **absence** of triple concurrence to characteristic zero. The computation alone is a certificate of finite mod-29 facts, not an assertion that arbitrary experiments prove a characteristic-zero theorem. Finite-étale lifting, Bézout degree 24 and determinant specialization are the separately stated proof steps. No external independent audit has been conducted.
