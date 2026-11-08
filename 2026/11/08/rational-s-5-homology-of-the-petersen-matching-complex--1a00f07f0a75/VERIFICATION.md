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

# Verification

Run `python3 verify_petersen_matching.py` using Python 3 with SymPy installed. The recorded output is `verification_output.txt`. The exact code enumerates the five face cardinalities, constructs signed boundary matrices, verifies consecutive compositions vanish, takes rational row-reduced echelon forms, and extracts exact boundary-image action traces from invertible minors. It checks all 120 relabelings commute with simplicial boundary on every oriented positive-dimensional face and verifies the full seven-class character table, not a statistical sample. There is no numerical approximation or modular-only rank assumption.

Exact domain: the matching complex of the 10-vertex 15-edge Petersen graph with vertex disjointness defining faces. The calculation covers every possible matching and every natural label permutation. The resulting module identification uses standard rational character theory, and quotient rational acyclicity uses finite-group transfer after barycentric subdivision. This computation does **not** address integral module structure or other graphs. The 2007 matching survey was not fully accessible, and no independent audit has been performed.
