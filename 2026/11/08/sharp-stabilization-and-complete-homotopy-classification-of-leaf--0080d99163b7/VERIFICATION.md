---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

Every multipath in the bidirected two-hub n-leaf graph uses each of four distinct hub/arc colors at most once by indegree/outdegree constraints. Arcs sharing one leaf must form either ordered pair 03 (u→leaf→v) or 12 (v→leaf→u); occupying both would make a directed 4-cycle. Thus leaf-permutation face orbits are exactly color subsets S with partitions into allowed blocks and |blocks|≤n. A setwise simplex stabilizer cannot exchange arcs since each has a unique color, so the geometric quotient (not the naive vertex orbit simplex) is a regular CW complex with distinct color-restriction face incidences. For n≥4 at most four blocks exist; the regular face poset stabilizes with (4,8,8,3) cells. Independently enumerated allowed signatures for n=1..5 and checked all 11 displayed free codimension-one pairs against every surviving higher coface: a single vertex survives at n≥4. At n=3 the stated four additional pairs leave (4,6,4) cells giving a connected closed surface of Euler characteristic 2, hence S²; at n=2 the four two-cells are a tetrahedral sphere with two extra one-cell chords, and n=1 yields two disjoint intervals. This supports S0, S²∨2S¹, S², and contractible types, respectively, including the precise sharp n=4 threshold.

## originality

PASS

The full geometric leaf-permutation orbit-space classification for bidirected two-hub complete bipartite digraphs is distinct from the underlying multipath complexes of one-way complete bipartite orientations, bidirected polygonal digraphs and unquotiented bidirected double-star graphs. Color-restricted quotient regular CW and sharp collapse supply additional topological content beyond a Burnside cell count. No inspected stronger source subsumes the n-dependent quotient types; best-of-knowledge PASS with specialized-source risk.

## value

PASS

Complete homotopy types, sharp stabilization threshold and an explicit simple-homotopy collapse for genuine group orbit spaces provide a structurally informative classification of a natural growing symmetric digraph family. S² to contractible transition is nontrivial and not a routine orbit-count substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
