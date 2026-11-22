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

# Reproducibility and verification

Run `python verify_fejer_bv.py` from this directory with Python 3, NumPy and SciPy. The package was tested with the original standalone file, returning:

```text
FINITE_FOURIER_VS_INTEGRAL_ARC_TESTS_PASS 96
PARITY_QUADRATIC_QUARTIC_TESTS_PASS 36
PARITY_THIRD_ORDER_ASYMPTOTIC_CHECKS_PASS 6
RANDOM_PERIODIC_BV_FFT_TESTS_PASS 240
ALL_FEJER_BV_CHECKS_PASS
```

The exact proof is contained in `RESULT.md`: its indispensable analytical steps are flux conservation and translation overlap, periodic BV coarea and strictness under disconnected components, finite Fourier integration, kernel Taylor expansion at the antipode, and Euler–Maclaurin asymptotics. No finite-grid verification proves the infinite-dimensional BV inequality or the all-degree asymptotic. In the FFT checks, discrete Riemann sums approximate continuous error, with a declared numerical tolerance; their role is error detection. No external certification or independent mathematical review is asserted.
