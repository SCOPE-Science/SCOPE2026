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

# Verification details

The self-contained `CHECKER.py` script uses the Python 3 standard library only. It directly tests the original (SN) requirement: for each owner-star facet and each different agent, it searches for a same-local-state facet outside the truth event. Independently it evaluates the full multivariate inclusion-exclusion polynomial, including signs and exponents, and the surjective-map count at minimal complement size.

Command: `python3 CHECKER.py`.

Observed output:
```
PASS: 108 parameter vectors, 54522 candidate-event inspections
grid (2,2,2): [0, 0, 2, 4, 1]
grid (3,3): total 27
grid (3,2,2): min-witness count 8
grid (4,3,5,2): min missing facets=5, extremal event count=1093500
```

Exhaustive testing covers exactly the finite parameter vectors and cell bounds in the checker, not arbitrarily large products. The all-size assertions rely on the written proof and classical identities. No independent external validation or historical-priority audit has been performed.
