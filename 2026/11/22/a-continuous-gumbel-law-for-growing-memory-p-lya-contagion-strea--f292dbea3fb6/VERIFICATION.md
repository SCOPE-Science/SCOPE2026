---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

I reconstructed the growing-memory argument, including the start/end and lattice issues. An M-window with the classical Pólya law followed by one predictor update has the exchangeable (M+1)-block law, so shift preserves the M-window distribution. Consequently P(1^k)=u_M q_M^{k-M}, and subtracting P(1^{k+1}) gives the exact probability of the start word 0 1^k. Common uniforms yield d_t <= sum_{j=1}^M d_{t-j}/(M+c); e^v-1 <= v e^v gives sum_{j=1}^M exp(kappa*j/M^2) <= M+kappa*exp(kappa) < M+c, hence uniform worst-state TV mixing on the M^2 scale with the stated prefactor. If n p_k tends to a strictly positive finite constant, q_M^{k-M}=O(M^{beta+1}/n), k=O(M log n), and the separation scale h=k+ceil(C_r M^2 log n) is o(n). For two start locations i<j, the state immediately before the second word's initial zero is at j-2, so there are at least g-1 (rather than g at exact equality) intervening updates if j-i>=k+g. Use epsilon_M(g-1); C_r can still make it o(n^-r), or increase the separation by one. Conditioning sequentially on history through the preceding tested word then gives p_k+O(epsilon_M(g-1)) at separated starts, hence the product main term. Close gaps at most k are impossible; at other close gaps the conditional probability is at most q_M^{k-M} (indeed, q_M^k also bounds the k successes), with no independence required. With j clusters the error is bounded by a constant times (n(p_k+epsilon_M(g-1)))^j (h q_M^{k-M})^{r-j}, which vanishes for j<r under the stated hypothesis. Restricting these counts to disjoint intervals gives mixed factorial moments, hence independent Poisson counts (tightness and uniform integrability use higher moments, and the Poisson moments determine the law). Bounded first moments and approximation by interval-constant test functions give convergence of the point process; using the unrestricted total count also controls absence, with no lost endpoint mass. The only possible long run not detected starts at bit 1, with probability p_k/(1-q_M)=O(M/n). The gamma ratio implies n u_M(1-q_M) tends to infinity in this regime, so the rounded threshold 1+floor(b+x/tau_M) is eventually >=M; the rounding affects n p_k by a factor tending to 1, proving the continuous limit. An independent Fraction calculation passed 3,500 assertions across M=1,...,4 and alpha,beta in {1/2,1,3/2,2,3}, checking initialization, invariant windows, k=M,...,M+3 word probabilities, and the initial-boundary event. Replay: python3 /workspace/branches/73ce06b5-d65d-4b94-8a33-dc217897be38/ordinal4_rational_check.py. This finite check does not test the asymptotic theorem; the shipped checker was not run. The stated sufficient growth regime, fixed positive masses, and natural initialization are retained.

## originality

PASS

Best of knowledge, the distinct result is the exact continuous Gumbel and spatial Poisson limit for this growing-memory triangular array, with a usable explicit growth condition and normalization. Neither the finite-memory model nor stationary word-count Poisson methods are new. General quantitative approximations are real precursors and may supply an alternative proof after the uniform-in-memory estimates, but the comparisons that could be assessed do not give the Pólya-array conclusion without these estimates.

## value

PASS

Long successive universal arrivals are a natural observable that is not recoverable from Gaussian edge statistics. The theorem separates exact stationary entrance frequency from persistence, quantifies the changing-memory scale, and identifies when the fixed-memory lattice obstruction disappears. The spatial law gives locations as well as lengths indirectly through threshold exceedances. No graph-wide or optimal-growth consequence is needed for this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
