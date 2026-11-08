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

# Reproducibility
Run `python check.py` with Python 3.9 or later; no external dependencies. The checker uses exact fractions. Observed results:

```text
INDEPENDENT_FULL_SIGNED_INCREMENT_ENUMERATIONS_OK 17
ALL_CLIQUE_CORE_CLOSED_FORMS_OK 30
EXACT_BALANCED_TRANSPORT_SLOPES_FOR_PATHS_OK 6
EXACT_EVENTUAL_QUADRATIC_IDENTITIES_OK 15
ALL_PENDANT_CORONA_SPREAD_CHECKS_OK
```

The direct step-sign enumeration compares the complete space of endpoint-increment patterns for the listed small cases, while the universal proof independently uses convexity, the law of total variance, integrality and gap estimates. Tests do not certify infinitely many parameters, unindexed literature, or independent audit.
