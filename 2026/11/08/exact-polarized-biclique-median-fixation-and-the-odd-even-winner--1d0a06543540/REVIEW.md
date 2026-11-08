# Scientific review

## Correctness — PASS

The claimed law uses weak-half thresholds, not strict-majority thresholds, because the nearest-current-opinion tie convention immediately prevents further favorable conversions in the opposing camp. The proof verifies the pre-threshold monotone state, the post-threshold absorbing basin, a.s. finite completion, exact continuous-time clock coupling, exponential-order-statistic density and integral, exact finite-rate sum, and uniform-permutation count. The parity inequalities follow from a beta-density reflection argument; rate calibration follows from the positive-support ratio of independent order statistics. All parameters are quantified over positive camp sizes and positive rates. Independent labeled-vertex state exploration plus exact rational formulas verify 196 finite cases and 72 labelled chains without substituting for the general proof.

## Originality — PASS (with residual priority uncertainty)

The original 2019 full HTML article (including appended supplementary sections) defines the nearest-current-median rule and studies simulated consensus frequency on randomized networks. The 2022 full HTML article including appendices establishes general qualitative convergence/equilibrium criteria, not the polarized complete-bipartite winner probabilities or the mixed-parity sign law. The 2024 continuous-time median-inertia paper uses continuous relaxation, not instantaneous stochastic binary imitation. The 2008 heterogeneous-network voter model instead copies randomly sampled neighbors, making its fixation law mathematically inapplicable here. A 2023 asynchronous majority paper introduces initial private signals and initially unannounced public opinions, unlike the fully announced polarized initial condition here. Independent mathematical research searches and recoverable earlier-claim comparisons found no covering statement. The generic order-statistic identities themselves are classical, so their mere appearance is not the claimed contribution. A missed unindexed graph-specific special case remains possible.

## Value — PASS

Uniform-size opposite camps are a natural adversarial starting condition for opinion cascades, yet qualitative consensus theorems alone do not determine which camp prevails. This result supplies an exact finite-population probability and a sharp structural parity rule for every pair of camp sizes, not just a numerical instance. Contrary to size-based intuition, any even-sized camp beats any odd-sized opposing camp under equal individual activity, while two odd-sized camps are exactly fair even at greatly unequal sizes. The exact \((2,3)\) example requires halving one camp's rate to restore fairness. These are mathematically motivated finite-size social-influence benchmarks and a nontrivial boundary effect caused by the tie rule, not arbitrary parameter substitution.

## Closest literature and limits

Model source: arXiv:1909.06474 (2019); structural convergence: arXiv:2212.08808 (2022); related but different mechanisms: arXiv:2404.16318 (continuous median inertia), Sood–Antal–Redner (random-neighbor voter), arXiv:2309.04691 (initially unannounced majority). Current proof covers only complete bipartite, internally uniform and fully polarized binary camps with per-camp homogeneous independent clocks and tie retention. Search cannot establish uniqueness across all unindexed literature; the noted source comparison remains the main priority uncertainty. The finite verifier is not an infinite formal proof.

Self-review: passed. Independent audit: not yet performed.
