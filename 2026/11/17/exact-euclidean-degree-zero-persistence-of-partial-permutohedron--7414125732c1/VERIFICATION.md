---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

Run `python3 check_mst.py` with Python 3 (standard library only). It enumerates the actual vertex configurations for each tested pair of positive integer parameters, forms every unordered pair, calculates squared Euclidean lengths in integer arithmetic, runs complete-graph Kruskal, and compares the resulting multiset with the theorem. The observed output was:

`PARTIAL_PERMUTOHEDRON_MST_CHECKS_PASSED parameter_profiles=55 exact_pairs=59105 cumulative_vertices=1429 examples=[(3, 4, [(2, 8), (4, 3), (9, 3), (16, 1)]), (4, 2, [(1, 12), (2, 3), (4, 1)]), (4, 5, [(2, 49), (4, 4), (9, 6), (16, 4), (25, 1)]), (5, 3, [(1, 60), (2, 19), (4, 5), (9, 1)])]`

Every check uses integer squared lengths; the keys in the example histograms are squared lengths. Profiles are restricted by the script to at most 210 vertices so complete pair enumeration is practical. A finite test is not a proof for all integer parameters. The proof's critical global step is the rank-separation/rearrangement inequality, which applies to every pair of vertices and rules out unobserved shorter connections, followed by explicit constructions at all predicted thresholds.

No external certification or independent review was performed.
