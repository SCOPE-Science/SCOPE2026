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

The general theorem is proved in `RESULT.md`; the finite program is an independent-in-method consistency check, **not** an infinite proof or an external certification. Run with Python 3.8 or later:

```sh
python verify_cycle_pav.py
```

The script enumerates **every** greedy tie branch at each size for each \(3\le n\le15\), independently evaluates original voter-level harmonic PAV scores, computes the theoretical adjacency formula, compares with the optimum over all size-matched committees, compares exact claimed spectrum, and tests the possible maximal-independent-set sizes. The execution completed successfully with **9766** reachable-state assessments and no failed assertions. Rational utilities are represented as integer doubled scores, eliminating floating-point uncertainty.

Limits: the program checks only finite cycle sizes; symbolic gap and marginal analysis in the proof establishes every positive order. No independent external audit has been performed.
