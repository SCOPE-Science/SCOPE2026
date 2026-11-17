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

The proof is self-contained in RESULT.md. All moment operators are simultaneously diagonal and the logarithmic reduction is exact for positive weights. The upper endpoint is proved by an explicit finite-support increment sequence and all translated windows; the lower endpoint by one negative increment. The global obstruction is a norm-one shift with a finite slowly varying ramp, for which the moment budgets and exact distance to every scalar shift are calculated analytically.

Run `python moment_weight_checker.py` with Python 3, no third-party dependencies. The checker performs 576 exact-rational upper-endpoint pulse checks, 15,000 feasible increment checks, 27 exact negative-step checks, and 12 floating-point ramp comparisons. It is supplementary finite verification only; it does not constitute exhaustive proof over real parameters or infinite sequences.

Both scientific novelty and the applicability of the theorem outside the stated positive unilateral-shift class require further independent assessment. Independent mathematical audit has not been performed.
