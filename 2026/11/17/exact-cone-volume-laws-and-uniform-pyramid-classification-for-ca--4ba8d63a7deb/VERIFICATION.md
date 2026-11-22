---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The centered unit-incidence zonotope in H has d=N-1. For each oriented bond S|T, the induced Euclidean facet area is sqrt(st) tau(G[S])tau(G[T]), its support distance k sqrt(N/st)/2, and total volume sqrt(N)tau(G); these independently yield cone mass k tau(G[S])tau(G[T])/(2d tau(G)). Cactus minimal cuts are exactly one bridge or two edges of the same cycle. Their spanning-tree ratios are respectively 1 and 1/ell, giving claimed masses, full facet counts, sum-one, and equal-mass iff. Independently enumerated a two-triangle bridge cactus: tau=9, 2 masses 1/10 and 12 masses 1/15, totaling one. Finite check corroborates; algebra and cut classification supply the universal proof.

## originality

PASS

Best-of-knowledge noncoverage after implication comparison; The general area/height calculation plus cactus-only minimal-cut analysis yields the result, while inspected published findings do not explicitly dominate the combined all-cactus mass and equality theorem.

## value

PASS

This is a natural complete facet-pyramid spectrum for an entire block-structured class and a nontrivial equal-cone-volume classification, including examples outside parallelotopes. The block bond decomposition converts standard spanning-tree ingredients into a useful explicit invariant; this is more than an arbitrary finite calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
