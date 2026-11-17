---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The exact two-cube convex hull gives W_O=max(2U,2V,U+V+T) and W_C=2max(U,V), T=|sum_j b v_j|. Normalizing W_O=2 gives feasible polytope with exactly six vertices; bounding Euclidean dual norm by Q(U,V,T)=U²/a²+(V²+T²)/(2b²), a strictly convex quadratic, reduces maximum to two vertices (1,1,0) and (0,1,1). Equality requires one lower active coordinate and one positive/negative upper pair, or one upper coordinate; tie at a=√2b includes both and no continuum. Vertex-to-vertex squared distances give the two separate diameter branches and exact equality pair classes. Exact finite profile checks confirm support and distance identities, not infinite classification.

## originality

PASS

All-scale two-level order minimal-width geometry and independent diameter transition not present in original enriched-poset metric/Ehrhart literature or the fully inspected earlier same-family unscaled support theorem. Prior chain/unscaled and convex-hull inputs are credited. Best-knowledge PASS.

## value

PASS

Complete sharp Euclidean width normal family and diametral-pair bifurcations for a natural Ehrhart-equivalent order/chain pair yield a constructive comparison of intrinsic metrics that Ehrhart data cannot recover. Two independent thresholds (scale-only, size×scale) provide meaningful geometry rather than an arbitrary sampled slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
