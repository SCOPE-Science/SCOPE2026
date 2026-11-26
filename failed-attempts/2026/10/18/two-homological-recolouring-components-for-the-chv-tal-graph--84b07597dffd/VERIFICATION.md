---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For any face of the open-neighborhood complex a common neighbor forbids its own color, so the coloring gives a simplicial map to the tetrahedron boundary. For a one-site move the union of the two images still avoids the common neighbor's color if that neighbor is unchanged; if it is the recolored vertex, the face itself has no changed vertex. Hence the two maps are contiguous. The signed 20-triangle chain is closed and pushes forward to a multiple of the oriented tetrahedron boundary; a palette permutation acts on that boundary by its sign. A separate exact enumeration using the listed graph and chain found no three-coloring, 18,024 labeled four-colorings, 64,320 undirected one-vertex moves and exactly two 9,012-state components, with degrees +1 and −1 on the respective components. It also checked the signs under all 24 label permutations. Replay: python3 /workspace/branches/021d8330-e34a-4dae-8fd5-a6e9399be218/independent_check.py. The bound scripts and logs were inspected but not executed.

## originality

FAIL

A distinct published Resultary result establishes the full same-graph census and component classification. Its signed rainbow-square invariant I is exactly −3 times the proposed homological degree on every labeled proper coloring, verified exhaustively in the independent replay. The chain formula gives a different explanation of this sign, but not a distinct component classification or invariant on the stated object. The indexed dates alone do not establish priority or record lineage.

## value

PASS

At the chromatic threshold on a canonical triangle-free four-chromatic graph, identifying exactly how single-site connectivity differs from Kempe connectivity is a natural question. The open-neighborhood cycle gives a topological reason for a persistent obstruction under legal moves, not merely a bare coloring tally. That mathematical use is independent of whether the classification is distinctive in the corpus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
