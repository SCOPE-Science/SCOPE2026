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

The accompanying `VERIFY.py` was executed from the materialized package and returned `VERIFY_OK: 26 exhaustive dihedral orbits; exact rational spectral bounds and strict global optimization comparisons`. The script generates all 251 four-coordinate selections for grid orders 5 through 9, partitions them into 26 orbits, verifies each exact-rational 3-by-3 spectral enclosure by principal minors, and strictly compares both criteria against all other orbits. The grid order 4 is trivial, as all four coordinates must be taken. The source theorem is a finite statement. No claim is made beyond the stated grid orders, and independent validation is unperformed.
