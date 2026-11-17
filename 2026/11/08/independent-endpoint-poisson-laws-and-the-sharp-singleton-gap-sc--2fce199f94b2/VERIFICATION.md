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

For each fixed set J of r singleton labels, the exact probability is B_{n-r}/B_n. Multivariate factorial moments for disjoint endpoint windows are the falling window-size products times this Bell ratio and converge to independent Poisson moments under a_n~W(n)/n; opposite windows disjoint because n*a_n grows. The resulting local point-process limit gives independent exponential first/last gaps. Expected-gap convergence is separately justified using fourth factorial moments of total singleton count, conditional hypergeometric uniformly random locations, and uniform integrability. Finite indicator covariance is strictly positive by Bell/Dobinski log-convexity. Independently enumerated every set partition n=2..7 and checked prescribed one-/two-singleton Bell ratios.

## originality

PASS

Best-of-knowledge: sharp joint endpoint spatial Poisson limit and n/W(n) mean gaps not found in earlier finite-extreme-label formulas or component-size Poisson approximations; inaccessible general-source implications remain a residual risk.

## value

PASS

The first and last singleton locations are natural extremes of the uniformly random set-partition model. Joint independence of opposite endpoint limiting Poisson processes and sharp mean gaps n/W(n) answer an explicit prior asymptotic question and explain emergence of independence despite strict finite-size positive correlations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
