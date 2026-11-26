# Independent mathematical audit

## correctness

PASS

In a two-sided stationary Poisson construction, the elapsed interval and earlier inter-reset intervals are iid exponentials; independent Brownian increments over them are iid Laplace with scale ℓ=√(D/r). Successive contractions give the stated weighted sum. Its variances are summable and identical-noise coupling contracts any initial difference by a raised to the number of resets, giving uniqueness. Writing w=ℓ²θ², the log product is ∑_{k≥1}w^k/[k(1−e^{−2εk})]; expanding the reciprocal as (2εk)⁻¹+1/2+O(εk), with the error bound valid also for large εk, gives Λ/ε−(1/2)log(1−w)+O(ε) with interior derivatives. At θ_y the tilted mean differs from y/ε by O(1). The tilted Laplace factors after centering and √ε scaling have product modulus bounded by (1+cεt²)^−⌊1/ε⌋, c=ℓ²e⁻². On |t|≤ε⁻¹/² this is bounded by an integrable Gaussian; outside, its integral is bounded by ε⁻¹/²(1+c)^−(⌊1/ε⌋−1) times the integral of (1+cu²)^−1. The characteristic-function limit thus gives uniform density convergence. Integrating the tilted density against e^−θ_y u for overshoot u≥0 gives √ε/[θ_y√(2πΛ″)], and exponentiating the order-one cumulant gives the stated boundary multiplier. For the full LDP, Λ is strictly convex and steep, local lower bounds follow by interior tilts and concentration, and Markov bounds and exponential tightness give the full upper bound. Near zero the quartic cumulant gives the stated negative quartic correction. At large y, 1−(ℓθ_y)²=e^−θ_y y gives y(1/ℓ−θ_y)→0 and Λ→π²/12, proving the claimed intercept.

## originality

FAIL

The LDP and dilogarithm were already stated for this model in Resultary. The remaining sharp equivalent is covered by the published stationary product, the standard asymptotic of that same q-product including the endpoint term, and the prior nonlattice mod-φ theorem. The applicability and substitutions below yield exactly the claimed multiplier, not just the rate or an unspecified prefactor. This is prior implication, not a claim that the exact reset-tail formula was previously printed verbatim.

## value

FAIL

The fixed-y coefficient is physically meaningful, but the frozen contribution combines a known stationary transform, its standard q-product asymptotic, and a precise-deviation theorem that already yields the full coefficient in this regime. The LDP is also covered. A self-contained derivation is useful exposition, but no further regime or nonroutine mathematical gap is closed by the stated claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
