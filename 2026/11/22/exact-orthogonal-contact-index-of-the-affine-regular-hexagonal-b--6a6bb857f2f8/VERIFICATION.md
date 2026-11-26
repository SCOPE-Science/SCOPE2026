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

Equalize the two nonzero perpendicular image lengths by shrinking the input columns to the smaller image length. In the orthonormal image coordinates this gives QS=rI and r≤1/||S⁻¹||. Rescaling either column outward to the sphere multiplies S⁻¹ on the left by a Euclidean diagonal contraction, so it cannot decrease the reciprocal, and Q=S⁻¹/||S⁻¹|| attains it for each independent sphere pair. Dependent pairs have reciprocal continuously extended as zero by the determinant formula. Evaluation on the six hexagon vertices gives denominator max(||row 1 of S||₂,||row 2 of S||₂,||row 1 + row 2||₂), with numerator |det S|. The stated rotation, reflection and sign changes reduce to the same edge (bound 1/√2) or columns (1,−s),(−t,1). Put 0≤s≤t. The two active denominators are A=√(1+t²) and B=√((1−s)²+(1−t)²). The score using A decreases with s; using B it increases, since the derivative numerator is (1−t)(1−s−t+t²)≥0 wherever B is active. For t≤τ=2−√3 the best is s=t, with score (1+t)/√2; for t≥1/2 the best is s=0, with score ≤2/√5. Between these cutoffs the best is s=1−√(2t), and the sign of the total derivative is that of −1−t+√(2t)(3+t²)/2, an increasing function there, so the maximum is at an endpoint. The difference in squared endpoint scores is (26−15√3)/5>0. At s=t=τ the three vertex norm constraints agree, and the claimed inverse matrix sends the columns to perpendicular vectors of length (1+τ)/√2=(3−√3)/√2. This covers the real norms and all degenerate edge cases. The uploaded floating-point diagnostics were read, not used as proof or executed.

## originality

PASS

The same invariant and hexagon were previously studied, with the strict inequality below one already established. The supported new content is the sharp value and attaining contraction, not the failure of unit contact itself. No examined prior result fixes the sharp number.

## value

PASS

This is the exact attained optimum of a pre-existing contact invariant on its motivating non-Euclidean test plane. It makes the qualitative obstruction quantitative and sharp even though the standard exact distortion and tensor constants only bound it. Both the numerical gap and extremizing contraction are useful as benchmarks for comparisons of these invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
