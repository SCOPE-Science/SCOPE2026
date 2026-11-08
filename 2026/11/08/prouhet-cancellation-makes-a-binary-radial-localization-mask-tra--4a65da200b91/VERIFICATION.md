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

# Reproducibility and checks

The exact object is the one-variable Gaussian Fock Toeplitz operator with indicator of positive Thue–Morse radial shells \(j\leq |z|^2<j+1\). All norms, shell widths and quantifiers are specified in `RESULT.md`.

Run `python3 checker.py` using Python 3.9 or newer, without third-party packages. The replayed script prints `THUE_MORSE_FOCK_CHECKS_PASS 120` and verifies finite Prouhet moments, low-mode Gamma-shell eigenvalues, sample nonasymptotic inequality cases, sign behavior at selected modes, and an interior-point generating-function identity.

The mathematical proof independently establishes the general finite-difference inequality, all-power summability, zero trace, and both signs. Numerical checks do not certify infinitely many indices or historical priority. The squared-logarithmic exponent is an upper bound only, not a sharpness claim.

No external independent audit has been performed.
