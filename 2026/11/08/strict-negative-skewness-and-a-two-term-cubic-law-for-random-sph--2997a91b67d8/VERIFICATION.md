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

# Verification and limits

## Reproducible computation

Install the dependencies specified in `requirements.txt` and execute `python check_perimeter.py`. The checker computes the harmonic-degree-one gamma coefficient in dimensions \(3,4,8,16\) independently from Gauss–Jacobi quadrature and confirms the exact Legendre eigenvalue identity \(\lambda_{2k+1,3}=\pi \binom{2k}{k}^2/[8(k+1)^2 16^k]\) through degree 23. It evaluates truncated positive spectral cubic series, checks the strict first-harmonic lower bound, and samples 890,000 independent spherical triples across ambient dimensions \(3,8,24,64\). The fixed random seed ensures reproducible outputs.

The executed code returned `SPHERICAL_TRIANGLE_PERIMETER_CUBIC_CHECKS_OK`. The truncated spectral cubic moments were approximately \(-1.0907021095\), \(-0.5437720265\), \(-0.1130328571\), and \(-0.0257395475\) for these first four dimensions respectively. The corresponding strict harmonic bounds were approximately \(-1.0900644145\), \(-0.5436308026\), \(-0.1130298721\), and \(-0.0257394942\). Numerical quadrature does not certify the infinite series, and these finite experiments are not infinite-dimensional proofs. Analytic convergence and strict positivity are established in `RESULT.md`.

## Analytical proof boundary

The critical nonstandard claim is strict positivity of the third cyclic arcsine kernel moment. It follows from an explicit positive tensor-power expansion, trace-class summability, and nonzero first- and third-harmonic eigenvalues. The coefficients of the \(d^{-2}\) and \(d^{-3}\) terms use exact spherical contractions; the term-by-term remainder is bounded through absolute moments and Hölder's inequality. The order \(d^{-2}\) error in standardized skewness uses cancellation, not a fitted numerical coefficient.

Independent mathematical review, exhaustive novelty proof, alternative-sampling models, and an all-dimensional closed-form perimeter density are outside these checks.
