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

# Verification scope

The ordinary analytic derivation is in RESULT.md. Independently reproduce the finite consistency checks with `python verify.py` from the same folder. The script requires only the Python standard library and reconstructs the signed volume from Hodge-paired area bivectors. Its 2,993 passing checks include 300 random tangent configurations, three small deformation scales for each, exact sum-of-squares comparisons, rigid rotations, angular Fourier modes, and a numerical 27-by-27 Hessian diagonalisation. Its maximum observed discrepancy from the analytically predicted quadratic eigenvalues was below \(8.1\times 10^{-9}\), in a finite-difference discretisation.

An additional, independently implemented SciPy convex-hull test compared the actual four-dimensional convex-hull volume to the second-order analytic formula for 20 tangent directions at three deformation scales and found cubic-order residuals. This additional test is not a dependency of `verify.py`. Its numerical outcome does not certify the infinite-dimensional quantifiers or substitute for proof.

The nonstandard algebraic point is the mixed-bivector coupling: after decomposing the transverse movements into first Fourier harmonics and residuals, its quadratic form is exactly a squared matrix sum, not an indefinite remainder. The six-dimensional nullspace is geometrically identified with simultaneous orthogonal rotations; all remaining spectral levels are positive. The local stability modulus is sharp only in the limit of vanishing orbit distance. An independent mathematical audit has not occurred.
