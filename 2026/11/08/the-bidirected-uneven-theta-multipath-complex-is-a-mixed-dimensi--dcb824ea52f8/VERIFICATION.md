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

The directed graph has exactly fourteen arcs on the uneven theta with paths 2,2,3. Independently enumerated 280 nonempty valid arc sets by indegree/outdegree <=1 and absence of directed cycles, face vector (14,64,114,76,12). Independently repeated deterministic face-poset cancellation: 134 elementary acyclic matches, critical cells one vertex, five 2-cells, six 3-cells. Independently built the full 280-face Hasse digraph and verified acyclicity, and evaluated all integral Morse projections by signed face orientations: every critical differential is zero. The 2-skeleton of the resulting CW complex is wedge^5 S2; Hurewicz identifies each 3-cell attaching class with its zero H2 column, hence all 3-cell attachments null and the claimed wedge^5 S2 wedge^6 S3 follows integrally.

## originality

PASS

The statement concerns the bidirected theta with a 3-arm branch and unequal lengths, not published multipath complexes of bidirected polygons, oriented paths, acyclic digraphs or bidirected double-star trees; these methods/results do not imply an exact mixed-dimensional integral homotopy classification of this cyclic branching example.

## value

PASS

A structurally motivated first uneven-arm theta tests the limits of bidirected polygon/path classifications in the presence of two cycles and branching. The exact coexistence of independent 2- and 3-dimensional sphere classes, with integral attaching maps resolved, is a useful model example rather than a trivial face count. No general-family theorem is required for this self-contained exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
