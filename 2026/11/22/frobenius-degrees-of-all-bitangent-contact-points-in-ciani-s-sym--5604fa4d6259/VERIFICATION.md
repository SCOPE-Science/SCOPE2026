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

# Reproducibility

Run `python3 verify_contacts.py` with Python 3 (standard library only). The exact verifier enumerates the complete rational line set and discriminant types, independently constructs all 28 geometric bitangents over explicit quadratic extension fields and calculates the contact Frobenius degrees. It checks every smooth parameter over prime fields of orders 5, 7, 11, 13, 17, 19, 23 and 29, verifying the three line-group decomposition and the number of parameters with six degree-four closed points.

Expected terminal marker: `CIANI_CONTACT_SUPPORT_FROBENIUS_VERIFIED`.

The infinite prime-power assertion relies on the explicit contact quadratic identities, the quadratic norm criterion, and a Jacobi sum, not on finite computational evidence. Characteristic three, singular parameters and unmarked moduli are not included. Independent mathematical audit has not been performed.
