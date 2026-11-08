# Scientific review

## Correctness — PASS

The estimator is the exact Gaussian likelihood-ratio form of one draw per independent probability stratum. Independence gives the cellwise variance identity. The unit-interval piecewise-constant projection limit, proved from a smooth Taylor argument and the Poincare inequality with density, turns the question into a precise \(L^2\)-derivative condition. Gaussian integrals show the \(s=1/2\) raw second-moment boundary, the \(s=3/2\) derivative-energy boundary, and the exact finite coefficient. The derivative of that coefficient factors through a cubic with exactly one root above the boundary. The ordinary importance-sampling comparison is calculated from a separate Gaussian fourth-moment integral. Actual symbolic and quadrature checks in `check.py` and `check_output.txt` support but do not replace these proofs.

## Originality — PASS, with precedence risk

The closest primary literature is He–Zheng–Wang (2022, arXiv:2203.03220), which supplies covariance-dependent randomized QMC error-rate bounds, and Chopin–Gerber (2022, arXiv:2210.01554), which develops higher-order stratification and reviews the classical smooth-integrand rates. Their general results motivate the object and cover background rate mechanisms; neither inspected text identifies the exact \(s=3/2\) transition and algebraic optimizing proposal variance \(s_*=3.77107268073615\ldots\) for the independent-stratum quadratic Gaussian problem or its contrast with the ordinary MC optimum \(s=3\). He–Wang–Wang (2024, arXiv:2403.11374) addresses shifted lattice integration for Bayesian inverse problems rather than independent equal-probability Gaussian strata. Broad historical importance-stratification literature, including Glasserman et al. (1999), is more general in application but primarily optimizes drift and stratification direction, rather than the centered Gaussian variance here. Its full text was not accessible in this check; this and any unlocated specialist computation remain precedence risks. A generic Sobolev projection theorem by itself is not presented as novel; the substantive design optimization and full variance classification constitute the assessed contribution.

## Value — PASS

Gaussian importance proposals are often selected by the ordinary Monte Carlo variance criterion. This exact, entirely specified benchmark proves that criterion does not minimize the asymptotic error of independent stratified inverse-CDF quadrature. It identifies both a sharp smoothness threshold for the \(N^{-3}\) variance scale and the unique Gaussian variance achieving the lowest coefficient (9.56% lower than the ordinary-MC optimum coefficient). The conclusion concerns a known quadratic Gaussian moment and does not claim to compute an otherwise unknown integral or improve unrestricted algorithms.

## Remaining scientific limitations

Only fixed proposal scale and this particular one-dimensional integrand and randomization are covered. The publication-precedence comparison is not a certification of uniqueness across all literature. Numerical comparisons near the Sobolev threshold converge very slowly; the threshold and uniqueness rely on analytic arguments rather than those finite checks.

Self-review: passed. Independent audit: not yet performed.
