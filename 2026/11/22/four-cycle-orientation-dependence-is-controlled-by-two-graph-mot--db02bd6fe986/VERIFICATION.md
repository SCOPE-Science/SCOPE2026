---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A cycle succeeds in 2 of 16 orientations, giving variance 7/64. Distinct four-cycles cannot share three edges because the three-edge path determines the closing edge. With no common edge, the events depend on disjoint variables. With one common edge, conditioning on it gives independent completions with constant probability 1/8 each. With two adjacent common edges, the distinct closing paths have different intermediate vertices, so the union is exactly a K2,3 edge-subgraph. The common path must orient consistently (probability 1/2), then the two completions have probability 1/4 each, giving 1/32 jointly. If the common edges are opposite, write the cycles as abcd and abdc with shared ab and cd. Matching the direction on ab forces contrary directions on cd. The union is K4, and the joint probability is zero. Each motif has three unordered pairs of constituent four-cycles with that union, and a pair determines its unique edge-subgraph union. Thus the covariance corrections are +6b₂,₃/64 and −6k₄/64; nonzero pair covariance detects either motif, and zero covariance implies independence for Bernoulli variables. In Q3 the graph is bipartite and distinct vertices share at most two neighbors. At any vertex, its three incident squares would require every pair of its three incident edge directions to differ, which is impossible. Independent exact enumeration reproduced the two motif probabilities and, for the cube's 4096 orientations, 512 occurrences per selected face, 64 per pair and none for the triple.

## originality

PASS

The supported distinct claim is the sharp two-motif classification and covariance/variance law for a fixed arbitrary underlying graph, with the cube as a higher-dependence witness. Neither the single-cycle baseline nor the complete-graph variance is credited as new.

## value

PASS

For a basic fixed-graph random model, the theorem decides pairwise independence by exact local obstructions and shows how the two obstructions affect variance with opposite signs. This distinguishes positive and negative dependence even where their contributions cancel in the total, and the cube establishes a genuine boundary between pairwise and three-wise independence without a tournament assumption.

The dated certificate retains the supplied scientific assessment, sources and limitations.
