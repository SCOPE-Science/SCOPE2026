# Review of finite-memory convergence under Bernoulli interpolation

## Correctness — PASS

The result treats the exact current-gradient, previous-sample-difference accumulator of the published AdaGrad-Diff algorithm. For an arbitrary nonnegative bounded scalar curvature sequence, eventual smallness of normalized steps (under the temporary assumption of divergent variation) gives a telescoping descent bound for squared gradients divided by the increasing weight. An elementary square-root summation contradiction proves that the variation accumulator must actually be finite, with no probabilistic input. On the Bernoulli model, infinitely many zero-to-active transitions rule out a limiting weight at or below the two-step stability barrier along any nonzero trajectory. Active steps then have a uniform strict contraction; the strong law yields exponential convergence, finite squared gradients, and the exact log rate, including its possible negative-infinity case. The event intersection is legitimate in finite dimension. The script checks rational identities and finite sample paths, but these computations are not the proof.

Risks and boundaries: no convergence or rate is claimed for general bounded nonnegative curvature paths without recurring active observations. In particular, the pathwise finite-variation lemma alone is not asserted to force minimizer convergence. Exact stochastic rates may not control moments of convergence times or expected errors.

## Originality — PASS, subject to independent historical verification

The primary source, Bojović–Salzo–Pontil, arXiv:2602.13112, Algorithm 3.6 and its deterministic and stochastic convergence results, explicitly distinguishes deterministic squared-difference summability from the stochastic interpolation question left open in its concluding future-work discussion. This result proves finite variation, unrestricted-step almost-sure convergence and an exact rate for a narrow but genuinely stochastic subclass (independent Bernoulli-zero or positive sample curvatures on a separable strongly convex quadratic). Their deterministic theorem does not imply the result, because the sampled gradient changes when the iterate does not.

Rodomanov–Jiang–Stich, arXiv:2406.06398, develops a variation-adaptive stochastic method under a finite feasible-diameter assumption and establishes expected optimization bounds, not the unconstrained Bernoulli pathwise claim. Ward–Wu–Bottou, arXiv:1806.01811, concerns AdaGrad-Norm accumulating gradient magnitudes, a different update. Related published records involving momentum/friction or plain SGD have a different state and cannot imply a statement about this cumulative-difference metric without a new reduction. No identity, duality or stronger known theorem was identified in the inspected sources; this is not a claim of exhaustive literature coverage.

Residual risks: older specialized results for one-dimensional adaptive stochastic recursions, or later versions of the direct preprint, may contain a covering corollary not found in the material examined. Independent literature priority verification remains required.

## Value — PASS

The paper explicitly highlights unresolved squared-gradient-difference summability under stochastic interpolation and its importance for iterate convergence. This theorem supplies a nontrivial positive test case with arbitrary base step, no bounded domain, multiplicative stochastic gradient noise and an exact random rate. Its deterministic bounded-nonnegative-curvature lemma explains why variation accumulation self-limits, and its Bernoulli argument explains how random recurrence forces the terminal weight into the ordinary stability interval. This informs which structural properties may support more general stochastic analyses, rather than providing a routine fixed-step quadratic computation.

The result does not solve the full stochastic interpolation problem, characterize nonseparable objectives, or give uniform stochastic complexity bounds.

Self-review: passed. Independent audit: not yet performed.
