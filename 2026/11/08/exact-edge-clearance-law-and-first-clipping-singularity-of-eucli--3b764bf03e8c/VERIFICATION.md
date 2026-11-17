---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For each free edge direction j, squared distance equals the sum of squared near-face gaps in the other d-1 coordinates; minimizing j removes the largest gap, so T_d² is the sum of the d-1 smallest squared iid Uniform[0,1] gaps. Joint order-statistic density d! gives an exact ordered-ball integral weighted 1-u_(d-1). Below t=1, homogeneity gives polynomial a_d t^(d-1)-b_d t^d. For 1<t<sqrt2 the clipped region has one coordinate v>1 and the others in an orthant ball; integrating its negative weight gives the stated positive correction. Beta integration yields K_d ε^((d+2)/2), hence sharp one-sided differentiability order. d=3 polar/arcsin integration, shrinking simplex at center for ε^d upper tail, and E(sum U_i²-max U_i²) produce the remaining formulas. Independently tested d=3 CDF at 8 points against order-statistic quadrature, exact endpoint and mean for d=3,4,5,9. Numerical checks do not replace the all-dimensional argument.

## originality

PASS

Best-of-knowledge PASS. Classical three-cylinder intersection yields the d=3 small-t polynomial and is expressly excluded as novel. Primary two-point-distance studies of random cubes, intrinsic wireframe distances, and vertex-to-surface distances concern different random variables. The searched mathematical corpus did not show the complete finite-edge d=3 CDF, the general first face-clipping correction with dimension-dependent exact cusp, or the all-dimensional center tail. An inaccessible 2012 intersecting-cylinder report and potentially equivalent polytope tube formulas remain material priority risks; no full-text negative inference is made from their abstracts.

## value

PASS

The Euclidean distance from an interior random point to the cubical wireframe is a natural clearance statistic. Its exact threshold at half-side is canonical—the first reach of a tubular neighborhood to the opposite faces. The sharp cusp order/constant, complete cubic distribution and center-tail law give concrete geometry across arbitrary dimensions; these are not implied by the already-known low-radius intersection volume or by generic two-point distances. Full d>3 middle CDF is explicitly outside scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
