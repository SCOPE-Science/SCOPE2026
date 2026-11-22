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

# Verification scope

The proof in RESULT.md gives analytic arguments for every asserted limit and the endpoint formula, including uniformity in evaluation time. No numerical enumeration is used to establish an infinite-dimensional statement.

Supplementary replay:

```sh
python projection_checks.py
```

Dependencies: Python, NumPy, SciPy. The checker separately integrates Gram entries, tests the exact kernel's projection identity at selected points, integrates the endpoint absolute kernel across known zeros, and probes the confluent and high-frequency limiting values. It passed when executed with these dependencies.

Checks not performed: a machine-verifiable formal proof; an exhaustive historical-priority search; exact finite-frequency global optimization; independent mathematical validation. Tests concern finite samples only.
