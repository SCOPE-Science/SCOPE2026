# Scientific review: hidden-reset-age information

## Correctness (PASS)
The common-reset stationary joint Gaussian mixture is exact; the squared radius is conditionally sufficient for elapsed reset age. Factoring the rescaled radius as an independent exponential times a Gamma variable yields the Bessel-\(K\) finite-population entropy formula. Strict increase follows from nondegenerate posterior uncertainty and the mutual-information chain rule. The asymptotic correction follows from the smooth small-log-Gamma-noise entropy expansion with variance \(1/k\), Fisher information one for log-exponential age, and the \(1/(6k)\) term in the log-Gamma entropy. The exact one-particle value and 78 computational tests independently check normalization and representative cases. Numerical checks do not prove the uniform infinite-population assertion.

## Originality (PASS with residual priority risk)
The source-specific Gaussian mixture and Bessel-\(K\) law are already in Biroli et al. (2022), Eqs. (4)–(5), and conditional backward reset ages already in Masó-Puigdellosas et al. (2022). The general \(\tfrac12\log N\) Bayesian information growth is also prior work, notably Clarke and Barron (1990). The assessed contribution is the exact hidden-age entropy observable, its strict population monotonicity and the first **positive** finite-population coefficient \(2/(3N)\). Relevant public hidden-common-environment results discuss different latent variables and do not visibly give that coefficient. Nonetheless the full scope of generic Gaussian-scale-mixture and Bayesian second-order expansions is not exhausted; independent publication-priority review is still needed.

## Mathematical value (PASS)
How well a single snapshot reconstructs the unobserved common reset clock is an intrinsic information invariant of the correlated Brownian gas; it differs from the already computed squared-position covariances. The finite-size coefficient quantifies a precise correction to the universal log-information law, and the exact integral is a reproducible benchmark for synchrony inference and hidden-age statistics. No downstream theorem or empirical measurement claim is presumed.

## Scientific limits
Free scalar Brownian coordinates; complete synchronous Poisson resets; perfect simultaneous observation. The statement does not extend without analysis to independently reset coordinates, imperfect detection or nonexponential clocks. The second-order remainder is asymptotic. Priority is qualified by implicit general-information-theory coverage. There has been no independent audit.

Self-review: passed. Independent audit: not yet performed.
