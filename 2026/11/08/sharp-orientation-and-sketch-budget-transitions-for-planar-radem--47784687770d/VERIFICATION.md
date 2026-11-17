---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For SPD 2x2, Nyström residual A−AwwᵀA/(wᵀAw) is PSD rank one with all three unsquared norms equal to 2det(A)/(wᵀAw) for sign w. Two projective Rademacher directions yield better and worse denominators b(κ+1±(κ−1)t), worse-only probability 2^−m. Reciprocal-affine sum is strictly convex in t for κ>1, so maximal risk at t=0 or1, switched at κ+1=2^m. Uniform circular Gaussian direction integral gives benchmark b√κ; endpoint comparison yields 2^m>=1+√κ. Independent rational endpoint, direct 2x2 residual and angular integration checks, with distinct candidate-cost caveat.

## originality

PASS

Best-of-knowledge novel self-contained sharp risk law for a natural low-rank approximation benchmark: two-sign Rademacher support, best of m rank-one Nyström candidates, exact worst orientation and Gaussian single-probe comparison. Known general sketch approximation results do not state or mathematically imply the closed-form minimax threshold under identical objective. Different computational budgets and narrow 2D scope are explicit.

## value

PASS

Under a clearly defined one-column Rademacher Nyström candidate-selection protocol, the exact worst-case orientation and sample-budget crossover and Gaussian reference are useful precise performance baselines for evaluating discrete sketches. It is a narrow but natural exact fact; computational cost asymmetry and restricted dimension are disclosed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
