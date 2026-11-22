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

# Reproducibility
`python verify.py` is the standalone proof-support check. It derives the exact height expansions using SymPy, asserts the fourth- and sixth-degree coefficients, and uses 65-digit mpmath arithmetic to compare normalized global height errors at 20 and 40 steps for representative northern, southern, and exceptional latitudes.

The analytical proof uses exact sphere-exponential and SLERP identities and a smooth scalar recurrence. Finite diagnostics do not certify a general infinite-step limit; the recurrence/telescoping argument establishes it. Results apply only to rigid-axis motion and the two precisely defined one-step schemes. No external/independent validation has been performed.
