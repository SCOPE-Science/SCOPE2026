---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For k=2,3,4 the exact marginal over the Poisson product has log correction [-s(s-1)/(2λ)+ks-k²λ/2]/n. Exponentiation on s≤n^(1/8) leaves O((1+s)^4/n²); bounded-mean binomial and Poisson exponential moments control the weighted tails beyond that cutoff and give O(n^-2) in polynomially bounded expectations uniformly on compact positive intensities. In the disjoint covariance, r_4(s+t)-r_2(s)-r_2(t)=-(s-2λ)(t-2λ)/λ, giving -c²/(λn)+O(n^-2). The exact diagonal moment is 2λ, adjacent Poisson covariance is τ-μ², and the numbers of pairs give the uniform O(1) total residual. The score identity c=λμ′ and the Bessel recurrences yield c=2λ exp(-2λ)I_0(2λ). Orthogonal decomposition leaves a positive degenerate-kernel component (the 0,1 mixed difference is -2). Expanding the terms with counts 0 through 3 gives τ=λ+2λ³+O(λ⁴), μ=2λ-2λ²+2λ³+O(λ⁴), and c²/λ=4λ-16λ²+40λ³+O(λ⁴). At high intensity, bounded scaled fourth moments justify taking the absolute-product moment of the Gaussian contrasts of adjacent correlation -1/2, giving the stated coefficient. These are two limits of v only. The frozen checker and its output were inspected, not executed; their finite corroboration is not the proof.

## originality

FAIL

A distinct Resultary finding directly covers the central law and proves the only possible quantitative distinction by implication. Its §§1–3 supply a polynomially weighted second-order Taylor bound and the same three-term counting identity, yielding the frozen uniform O(1) variance error by summing Poisson moments before counting pairs. It also states the same score and Skellam identities, so the Bessel form of the correction follows by differentiation. This is demonstrated coverage, not an inaccessible-source or missing-evidence verdict.

## value

FAIL

The order-n conditioning correction is substantively useful, but is the same contribution already made for this statistic. The displayed O(1) remainder and Bessel rewrite are mechanically obtainable from the prior weighted error and score identity; no separately useful unknown invariant or new regime survives in this finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
