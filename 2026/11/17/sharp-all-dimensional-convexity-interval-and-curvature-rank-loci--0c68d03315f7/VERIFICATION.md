---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For orthonormal u,v, differentiating the homogeneous quartic great-circle restriction gives Q=12a-3b-3/(d+2), a=Σu_i²v_i², b=Σu_i⁴. Minimum -3-c is attained at axes; for the maximum, 2a<=b+g, a+g<=1, a<=1-b, and a<=1/2 imply 4a-b<=3/2 by the split b<=1/2 or >=1/2, attained only at balanced signed two-coordinate normals with complementary tangent. Hence Q_max=9/2-c and support Hessian is semidefinite precisely on the stated epsilon interval. Equality analyses determine at the positive endpoint rank zero at ±e_i and at negative endpoint rank d-2 at two-coordinate normals. Positivity and differentiability of the homogeneous extension ensure strict convexity including curvature-degenerate endpoints; no assertion of positive curvature there. Independent exact-rational checks at d=3,4,5,10 reproduced thresholds and coefficient. The normalized harmonic variance 24(d-1)/[(d+2)^2(d+4)(d+6)] with Laplace eigenvalue -4(d+2) gives V/(2V)=-36d(d-1)(d+3)/[(d+2)^2(d+4)(d+6)], and determinant support-coordinate formula gives the polynomial-degree bound.

## originality

PASS

Best-of-knowledge PASS for sharp d>=4 support convexity amplitudes, all-dimensional equality/rank loci and volume coefficient. The 2026-10-18 published d=3 result treats identical quartic family at d=3 and is fully acknowledged; it does not state all d>=4 extremal tangent pairs. The broad primary Antunes–Bogosel support-function optimization method is numerical in dimensions 2 and 3 and does not dominate this all-dimensional sharp tensor result.

## value

PASS

This sharply classifies when a canonical degree-four hyperoctahedral harmonic actually defines a convex support body in every dimension, including singular normal strata and distinct rank degeneracies at opposite thresholds. It quantifies the second-order volume loss at constant mean width. The universal extremal pair inequality and d-dependent curvature nullity make the extension substantive, not a cosmetic d=3 substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
