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

The included `checker.py` was executed with Python 3 using the standard-library `fractions.Fraction` type. It reconstructed the graph and its state-dependent eligible edges directly, checked a nonempty compatible-neighbor set at all steps, and passed for source counts \(1,2,3,4,6,30\), 1100 steps each. It additionally checked 100 exact-rational steps of the proved invariant difference recurrences. The analytic proof covers all integer source counts and infinite time. No independent audit has been performed.
