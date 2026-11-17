---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For A=uu^T, Z factors into two independent normalized Bernoulli counts and a probe-coupled final factor. Exact Rademacher pairing gives E[H²]=2-2/n+1/p3; the product of moments gives the displayed variance for all p_j>0. Strict convexity of log(c+1/p) on (0,1], budget KKT and monotone s(1+(n-1)s)=t(1+(2-2/n)t) give a unique optimizer, t cap, and high-n limits. Independent exact rational enumeration of all original masks/probes for n=2,3 and symbolic/numerical KKT checks agreed.

## originality

PASS

Ghosh et al. already introduce independently masked incomplete-product cubic trace estimators and variance expansions. Their available primary full text does not state the heterogeneous-stage Bernoulli minimizer, strict preference for final-stage sampling, exact cap transition or asymptotic threefold comparison on this rank-one benchmark.

## value

PASS

Variance-optimal allocation with a finite-budget saturation threshold is a substantive design fact for incomplete-product estimators: final-stage probe coupling makes equal mask budgets strictly suboptimal. The test matrix is deliberately a tractable rank-one projector, not a general adjacency or universal optimizer; the explicit gap remains a meaningful method diagnostic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
