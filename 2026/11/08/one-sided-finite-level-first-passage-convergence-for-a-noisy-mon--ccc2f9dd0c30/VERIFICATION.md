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

# Verification of the finite-level first-passage theorem

Run the included `check.py` from the directory containing this document:

```
python check.py
```

The only dependency is the Python 3.9+ standard library. The run checked 1,232 assertions, including exact rational solutions of the stopped Markov backward system versus the claimed Laguerre ratio, strict normalized Laplace comparisons, numerical Bessel series and the first inverse-threshold coefficient, and the exact second-moment formula. Independently computed finite solutions validate the normalization and generator signs; the argument for all thresholds and all positive Laplace arguments is the analytic coefficient-product comparison and summable remainder in `RESULT.md`.

Reproducibility limits: finite computations are not proofs of asymptotic statements. The proof's uniformity is restricted to bounded Laplace-parameter intervals. No finite measurement-spacing correction, arbitrary-initial-state statement, CDF dominance or independent external validation has been asserted.
