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

# Reproducibility checks

Execute `python checks/cantor_checker.py` from the package root using Python 3. The checker depends only on `fractions` and `collections` in the Python standard library. Its exact rational interval pullbacks cover four strictly admissible rational contraction factors, four positive transverse coordinates, and stages zero through nine. It reconstructs all finite-stage cylinder counts, equal lengths, global endpoints, and exact gap histograms, and checks the planar-to-triangular conjugacy. Expected output:

```
FIBER_CANTOR_EXACT_INTERVAL_GAPS_OK 160 cylinders_max 512
AFFINE_SKEW_PRODUCT_AND_FIBER_PHASE_CHECK_OK
```

The analytic argument in `RESULT.md` separately verifies all real parameters in the theorem, the two boundary cases, infinite-depth Cantor structure, and the exact tail law. The finite tests alone do not establish the infinitely many stages or all real parameters. No independent mathematical audit or external certification has been performed.
