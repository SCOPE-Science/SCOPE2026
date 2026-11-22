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

# Reproducible checks

Run `python3 check_matrix.py` and `python3 check_states.py` in the directory containing the accompanying files. These are standard-library Python programs implementing the stated synchronous update from adjacency information. The matrix program tests the graph parameter and matrix-rank identities for seven prime Paley orders; the state program independently enumerates all \(8,224\) initial binary configurations on the two smallest tested Paley networks. The recorded outputs are stored in `verification_run.txt`.

The tested prime orders are \(5,13,29,37,53,61,101\). On all seven, the single-feedback matrix has exact sixth power equal to the identity, nontrivial third power, third-iterate defect rank two, and one-dimensional fixed space. For orders \(5\) and \(13\), the exhaustive period populations are respectively \((2,6,24)\) and \((2,2046,6144)\) at periods \((1,3,6)\). The unmodified dynamics also matches the predicted periodic and one-step-transient counts.

These computations are reproducible finite checks, not a proof by enumeration of all conference graphs or all field extensions. The universal result follows from the parameter-based algebraic argument in `RESULT.md`. Independent audit remains unperformed.
