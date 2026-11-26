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

The squared normalized coherent-state overlap is exp(−|z−w|²), giving the factor π⁻² in the double area integral. Outside any fixed neighborhoods of the unique facing support points the horizontal gap increases by a fixed positive amount, so the omitted integral is exponentially smaller than exp(−L²)L⁻³. For an independent check of the coefficient, disintegrate into vertical slices at horizontal deficits r,s. The two slice widths are asymptotic to 2√(2r/κ_A) and 2√(2s/κ_B) by inversion of the nondegenerate local boundary quadratics. On those slices the transverse factor tends uniformly to exp(−η²) as r+s tends to zero. Scale r=x/L, s=y/L. The widths contribute L⁻¹ and the two deficit differentials L⁻²; the remaining exponential is bounded by exp(−2x−2y) and the rescaled widths by constants times √x and √y. Dominated convergence gives π⁻² exp(−η²)·8/(√(κ_Aκ_B))·[Γ(3/2)/2^(3/2)]² = exp(−η²)/(4π√(κ_Aκ_B)). For centered disks the curvatures are 1/R and 1/S, η=0 and L=d−R−S. The proof uses positive facing curvatures, not merely strict convexity.

## originality

PASS

The distinct claim is the normalized far-separation asymptotic for fixed convex bodies, not the Gaussian trace identity, the representation by a covariogram, or the Laplace method. In the strongest inspected related finding the shape itself grows first and the gaps remain bounded in the proved limit. The inspected literature gives an integral starting point, but does not give this fixed-shape asymptotic or cover its conditions and coefficient.

## value

PASS

For two Gaussian localization measurements the mixed trace quantifies cross-interaction and, in the disjoint Ginibre interpretation, determines the small count covariance. The theorem identifies the sharp polynomial correction to the Gaussian decay and the precise dependence on two facing curvatures and fixed transverse offset. A rough distance estimate, the exact Gaussian integral alone, or the related dilation theorem gives none of those data. The result uses a classical method to answer a concrete geometric asymptotic question rather than claiming novelty for Laplace's method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
