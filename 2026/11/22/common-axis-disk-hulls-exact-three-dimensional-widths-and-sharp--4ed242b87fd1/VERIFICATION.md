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

# Verification record
The theorem's independent numerical checker is `verify_width.py` and was run using Python 3, NumPy and SciPy. It completed with the exact terminal marker:

```
COMMON_AXIS_DISK_WIDTH_CHECKS_OK; 51 CDF, 51 density, 36 support, 6 empirical CDF, second moment, 6 lower-tail, 5 high-dimensional quantiles
```

The test families include independent conditional spherical quadratures, finite angular disk-support maximization, half-million-sample uniform-sphere comparisons, Dirichlet small-simplex integration at three dimensions, and comparison of 12,000 simulated high-dimensional samples to independently simulated limiting variables. Finite numerical tests cannot prove all-dimensional identities or convergence; the analytical proof in `RESULT.md` supplies the infinite argument. Numerical coefficients at extremely small probabilities are not certified by these tests. No independent mathematical audit has been performed.
