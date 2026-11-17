---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Connected graph Laplacian forces all vertices to fire an equal count in any three-round periodic orbit. For primitive period three that count is one or two. Fix one hub phase and enumerate each triangle's feasible peripheral firing phases; precisely three ordered choices have feasible chip intervals. With a synchronous-pair triangles, 0<=r<=k−a−1 hub excess choices give one-firing mass 3k+a+r and coefficient 3 sum_{a<=j}binom(k,a)2^(k−a) for 0<=j<k. Chip complement Cσ(v)=2deg(v)−1−σ(v) commutes with the update on bounded periodic states and reflects masses across 10k−1, establishing high band and completeness. Sum of coefficients yields 12k3^(k−1); size-biased B=1+Bin(k−1,2/3) and uniform hub excess yield two uniform limit intervals. Independent direct bounded-state simulation yielded k=2 total72 and k=3 total324 with exact mass histograms, matching the analytic polynomial. Finite simulation is corroboration, not the all-k proof.

## originality

PASS

The general Ji–Li–Wang period-three exclusion only constrains the open middle interval; the friendship endpoints, every mass coefficient and the two-uniform asymptotic are not consequences of that prohibition. Related fan K1 join path, complete, complete bipartite and friendship period-two findings have different graph dynamics. The separate shared-hub/triangle phase count is needed for friendship primitive-three census.

## value

PASS

The friendship graph is a natural windmill family and the exact full mass-resolved population and sharp realization at BOTH universal middle-stair endpoints answer a motivated dynamical counting problem. The binomial coefficients and limiting two-uniform mass law have genuine finite-to-asymptotic structure, not a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
