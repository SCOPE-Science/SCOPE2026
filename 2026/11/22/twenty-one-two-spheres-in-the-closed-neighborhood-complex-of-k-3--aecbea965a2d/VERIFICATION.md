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

The Cartesian adjacency rule gives twelve distinct equal-sized closed neighborhoods of five vertices, so these are exactly the maximal faces. An independent set-based reconstruction tests subsets of the 12-vertex universe for containment in one of them and gives all 250 nonempty faces and vector (12,54,112,60,12). At each pivot, toggling that vertex defines disjoint candidate pairs, so successive removal within a stage makes the same matching as simultaneous removal. For all three specified pivot orders the independent code obtained 114 pairs and critical vector (1,0,21,0,0), and used depth-first cycle detection on all 744 directed cover incidences, orienting just the paired ones upward. Finite discrete Morse theory therefore gives a CW complex with one vertex and just 21 two-cells, all attached to the vertex by constant maps; its ordinary homotopy type is the asserted wedge, proving the integral homology and fundamental-group conclusions. Finite-field ranks are not needed for the strongest conclusion.

## originality

PASS

A genuine short-cycle exception to the verified closed Čech clique-fiber theorem. The closest closed theorem excludes base four-cycles, the classical complete-factor theorem has different hypotheses, and the nearby short-cycle open-complex computations do not state or imply the closed-complex homotopy type here.

## value

PASS

This is the first base cycle precisely excluded by the natural longer-cycle theorem, where its bridging hypothesis fails. The computation decides that the stable fundamental circle disappears and provides the exact replacement homotopy type with a small replayable Morse certificate, rather than a homology-only sanity check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
