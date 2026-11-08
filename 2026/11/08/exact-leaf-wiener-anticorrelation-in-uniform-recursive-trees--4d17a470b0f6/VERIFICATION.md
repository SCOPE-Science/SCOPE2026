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

# Verification record

Execute `python3 checker.py` in this directory. Its standard-library exact arithmetic makes no use of Monte Carlo sampling. The observed run completed with 2532 assertions passing: all \((n-1)!\) independent parent sequences for each \(2\le n\le9\), including all 40320 trees of order nine, were checked by breadth-first distances, and the exact expectation and covariance recurrences were checked through order 501.

The program independently computes \(W_n\), rooted leaf count \(L_n\), and the leaf transmission sum \(Q_n\) from each enumerated tree and compares their averages to the claimed expressions. The unrestricted all-integer conclusion follows instead from the algebraic conditional-expectation and telescoping proof in `RESULT.md`. The published Wiener-variance asymptotic used for the optional correlation limit is not re-proved or machine-certified here. No independent audit was performed.
