---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

For GP(8,3) with 16 labeled vertices and 24 distinct edges, an edge matching is inclusion-maximal exactly when its unmatched vertex set is independent. Source recursive inclusion/exclusion visits each matching once and reports sizes 6:176, 7:336, 8:33 with none <=5. An independently implemented exhaustive combinations enumeration of all k-edge matchings confirmed 0 for k<=5 and the three counts. At each of 176 six-edge matchings, replace exactly one of six chosen graph edges by an unused edge, retaining only enumerated six-edge maximal matchings. Independent exchange adjacency yields 96 undirected pairs, degree distribution eighty vertices of degree0 and 96 degree2, and six connected 16-vertex cycles; six C16 plus 80 isolates, eccentricity8 within each nontrivial cycle. The pivot lemma: disjoint removed and inserted edges would allow the removed edge to append to new matching, contradiction. Original GP labeling and independent LCF complement verifier were read and checked; finite exhaustive proof is appropriate because the claim concerns a single finite graph.

## originality

PASS

Existing exact matching-complex homotopy and perfect-matching trade results cover a different invariant or different state space; inspected source texts do not state or imply the minimum maximal matching exchange topology. Unindexed computational databases remain risk.

## value

PASS

A complete optimum-state mobility decomposition for the canonical cubic symmetric 16-vertex Möbius–Kantor graph is a motivated exact finite reconfiguration invariant. It sharply distinguishes six 16-cycles from 80 frozen local states, is not merely a cardinality, and may be a useful benchmark for maximal matching reconfiguration algorithms. No general theorem is required for its precise mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
