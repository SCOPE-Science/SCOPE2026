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

## Reproducibility

Run `python arbo_checks.py` with Python 3 and no external packages. The program reconstructs every rooted out-arborescence from Prüfer-generated trees, checks all arc-support traces for orders 2 through 5, confirms exact labeled face counts, and checks deterministic random samples at order 6. A successful test ends with `ROOTED_ARBORESCENCE_SHATTER_PASS 66866`.

## Limits

The finite test does not establish the statement at arbitrary order. The unrestricted proof is the component-attachment argument in `RESULT.md`; the enumeration uses the all-minors matrix-tree theorem. An independent audit has not been performed.
