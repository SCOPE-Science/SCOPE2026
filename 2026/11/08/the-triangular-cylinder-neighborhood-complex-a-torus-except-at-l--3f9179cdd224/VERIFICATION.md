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

`verify.py` reconstructs the graph and the exact open-neighborhood complex, checks every elementary collapse for lengths \(3\le n\le18\), and cross-verifies the core with a second face-generation specification. It independently computes binary boundary ranks for each case, tests links and oriented surface connectivity for every nonexceptional length, and constructs a complete free-group attaching-word certificate for \(n=4\).

The exceptional certificate starts with twelve vertices, thirty edges, twenty-four triangles, an eleven-edge spanning tree, nineteen one-cell generators, and twenty-four two-cell relators. Eighteen legal generator/relator eliminations yield a CW complex with one one-cell and six two-cells attached along trivial words. The procedure explicitly checks that the removed generator occurs exactly once in its eliminated relator and that every surviving relator is reduced by actual substitutions. Read `verification_output.txt` for the exact recorded output.

This verifies the finite range and the exceptional finite certificate. The all-length result relies on the symbolic common-neighbor argument, explicit six-cycle links, and oriented periodic-diamond covering proved in RESULT.md. No claim of external independent mathematical certification is made.
