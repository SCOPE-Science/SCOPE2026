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

# Verification evidence and limits

The displayed theorem is proved analytically in `RESULT.md`. The companion standalone `verify.py`, using SymPy, NumPy and SciPy, independently evaluates the two-stroke variance recursion, symbolic stationary formulas, the rational derivative and the cubic reduction, the positive derivative at the mean-work optimum, and the Gaussian covariance identity behind the exact work-sign probability. It further tests a dense grid of interior allocations for 49 distinct parameter pairs and three independent physical recursion examples.

Invoke `python verify.py` from the same directory as the files. A successful run prints a PASS message with the numerical test count. Positive finite computations do not prove uniqueness for arbitrary continuous rates: that part follows from the sign and derivative arguments in the mathematical proof. The stochastic equation is formulated for an ideal periodic engine; no laboratory observations, finite-sample performance estimates, or external scientific audit are claimed.
