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

Run the standalone companion `two_square_phase_retrieval_check.py` with Python and NumPy. The observed local result was:

```
TWO_ROTATED_SQUARES_CHECKS_PASS 782
```

The script independently constructs the eight raw intensity-lifting rows in Frobenius-orthonormal Hermitian coordinates, checks the predicted two diagonal singular values, four adjacent-sector singular values, two outer-sector singular values, and compares the closed determinant formula with the direct determinant. It also checks the explicit Hermitian null vector, rank degeneracies, witness polynomial pairs at singular angles and equal or zero radii, and a finite-grid comparison of the determinant with the \(lpha=\pi/4\) design.

The universal conclusions are established by the Fourier-mode algebra and minimality argument in `RESULT.md`, not by exhaustive computation. Near-singular radii or resonant angles are mathematically excluded from the positive stability assertion; finite-precision singular-value tests cannot certify arbitrary proximity to those exclusions. The listed quantitative bound is explicit but not claimed sharp, and independent mathematical validation has not been performed.
