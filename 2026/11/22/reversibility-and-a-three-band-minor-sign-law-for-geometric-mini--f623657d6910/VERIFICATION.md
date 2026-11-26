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

A direct reconstruction avoids reliance on symbolic cancellation: for X geometric with tail r and independent Z with tail q, put U=min(X,Z) and V=X−U. The mass at U=k,V=0 is (1−r)(qr)^k, and at U=k,V=l>=1 is (1−r)(qr)^k(1−q)r^l. These factor exactly into Geo(qr) and the stated innovation mass. Adding the independent next innovation therefore yields the claimed stationary pair with identical marginals, and symmetry gives detailed balance for the stationary Markov path, not a single common variable for every time. In the Gram array J, J_(i,j+1)=r J_(i,j) for j>i. At j=i the discrepancy J_(i,i)−J_(i,i+1)/r is w_i K²q>0, where w_i is the mass of U at i. Thus the next off-diagonal determinant is −r J_(i,i+1) times the discrepancy at i+1, while farther determinants have proportional columns. At the diagonal the Gram vectors at i and i+1 are independent because only the latter has a nonzero coordinate i+1; Cauchy–Schwarz is strict. All masses are positive and row normalization preserves signs. Common-shock conditional upper-tail functions are nondecreasing and both strictly increase between W=0 and W>=max(a,b) for a,b>=1, giving strict lag-one quadrant dependence. Shared future innovations and thresholds preserve order and give nonnegative upper-tail covariance at arbitrary lags. The recorded symbolic and finite grid checker was inspected, not relied on or run.

## originality

PASS

The geometric model, its one-step transitions and its general consecutive-pair generating function are explicitly prior art. The strongest exact-model overlap supplies the unfactored distribution; the frozen analytic contribution is its consecutive-pair structure and uniform all-index signed-minor law, including the strict negative neighboring band alongside monotonicity and reversibility. The inspected same-day nearby result is for another model and a restricted column pair. This supports the distinct minor classification, not historical priority for reversibility or minification generally.

## value

PASS

This is an exact dependence boundary for a natural existing two-parameter chain, not merely a new algebraic presentation of its pgf or one small example. It locates every adjacent failure of likelihood-ratio order while explaining why stochastic monotonicity, reversibility, and positive quadrant dependence coexist with those failures throughout the interior. The shared-shock derivation gives a useful reason for both strict positive quadrant dependence and the zero and negative determinant bands.

The dated certificate retains the supplied scientific assessment, sources and limitations.
