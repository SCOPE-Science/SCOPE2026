---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For any one-Lipschitz f on a positive-length bridgeless metric graph, two edge-disjoint routes between min/max points give at least 2(v-u)/L arclength mass for each intermediate level interval. Its nondecreasing quantile Q has 0<=Q(t)-Q(s)<=(L/2)(t-s); thus Q(t)-(L/2)t is nonincreasing and centered stop-loss integrals are bounded by those of a centered uniform interval of length L/2. Equality for strictly convex tests requires Q to be affine with that slope; edge-disjoint min/max paths must each have length L/2 and exhaust the graph, forcing f to equal distance from a diametral point up to additive constant. This validates the claimed sharp law, variance L²/48 and equality graph characterization, including graph subdivisions, parallel edges and nonconstant test functions. Finite cycle/figure-eight exact variance was independently checked, but does not prove the universal case.

## originality

FAIL

Existing Nakajima–Shioya isoperimetric-dominance theorems (Theorems 1.8 and 3.4 and Corollary 3.17) are stronger: when I_X>=I_uniform, the interval-uniform law is an iso-dominant, so every one-Lipschitz graph pushforward is a monotone one-Lipschitz image of that uniform law. Bridgeless graph arclength has isoperimetric perimeter >=2/L at every interior volume because each proper cut requires at least two boundary crossings, exactly the normalized uniform interval profile. Quantile contraction and centered convex order follow, including equality distributions; Theorem 1.5 relates equality to maximal diameter. The two-geodesic extremal graph geometry is an immediate Menger/edge-length exhaustion consequence, not an independent unknown theorem. In addition, an existing bridge-budget theorem gives the exact B=0 variance L²/48. This is prior implication rather than mere title/parameter similarity.

## value

FAIL

The all-convex-function statement is mathematically useful, but it is a direct natural special case of the earlier general 1-measurement/isoperimetric comparison and Lipschitz-order machinery; the variance sharpness is independently already published at bridge budget B=0. The elementary extremizer graph description does not supply a substantively new structural classification beyond saturated diameter and edge-disjoint paths. As a new standalone contribution, the submitted complete claim is substantially covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
