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

# Verification

Run `python3 CHECK.py` with standard-library Python. It verifies the exact rational five-point experiment: all evaluated per-capita ODE derivatives, conservation of \(yz\), a nonzero first-leaf four-column minor \(185495875/789933095424\), a nonzero pooled five-column minor \(185495875/526622063616\), and an exact out-of-leaf rate displacement \(3/2\). The analytic proof in RESULT.md establishes the full arbitrary-parameter theorem and clearly states the required positivity, nonstationarity, and nonresonance hypotheses.

No finite computation validates the general claim on its own. All independent review and validation remain unperformed.
