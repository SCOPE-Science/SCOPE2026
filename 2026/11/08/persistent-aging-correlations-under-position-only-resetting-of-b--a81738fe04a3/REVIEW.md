# Self-review

## Correctness — PASS

The final statement concerns position-only Poisson resets of the Brownian-squared diffusion coefficient model \(D_t=2\Lambda^2B_t^2\). The position integral after the most recent reset is exact. Gaussian Wick identities yield exact second/fourth/mixed moments and the conditional future second-moment semigroup gives an exact two-time formula. At proportional lags, the leading terms give the squared-correlation coefficient \(2/(17c)\). The multi-time weak limit follows from a vanishing local-Brownian-increment error, Poisson window separation and Brownian scaling. The product-of-normal-and-Laplace density, logarithmic central singularity and stretched-exponential saddle are independently reconstructed. The standalone checker verifies numerical consequences but is not a substitute for infinite-time arguments.

## Originality — PASS with stated residual risk

The original Brownian-diffusivity paper explicitly resets **both** the position and volatility and identifies position-only resetting as a future question (arXiv:2205.00549, Section 7). The strongest similar published prior, arXiv:1812.05664, leaves a **deterministic** diffusivity unreset and thus has a Gaussian conditional input with no common stochastic-volatility mixing. Targeted searches across aliases, scaling laws and squared-position aging found no stronger explicit matching theorem. Generic jump-SDE resetting theory is acknowledged and does not by itself state the explicit limit or constant. Unindexed literature remains a residual priority risk.

## Value — PASS

The physically motivated question is whether resetting only a tracer, rather than its external diffusivity, thermalizes it. The answer is structurally negative, quantified by a nonstationary normal-Laplace product law with different tails from the simultaneous-reset case. The unexpected long-range squared-amplitude correlation persists despite exponentially extinguished linear position correlation; its parameter-independent coefficient is a natural, measurable signature of the unrejuvenated environment, not an arbitrary finite slice.

## Limitations

The stochastic diffusivity is Brownian squared and therefore unbounded; the reset clock must be independent Poisson. The time ratio \(c>1\) is fixed, not the equal-time limit. A singular environmental reset-rate limit is not claimed. Published-record searches cannot certify global publication novelty. Independent review has not been performed.

Self-review: passed. Independent audit: not yet performed.
