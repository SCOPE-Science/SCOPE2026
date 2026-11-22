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

The independent-audit channel has not been performed. The ordinary computational checker reconstructs the group algebra directly and does not use matrix-block factorizations when testing the rank distribution. It exhaustively evaluates all coefficient vectors for H=C3,C5,C7,C3xC3 over F2 and H=C3 over F4. It separately enumerates all square-zero binary linear subspaces for H=C3,C5,C7 to check all maximal subspaces and pairwise intersection sizes. Reproduce using `python3 verify_generalized_dihedral_squarezero.py` with Python 3 standard library only. Recorded raw output is checker_output.txt. Infinite cases are established by the algebraic decomposition and projected-line rigidity arguments, not by computational tests. The reduced algebraic set is not asserted to coincide scheme-theoretically with the original equations.
