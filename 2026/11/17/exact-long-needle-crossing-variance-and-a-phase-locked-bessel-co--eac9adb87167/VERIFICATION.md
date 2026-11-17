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

# Verification evidence and limits

The proof of the exact identity is the conditional Bernoulli count law, total-variance decomposition, uniform Fourier expansion of the fractional-part quadratic, and the angular Bessel integral. The fixed-spacing large-length expansion follows from the standard real-axis Bessel asymptotic and an absolutely convergent error sum. These are infinite mathematical arguments; finite checks alone would not prove the theorem.

The standalone `check.py` was executed with Python, NumPy and SciPy, using the actual embedded code. It passed seven comparisons between the Bessel series and an independently integrated conditional-variance formula with angle intervals split at projection thresholds; checked the classical short-needle polynomial; and compared four direct endpoint simulations, each of 500,000 samples, with the predicted moments. It also compared scaled integer/half-integer remainders at lengths 10, 50 and 100 with their analytic limiting coefficients, yielding:

```
length=10, rescaled=-0.061082894, limit=-0.061185981
length=10.5, rescaled=+0.039472616, limit=+0.039553470
length=50, rescaled=-0.061165494, limit=-0.061185981
length=50.5, rescaled=+0.039536773, limit=+0.039553470
length=100, rescaled=-0.061175743, limit=-0.061185981
length=100.5, rescaled=+0.039545088, limit=+0.039553470
LONG_BUFFON_GRID_VARIANCE_OK
```

The finite numerical tests and truncations are corroboration, not independent validation or an infinite proof. The result is not asserted for biased angular laws, nonrectangular grids, or simultaneous degeneration of grid spacing. Historical priority remains provisional because the complete Diaconis 1976 article and some older monographs were inaccessible. Independent audit has not been performed.
