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

The standalone `verify.py` (requires Python 3 and SymPy 1.14) constructs the published cohomology determinant, verifies three symbolic normal-form nonvanishing determinants, checks a coefficient plane section through fifteen unisolvent evaluation points over \(\mathbb F_{101}\), and recomputes the complete plane-quartic Jacobian ideal and its three ordinary noncollinear singularities. The exact returned lines are `VERTICAL_WITNESSES_OK`, `TERNARY_SECTION_IDENTITY_OK`, `THREE_DISTINCT_NONCOLLINEAR_NODES_OK`, and `CERTIFICATE_OK`.

The determinant identities were checked against the coefficient ordering and source-block dimensions in the stated matrix construction. The full all-parameter geometric irreducibility step uses characteristic-zero geometry and is not an exhaustive finite computation. No independent audit has been performed.
