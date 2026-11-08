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

Run `python3 verify.py` (no external dependencies). It builds the actual finite sieve masks and compares direct Fourier magnitudes with the Chinese-remainder local formula for every frequency modulo 30 and 210 and thirteen frequencies modulo 2310, plus full numerical first- and second-moment checks over all spectra for those three moduli. It checks the local cyclotomic log products, then constructs the 30-by-30 integer circulant and determines its determinant exactly by fraction-free Bareiss elimination. The expected output is:

```
FOURIER_CHECK P 5 N 30 survivors 3 tested_freq 30 full_spectral_moments=yes
FOURIER_CHECK P 7 N 210 survivors 15 tested_freq 210 full_spectral_moments=yes
FOURIER_CHECK P 11 N 2310 survivors 135 tested_freq 13 full_spectral_moments=yes
DET_CHECK N 30 determinant -729 exact_integer=yes
VERIFY_OK frequencies 253 local_nonzeros=yes local_log_product=yes exact_determinant=yes
```

The direct trigonometric comparison uses a relative tolerance of 1e-8 and is numerical, whereas the determinant uses integer arithmetic. In particular the checker is neither a full infinite computation nor a test of the Berry--Esseen limit; those follow from the analytical proof in `RESULT.md`.
