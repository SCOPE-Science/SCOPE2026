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

Exact integer certificate: `proof_transfer.py` reconstructs a 26-state deterministic labelled transition system using Rule 110's truth table, verifies its agreement with `transfer_table.json`, computes 31 successive integer transfer coefficients and checks 26 consecutive zeros of the degree-five recurrence residual. Cayley--Hamilton proves the residuals vanish at every subsequent index. The rational numerator follows by direct coefficient multiplication.

Independent simulation: `independent_forward.py` exhaustively enumerates every original configuration for ring lengths 3 through 16 using a separate direct Boolean implementation of Rule 110; it independently evaluates every candidate output through length 13 with a predecessor feasibility algorithm. Both scripts were executed and passed; exact outputs are stored in `proof_transfer_output.txt` and `independent_forward_output.txt`.

Limitations: finite simulation alone is not an infinite proof; the all-length step relies on the explicitly constructed transfer and finite Cayley--Hamilton certificate. No long-time dynamics, changing update orders, or independent external verification is covered.
