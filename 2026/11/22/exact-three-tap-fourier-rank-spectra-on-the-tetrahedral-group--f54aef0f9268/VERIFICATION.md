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

# Reproducibility and boundaries

Run `python3 verify_symbolic.py` and `python3 verify_regular.py` from the directory containing those files. Both use only Python 3 standard-library modules. Their saved outputs are in `verification_output.txt`. The exact symbolic verifier builds the three-dimensional representation by restriction of permutation matrices, checks all four determinant polynomials as coefficient dictionaries over \(\mathbb Z[x,y]\), checks the rank-minor obstructions, and proves the substitution identity for any scalar block zero. The independent regular-matrix verifier enumerates every even permutation, constructs all \(220\) three-point supports and their four translation/conjugation orbits, and checks \(696\) integer-coefficient examples by rational Gaussian elimination on the full 12-by-12 convolution matrix.

The finite witness computations alone do not exclude rank values for arbitrary complex coefficients: those exclusions depend on the irreducible Fourier decomposition, invertibility of the three-point quotient Fourier matrix, the nonvanishing minors of the degree-three blocks, and the scalar/degree-three resultant identity proved in `RESULT.md`. The classification is over complex coefficients only and is not a statement about eigenvalue conditioning, numerical stability, larger groups or other support cardinalities.

No independent validation is asserted. This document records reproducible evidence and the explicitly limited self-review only.
