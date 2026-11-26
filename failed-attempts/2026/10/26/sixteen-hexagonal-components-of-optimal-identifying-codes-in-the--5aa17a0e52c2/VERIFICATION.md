---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Sixteen distinct nonempty traces require at least five code vertices since 2^4−1=15. Independent enumeration (python3 /workspace/review_checks.py 4) used the six specified differences, compared all sixteen closed-neighborhood traces for each of the 4368 five-subsets, and found exactly the 96 distinct sets obtained by taking the three other vertices of the root's parity coset plus an edge of its open neighborhood. An independent exchange construction indexed the accepted sets by their four-element subsets; it gave degree two at each vertex and precisely sixteen connected groups of size six. There is also a direct check that distinct roots cannot exchange: for distinct cosets their cores are disjoint and an adjacent pair meets either specified coset in at most one vertex. To have intersection four would require both extra vertices of each code in the opposite core, so this is impossible. In the same coset distinct cores intersect in two, so intersection four would require a common adjacent pair in both root neighborhoods. For each nonzero parity-coset displacement (2,0), (0,2), (2,2), the two common neighbors are opposite and nonadjacent. For a fixed root the six edges of the neighborhood cycle give their line graph, again a six-cycle. These checks use the labeled graph, nonempty traces and unrestricted replacement exactly as specified.

## originality

FAIL

A distinct public Resultary record, 7b3432c6fd0d, explicitly covers every asserted Shrikhande conclusion: the minimum five, all 96 labeled optimum sets, the unique parity-coset and neighborhood-edge formula, and the exchange graph 16 C6. No mathematically distinct finding is established for this record relative to that coverage. Both records are dated the same day; which came first is not established. This is a failure to establish distinct contribution, not a finding that the theorem is false or a claim about priority or derivation.

## value

FAIL

The exchange classification itself is a useful structural invariant: a bare optimum size does not imply disconnectedness or the parity obstruction. But the assigned record offers no separate useful mathematical increment over the exact same labeled classification and exchange structure in the distinct matching record. Its numerical replay validates the fact rather than supplying a new invariant or an improved structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
