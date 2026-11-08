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
Run `python3 verify.py` with Python 3 and the standard library. Compare its stdout byte for byte with `verification_output.txt`. The program reconstructs the graph neighborhood complex, executes every free pair from the two-stage collapse, checks the terminal surface's face vector and vertex links, checks its full dihedral invariance, and calculates all signed simplicial chain traces on the invariant triangulation for each group element. It was executed successfully for all \(9\le n\le80\): 72 complexes, 3,204 rotations and 3,204 reflections. This is a direct code-level consistency check, not an independent mathematical audit or an infinite-case verification.

The proof in `RESULT.md` gives the infinite-case justification using common-neighbor intersections, orientability and finite-order rank-two representation theory. It is unnecessary to trust a finite run to establish a statement about infinitely many \(n\).
