---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Translate the center to zero and set A=(L²)^(−1). A boundary contact satisfies xᵀAx=1 and pᵀAx=1: the joining line lies in the unique tangent hyperplane, which meets the strictly convex ellipsoid only at x. For t=pᵀAp>1, all contacts are x=x₀+z with x₀=p/t, z∈(Ap)^⊥, zᵀAz=1−1/t. This follows by expanding the quadratic and gives the complete nonempty section. Comparing |p−x₀−z|² and |p−x₀+z|² for all such z forces p−x₀ parallel to Ap; these z span (Ap)^⊥. Since t>1, p is therefore an eigenvector. Constant distance also forces |z| constant on that section; scaling arbitrary nonzero vectors in the section's linear space shows A is scalar there by polarization. This also suffices for equal lengths. Hence a round ellipsoid admits every exterior point. Otherwise for n≥3 the scalar complement has multiplicity n−1 and only the simple eigenline can serve as observer axis; the strict exterior condition removes |h|≤b from it. If there is no such eigenspace decomposition, no observer works. In n=2 scalar compression is automatic, so both axes can appear; it is correctly not imported into n≥3. At an axial observer the contact height is b²/h and the transverse radius is a√(1−b²/h²). Their squared-distance formula expands exactly as in RESULT.md, and its domain and far-field intercept give b and a. Inspected RESULT.md lines 26–50, VERIFICATION.md and equitangent_checker.py. The checker was not run; it uses finitely many directions and in dimensions above three a selected two-dimensional direction subspace, not an exhaustion. The symbolic argument is decisive.

## originality

PASS

The inspected literature defines the property and establishes distinct global rigidity and planar results; it does not imply the complete pointwise classification for a fixed ellipsoid in n≥3 or the explicit common-length profile. The key distinction from a circular section alone is that the circle center must be the perpendicular projection of the observer onto the contact plane. The related inverse results measure different data. Priority is qualified by incomplete access to historical quadric treatments.

## value

PASS

This resolves a natural complete locus problem for a standard class in which planar intuition would give a wrong higher-dimensional prediction. The result distinguishes round, rotational and more general ellipsoids by existence and placement of admissible observer rays. The profile recovers both semiaxes in the nonround surviving case. The value lies in the full necessity and sufficiency classification and sharp dimension distinction, not merely computing one axial length or rearranging an inverse formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
