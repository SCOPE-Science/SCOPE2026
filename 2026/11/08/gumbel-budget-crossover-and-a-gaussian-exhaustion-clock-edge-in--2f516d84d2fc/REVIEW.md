# Scientific assessment

## Correctness — PASS

The claim is a joint-limit theorem rather than a claim about finite-rate simulations. The proof fixes independent Brownian first-passage and exponential resetting clocks and the exact convention that the \(n\)-th alarm exhausts the budget. Its one-attempt Laplace transform is derived by a survival integral; differentiating gives the exact failure-conditioned mean and variance. Under \(e^{-z}=e^{-c}/n\), the geometric success index yields an exponential limit. Stopped-martingale orthogonality shows total scaled time differs negligibly from the number of attempted cycles. On exhaustion, the attempt clocks are conditionally independent, with bounded third moments and variance tending to one, so Lyapunov's theorem supplies the Gaussian edge. The discontinuity of the geometric-index mapping lies at a point of zero limiting probability. The narrow-deadline limit follows by splitting success and failure events and controlling successes that terminate near the budget endpoint. The packaged standard-library checker evaluates independently the critical formulas and reports 76 passing diagnostics; it is not an infinite-proof certificate.

## Originality — PASS (qualified)

**Closest prior sources.** Bressloff (arXiv:2310.20502, Sec. V) already developed the truncation framework and exact finite-reset splitting probabilities and conditional first-passage means. Linn–Lawley (arXiv:2302.05409, main frequent-reset limit) already established an exponential clock law without finite budget. Sunil et al. (arXiv:2304.09348, joint time/reset-count transform) already contains exact renewal/count information. The present assertion is specifically a *joint large-budget/high-rate regime* and its associated two-scale time law, not any of those existing exact formulas. Primary sections, relevant research-record matches, and multiple literal/alias searches did not reveal explicit coverage of the coupled Gumbel-to-Gaussian boundary layer. The mathematical conclusion is not established as uniquely unpublished: a general renewal or triangular-array theorem, or an unindexed finite-budget analysis, might imply it without matching vocabulary. This is a residual publication-priority risk rather than a proof of absolute uniqueness.

## Mathematical value — PASS

The finite resetting count is a physically motivated resource cap in the source's model. The result gives the critical rate scale at which the particle has a nontrivial chance of exhausting the resource; the full termination-time law on the resource timescale; and an additional Gaussian layer that resolves the atom into a practical narrow-deadline success/failure profile. The conditional Gaussian width supplies the narrow-deadline information not determined by an already known conditional mean or an unbounded-reset exponential approximation. The cutoff classification is complete in the specified critical window and combines different limiting mechanisms, rather than arbitrarily evaluating a single parameter value.

## Limitations and research priority

The theorem is restricted to one-dimensional Brownian absorption, fixed-distance instantaneous Poisson resets, and \(r_n=(D/a^2)(\log n+c)^2\) for fixed \(c\). No uniform quantitative rates, higher-dimensional extensions, alternative restart laws, or independent validation are claimed. Existing finite-budget moment identities are entirely attributed to Bressloff; the novelty assessment is for the simultaneous critical-window and clock-layer conclusion only. The accessible research record is not a complete literature census.

Self-review: passed. Independent audit: not yet performed.
