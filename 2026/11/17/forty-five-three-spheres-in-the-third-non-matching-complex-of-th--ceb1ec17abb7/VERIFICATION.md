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

# Finite verification and limits

Run `python3 verify_nm3_mobius_kantor.py` with Python 3 and no third-party dependencies. The accompanying `verification_nm3_mobius_kantor.txt` is the output of that exact checker and concludes with `ALL_CHECKS_PASS`.

The script constructs the graph from its defining edges, checks all twenty-four edge labels and bipartiteness, and builds the simplicial faces both by recursively excluding every three-edge matching and by taking all subsets of each two-vertex cover's incident edges. These constructions agree on all 3,149 augmented faces. It then generates the full sequential element matching, counts exactly 1,552 pairs and 45 critical three-simplices, and verifies acyclicity by complete topological sorts of the 11,832-cover augmented Hasse graph and the 11,808-cover nonaugmented Hasse graph.

After removing the empty-face matching pair the critical cells are one vertex and 45 three-cells. Applying the ordinary integral discrete-Morse theorem to these *exhaustively verified* finite data gives the wedge homotopy type. Face counts and Euler characteristic are cross-checks, not substitutes for the acyclicity proof. No independent external audit, general-graph theorem or higher-threshold verification is claimed.
