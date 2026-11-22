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

The analytical theorem is proved by the explicitly diagonalized signed Laplacian, the fractional-generator off-diagonal test, the strictly convex scalar exponential crossing, and a uniform-in-time spectral-projector formula. The exact endpoint norm follows from signed row sums. The near-critical error order is obtained from a local Taylor expansion with strictly positive quadratic coefficient, and the near-degenerate limit follows from the positive-root equation.

The included `checker.py` is a Python 3 finite diagnostic that requires NumPy and SciPy. Run `python checker.py` from the extracted package. Expected output: `VERIFICATION_OK 2941`. It constructs the signed Laplacian directly and compares its eigendecomposition-based fractional exponential against the independent projector formula on diverse network sizes, weights, exponents and times. It also checks critical-root coefficients and slow spectral-gap recovery. Exact zero-eigenvalue roundoff is clamped to zero numerically before taking fractional powers. All finite numerical computations are supplementary; the proof covers the stated infinite continuum of real exponents and times.

There is no external independent audit, no formal proof-assistant certification, and no claim that finite experiments establish historical priority.
