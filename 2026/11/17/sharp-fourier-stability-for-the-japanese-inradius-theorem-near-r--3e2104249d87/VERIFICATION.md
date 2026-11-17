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

# Reproducibility and scientific limits

Run `python artifacts/verify_japanese_stability.py` from the extracted package with SymPy and NumPy installed. The checker proves the four-point radial coefficient identity by exact symbolic simplification after the tangent-half-angle substitution; verifies finite-difference Jacobian entries and discrete Fourier singular values for polygon sizes 4, 5, 6, 7, 11 and 30; tests second-harmonic ratios at small radial amplitudes; and checks vanishing defects on an off-center circle. Successful execution prints `JAPANESE_INRADIUS_FOURIER_CHECKS_OK`.

The rigorous infinite statement does not follow from finite numerical checks. It follows from the symbolic derivative, the Japanese cyclic-quadrilateral equality, the algebraic Fourier calculation, the implicit-function theorem and a tubular-neighborhood estimate. Neither full priority nor independent mathematical audit is asserted.
