# Self-review

## Correctness — PASS

The exact bridge covariance integrations produce the two conditional-risk gains and prior variances. After the one-to-two map from sampling time to \(u=t(1-t)\), the derivative has a quadratic sign factor with exactly one positive zero, including the noiseless case. This proves all global maximizers without numerically presuming concavity. Boundary signs, equality at the bifurcation, the equal-variance calibration \(w=15\), and the two implicit-function expansions were reconstructed symbolically. The packaged standalone checker passed 84,948 finite algebraic, rational and objective comparisons. Finite checks are corroboration, not proof of global claims.

## Originality — PASS (provisional priority)

The first public source for the multi-integral setting is Xi–Briol–Girolami (2018-01-12), which provides posterior Gaussian quadrature formulas and convergence rates but no weighted two-Legendre Brownian-bridge one-point design threshold. Foster–Lyons–Oberhauser (2019-04-15) establishes Brownian polynomial-moment approximations under a different observation model, and Karvonen–Kanagawa–Särkkä studies quadrature-weight stability. Related published two-node Brownian-bridge records concern single-integral, two-reading designs, not the theorem's joint target and one reading. Actual database and source comparisons found no covering claim, but this is not a uniqueness certification; uncatalogued older work remains a risk.

## Value — PASS

The two targets are the first nontrivial polynomial moments of one bridge and correspond to simultaneous integration of mean and linear trend. Equal variance-normalization determines the canonical weight \(w=15\) without arbitrary tuning and yields a sharp, usable noise tolerance \(\eta=1/2\); the optimum jumps in multiplicity but moves continuously with square-root separation. The full relative-weight phase diagram explains precisely when a single measurement should prioritize the antisymmetric moment instead of the central integral. Generic Gaussian conditioning alone does not state these exact global design regimes.

## Limitations and status

Only one nonadaptive noisy point reading; known pinned-bridge covariance and Gaussian noise; the first two specific polynomial moments and squared Bayes risk. The priority comparison is source-based, not independent historical proof. No claim of a multi-reading or arbitrary-kernel result.

Self-review: passed. Independent audit: not yet performed.
