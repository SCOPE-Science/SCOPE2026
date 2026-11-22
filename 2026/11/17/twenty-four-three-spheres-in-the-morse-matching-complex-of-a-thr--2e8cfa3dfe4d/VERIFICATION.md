---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Reconstructed the face poset from the three triangles 012,013,023: 13 nonempty base faces, 21 Hasse incidences, exactly 2,121 nonempty gradient simplices with f-vector (21,162,560,846,468,64). Independently replayed the complete 1,048 pair certificate and all 25 critical simplex bitmasks; all 2,121 nonempty faces partition exactly, each pair is a genuine cover, and the reversed entire 8,112-edge Hasse DAG topologically sorts all 2,121 vertices. Critical inventory is one 0-cell and 24 3-cells with no positive lower skeleton; Forman discrete Morse theory yields an integral wedge of 24 three-spheres, stronger than mod-two Betti numbers. The empty gradient matching is not a geometric 0-cell.

## originality

PASS

Comparison is with ordinary, not strong, discrete-Morse complexes, and with full homotopy rather than just inclusions. Scoville classifies the full tetrahedron and its boundary and proves a cone inclusion map null, but does not determine this deleted-facet disk. No earlier same-object 24-sphere calculation surfaced; best-of-knowledge only.

## value

PASS

Removing one face from the tetrahedral boundary is a natural minimal topological perturbation. Its ordinary Morse complex changes from known mixed-dimensional sphere wedges to a pure 24-sphere wedge; a complete integral homotopy classification is a precise reusable structural test for cone inclusion and Morse matching topology, not just a mod-two rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
