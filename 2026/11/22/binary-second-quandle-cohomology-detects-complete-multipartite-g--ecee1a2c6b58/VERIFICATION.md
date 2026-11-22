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

# Reproducibility and verification

Run `python3 verify_graph_quandle_h2.py` with Python 3 and no nonstandard packages. The checker assembles each normalized cocycle equation from the actual quandle action and every coboundary from the defining one-cochain formula, then computes binary row ranks. It exhausts connected labeled graphs on at most four vertices, plus representative connected graphs of sizes five through seven, in 60 independent cochain systems. The expected marker is `GRAPH_QUANDLE_BINARY_H2_VERIFIED`; it reports 13 versus 25 four-vertex rank strata. It never assumes the proved matrix reduction inside the cochain solver.

The symbolic argument in RESULT.md is the proof for all connected finite graphs. The finite checker does not prove the formula for unbounded graph sizes or identify integral torsion. No independent external mathematical audit has been performed.
