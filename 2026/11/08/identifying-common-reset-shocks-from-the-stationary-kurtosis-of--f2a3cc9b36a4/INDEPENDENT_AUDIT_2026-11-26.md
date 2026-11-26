# Independent mathematical audit

## correctness

PASS

Construct the process from the last resets on a two-sided clock realization. Coupling erases the initial diffusivity at its first reset, then the initial position at the next position reset. Conditional on the clocks and Ω, X is centered Gaussian of variance 2V, with V=∫₀^∞ Ω_{−s}² 1{no position reset in (−s,0]} ds. The absence event at each s is independent of Ω_{−s}; Minkowski and ∫₀^∞e^(−Rs/p)ds<∞ bound every L^p norm of V by the stationary Laplace moments of Ω. For the two ordered times in V², absence of a position reset since the earlier time leaves exclusive internal reset rate q=Q−c. Given the earlier Ω=u, its later mean square is e^(−qd)u²+2Λ²∫₀^d e^(−qv)dv at gap d, valid also for q=0. Integrating the earlier-later product with survival weight gives E[V²]=(2/R)[E[Ω⁴]+(2Λ²/R)E[Ω²]]/(R+q). Thus E[X⁴]=12E[V²], with E[Ω²]=2Λ²/Q, E[Ω⁴]=24Λ⁴/Q² and E[X²]=4Λ²/(RQ). This independently reconstructs the moment-generator calculation in RESULT.md (in particular the common clock removes X²Ω² only once). Future Brownian increments are centered given the reset histories, and survival of the respective marginal clocks gives conditional mean factors e^(−Rt), e^(−Qt). The equal-time cross moment vanishes by W symmetry, proving both lagged cross entries vanish. Strict monotonicity on 0≤c≤min(R,Q) and algebraic inversion give exactly the stated feasibility test, including c=Q or c=R and the equal-rate contrast. Full synchronization in the record's contrast is only when R=Q=c. The supplied checker.py and VERIFICATION.md were read; their reported 680 bounded assertions are not a fresh run. The replayable check is the analytic integral and generator reconstruction against RESULT.md lines 54–96.

## originality

PASS

The synchronized and independent endpoints are documented separately and must not be counted as novel. The distinct result is the stationary three-clock interpolation at fixed marginal rates, with its sharp inverse, despite invariance of the full linear two-time covariance matrix. The compared sources do not cover that variable-overlap statement.

## value

PASS

The exact overlap-dependent law answers a motivated identifiability question left open by joint-reset dynamics. Holding fixed both marginal rates and all linear covariance lags, ordinary kurtosis both separates the couplings and gives a sharp model-specific realizability test. This is more informative than recovering a fourth moment at one endpoint; it is not a finite-sample error bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
