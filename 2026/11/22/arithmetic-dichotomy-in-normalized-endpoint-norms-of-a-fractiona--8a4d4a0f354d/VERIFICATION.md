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

# Verification details

The analytic proof specifies two global boundary maximizers, their common phase velocity, the positive-real-part complex curvature, the Gaussian local approximation, and the Parseval second-moment bound controlling coefficients outside the main window. The irrational case uses absolutely convergent Fourier harmonics and a bounded-geometric-sums argument. The rational case uses residue-class Riemann sums, a nonzero Gaussian harmonic, and explicit mean and period; it does not rely on experimental evidence for nonconvergence.

The supplementary `CHECK.py` requires Python 3 and NumPy. Running `python CHECK.py` reports `FRACTIONAL_WIENER_ARITHMETIC_DIAGNOSTIC_OK 49`. It tests three orders, boundary maximum and derivative formulas, periodicity, strict profile variation, and discrete Fourier-coefficient predictions at three finite times. The FFT is a finite approximation and its aliasing is not an analytic certificate; this program does not independently establish the infinite-time theorem.

No independent mathematical audit or external certification has been performed.
