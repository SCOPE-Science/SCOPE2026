# Independent mathematical audit

## correctness

PASS

The frozen Brownian-window proof incorrectly attributed tightness to independent binomial increments: in a fixed-size sample, disjoint interval counts are jointly multinomial, not independent. The complete corrected RESULT.md is in repairs/1. It Poissonizes the sample size with mean n (independent of an infinite observation sequence), applies the rate-one Poisson functional CLT at time nF(u/a_n), and couples back. The expected supremum discrepancy on [0,M] is at most F(M/a_n)√n; after scaling by √(a_n/n) this is at most M/√a_n. For s=sample mean of unit-rate observations, the deterministic part of the fitted-scale count identity is n(1−1/s)F(sy). On y=u/a_n it has normalized supremum O_P(a_n^(−1/2)), and continuous-limit time change and the O(a_n^(−1)) integrated centered term preserve the Brownian limit. The pathwise identity for H follows from ΣY_i=n and substitution gives Q=(a/n)∫H_n(u/a)² exp(−u)du. Under the null, simplex shifts give one- and two-coordinate survival r^(n−1) and s_2^(n−1), and conditional first/second moments on each translated simplex give (4), including n=2. Negative indicator covariance and the exact mean of H give the integrable tail uniformly in a/n. For small y the pair-covariance sum is O(ny²), via r²−s_2=y²/n². The integrated centered count has L² norm ≤(2/3)√n y^(3/2); together these justify the repaired moment expansion ny(1+o(1)) and E Q_n→1 for every divergent sequence. Local rare-event convergence with asymptotically unit sample-mean scaling gives the critical Poisson functional, while the supercritical compact count is identically zero with probability tending to one; the same weighted tail handles both. Independent increments and fourth moments give the squared-process covariance 2min(u,v)²/c²+min(u,v)/c, hence mean 1 and variance 1+c/2; Brownian gives variance 1. The same compact-and-tail argument checks both interpolation endpoints. The fixed-n limit follows by integrating H=−ny below the positive sample minimum. The bounded independent algebra check reproduced the Poisson moments and fixed-sample endpoint. The frozen verification.py was inspected, not executed; finite numerical diagnostics do not establish these limits. No statement is made for adaptive tuning or power.

## originality

PASS

The corrected result explicitly credits the already covered fixed-n endpoint. The surviving claim is the joint diverging-weight null transition of the exact fitted statistic, with its weighted functional, Poisson variance and supercritical escape of expectation. Neither fixed-a convergence nor the original stronger fixed-n a→∞ expansion supplies that joint theorem.

## value

PASS

The repaired result resolves how order-n weighting changes null calibration for a published exponentiality test: the local Gaussian input becomes a compensated-Poisson input with an explicit variance increment c/2. Faster weighting drives the statistic to zero in probability but not in mean, which is not visible from either of the known one-parameter limits. This matters for calibrating highly localized deterministic weights and supplies an analytic check on approximations. It does not give a power-optimal tuning or promise adaptive validity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
