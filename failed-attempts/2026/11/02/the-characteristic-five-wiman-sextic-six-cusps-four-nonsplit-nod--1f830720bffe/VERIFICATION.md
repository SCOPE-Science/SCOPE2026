---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The equation is 2Q^3+P^2 with Q=X²+Y²+Z² and P=XYZ. The gradient forces either a single zero coordinate with Q=0 or three equal nonzero squared coordinates. The finite singular support also excludes a repeated component. At the six axis points, P,Q are parameters, giving A2 and one rational branch; the four remaining points have tangent discriminant 3 and two conjugate branches. Every component has degree divisible by three by intersecting an axis (the only intersections are transverse axis–conic supports with curve–axis multiplicity three); two cubic components would each have three cusps, impossible. The genus defect is ten, and the normalization has a rational point. Normalization-unit quotients give one additive group per cusp and one torus per node; the morphism to the norm-one torus is a↦a/σ(a), with σ the nontrivial field automorphism on the coefficient algebra, not absolute Frobenius on variable points. The normalization fibers give correction −4(−1)^m and zeta numerator (1+U)^4. Independent symbolic and finite checks in /workspace/review_replay.py reproduce the mod-5 equation, the tangent discriminants and counts 10,22 over F5,F25. The geometric arguments, not the two counts, prove the extension formulas.

## originality

FAIL

A distinct indexed Resultary finding gives the same model and characteristic, geometric integrality, complete arithmetic basket (including nonsplitting), rational normalization, all-extension counts and zeta. The remaining Picard-group statement is a direct consequence of those explicit data by the standard normalization-unit sequence. The two records are dated the same day; this is statement-level coverage, not an assertion of chronological priority.

## value

FAIL

The arithmetic singularity classification of this canonical model is meaningful, but independently indexed work supplies it along with the curve counts and zeta. Only the formula for a standard local-units product is explicitly additional; the precise product and its counts can already be recovered immediately from those data, so there is no valuable uncovered claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
