---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

In the stated unrescaled inner product, a convex combination y of signed edges is the projection exactly when each signed-edge inner product with x−y is at most ⟨x−y,y⟩. For d=1 the residual is zero; for d=2, y=x/2 and the nonadjacent endpoints give support 1/2 and squared norm 1/2. For d=3 along the chosen arc, the weights (3,1,3,2,2)/11 yield residuals (6,2,−2,−6)/11 along the arc, with 2/11 immediately before it and −2/11 immediately after it. Adjacent differences have magnitude at most 4/11, including the closing −2/11 to 2/11 jump at n=6, and all five selected signed edges attain that support. The squared norm is (72+16)/121=8/11. For d≥4 both arcs separate the two triples of nonzero values by at least one zero; the quarter-weighted incident edges attain support 1/4 and the residual has squared norm 2(1/2)^2+4(1/4)^2=3/4. The support test also gives uniqueness and covers both shortest-arc choices at a tie. For a convex combination of roots, the squared norm of the corresponding combination of their residuals bounds the squared distance above. Equality at the maximum requires all contributing residuals to have the maximal norm and be identical by the strict variance identity. The unique extrema in each such residual recover the ordered endpoints. Thus no nonroot is farthest. The root counts are 2n per nonantipodal cyclic separation and n at an antipodal separation, giving all three stated Hausdorff and farthest-count regimes. Reading the supplied checker corroborates the certificate design; its two directions of an even antipodal separation coincide as ordered-root inputs and the all-n proof does not rely on this finite test.

## originality

PASS

The standard symmetric edge hull and normal-cone criterion are not new. The distinct result is the combination of exact cycle-specific Euclidean shells (including saturation at four) and the full set of continuous maximizers. The strongest indexed analogue uses a path; it shares an interior 3/4 value but is not a statement of this law.

## value

PASS

The cycle is the natural closed counterpart of the path, and its exact Hausdorff error against the complete root hull measures the Euclidean effect of keeping only rim edges. The short-shell transition and saturation explain why many ordered roots, rather than two path endpoints, tie for worst error. Classifying the equality locus in the full continuous hull, not merely identifying a root with maximal error, is independently useful for extremal comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
