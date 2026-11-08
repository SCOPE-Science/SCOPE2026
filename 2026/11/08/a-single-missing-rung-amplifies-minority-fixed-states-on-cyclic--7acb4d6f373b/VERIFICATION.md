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

# Verification and proof scope

The file `checks/check_transfer.py` constructs the exact sixteen-state integer transfer matrices for ordinary and missing rungs, and a row-swap seam permutation. It confirms the matrix identity \(T^2(T^2-T-I)(T^6-I)=0\) exactly, checks the eight starting traces for the recurrence, and reproduces both stated formulas for \(3\le n\le30\). The proof in `RESULT.md` uses the exact matrix identity and the order-eight recurrence, not numerical fitting.

The separate executable `checks/check_direct.py` constructs the actual labelled graphs with one missing rung and simulates the stable-state minority condition at every vertex for all binary configurations for \(3\le n\le9\), including all 699008 states of the two graph families in that range. The two `.out` files capture actual executions. Run both programs with standard Python from their included paths.

This is a self-review, not independent audit. Verification concerns fixed configurations only, not attraction dynamics, and the finite test range is not presented as an infinite proof.
