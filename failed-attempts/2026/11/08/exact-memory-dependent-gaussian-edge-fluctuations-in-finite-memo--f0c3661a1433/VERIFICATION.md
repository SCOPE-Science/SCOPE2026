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

For fixed M, strict positivity of every append probability makes the shift chain irreducible, and its zero-state loop makes it aperiodic. Extending the initial Pólya block by one draw and dropping its first coordinate preserves the law by exchangeability. An independent analytic variance check uses f(H)=Z_M−ρ and the Poisson solution g(H)=∑_{j<M}jδ(Z_j−ρ)+(1+Mδ)(Z_M−ρ): substituting the append mean gives (I−P)g=f, including M=1. Within the stationary block the distinct-coordinate covariance is vδ/(1+δ), from the Pólya two-draw law. Hence 2〈f,g〉−v gives exactly vD_M. In the frozen argument the bounded innovations have predictable variation converging uniformly after division by N, by the ergodic theorem and monotonicity, so the martingale functional CLT applies. Lag shifting in the edge-weighted sum costs O_M(N) uniformly in the edge horizon, and division by N^(3/2) makes this negligible. Summation by parts maps a draw partial-sum path x to tx(t)−∫_0^t x(s)ds at continuous limits; applied to Brownian motion this is ∫_0^t s dB_s. The covariance is therefore vD_M min(s,t)^3/3; dividing by the asymptotic N²/2 edge denominator gives the stated density variance. Ergodicity and the conditional Bernoulli law respectively give the finite-memory deterministic density limit and the infinite-memory Beta limit. The monotonicity and quadratic growth of D_M follow from its formula, without asserting a joint M,N limit.

## originality

FAIL

The earlier edge-count record gives the same terminal edge CLT and the draw FCLT under an equivalent parameterization. The remaining time-indexed statement follows mechanically by deterministic summation by parts, and the explicit multiplier also follows by a direct summation of older exact covariance recurrences. This is prior coverage by mathematical implication, not a claim that the earlier papers printed the full graph path theorem or that catalogue dates establish authorship.

## value

FAIL

The explicit inflation coefficient is useful, but the frozen submission adds only the deterministic weighting of an already obtained draw FCLT and rederives a known edge variance and terminal limit. The classical Beta comparison and elementary properties of the multiplier do not leave a distinct valuable remainder. No genuine repair within the frozen evidence was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
