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

# Verification notes

The proof in `RESULT.md` is analytic. Its critical nonstandard identity is the Poisson mark-cumulant formula: differentiating the logarithm of the Poisson exponential moment generating functional selects the one-particle joint indicator product even for a non-Markovian projected position process. The signed triangle then follows from the complex first harmonic of angular increments.

The enclosed `verify.py` was executed after writing its actual file contents; it returned `PASS: 89 independent quadrature, symmetry, asymptotic and derivative checks`. It compares exact two-dimensional numerical integration against the closed form at positive, zero and negative angular drift; verifies that the mean-square displacement is even and the signed triangle is odd in angular drift; tests the first two short-lag coefficients at multiple parameter values; checks all four right-derivative formulas; and checks a marked-Poisson cumulant differentiation identity. These checks are finite, hence neither a proof of global uniqueness nor a substitute for the symbolic derivation.

The exact observational conclusion assumes all spatially resolved count covariances and three-time cumulants are known in the ensemble. No finite-sample, finite field-of-view, or measurement-noise guarantee is established. Independent scientific audit has not been performed.
