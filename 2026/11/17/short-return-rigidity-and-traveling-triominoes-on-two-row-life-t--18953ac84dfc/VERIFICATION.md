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

# Reproduction instructions

Execute `python verify_transfer.py` and `python verify_direct.py` from the directory containing these files. The scripts use the Python standard library only. The first constructs and examines all \(4^3\) one-update and \(4^5\) two-update local column words, determines every cyclic strongly connected component by two independent graph procedures, verifies the required fixed-one-step status and isolated four-cycles, and checks the characteristic polynomial by exact determinant evaluations. The second independently constructs every site's eight offset neighbors, exhaustively counts all \(4^n\) states for \(3\le n\le8\), and tests the traveling triomino through \(n=30\).

Exact output of the two runs is archived in `transfer_output.txt` and `direct_output.txt`. All local-graph loops are finite and exhaustive; these checks underwrite the general transfer conclusions. The direct circumference enumeration is supportive, not the proof for unbounded \(n\). The symbolic glider shift is checked by the explicit rule and proved in `RESULT.md`. No longer-cycle or attraction-basin census is asserted.
