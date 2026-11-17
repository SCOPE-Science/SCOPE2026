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

A locating-dominating set in K_{m,n}, m,n>=2, is exactly a set whose complement removes <=1 vertex per side; the forward direction uses false twins, reverse direction checks domination and distinct opposite-side traces. In an LDC partition, any coalition pair leaves at most two complementary singleton-class vertices, so >=5 vertex graphs have <=3 blocks. Two-block total is 2^{N-1}-(m+1)(n+1). Three-block partitions are exactly those with at least two transversal blocks; for N>=7 exactly two such blocks and the remaining large block, enumerated as two same-side singletons, a singleton+cross-pair, or two disjoint cross-pairs. Boundary N=4,5,6 exhaustively analysed. Independent direct labelled graph neighborhood-trace checks across 56,941 set partitions match the given polynomial and exceptional triangle counts for tested m,n.

## originality

PASS

Chellali et al arXiv:2602.18760v2 (full 23-page PDF inspected) prove general bounds and small C4 coalition case, not the all-biclique two-/three-class polynomial or exact six triangle-coalition partitions. Published 11/2 multipartite theorem proves only maximum C_L and counts four-class maxima in all-part-size-two multipartite graphs, not the full polynomial for arbitrary K_mn. Alternative locating-domatic and super-coalition definitions differ. Hence exact full all-partition census is non-implied.

## value

PASS

The introduced LDC-partition is a natural discrete graph invariant; full labelled biclique polynomial determines all feasible sizes, sharp exceptional small graphs and coalition-graph structure, beyond previously known scalar maxima. The twin-complement transversal criterion yields a reproducible classification applicable as an exact model for multipartite extensions. Not merely recomputing a known optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
