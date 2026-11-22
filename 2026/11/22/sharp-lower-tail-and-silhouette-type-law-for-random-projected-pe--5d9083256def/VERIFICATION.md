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

# Verification and limits

The analytic claim is established by the five proof steps in `RESULT.md`. To replay independent finite numerical diagnostics, run `python3 checker.py` with NumPy and SciPy. The executable compares exact edge-projection perimeter formulas against planar convex-hull construction for 2,000 seeded uniformly distributed test normals, checks extremal bounds and silhouette types, and numerically evaluates the exact local spherical integrals for three positive tail cutoffs. It also verifies the tangent angular formulas and leading-area integral. The preparation run passed **6,199** assertions, returning a leading coefficient approximately `1.1953469179961405` and conditional triangular fraction `0.2118330336632897`.

The finite random checks do **not** establish global inequalities; the rigorous arguments appear in the proof. The printed decimal values are quadrature approximations, not separately certified interval enclosures. Independent external review has not been performed.
