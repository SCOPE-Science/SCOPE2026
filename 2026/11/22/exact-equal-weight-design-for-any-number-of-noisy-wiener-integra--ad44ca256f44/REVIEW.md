# Scientific review

**Correctness: PASS.** The Itô-isometry objective is exact, including the noise penalty. An M-matrix proof ensures positive coefficients at distinct sites; zero sites, coincident sites and the final endpoint are excluded by explicit improving perturbations. Consecutive normal equations plus midpoint knot stationarity force identical weights for every sample count. The last normal equation has exactly one admissible root; a compactness argument establishes unique global optimality. Exact-rational reconstruction and finite grid checks are supplemental, not infinite proofs.

**Originality: PASS, qualified.** The noiseless Wiener design and generic Gaussian posterior kernel formula are prior work. Cai–Lam–Scarlett (2022) covers noisy rates rather than exact sample placement. Benhenni–Cambanis (1992) treats regular-sequence integral sampling. Mukherjee (2003) is the closest potentially dominating paper on product-covariance integral designs; its full text was inaccessible. The accepted mathematical claim is the all-\(n\), strictly positive-noise formula and no-replication/rigidity result; publication priority requires an independent literature check.

**Value: PASS.** Arbitrarily many fixed noisy measurements admit a common explicit weight and one quadratic specifying every site. The structural theorem distinguishes independent measurement noise from erasures and noiseless schemes; it gives a closed-form implementable design and a sharp exact error for any sample budget without solving a large nonlinear optimization. It is not merely a one- or two-node numerical example.

Scientific limitations: standard Wiener prior, known iid positive Gaussian noise, deterministic nonadaptive sites and unweighted path integral. No wall-clock cost optimization or empirical performance guarantee is claimed.

Self-review: passed. Independent audit: not yet performed.
