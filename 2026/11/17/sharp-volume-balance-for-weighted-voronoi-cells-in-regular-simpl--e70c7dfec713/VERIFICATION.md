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

Run the package-local standard-library `verify_simplex.py` with Python 3.9 or later. It prints `PASS: 137 exact rational test cases, independent flag-determinant volumes in dimensions 2--6` on success. The checker reconstructs vertex-foot coordinates, exactly integrates via rational determinant decompositions independent of the inclusion-exclusion expression, and tests equality, strict bound samples, endpoint formulas and conservation. A separate numerical checker was also executed for 164 additional comparisons during development but is not required to reproduce the exact certificate.

The analytic proof, not finite enumeration, establishes the all-dimensional statement. No external certification or independent audit is represented by these computations.
