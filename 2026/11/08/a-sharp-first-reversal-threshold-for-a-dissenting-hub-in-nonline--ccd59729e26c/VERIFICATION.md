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

# Reproducibility checks

Run `python3 verify.py` from the extracted directory using only the Python 3 standard library. The verifier constructs the independent exponential-race recurrence for first hub reversal, compares the exact-rational hitting probability and every finite CDF to the claimed product for 15 star sizes and four integer exponents, verifies normalization and the \(q=1\) and \(q=2\) boundaries, and independently solves the entire two-opinion absorbing star process for small stars to confirm the lower bound on eventual fixation. A numerical check compares finite-star survival probabilities to the limiting \(e^{-1/q}\). The expected program output starts with `VERIFY_OK` and specifies the check count.

The checker does not exhaust real values of \(q\), unbounded star sizes, or the continuous limiting law. Those statements follow from the written competing-rate, monotonicity, and limiting-sum proofs. No independent external certification is claimed.
