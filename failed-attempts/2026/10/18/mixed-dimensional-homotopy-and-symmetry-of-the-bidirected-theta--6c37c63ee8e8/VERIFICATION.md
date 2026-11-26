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

Independently enumerated path forests by cutting permutations of the five vertices into directed paths; every such forest appears in some ordering, and only available arcs were accepted. This yields the stated 114 nonempty faces. Reconstructed the specified 53 matching pairs, the 276 oriented Hasse incidences, and acyclicity by depth-first topological sorting. Integral elimination of matched edge-triangle incidences gives zero for all six critical degree-two attaching degrees. Discrete Morse theory gives a CW complex with one vertex, one loop, and six two-cells; each attaching map to the one-loop skeleton has degree zero and is null, giving the claimed integral homotopy type. For the action, an independent rational chain calculation used a different spanning tree and solved all triangle relations on chord coordinates to extract the H^1 functional; its pairing gives the H_1 trace on all 24 actions. Signed fixed-face counts then determine the H_2 trace. The traces agree in every class with the record, and the modules split over Q as stated. Replay: python3 /workspace/review_evidence/2-check.py.

## originality

FAIL

The integral homotopy type is stated exactly in distinct indexed findings. Combining that degree concentration with the broader indexed dihedral virtual character forces both claimed degreewise modules, not just their alternating sum. Thus the purported additional character result leaves no uncovered assertion in the frozen finding. This is mathematical coverage; it does not establish chronological priority.

## value

FAIL

The smallest simple bipartite theta and its natural branch-symmetry action are well motivated, and mixed homology would be useful as a base case. Here the wedge type already appears as that base case and both degreewise characters follow by elementary decomposition of the indexed virtual character. The frozen finite certificate provides another calculation, but the finding proves no further invariant or structural result beyond this covered case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
