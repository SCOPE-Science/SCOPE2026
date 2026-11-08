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

Execute `python3 dodecahedral_dominance_verify.py` with Python 3 and no third-party dependencies. The package includes the exact output in `dodecahedral_dominance_output.txt`. Face tests are exhaustive over all vertex masks. Both Morse matchings are checked for acyclicity by topological sorting every Hasse covering; signed Morse differentials and primitive minors are computed from integral arithmetic, not inferred from reductions modulo two. The graph's adjacency and the explicit permutation to generalized Petersen \(\operatorname{GP}(10,2)\) are checked inside the executable. Verification shows precisely the three torsion-free reduced homology groups and connectivity claimed in `RESULT.md`.

The output does not determine a complete homotopy type, and exact enumeration here concerns one fixed finite graph. A self-review has passed; no independent validation or external certification is asserted.
