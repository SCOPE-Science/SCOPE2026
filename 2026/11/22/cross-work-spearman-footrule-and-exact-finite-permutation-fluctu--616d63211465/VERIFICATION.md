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

For integral displacements the sum of the absolute displacements at the two neighboring positions equals twice the central absolute displacement except for a correction of two at a fixed point. Directly subtracting at the two endpoints gives −f(1) and f(n)−(n+1), including n=2. In S_n the double-centered squared norm of |i−j| divided by n−1 gives Var D=(n+1)(2n²+7)/45. Conditioning on each fixed-point event deletes one row and column, yielding Cov(D,F)=−(n+1)/3. Sampling the two endpoint images without replacement gives Var Δ=n(n+1)/6 and Cov(D,Δ)=−n(n+1)/6; conditioning on an endpoint fixed gives Cov(F,Δ)=1. Together with Var F=1 this gives (2)–(3), including strict negativity at n=2,3 and positivity for n≥4. For R=2F+Δ, Var R=n(n+1)/6+8 and Cov(D,R)=O(n²). Its variance after regression on D is n²/6+O(n), yielding the leading correlation loss Var(R residual)/(8 Var D) = 15/(32n)+O(n^−2). The centered R has standard deviation O(n), negligible compared with the n^(3/2) footrule scale, so the standard combinatorial CLT for the double-centered footrule array (entry size O(n) versus standard deviation of order n^(3/2)) transfers to W. As an independent algebraic route for full maps, independence gives Var D=(n²−1)(3n²+8)/(60n), Var F=1−1/n, Cov(D,F)=−(n²−1)/(3n), Var Δ=−Cov(D,Δ)=(n²−1)/6 and Cov(F,Δ)=(n−1)/n. Substituting in the identity gives (5). Each centered independent W row contribution is O(n), negligible at the n^(3/2) total scale, so Lindeberg applies. The leading variance coefficients are 8/45 and 1/5, giving 8/9. Uniform image marginals give the same mean in both laws, without assuming permutation images independent.

## originality

PASS

Cross-work itself, its two means, and the classical footrule variance and normal limit are not new. The checked sources do not supply the fixed-point and endpoint correction with its resulting exact cross-work/footrule covariance and two-law fluctuation comparison. Normality as such uses standard limit theory, not an originality claim.

## value

PASS

The same natural transformation statistic has identical means but different exact fluctuations under sampling with and without replacement. The decomposition identifies which local coincidences and endpoints affect those fluctuations; the small-order covariance reversal versus strong positive asymptotic correlation and the nonunit variance ratio quantify meaningful differences that a mean or a general CLT would conceal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
