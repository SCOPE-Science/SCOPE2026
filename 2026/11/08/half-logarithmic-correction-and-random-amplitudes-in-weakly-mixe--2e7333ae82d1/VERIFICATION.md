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

The included standalone `check.py` uses Python 3 standard-library exact rational arithmetic. Run `python3 check.py` after extraction. It tests the one-step quenched conditional drift, positive factors, finite martingale means and monotone second moments across exogenous rule strings, and strict conditional variance after a Pólya step. It returned `9404 exact rational assertions passed`.

Reproduction has no third-party library requirements. These checks cover finite algebraic identities only. The almost-sure limit is justified mathematically in RESULT.md by summable Hoeffding deviations, square-summable independent weighted switch deviations, the product expansion and conditional martingale convergence. The limit distribution is not explicitly calculated, and independent mathematical verification has not been performed.
