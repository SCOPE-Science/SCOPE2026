---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The projector preserves means, and the minimum-norm lift of a difference vector u is D^T(DD^T)^(-1)u. Thus the induced problem is an H-metric projection onto the ℓ1 ball for H=(DD^T)^(-1). On a signed support J, fixing all other coordinates to zero and enforcing s^Tz_J=τ gives the stated affine derivative; strict off-support KKT slack makes the chosen face cell locally full-dimensional. The inverse principal Green matrix has the gap-conductance Laplacian form by eliminating the unselected nodes. Green-kernel linearity gives nonnegative interpolation columns of total mass at most one; the entries of Bs align with s, so ||Bs||_1=s^TBs. Dividing the rank-one correction by this positive denominator gives a column bound of two. Piecewise affinity and continuity extend the slope bound across cell boundaries. Scalar clipping and the two displayed 2×2 full-support cases, with zero singleton derivative, give the upper bound one for n=2,3. In n≥4 the full ascending face has correction supported on the two end edges, so shifting one interior input difference by ε yields output difference εe_k−(ε/2)(e_1+e_m); the residual multipliers 1 and 1+ε/2 certify the claimed projections. The two ratios are attained in the interior for low n and by this pair scaled to any τ>0 for high n. Radius zero yields zero modulus as stated. Replay: frozen RESULT.md §§1–6. The provided rational checker was inspected, not run; finite face enumeration is a supplement, not the all-dimensional proof.

## originality

FAIL

The distinct indexed result 43b65933e518 already states the exact same theorem, with the same open path, real inputs, unweighted Euclidean projection, two-input seminorm, quantification over all positive radii, constants and attainment. Its original Finding and proof were inspected. This is demonstrable coverage, not a conclusion about who first derived it or about provenance. The Green-matrix presentation is the difference-coordinate form of the same face-tangent mechanism and is not a surviving new claim.

## value

FAIL

The sharp instability transition is intrinsically a meaningful stability question, but this record adds no distinct useful theorem to the existing exact classification. The inverse-Green computation expresses the existing block-face calculation in edge coordinates and neither extends the geometry or metric nor identifies a new exact invariant. A different witness normalization and extra finite checks do not rescue a statement already proved. No repaired claim is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
