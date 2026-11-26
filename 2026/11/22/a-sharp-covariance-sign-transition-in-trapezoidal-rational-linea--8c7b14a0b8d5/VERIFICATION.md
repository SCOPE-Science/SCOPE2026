---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

At height z the slice is sT with s=1−(1−t)z, hence for t<1 its volume-induced scale distribution is proportional to s² on [t,1]. Conditional on scale the dimensionless base coordinates (U/(bd),Y′=V/b) are independent of scale, with Y′ density (r+1−y)/(r+1/2) and E[U/(bd)|Y′=y]=(r+1−y)/2. Thus base cross-covariance in these coordinates is −Var(Y′)/2; E[Y′]=(r/2+1/6)/(r+1/2) and E[Y′²]=(r/3+1/12)/(r+1/2) give the claimed ρ. Scaling gives Cov(X,Y)=E[S²]Cov(U,V)+Var(S)E[U]E[V]. The positive prefactor leaves q−ρ with q=1−15(1−t⁴)²/[16(1−t³)(1−t⁵)] for t<1. Cancellation gives the finite endpoint values q(0)=1/16 and q(1)=0 and the displayed strictly negative derivative for 0<t<1; the prism also directly has the negative base covariance. The sign of q(0)−ρ is that of the given cubic; one sign change and opposite endpoint signs give its single positive root. Strictly decreasing ρ gives increasing t*, with t*→0 as r↓r* and t*→1 as r→∞; matching q(t)∼(1−t)²/12 to ρ(r)∼1/(6r) gives the stated √2 limit. A fresh bounded numerical check from the slice moments also agreed with the root and both signed witness moments. The supplied checker was inspected, not executed; its finite tetrahedral tests use floating hull triangulation with rational moment integration and are supplementary. The positive-to-negative orientation is for increasing t (widening the top); the phase diagram itself gives the direction unambiguously.

## originality

PASS

The exact polytope family is not new, and neither is the covariance decomposition. In the strongest inspected comparisons the same family has rational-linear-precision/Horn and inradius results, while a broader frustum result concerns directional widths. None supplies the distinguished-coordinate uniform-volume crossing, its aspect threshold or taper asymptotic. The indexed exact hit is the assigned article itself, not a distinct duplicate.

## value

PASS

In this canonical nonrectangular coordinate family the negative base cross-covariance competes with a positive common-scale fluctuation. The theorem tells a user exactly whether taper can reverse it, gives the unique taper at which the moment vanishes when reversal is possible, and quantifies the thin transition scale at large aspect. This complete sign diagnostic for a natural interpolation between prism and pyramid is more useful than computing a moment for an isolated shape and makes no affine-invariant or general-prismatoid claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
