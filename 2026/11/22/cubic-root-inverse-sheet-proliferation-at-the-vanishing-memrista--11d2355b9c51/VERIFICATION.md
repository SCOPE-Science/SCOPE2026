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

# Verification

The exact reduction, endpoint localization, nonvanishing inner-root derivatives, bounded edge-root count, properness and degree are proved in RESULT.md. Run the included finite checker with:

```bash
python3 checks/verify_inverse.py
```

The checker uses only the standard Python library and reports 500 deterministic scalar-inverse/Jacobian identity checks and 21 finite sampled inverse-count checks. These are diagnostics, not a proof of the infinite-parameter limit. The exceptional targets with \(u=\pm\alpha\) have intentionally not been covered by the quantitative claim. No independent mathematical audit has been performed.
