---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

From the actual package definitions, conditioning on which walk and index is updated gives E[epsilon(t+1)|epsilon(t)]=(I-L_m/(2m))epsilon(t) for one walk, where L_m is mixed Neumann/antisymmetric terminal Laplacian, diag 1,2,...,2,3 (m=1: [2]), off diag -1. IID centered starting increments give C=1^T P^t 1/m. Verified half-integer cosine ghost boundary eigenvectors and their squared projections 1/[2m^2 sin^2(theta/2)], all nonnegative bases and sum-one coefficients. Exact Green vector x_j=(m^2-j(j-1))/2 solves Lx=1, sum yields cubic formula. Fixed-k eigenvalue limit under t/m^3->s plus O((k-1/2)^-2) summable weights prove F(s), including s=0. F is continuous strictly decreasing (F(0)=1, F(infinity)=0), so every fixed threshold has unique cubic crossing. M=1 and extra-inert convention are correctly handled. Independently constructed full finite-state rational Markov kernels at m=1..7 for both update clocks, compared 12 lags per case to exact conditional expectations and numerical spectral formula, 350 checks; independent exact Git tree reconstruction and high-precision F threshold bisections support finite constants, not infinite proof.

## originality

PASS

Best-of-knowledge original exact solution of the endpoint-correlation half of Wei's explicit open exponent conjecture: a normalized finite-m all-lag cosine expansion, integrated cubic polynomial, and nontrivial complete crossover profile. Classical one-reservoir SSEP and Fourier methods are established; inspected prior mixing, hydrodynamic and static/spatial covariance theorems have different precise conclusions. Potential unindexed exact exclusion reformulation is a genuine priority caveat, not a claim of absolute novelty.

## value

PASS

This exact, size-uniform endpoint time-correlation law answers a specifically posed recent numerical exponent question for a natural two-walk representation of meandric systems. The nontrivial full scaling curve, lag-integral Green polynomial, explicit threshold constants and sampling-clock distinction are mathematically useful benchmarks for isolating endpoint transport from as-yet-unanswered crossing-event fluctuations. Even though Fourier diagonalization/exclusion duality are classical methods, the precise conjecture resolution and quantitative normalizations are not a mere renaming or textbook tautology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
