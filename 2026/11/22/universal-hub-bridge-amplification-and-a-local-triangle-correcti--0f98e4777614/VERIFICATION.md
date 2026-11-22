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

# Reproduction and limits

The mathematical claim follows from the block eigenvector equations, resolvent uniqueness, uniform Neumann-series expansion and explicit coefficient matching given in `RESULT.md`. No computational result is used as a surrogate for a proof over unbounded graph orders.

A standard-library verification is supplied in `VERIFY.py`. From the extracted package directory, run:

```text
python3 VERIFY.py
```

Expected terminal output ends in `ALL TESTS PASSED: 9 spectral/resolvent comparisons; no infinite assertion inferred`. For each sample the code independently computes the largest adjacency eigenvalue of the complete fan graph by positive power iteration and by bisection of the scalar diagonal resolvent; it checks equality to numerical tolerance and the asserted asymptotic scale. It checks cycles and Cartesian products of cycles with distinct local triangle counts. Because a finite floating-point check does not certify the coefficient uniformly, the analytic proof is necessary and supplied separately.

Only the independent audit channel is marked unperformed; no external verification or peer certification is asserted.
