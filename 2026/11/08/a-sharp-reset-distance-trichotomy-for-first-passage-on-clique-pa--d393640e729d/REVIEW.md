# Scientific review: reset-distance trichotomy

## Correctness: PASS
The transient-generator backward equations yield the exact target transform, the ordinary exponential-restart renewal formula yields the MFPT, and explicit binomial polynomials make the global rate derivative fully positive for path length at least three. At lengths one and two the functions and their exact optima follow by elementary differentiation. The coefficient argument is uniform for all integer clique sizes and path lengths and every nonnegative real reset rate. Full-state rational linear algebra independently matches 280 instances, supplementing rather than substituting for the infinite-parameter proof.

## Originality: PASS on inspected material
The starting restart renewal identity is not original; it is explicitly attributed to the classical literature. The strongest same-graph comparison is Zelenkovski et al. (2023), which treats lollipop structures using degree-normalized discrete-time transitions, resetting probabilities and all-target averaged statistics, not a single pendant-endpoint mean under unit-rate-per-edge continuous time. Riascos et al. (2019/2020) additionally introduce spectral network-resetting methods and the continuous-time version of a degree-normalized kernel; Förster et al. (2021) establish non-reset first-passage reductions for necklace structures. Neither material states the particular all-length optimization law. Pal–Reuveni's general restart identity permits computing this case but does not itself state the sharp three-way global minimizer classification. Riascos et al. study discrete-time graph walks. Current indexed mathematical searches and available primary sources did not disclose this precise joint claim. This is best-knowledge originality, not exhaustive priority certification; implicit coverage in an unindexed derivation remains a residual risk.

## Mathematical value: PASS
A clique acts as a natural excursion trap, and the terminal path distance measures the cost of losing partial progress on reset. The result reveals an unexpectedly strict threshold at path length three, independent of arbitrarily large trap size, and a nontrivial optimizer with a quantifiable saving at length two. This resolves a physically motivated finite-network first-passage control problem in a complete infinite parameter family, not merely one computed graph.

## Scope and limitations
The process has rate one on every incident edge, not a normalized total jump rate, and resets only to the gateway. No prediction is claimed about network-averaged first-passage time, total-variation mixing, non-Poisson restart, or other targets. The analytical proof is separate from finite checks. The scientific priority of the classification has not been independently validated; an equivalent specialization of a broader inaccessible result remains possible.

Self-review: passed. Independent audit: not yet performed.
