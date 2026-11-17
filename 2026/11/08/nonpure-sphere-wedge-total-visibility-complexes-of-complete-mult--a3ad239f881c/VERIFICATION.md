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

For each intra-part nonedge in K_{n1,...,nr}, distance is exactly 2 and the common neighbors are the vertices outside that part. Thus S total-visible iff its complement C is not contained in any part U_i of size≥2. Inclusion–exclusion of a forbidden upward families yields F=(1+z)^N−Σ_{large i}z^{N−n_i}(1+z)^{n_i}+(a−1)z^N; minimal permitted complements are a singleton-part vertex or a pair crossing two large parts, giving M=bz^{N−1}+Σ_{i<j large}n_i n_j z^{N−2}. No-singleton case is dual rank-two partition-matroid independence complex; matroid shellability and reduced Euler characteristic give ∨^{a−1}S^{N−3} over integers. For b≥1 the explicit union (Δ_U*∂Δ_B)∪(K0*Δ_B) of two cones has intersection K0*∂Δ_B, giving b-fold suspension; a≤1 cases are contractible. Facet equicardinality proves exact purity/matroid boundary. Independently computed shortest paths with selected forbidden vertices for all subsets of seven distinct 3+-part profiles (including a=0,1 and nonpure a≥2,b≥1) and verified formula f-vectors and facet counts; finite BFS cannot prove homotopy or integral torsion-freeness.

## originality

PASS

PASS best-of-knowledge for the complete arbitrary-part-size enumeration, precise nonpure/matroid boundary and integral wedge classification. Prior mathematical ingredients cover special cases but no inspected stronger result includes their total combination or explicit formulas.

## value

PASS

A natural complete classification of total mutual-visibility simplicial complexes for the entire complete multipartite graph family is useful beyond its maximum cardinality: both labelled all-face and facet polynomials, exact matroidality/purity threshold and integral wedge homotopy are determined. Singleton classes furnish an instructive infinite nonpure sphere-wedge boundary while retaining a single homology dimension; this is mathematically motivated, not an arbitrary small slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
