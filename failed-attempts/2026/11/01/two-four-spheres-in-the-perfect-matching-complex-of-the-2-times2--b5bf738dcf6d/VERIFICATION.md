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

Independent reconstruction from the polygon and exact triangle incidences gave 32 graph vertices and 41 edges, with 50 perfect matchings (also confirmed by bipartite DP and MacMahon's product). The complete union of their subsets has 2,517,788 faces including the empty face. Replay of all 41 pivots gives 1,258,893 disjoint covering pairs and the two critical dimension-four faces {1,11,12,21,35} and {1,10,16,20,37}. Acyclicity can be seen directly: upward arrows in a directed cycle cannot be consecutive since matched endpoints are disjoint, and the numbers of up and down steps must coincide, so the cycle would alternate. Let e be the earliest pivot of any upward arrow on a putative cycle. The label e must also be lost on a downward arrow somewhere on the cycle. Both endpoints of that downward arrow belong to upward pairs of stage at least e, hence were still available at pivot e and should have been paired across the arrow, a contradiction. Restrict to the ordinary face poset by discarding the empty face and its pair, leaving its paired vertex critical. Forman's CW theorem then gives one vertex and two four-cells, with attaching maps to that vertex; this proves the integral wedge rather than just a Betti number census. Replay: python3 /workspace/branches/e0c365fa-9569-4bd2-b20b-8659e84c2a61/reconstruct_honeycomb.py --sides 2 2 3 (saved h223_reproduction.json in that directory).

## originality

FAIL

An earlier-dated, distinct Resultary entry (2026-10-18, bc0202f43949) establishes the exact same integral homotopy equivalence for the same dual honeycomb graph and complex. Its proof also uses exhaustive finite simplicial data and an acyclic Morse matching. Different pivot labels/order and using the empty face do not change the result. This is demonstrated prior coverage, not a conjecture based on a title or inaccessible source.

## value

FAIL

The topology of the first enlarged side-two honeycomb is a well-motivated exact invariant, but its precise homotopy type and finite census were already computed and proved. This record reperforms that known finite computation with another Morse witness of the same critical dimensions; it does not establish a new invariant, classification, or structural improvement that addresses a remaining gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
