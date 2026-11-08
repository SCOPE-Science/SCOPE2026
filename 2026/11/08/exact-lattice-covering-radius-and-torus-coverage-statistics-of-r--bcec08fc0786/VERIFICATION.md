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

Exact derivation: parameterize a point in an integer translate of a dilated Reeve simplex by three nonnegative barycentric coefficients, minimize over the first two integer coordinates, then reduce the third integer coordinate to a finite cycle of length \(q\). The optimization yields the exact fractional-part formula. Taking the supremum gives the covering radius. Integrating the formula over the fundamental torus gives the unit-scale uncovered volume and the mean. A deterministic coupling gives the distributional limit.

Supplementary independently executed check: `python verify_reeve.py`, using the Python standard library. Output reports 19,773 independent exact-rational comparisons of cyclic minimization against the claimed closed formula for \(q=1,\ldots,9\), exact rational polygon integrations \(J_1=5/12\), \(J_2=11/12\), \(J_h=1\) for \(3\leq h\leq11\), and corresponding exact arithmetic identity checks. No floating-point tolerance is used.

Finite-grid calculations do not prove the arbitrary-parameter theorem; the argument in RESULT.md does. No exhaustive search of all historical literature is claimed. The complete text of a plausible related 2026 Reeve-construction paper was not available for inspection, and there has been no independent mathematical audit.
