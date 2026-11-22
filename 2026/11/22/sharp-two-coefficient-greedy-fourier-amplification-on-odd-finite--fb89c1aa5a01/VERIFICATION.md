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

The analytical proof and exact modulus formula are in `RESULT.md`. The standalone `verify.py` runs without third-party libraries: `python3 verify.py`. It prints `VERIFY_OK: 99 odd orders and one noncyclic product quotient` on successful completion. Tests cover every odd modulus from 3 through 199, including composite moduli; test the Fourier coefficients of the phase witness; check the two selected coefficients strictly dominate the others; compare the two-term sum with the projected kernel; and verify a two-coordinate quotient lift. These tests have finite scope and are not used as a proof of the all-group theorem.

The critical all-group deductions are exact: convolution normalization, cyclic image of a finite-order character, finite cosine summation, strict monotonicity in character order, the analytic Fourier-coefficient formula, and equality in the finite triangle inequality. No unproved computational certificate or external artifact is needed.

No independent mathematical audit or external validation is claimed.
