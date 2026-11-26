---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reconstructed RESULT.md lines 47–109. Set u_n=log[(lambda+n^2)/(lambda+(n-1)^2)] and F_n=exp(u_n-u_{n+1}). For two exponential terms with one positive and one negative exponent, increasing both the positive exponent and the sum of exponents gives domination for every s>0: any lost negative-branch increment is compensated over an interval where the derivative is strictly larger. On the stated interval F_1<=1<F_2, F_n>1 for n>=2, and F(y)=(lambda+y)^2/[(lambda+y+1)^2-4y] decreases for y>=9 (derivative sign 3lambda+1-y). Its n=2 versus n=3 comparison has numerator 295-140lambda-30lambda^2. This gives the required two inequalities and strictness even at both endpoints: the F inequality is strict against mode 1 at lambda=1/2 and the positive exponent is strict against mode 3 at lambda=lambda_*. AM–GM gives R_2>1>R_0. The leading exponential for lambda<1/2 and the derivative at s=0 for lambda>lambda_* prove necessity. For s>1/2, absolute summability and Fourier positivity give w_n=a_|n|(1+bR_|n|) and hence the sharp cutoff, -2/3 at lambda=s=1. At the boundary the consecutive frequencies starting at 3 give an invertible Vandermonde system for any finite set of distinct points, while the missing second harmonic precludes uniform density of the RKHS. With strictly positive weights the trigonometric polynomials are in the RKHS. This does not assert maximality on the restricted order range s>1/2. CHECK.py was inspected, not executed; its bounded numerical and rational tests are not an infinite certificate. VERIFICATION.md records no independent, expert or Lean verification in the frozen evidence.

## originality

PASS

The generic Fourier positivity reduction and the Matérn spectral family are known. The supported distinct result is the exact all-positive-orders parameter interval and unique active mode for the Bessel-power shifted-ratio family, with its corresponding threshold in the continuous-kernel regime. Neither the closest circle modulation records nor the inspected Matérn theorems imply that comparison of all modes and both endpoint obstructions.

## value

PASS

The mode selection has a concrete use: it determines the largest admissible negative cosine modulation and the exact spectral defect in a standard circle covariance family. The exact interval simultaneously valid for all positive orders, with distinct failure mechanisms on its two sides, is an informative classification not supplied by the generic Fourier test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
