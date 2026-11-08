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

# Reproducibility and limits

Run `python verification/verify.py` using Python 3.9 or later. The verifier constructs each graph and checks all vertex masks in two independent ways. It proves acyclicity by checking the complete reversed-matching Hasse graph for a directed cycle, computes original mod-two boundary ranks, and uses both signed gradient path recursion and direct full-chain integral cancellation for the Dürer Morse differential. It verifies a unit entry in that rank-one differential and the predicted critical cells. The packaged output must end with `ALL_CHECKS_PASS`.

The two independent chain reduction algorithms agree exactly. The signed boundary distinguishes an integral \(\mathbb Z\) summand from a rational-only answer. The cell cancellation relies on \(\pi_3(\bigvee^4S^3)\cong\mathbb Z^4\); it is not an assumption about arbitrary higher homotopy groups. These computations do not address other graphs or any independent validation.
