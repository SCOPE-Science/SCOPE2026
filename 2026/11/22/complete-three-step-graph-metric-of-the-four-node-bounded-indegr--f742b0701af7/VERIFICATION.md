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

Every distinct 0/1 imset is exposed by the signed coordinate functional maximizing agreement with that vector. For each candidate pair, holding equal coordinates fixed gives an exposed face, and complementing differing coordinates puts the two endpoints at all-zero and all-one. A zero-sum normal strictly separating all other vertices there proves an edge, also an edge in the containing polytope. Conversely an exact convex combination of other vertices giving the midpoint refutes adjacency: every positive contributor would have to belong to any exposing face of the segment. These are sufficient tests, not an unsupported assumption that all nonedges admit midpoint witnesses. An independent checker (/workspace/branches/95ffbd82-42fe-449d-8eea-c01bd8d8562b/replay_imsets.py, with full_replay.out beside it) read the frozen imset_certs.json as data, independently reconstructed 443 admissible DAGs and 150 distinct imsets from all 729 ternary possibilities, and checked exact witnesses for all 11,175 unordered pairs (2,508 edges, 8,667 nonedges). BFS reproduced (2508,7666,1001) for distances 1–3, eccentricity 3 at all 150 vertices, Wiener index 20843, and the entire 13-class degree spectrum. The replay checks, but does not independently discover, the supplied witnesses.

## originality

PASS

The f-vector and hence the counts of 150 vertices and 2508 edges are explicitly prior. The supported exact metric and degree profiles are not implied by that vector, by the same numerical diameter on the unrestricted polytope, or by fixed-skeleton diameter/edge statements. No complete earlier adjacency list or metric census of this face was identified in the inspected material.

## value

PASS

The first four-node case with a proper in-degree-two restriction is a natural exact benchmark for polyhedral edge walks. Its graph is self-centered but nonregular, and exactly 1001 pairs require all three steps. These facts quantify connectivity beyond the known face totals and provide explicit checks for adjacency computations. They do not measure monotone score paths or imply a general size bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
