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

# Verification of mathematical calculations

The standalone Python script `check.py` ran successfully in the delivered package directory, returning `VERIFICATION_OK 993`. Its 993 checks include exact rational equalities for Laguerre-polynomial moment formulas, exact biorthogonality of dual shifted/exponential vectors, exact polynomial coefficients of commuting rank-one projections for rational affine contractions, numerical dual-norm Gaussian sums, and independent asymptotic convergence tests for both displacement regimes.

The proof of the infinite-dimensional statements is analytic and reproduced in `RESULT.md`: compactness follows from an explicit Gaussian Hilbert–Schmidt integral; algebraic spectral simplicity follows from the Taylor expansion; the sharp high-degree result uses concentration of positive Bessel-series weights and the Laplace method; critical scaling follows from dominated convergence; and the basis/similarity obstruction follows from uniform boundedness of spectral projections.

Limitations: finite tests alone cannot establish infinite spectral completeness or asymptotics; no external independent audit or formal certification has been performed. All arithmetic dependencies of the verification program are in the Python standard library.
