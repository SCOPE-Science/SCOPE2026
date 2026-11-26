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

Independence fixes the mean at μ and gives variance μ+t². The identity ∂_t G_t=t(1−z)²G_t/[1+t(1−z)] verifies convex ordering independently of a growth-restricted test class: the derivative of E[(X_t−k)_+] for each integer k≥1 equals t times the mass at k−1 of X_t plus an independent geometric of mean t. It is positive on the interior. Any convex sequence on the nonnegative integers is its initial affine part plus a nonnegative combination of these stop-loss functions, so monotone summation extends the comparison to finite expectations and gives strictness for strictly convex tests, also between the endpoints. The displayed truncated-exponential identity gives strict log-concavity for 0<t<μ. Applying the coefficient derivative identity to −log p_n(t) at fixed t gives strict positive entropy derivative, since every second discrete difference is positive; local geometric bounds justify differentiation, and a uniform exponential tail gives endpoint continuity. Near zero p′_n(t)/t is bounded by C R^(−n) for some R>1 by coefficient extraction, while p_n(t) is bounded below by the no-geometric-jump Poisson term with mean at least μ/2. Hence h′(t)/t converges by domination to −Σ(π_n−2π_(n−1)+π_(n−2))log π_n = E log[(N+2)/(N+1)]. Integration gives half that value. At μ the entropy gap equals D(p||g) because −log g_n is affine and the mean is fixed. The endpoint score obtained from ∂_t G_μ is s_0=q_* and s_n=(n−1−2μ)/(μ(1+μ)) for n≥1; conditioning on N≥1 under g leaves N−1 geometric of mean μ and yields E_g[s²]=1/(1+μ). For rigor of the quadratic expansion, the formula for p_n(t)/g_n has a factor (q(t)/q_*)^n≤1 near μ and a bounded truncated exponential factor with bounded parameter derivatives, so the t derivative is at most C(n+1). Since 0≤x log x−x+1≤(x−1)², the quadratic KL quotient is dominated by C²(n+1)² against g, and termwise convergence gives 1/[2(1+μ)]. Both results are pointwise for each fixed μ>0; no uniform-in-μ conclusion is used. RESULT.md lines 41–116, VERIFICATION.md and verify.py were inspected. The code was not run; its finite checks are supplementary.

## originality

PASS

The count family, calculus of local KL divergence, and qualitative entropy-order principle are preexisting. Supported distinct content is the actual fixed-mean ordering of this path and, in particular, its two explicit quadratic entropy coefficients taken together. In this check the full originating arXiv preprint was available, unlike the access situation recorded in the frozen package; it gives a different stochastic parameter comparison. No inspected prior theorem supplies both endpoint evaluations. The conclusion is bounded by the sources compared, not a priority certification.

## value

PASS

Holding the mean fixed gives a natural comparison of entropy under increasing overdispersion between two canonical count laws. The two curvatures locate precisely the endpoint sensitivity where the qualitative order and first derivatives alone provide no rate. They give useful distinct benchmarks for the same model, beyond restating a general entropy-order or maximum-entropy principle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
