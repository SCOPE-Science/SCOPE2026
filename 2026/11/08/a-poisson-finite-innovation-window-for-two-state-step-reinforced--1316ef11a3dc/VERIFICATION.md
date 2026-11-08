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

The ordinary Python 3 `verify.py` uses exact rational arithmetic to compare two independently constructed finite recurrences for the same two-state model, and uses ordinary floating-point arithmetic for illustrative critical-window horizons. It reports 135 passed assertions; no outside data or libraries are needed. The analytic proof (rather than finite computation) is responsible for the joint Poisson marking limit, exact \(2^{-\lambda}\) window and infinite-horizon classification. No independent audit has been conducted.
