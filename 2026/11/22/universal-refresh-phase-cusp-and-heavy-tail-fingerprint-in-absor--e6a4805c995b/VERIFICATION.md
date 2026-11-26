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

The killed unit-total-rate sine kernel has eigenvalue ℓ=1−cos(πp); summing over live sites gives Aₘ=sin(mπp)cot(πp/2). For example the sum can be Abel-regularized: the geometric sine sum tends to sin(πp)/[2(1−cos(πp))], and its product with sin(mπp) is bounded, giving the stated integral. Independent integrated rates multiply the spectral weight by φ(τℓ)^n φ(θτℓ). Near zero, Aₘ→2m and 1−φ(τℓ)~a p^(2α) with a=cτ^α(π²/2)^α; away from zero φ(τℓ) is bounded strictly below one even if the rate has a zero atom. Rescaling p=(an)^−ν y yields the stated leading constant. Subtracting before rescaling gives the additional factor n[1−φ(θτℓ)]→θ^α y^(2α), dominated by a polynomial times the same integrable stretched exponential; normalizing the integrals gives νθ^α. The normalized decrements are monotone in phase, so their convergence to the continuous limit is uniform by a finite-mesh squeeze, even though Aₘ may change sign. Expanding the time normalization yields ν(θ−θ^α), including both endpoints and the identically zero α=1 case. Direct differentiation verifies the minimum and strict α monotonicity in the interior. At fixed n, the Laplace hypothesis uniformly on 0≤ℓ≤2 gives the fractional cusp coefficient. In its Bernstein representation Fubini is justified by the bounded spectral weight and min(2v,1), and strict positivity follows since the mth jump time has positive density at every positive operational time and all of the first m jumps can be leftward. This gives a strict survival decrease over any positive added operational time and hence an infinite negative right slope. On the preceding block at elapsed time bounded away from zero, s|φ′(s)|≤1 bounds the derivative integrand, including the limit from the left. Rescaling the cusp coefficient uses the same Gamma ratio ν. These are separate limits for fixed model and fixed m, not a joint boundary-layer expansion. Read RESULT.md, VERIFICATION.md and check.py; the 193 numerical assertions are the source's reported finite evidence, not rerun or assumed to prove uniformity or positivity.

## originality

PASS

The strongest exact overlap is the known killed-walk spectral survival law and leading equivalent; the earlier Resultary law covers the latter even for a correlated environment on its stated domain. Finite jumps of first-exit density at redraws were also known. Pass is for the uniform first-relative-order phase law under only the stated Laplace assumption and the strict infinite-mean fractional cusp with its positive and normalized amplitude, not for the leading tail, the refresh model, or the existence of finite density discontinuities.

## value

PASS

The refinement isolates a physically meaningful phase effect that a leading power law erases and gives its exact profile without a second-order rate-law hypothesis. The same setting exhibits a qualitative infinite-mean redraw cusp with strictly positive amplitude for every positive redraw instant and a quantitative late-time normalization. These distinguish phase-resolved survival from a smooth power-law interpolation, without promising identification from noisy data or a full second-order survival expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
