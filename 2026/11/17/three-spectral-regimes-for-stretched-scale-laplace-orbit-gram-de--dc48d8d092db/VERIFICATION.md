---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The normalized Laplace inner product is the exact Cauchy kernel 2sqrt(lambda_i lambda_j)/(lambda_i+lambda_j). Cauchy double-alternant gives the tanh product. For alpha<1, the kernel F_c(u)=-2 log tanh(cu/2) has integral pi^2/(2c) and the k-mesh near i has spacing alpha*i^(alpha-1); summing row terms yields N^(2-alpha)*pi^2/[2c*alpha*(2-alpha)]. Uniform tail truncation is supported by concavity and exponential decay. At alpha=1 the equal-index-gap sum gives gamma(c)N-beta(c)+o(1). For alpha>1 sum of off-diagonal sech entries is absolutely finite, G-I is trace class, injectivity from uniqueness of the Laplace transform of a finite atomic measure gives bounded invertibility and positive Fredholm determinant. Toeplitz positive symbol for alpha=1 and coherent large blocks for alpha<1 establish the frame/Bessel threshold. Inspected frozen RESULT.md and check.py; numerical diagnostics are finite checks, not proof of limits.

## originality

PASS

PASS best-of-knowledge for the explicit three-regime sharp finite-volume determinant asymptotics and coefficient, not for the classical Cauchy determinant identity, Carleson separation or generic frame equivalence.

## value

PASS

The exact determinant decay is a natural quantitative condition-volume invariant for normalized Laplace orbit samples, with a sharp phase transition from non-Bessel to stable frames and trace-class perturbations, and a nontrivial pi-squared asymptotic coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
