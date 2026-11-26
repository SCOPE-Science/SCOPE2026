# Independent mathematical audit

## correctness

PASS

Scale invariance reduces to rate one. The independent exponential pair transforms to an independent gamma sum and uniform split; thus each contrast is uniform and a single matching has variance 1/(6N). Integrating the conditional contrast on either side of y=x gives the displayed E1 expression. The projection is nonconstant (its limit at zero is 1 before centering), and the degenerate remainder has positive variance because the continuous nonconstant contrast cannot be additive in x and y and vanish on the entire diagonal. Given data the matching mean is the complete pair U-statistic: every pair is included with probability 1/(N−1). Its variance counts 2(N−2) ordered shared-index neighbors per edge and has covariance ζ on each such overlap. Conditional independence of resamplings gives the exact V_N plus the residual divided by B, so the removable term vanishes at N=2 and is positive at N>=4. Given fixed B matching draws, tagged edge contrasts have a bounded-degree dependency graph. A pair of matchings with K common edges has K identical pairs and N−2K shared-one-index pairs; E[K]=N/(2(N−1)), so the conditional scaled variance converges in probability to the stated limit. Cumulants of order r>=3 are uniformly O(N) before scaling, from bounded variables and O(N) connected tuples. The corresponding conditional moments converge after scaling, remain uniformly bounded at each fixed order, and integrate to the Gaussian moments. For B_N→∞, the degenerate U-statistic remainder is O(N^−2) in variance, while N times the mean-square matching error is at most 1/(6B_N); projection CLT and Slutsky give the second limit. An independent Dirichlet-simplex integral of the product of centered contrasts gave ζ=0.015867282799652 and reproduced the three printed ratios. Replay: `python /workspace/audit-replay.py 5` (also enumerates overlap counts up to N=8).

## originality

PASS

The supported distinct contribution is the explicit shared-data variance and numerical kernel projection for independently resampled complete matchings, together with the fixed-B Gaussian law with that variance and the unrestricted growing-B limit. The paired contrast, permutation average, single-pairing CLT and standard variance decomposition are prior; the original paper also suggests applying its CLT to the repeat average. The independent contribution is the quantitative law accounting for dependencies, not the idea that the average can be approximately normal.

## value

PASS

The published procedure uses 50 reorderings and explicitly studies d=0. The exact separation between pairing noise and data noise, with a 39.32% asymptotic variance fraction remaining at 50, answers a concrete design and calibration question not settled by the generic 1/B Monte Carlo reduction. The Gaussian laws quantify the uncertainty of a shared-data average rather than that of independent datasets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
