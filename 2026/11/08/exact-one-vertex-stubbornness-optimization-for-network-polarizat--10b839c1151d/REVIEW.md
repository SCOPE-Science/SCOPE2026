# Scientific review

## Correctness: PASS

For a connected weighted graph, \(M=L+K_0\) is positive definite despite the selected zero entry of \(K_0\); this is proved from the Laplacian energy and at least one positive fixed stubbornness coefficient. The scalar equation for the selected node determines the exact equilibrium as \(x_0+d\eta(t)u\). The objective form \(H=L+I-\mathbf1\mathbf1^{\mathsf T}/n\) is positive semidefinite with constant-vector kernel; \(u=M^{-1}e_\ell\) is provably nonconstant, giving strictly positive quadratic coefficient when \(d\ne0\). The unique optimum follows by direct scalar convexity and proper treatment of the unattained infinite-resistance boundary. The example's rational formula and derivative are checked independently. A standalone exact-rational verifier passed 540 connected configurations and 12,831 listed assertions; this is supporting finite evidence rather than proof of universal cases.

## Originality: PASS, subject to explicit residual priority risk

Relevant first-party literature was read at the mathematical-statement level. Shirzadi–Zehmakan (arXiv:2410.22577v1), Section 4 and Theorem 4.3, gives special-baseline change formulas and neutral-node direction claims, but not the present arbitrary-baseline global coordinate optimizer, phase classification and strict interior example. Abebe et al. (arXiv:2011.02583v1), Section 5.1 and Corollary 5.4, establish marginal monotonicity for the distinct *linear sum-of-opinions* objective, not for quadratic polarization–disagreement. Hunter–Zaman (arXiv:1806.11253), Sections 4–5, optimize selection/placement of stubborn agents and mean/threshold outcomes, not the same continuous variable and social objective. Searches for equivalent formulations, broad matrix-reduction coverage and exact tables did not locate a theorem implying the whole claim. The algebraic Sherman–Morrison identity and prior special cases are acknowledged as known; an equivalent unindexed coordinate-optimization argument remains possible.

## Value: PASS

The question is motivated by an explicit research gap: whether changing a single individual's stubbornness should increase or decrease a standard polarization–disagreement metric and where to set that coefficient optimally. The complete formula replaces repeated inverse solves or scalar searches with two linear solves and one scalar projection for arbitrary fixed heterogeneity. It also establishes a qualitative difference from earlier endpoint-only optimization for total expressed opinion. The small exact path example shows a genuine attained interior improvement over both low and arbitrarily high resistance, so the conclusion is not merely a textbook restatement of a rank-one identity.

## Scientific limitations and remaining risks

The result is a deterministic one-coordinate theorem, not a joint-optimality or empirical behavioral assertion. The fully resistant endpoint is not finite, the other stubbornnesses must remain positive, and independent publication-priority verification has not occurred. Full text was examined in the relevant mathematical sections of the main 2024 and 2020 works and in the relevant sections of the 2018 supporting work; not every existing publication can be ruled out.

Self-review: passed. Independent audit: not yet performed.
