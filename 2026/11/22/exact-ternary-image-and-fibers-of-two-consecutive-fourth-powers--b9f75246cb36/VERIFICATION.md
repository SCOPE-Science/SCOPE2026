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

Run `python3 CHECK.py` from this directory. The checker uses Python's standard library and performs exhaustive counts for every residue modulo \(3^k\), for \(k=1,\ldots,9\). The expected fiber formula is evaluated from a separate square-root-counting formula rather than from the polynomial enumeration and checks the full singular branch, including its transition at \(k=3\). The observed image counts are \(2,4,10,29,85,254,760,2279,6835\).

The infinite result is not certified by these tests; it is proved in RESULT.md using the centered quartic identity, Hensel lifting for the unit classes, a three-adic bijective normal-form transformation, and exact counts of square roots modulo powers of three. The independent mathematical audit and external validation have not been performed.
