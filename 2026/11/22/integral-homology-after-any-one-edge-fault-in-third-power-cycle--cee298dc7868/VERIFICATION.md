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

# Reproducibility

`python3 verify.py` uses the standard library and reconstructs every claimed face from graph adjacency. It checks 108 fault cases at orders 13 through 48, covering all three edge-distance orbits. Its checks include signed chain composition, exact unit-pivot cancellation of the relative integral boundary complex, the ten published elementary-collapse families whenever admissible, the explicit fault-local corrective collapses, and the connected-to-boundary tetrahedral dual graph. At selected orders, a separate binary elimination tests the absolute Betti ranks.

Observed execution ended with `VERIFY_OK`. The full mathematical claim uses two explicit unbounded reductions given in `RESULT.md`: fixed-offset locality for the relative chain complexes at all orders at least 25, and the periodic tetrahedral-backbone continuation after finitely many fault-local exceptions. The finite test range alone would not prove these universal statements.

No independent audit has been performed. The theorem does not claim a homotopy-equivalent wedge of spheres.
