---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The pinned RESULT.md proves radial/angular factorization for differences of two independent uniform interior-ball points. The positive beta-integral c_{d,k} calibrates the radial moment, and squared spherical coordinates have Dirichlet(1/2,...,1/2) law. Consequently the moment series is product_i(1-a_i^2 t)^(-1/2), whose reciprocal square truncated at degree d recovers all axes including repeats. Invertible power-sum transformations and a Vandermonde Jacobian prove the generic lower cutoff; supplying volume fixes e_d, saving one moment. p_1^2/d <= p_2 < p_1^2 gives the two-moment range and endpoints. Independently checked the radial calibrations for dimensions 2 through 7 and source symbolic check_ellipsoid.py, rather than trusting its exit claim. No finite test is used to prove general d.

## originality

FAIL

Decisive exact prior coverage: the complete published 2026-11-02 RESULT.md for sharp finite distance-moment tomography treats identical solid ellipsoids, identical pair-distance sampling, d-even-moment reciprocal-square reconstruction polynomial, and exact generic necessity. Its normalization b_{d,k} is the same radial beta moment by recurrence, and it additionally proves optimal global 1/d-Hölder inverse stability. Volume-known d-1 follows mechanically by fixing the missing product coefficient; the simple moment-ratio inequalities are not a new inverse theorem.

## value

FAIL

The finite inverse cutoff and polynomial reconstruction are already provided verbatim up to normalization by a published stronger theorem. Volume-known d-1 and the two-moment elementary inequalities are consequences/recomputation, not an independently motivated unaddressed exact problem. A new algorithmic certificate for the covered claim would not restore new scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
