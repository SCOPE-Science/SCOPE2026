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

The standalone file `delannoy_new_verifier.py` uses Python 3 standard library only. Invoke `python3 delannoy_new_verifier.py` from the extracted package directory.

The completed checks printed:

```
coefficient bounds: OK
finite fiber indices: 16380
shift and shell tests: 1525
PASS
```

The checker verifies finite modular fiber data, all low-index exceptional rational coefficients, the finite segment of coefficient valuation bounds, shift congruences and critical-shell isometries. No exhaustive computation of infinitely many indices is implied. The infinite theorem rests on the two-adic analytic proof in RESULT.md.
