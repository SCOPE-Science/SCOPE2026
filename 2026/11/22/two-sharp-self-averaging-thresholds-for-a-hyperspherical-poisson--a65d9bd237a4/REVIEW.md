# Scientific assessment: Two sharp self-averaging thresholds for a hyperspherical Poisson-kernel uniformity statistic

## Correctness — PASS

The stated conclusion applies to a normalized off-diagonal Poisson-kernel average with independent uniform points on \(\mathbb S^{d-1}\), fixed \(\rho\in(0,1)\), and exponentially many sample points. The proof identifies an exact angular large-deviation rate, derives pairwise independence even for shared-endpoint edges, and uses concentration of angular-bin counts to justify the constrained Laplace principle despite triangular dependence. The variational maximum follows from an explicit nonnegative square and a signed derivative. Above the first threshold, truncation at a fixed angle just beyond \(\rho\) has asymptotic mean one and exponentially vanishing variance, while the nonnegative omitted term has vanishing expectation. The exact second moment comes from the classical Poisson-semigroup identity, giving the sharp second threshold. The accompanying checker passes 2,566 numerical/algebraic assertions; numerical assertions alone are not the proof.

## Originality — PASS, with priority risk

Fernández-de-Marcos and García-Portugués (2023, arXiv:2304.04519, full article and supplement) define the same off-diagonal statistic, its finite-dimensional moments, and fixed-dimension null asymptotics. Ding, Markatou and Saraceno (preprint SS-2022-0347, full primary text) give the same spherical Poisson kernel, kernel convolution and variance: **the finite variance is covered prior work and is not claimed as new**. Cai, Fan and Jiang (2013, arXiv:1306.0256, full text) establish the relevant exponentially sampled extreme-angle laws; their published limiting extreme and empirical angular laws do not specify this exponentially weighted average's probability-concentration transition or its separation from mean-square concentration. A research-record search and accessible earlier findings revealed no direct statement of the two-threshold law, nor a verified stronger statement that implies it without an additional rare-weight analysis. Random-energy and large-deviation models motivate similar transition phenomena; an unlocated general theorem could still bear on historical priority.

## Value — PASS

For a published hyperspherical goodness-of-fit statistic, the theorem locates the sharp exponential sample-size rate separating typical collapse of the uncentered kernel average from consistency, and proves a distinct much higher rate required for mean-square concentration. The intermediate regime converges to its expected value in probability while its variance diverges exponentially. This is a substantive warning against substituting moment convergence for typical behavior in high-dimensional calibration and supplies an explicit quantitative phase diagram with proven bounds.

## Limitations and provenance

The probability limit at the first critical rate is not identified; the logarithmic rate is proved there. The second critical point has a variance limit but no claimed distribution limit. These are simple-null, fixed-kernel-parameter, dimension-varying results and do not establish alternative-power claims. Prior work is credited for the finite variance. The attached proof and code permit ordinary independent review; no independent audit has been completed.

Self-review: passed. Independent audit: not yet performed.
