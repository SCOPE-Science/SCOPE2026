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

The standalone `verify.py` performs exact-rational checks without third-party packages. It derives the count-state transitions directly, checks every nonabsorbing Bellman equation for each pair of group sizes \(1\le a,b\le8\), and exhaustively checks the \(400\) even-by-even size pairs within the finite rectangle. It verifies the integer central-binomial inequality at size \(42\), as well as the exact supersolution constants used in the infinite tail proof.

The infinite statement relies on the analytic central-binomial monotonicity and Bellman supersolution argument in RESULT.md; no finite test alone is treated as an infinite proof. No independent external validation has occurred.
