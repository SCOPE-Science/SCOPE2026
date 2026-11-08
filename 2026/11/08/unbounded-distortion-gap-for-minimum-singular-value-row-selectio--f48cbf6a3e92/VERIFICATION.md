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

# Reproduction and mathematical checks

The exact derivation classifies every two-row subset of the prescribed two-column orthonormal frame, checks strict amplitude ordering for every integer \(N\ge2\), and proves the SPD matrix and exact Arnoldi realization symbolically. The proof is in `RESULT.md`.

`python verify_krylov.py` was executed from the candidate files with Python 3, NumPy and SciPy. It returned:

```text
CHECKS_OK; 95274 exact row pairs over N=2..80; 10 numerical DEIM/QR/whitening tests; 6 SPD Arnoldi tests
```

The checker enumerates squared singular amplitudes using `fractions.Fraction`, computes the true QR-pivoted row selection using SciPy, and reconstructs the SPD operator and Arnoldi pair. This finite evidence does not prove the uniform-in-\(N\) statement by itself; the complete symbolic four-type classification supplies that proof.

Known scope limits: no rounding-error analysis, no guarantee for additive sketch noise, no solver residual or runtime guarantee, and no assertion of independent mathematical validation.
