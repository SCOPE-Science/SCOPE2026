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

Run `python3 verify.py` alongside this document. Expected output:

```text
EXACT_INTERSECTION_CASES_OK 2014
ANTICANONICAL_VOLUME_AND_NULL_CURVE_TESTS_OK
```

The code checks rational intersections, discrepancy-corrected squares and exceptional-chain null conditions in the specified finite range. For the general theorem, the proof's key non-computational checks are the infinitely-near Bézout inequality and the exact contractions of curves supplied by arXiv:2610.07164, Theorem 3.2 and Section 4. No exhaustive enumeration of curves outside the test range, independent audit, or outside validation is claimed.
