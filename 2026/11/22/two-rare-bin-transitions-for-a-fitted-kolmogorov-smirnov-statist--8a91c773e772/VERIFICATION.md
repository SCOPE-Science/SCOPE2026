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

The exact-statistic and boundary-event formulas can be checked with the included self-contained `check_ks.py` using Python 3 standard library only. It uses exact rational arithmetic to verify finite, reproducible CDF and likelihood identities in a bounded range, and independent seeded finite-sample simulations solely as diagnostics. The run completed with `Exact finite identities checked: 1890` and `Checker PASS`. The complete proof for unbounded samples is in `RESULT.md`; finite enumeration does not certify an infinite limit.

Important scope boundaries are exact iid Pareto data, a known lower endpoint, and deterministic coarsening. The extended geometric MLE may lie on the zero-probability boundary. In the first-bin window, convergence of scaled statistics does not assert moment convergence, and the ideal bootstrap result includes ties and assumes exact tail probabilities rather than a finite number of Monte Carlo replicates. Historical-priority assessment remains subject to listed inaccessible full texts.
