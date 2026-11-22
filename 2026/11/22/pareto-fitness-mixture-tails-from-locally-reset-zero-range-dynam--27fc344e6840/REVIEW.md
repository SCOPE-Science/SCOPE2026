# Self-review of a critical fitness-mixture tail law

## Correctness (PASS)

The claim is confined to a precise order of limits. The single-site, time-since-reset negative-binomial generating function gives the independent-site product limit without invoking numerical fitting. The critical high-fitness scaling is an ordinary dominated-convergence limit of a positive Laplace integral, and the full Pareto coefficient is obtained by changing variables in the uniformly sampled fitness integral. Uniform moments are bounded through explicitly nonnegative factorial cumulants. An exact layer-cake identity proves the asserted moment frontier. The checker independently evaluates the exponential-integral identity, compares the prelimit transform with its limiting transform, and verifies the first three scaling moments. Numerical checks do not substitute for the infinite proof.

## Originality (PASS, with explicit access risk)

The 2023 preprint by Grange, *Local resetting in non-conserving zero-range processes with extensive rates* (arXiv:2311.12414), was read in its publicly accessible HTML representation, including model dynamics, equations (25), (31), (41), (44), condensation Section 5.2, and discussion. It establishes the kinetic generating function and a mean-density condensation transition, but not the uniform-fitness mixed-occupation Pareto law or the universal high-fitness rescaling distribution. The older Grange global-reset work (arXiv:1910.05991) has a different common-reset process. A published 2026 same-model result, *A hidden co-occupation threshold below fitness condensation* (published-finding corpus ID 2026/11/8/SCOPE-a-hidden-co-occupation-threshold-below-fitness-condensation--b88c55090541), provides the closest known overlap: a pair-crowding moment threshold at \(\nu=1/2\). Its accessible indexed summary reports a finite/critical/divergent second-factorial-moment result, not the distributional Pareto theorem. The full text could not be accessed, so full-document exclusion is **not** asserted; that is the leading residual publication-priority risk. The present tail claim neither identifies within-site pair counts with total-level occupancy nor treats a previously known variance threshold alone as novelty.

## Mathematical value (PASS)

The fitness distribution is a natural observable in selection/mutation and network-degree interpretations of this model. While the mean population density remains finite for all \(0<\nu<1\), a randomly chosen fitness level has an exact heavy-tailed *full population distribution*, with a universal, explicitly transformed high-fitness scaling law and sharp nontrivial prefactors. For example, the levels' total occupancy has exact survival prefactor \(3/C^2\) when \(\nu=1/2\), reflecting cross-microstate fluctuations absent from a single-site co-occupation statistic. The claim predicts all positive-moment thresholds and the strength of rare, high-fitness load events. It is not a mere recomputation of the previously known mean or a single extra low-order moment.

## Limits and closest literature

This is not a finite-network theorem at the exactly critical maximal-fitness site, and it uses a uniform distribution over *levels* rather than over microstates or particles. The close 2026 same-model full text was inaccessible; only its indexed summary was available. Other unindexed equivalent tail results remain possible. The exact source-date and domain of the older motivating paper have been recorded.

Self-review: passed. Independent audit: not yet performed.
