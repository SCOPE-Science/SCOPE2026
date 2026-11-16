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
# Reproducibility and limits

Run `python3 CHECK.py` from this directory, using Python 3 and no external packages. The check completed with 107 passed finite assertions. It numerically approximates Poisson energy of the strip logarithm composed with monomial inner functions at interior points, verifies harmonic means and normalizations, checks monotonicity of finite Hilbert-block Rayleigh quotients, and checks the predicted norming diameters. Finite quadrature and finite matrices cannot establish the infinite-dimensional assertion.

The mathematical proof is in `RESULT.md`. Its nonnumerical critical points are: exact orthogonality of inner powers when \(B(0)=0\); a bounded boundary symbol of modulus \(\pi\); an exact generalized-Hilbert compression; the logarithmic Rayleigh limit and weakly-null tail sequence; and the Poisson variance formula from the two-valued boundary imaginary part. No independent audit has been performed.
