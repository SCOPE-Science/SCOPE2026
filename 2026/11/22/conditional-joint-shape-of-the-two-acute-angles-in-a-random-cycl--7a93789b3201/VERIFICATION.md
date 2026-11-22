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

The self-contained proof derives the exact joint density by transforming a three-gap Dirichlet marginal and integrating its feasible region. For independent finite verification, run `python3 CHECK.py` with the standard Python 3 library. The checker reports 1,251 successful assertions, including two independent exact-rational moment integrations for each of 21 sample sizes and independent exponential-spacing simulation at sample sizes 4, 6 and 8. The random check uses a fixed local seed and broad tolerance; it is not used to certify infinite-sample properties. The all-\(n\) result and gamma limit follow from the analytic proof, not the finite checks.
