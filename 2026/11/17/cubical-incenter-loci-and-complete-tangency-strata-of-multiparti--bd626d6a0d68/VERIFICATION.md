---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS — The actual irredundant perfect-graph Hansen clique inequalities have signed normal norm sqrt(4|C|+1). Maximal clique opposite pairs force radius R=(4r+1)^−1/2 and center conditions x_v=a_j constant within each part and z=2Σ a_j. Missing t classes give |Σ_{j∈T}a_j|≤β_t=(1−sqrt((4(r−t)+1)/(4r+1)))/2. Strict convexity β_t>tβ_1 for 2≤t≤r makes the r singleton inequalities necessary and sufficient, including singleton graph parts; only maximal cliques and saturated omitted-one-part cliques contact. The exact facet count is 2Π n_j+Σ_{|a_j|=h}Π_{k≠j}n_k. The center-basis Gram matrix diag(n_j)+4·11^T proves the intrinsic volume determinant formula. Independently checked strict β inequalities for r=2..50 and representative formulas; exhaustive software only corroborates all-parameter proof.

## originality

PASS

PASS best-of-knowledge — Prior perfect-graph Hansen literature supplies the complete clique-facet system, and published research supplies the scalar radius and origin-centered contacts. Neither entails the entire noncentral maximum-ball center parallelotope with face-stratified tangent-facet counts and intrinsic volume. Similar box classifications for twinned chain polytopes concern a genuinely different polar/facet construction and do not imply this Hansen result.

## value

PASS

PASS — The set of all centers of largest balls in a natural family of graph polytopes is a full r-dimensional continuum, with explicit precise contact transitions and Euclidean r-volume. This answers a structured geometric optimization/classification beyond a known scalar inradius, and its strict missing-class convexity has reusable explanatory content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
