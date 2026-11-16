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

The analytic proof appears in `RESULT.md`, including the exact Fourier normalization, Bessel energy derivative, endpoint arguments, the strictly positive derivative of the inner-scaled zero, and the one-to-one stationary-point classification. `checker_all.py` performs independent SciPy root bracketing and Bessel evaluations for six dimensions; it tests the first eleven roots at 53 inner radii each and reconstructs all stationary radii through index ten. Executed output in `check_output.txt` reports 18,216 successful numerical checks and the planar second-zero maximizer.

Run `python checker_all.py` with Python 3, NumPy, and SciPy. The computation verifies sample cases, not all infinitely many indices, radii or dimensions. Analytic arguments establish the universal result. No independent external validation has been performed.
