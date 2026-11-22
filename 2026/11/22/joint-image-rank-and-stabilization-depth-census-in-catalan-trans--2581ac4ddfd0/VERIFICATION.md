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

The embedded \(\texttt{verify.py}\) uses only the Python standard library. Running \(\texttt{python3 verify.py}\) exhaustively enumerates all nondecreasing regressive maps on chains of sizes one to nine, computes original image rank and stabilization depth directly, and compares each joint cell with separately generated bivariate rational-series coefficients. It additionally verifies the rank-equals-depth binomial multiplicity and rank/depth bound for every tested map. Exactly 6,917 maps are checked; the output ends with \(\texttt{VERIFY\_OK}\), and \(\texttt{check_output.txt}\) is the captured checker output.

This is a finite regression test, not a proof for unbounded size. The proof for all dimensions is the explicit forest bijection, rank/height translation, rational tree-sequence decomposition and boundary-spine count. Literature-priority reservations are stated in the scientific review, including incomplete access to a closely related older potency/ordered-tree paper. No independent mathematical audit has been carried out.
