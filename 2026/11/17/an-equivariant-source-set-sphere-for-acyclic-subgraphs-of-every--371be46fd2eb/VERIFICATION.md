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
# Reproducible mathematical verification

The proof is the equivariant head-support fiber argument in `RESULT.md`; the accompanying exact finite checks are supplementary. Execute `python3 verify.py` from a directory containing this file and `verify.py`.

The script uses only the Python standard library. It enumerates the subgroup actions and the acyclic orbit-face complexes for 55 small test cases. All strongly connected directed graphs and automorphism actions are checked from the explicit edge sets. It checks the predicted fixed-point mod-two Betti numbers and, for each invariant proper head-support subset, verifies that the outgoing cut is nonempty, invariant, and can be joined to every permitted invariant acyclic face without creating a directed cycle. No missing cases are treated as exhaustive for arbitrary graph order. The program does not establish genuine homotopy equivalence by itself; that is the separate all-subgroup Quillen argument.

`verify_output.txt` is the recorded stdout of `python3 verify.py` and ends in `ACYCLIC_DIGRAPH_EQUIVARIANT_HEAD_MAP_CHECKS_PASS`.

The strongest publication-priority risk is the inaccessible full text of the original 1999 complete-digraph paper; no claim of independent verification is made.
