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

The accompanying standalone `verify.py` runs on Python 3 with NumPy, SciPy and SymPy. Invoke `python verify.py` from the extracted artifact directory. The program constructs the two-coordinate phase matrix in two ways: (i) independent real one-dimensional radial and relative-angle numerical quadrature and (ii) the gamma-function moments in the theorem. It performs all three-dimensional quadratic spectral and multivariate ambient-multiplicity comparisons, a symbolic characteristic-polynomial identity, and finite tests for monotonicity of the extreme eigenvalues in degree.

A completed run reported:

```
PASS: 42 exact-structure vs independent quadrature checks, max error 2.6756374893466273e-14
PASS: all 6 quadratic spectra match; finite monotone spectral-edge tests k=0..6
PASS: symbolic cubic characteristic polynomial
PASS: all-dimensional quadratic multiplicities d=2..8, three apertures
half-phase spectrum d>=3: [0.125, 0.25, 0.5, 0.75, 0.875]
squared restriction condition number: 7
```

This is numerical and symbolic corroboration of specific finite cases, **not** exhaustive testing of all angles, dimensions or degrees. The universal assertions rely on the Dirichlet-and-phase derivation, exact three-by-three characteristic polynomial, convex-combination degree comparison, and explicit geometric exponential bounds in `RESULT.md`. No independent audit has been performed.
