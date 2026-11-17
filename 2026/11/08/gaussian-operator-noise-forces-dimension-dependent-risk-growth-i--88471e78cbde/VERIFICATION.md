---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed fixed-data scalar recurrence X_t=(B/A)(1-(1-q(A))^t). For lambda0=0, E|A|^-2 diverges in both 1 and 2 real dimensions; for lambda0>0, all fixed-iteration moments are finite by |F_t|<=min(2,t omega |A|^2/lambda0). Small-A scaling A=sqrt(lambda0/(omega t))u gives real sqrt(t) coefficient 2 sqrt(pi)(2-sqrt(2)) beta p_A(0) sqrt(omega/lambda0); polar integration yields complex pi beta f_A(0) log t. Cross term is lower-order by Cauchy-Schwarz; a.s. fixed-A limit B/A. Independently quadrature verified universal real integral 2.07655885436006, equal to 2 sqrt(pi)(2-sqrt2). Separate fixed from resampled noise; lambda0, tau boundaries checked.

## originality

PASS

Published SD-TRK conditional fixed-perturbation estimate does not evaluate the expectation over a Gaussian operator singularity, and generic pseudoinverse sensitivity does not supply the specified regularized finite-time sqrt(t) versus log(t) rates and coefficients. Resultary search included distinct Gaussian Aitken and resampled-noise Kaczmarz results; none is an implication for the fixed-observation one-mode regime. Originality remains qualified by uninspected complete spectral-filter literature.

## value

PASS

Small noisy singular values produce a sharp dimension-sensitive risk divergence hidden by finite-iteration conditioning. The analytic constants distinguish real Fourier modes and complex Fourier modes of a practical regularized row-action solver and give a precise limitation of positive damping floor; significant despite scalar scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
