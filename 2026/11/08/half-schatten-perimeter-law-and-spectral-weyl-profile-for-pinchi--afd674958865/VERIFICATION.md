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

# Verification and reproducibility

The exact commutator-band formula, positivity, finite Schatten membership, finite-window moment convergence, geometric critical constant, and residual-science limits are proved in `RESULT.md`.

Run `python check_laurent.py` with Python 3.10 or later, NumPy and SciPy installed (`pip install -r requirements.txt`). Its successful output is exactly `ANNULAR_LAURENT_CHECK_OK 12162`. The checker tests the rational cross-commutator numerator identity, compares independently constructed finite matrices against the formula, and carries out finite spectral checks for explicit two-term Laurent examples. Calculations are corroboration only: they neither exhaust arbitrary Fourier coefficients nor replace infinite-dimensional limit proofs.

The time-dependent spectral statement fixes the Laurent coefficients and exponent before letting the inner radius tend to one. The source setting uses **equal normalized measures on both boundary circles**. No claim is made about expert certification, independent audit, or priority verification.
