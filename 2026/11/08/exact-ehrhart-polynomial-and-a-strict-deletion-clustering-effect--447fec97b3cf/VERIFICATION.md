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

Use `python3 artifacts/verify.py` from the package root. The verifier is standalone aside from optional NumPy/SciPy used solely for independent small convex-hull volume calculations; the integer enumeration and algebraic checks use only the Python standard library.

Executed output:

`DELETED_STAR_POLAR_EHRHART_CHECKS_PASSED independent_counts=32 numerator_and_lead=45 strict_matching_comparisons=175 independent_hulls=6`

The integer enumeration constructs every edge of the deleted-star graph and tests the defining absolute-difference inequalities with distinguished coordinate anchored at zero. It is not an enumeration of the proof's overshoot classes, so it provides an independent finite check. Ehrhart leading coefficients are extracted using exact forward differences, the polynomials' h-star symmetry is checked in finite profiles, and matching comparison values are computed separately. SciPy halfspace intersections and convex hull volumes check the rooted-coordinate volume without using the closed volume formula as an input.

These finite checks do not prove the infinite-family identities or historical novelty. Both rely respectively on the exact proof and the documented literature comparison. Independent mathematical audit remains unperformed.
