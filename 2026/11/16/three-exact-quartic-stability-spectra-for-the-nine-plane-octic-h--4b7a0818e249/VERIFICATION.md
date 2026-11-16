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

The bundled Python-standard-library program `verify_f9.py` reconstructs the finite field, all four odd character matrices, exact degree-eight characteristic polynomials over the 24th cyclotomic integer ring, and the three disjoint affine orbit classes. It proves all 126 selected-set cases using orbit invariance rather than random enumeration, and verifies disjoint rational root isolations and the sharp extremal orbit. Run `python3 verify_f9.py`; a final PASS line indicates the internal finite computation succeeded. Decimal displays are derived from exact algebraic roots and are not used as certificates. This document does not assert independent audit.
