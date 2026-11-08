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

# Verification of exact bridge moments

`check_bridge.py` uses Python standard-library `fractions`, `itertools`, and `math` only. Running `python check_bridge.py` in the extracted artifact directory prints `PASS 92 parameter-case checks; exact exhaustive paths up to 16 steps`.

The exhaustive check ranges over all \(\binom{2n}{n}\) simple bridges for \(1\le n\le8\), testing the covariance, the first two return moments, the squared-sojourn moment and full Chung–Feller marginal, all as exact integers or fractions. A separately implemented excursion dynamic recurrence checks \(\mathbb E K_n\), \(\mathbb E D_n^2\), and \(\operatorname{Cov}(K_n,D_n^2)\) for \(1\le n\le80\); four larger parameters are numerical consistency diagnostics.

No finite check is used to infer a theorem for all \(n\). The all-size proof is the exact formal-power-series calculation in RESULT.md, including the conditional random-sign reduction and the algebraic coefficient extraction. No independent expert audit is claimed.
