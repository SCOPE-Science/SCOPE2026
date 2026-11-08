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

# Reproducibility and limits

Execute `python CHECK.py` in a directory containing `requirements.txt` and the script. On the reviewed source, the executable completed with `PASS: 3446 deterministic tests; exact formula proved independently in RESULT.md`. It checks matrix spectra against the explicit Fourier-product formulas for several even bases, integer-digit parity, and direct finite-cylinder integration. It also checks the finite-digit coupling bound and high-base normalization.

The proof for arbitrary base and depth is the analytic cross-Gram calculation in `RESULT.md`, not a finite enumeration. Infinite products are convergent by uniform estimates on compact sets; finite product truncations in the code are numerical approximations. The code is not an independent verifier of mathematical novelty. No independent audit or outside validation has been completed.
