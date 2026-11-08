# Self-review

## Correctness — PASS

The stated post-erasure chain is exactly the mechanism in Cruciani–Dudeja. For an arbitrary fixed \(k\)-set, one-step stationary conditioning yields \(a_{n,k}=q^k[(1-k/n)a_{n,k}+(k/n)a_{n,k-1}]\), with strictly positive denominator for \(0<p<1\). Iterating gives the all-present stationary probability as a finite product; binomial inversion recovers the entire count distribution. Common-draw/common-loss coupling preserves subset inclusion, proving the union-bound lower hitting-time estimate. The same coupling eliminates each initial coordinate discrepancy by survival probability at most \(q^t\), proving the total-variation estimate and geometric-block upper hitting-time estimate. For \(p=c/n\), the exact product is a Riemann sum of a jointly continuous integrand; its positive limiting rate and polynomial mixing blocks prove the exponential limit. Strict convexity of the exponential function gives the strict comparison with the one-point heuristic. The 491 programmed exact and finite numerical assertions passed; the asymptotic proof is analytic, not extrapolation from enumeration. No missing boundary case is used: \(c>0\), \(n>c\), and completion is post-loss.

## Originality — PASS (provisional)

Cruciani and Dudeja, arXiv:2602.20705v1, Sections 3–4, derive the marginal mean \(q_*\), metastability, a non-sharp upper and a matching-to-mean-field lower-bound heuristic, and an algorithm for the exact expected time; they do not give the critical exponential-rate integral. Long, arXiv:2605.14511v1, Sections 5.1–5.5, determines the stationary high tail and rare hitting law only for fixed \(p\in(0,1)\); his constants, comparison bounds and infinite immigration-thinning limit depend on fixed \(p\) and do not imply the moving \(p=c/n\) formula. His fixed-loss result already refutes the marginal heuristic in a different scaling and is credited explicitly. The deterministic-expiration variant arXiv:2604.26298v1 is a different model. Searched published mathematical records for the precise post-loss chain, stationary inclusion identities, fixed versus moving loss probabilities, and transformed exponential-rate formula; the closest located published-finding corpus records concern global catastrophic resets, general exchangeable Bernoulli counts, or unrelated refresh transports, with no matching implication. Novelty is best-knowledge only, not a uniqueness proof; a broad stochastic-cache stationary identity or an unindexed new paper could cover the exact product or rate.

## Mathematical value — PASS

The new exact logarithmic mean-completion rate resolves a natural critical case left at only \(e^{\Theta(n)}\) in the foundational paper. In particular it shows its proposed independence heuristic is *strictly exponentially too optimistic* for every fixed \(c>0\), not merely by a constant. The stationary inclusion product also supplies an exact all-present mass and full count-distribution transform for the nonmonotone chain, useful for investigating other rare-state questions. This is structurally nontrivial, not a numerical recomputation of the authors' exact finite algorithm; the stationary measure and polynomial-scale comparison yield a different analytic route. It does not claim an exact prefactor, a limiting hitting-time distribution, or universality beyond uniform independent post-loss erasure.

## Closest literature and residual risks

- E. Cruciani and A. Dudeja, *The Careless Coupon Collector’s Problem*, arXiv:2602.20705v1, especially Section 4 and the stated future direction on sharpening bounds: motivating model and nonsharp critical regime.
- C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511v1, Sections 5.1–5.5 and Remark 5.16: important fixed-loss theorem and explicit warning about independent-marginal heuristics, but no moving-loss exponential rate.
- C. D. Long, *The Expiring Coupon Collector*, arXiv:2604.26298v1: distinct deterministic-window model.

Independent historical priority checks, a broader cache-thinning formulation, and independent proof validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
