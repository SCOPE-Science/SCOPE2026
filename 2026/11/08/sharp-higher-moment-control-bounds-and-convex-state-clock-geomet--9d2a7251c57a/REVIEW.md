# Scientific review

## Correctness — PASS

The claim is proved in five logically separate steps. Almost-sure finite absorption guarantees an invertible transient generator, entrywise nonnegative Green matrix, finite positive moments and the exact \(m!G^m\) representation. A common-source rate multiplier makes a single matrix row affine, forcing every positive Green entry to be a ratio of nonnegative affine polynomials on the whole positive axis, and giving entrywise elasticities in \(\([-1,1]\)\). Positivity of the moment path expansion yields the sharp \(\([-m,m]\)\) bound; global time change yields the \(-m\) budget. Explicit one- and two-state examples prove negative and positive sharpness. Independent state-clock scaling produces a finite positive exponential sum whose log Hessian is a covariance matrix. Exact symbolic sharpness checks and independent finite-network derivative/integral checks passed. No extrapolation from finite tests is needed for the general proof.

## Originality — PASS, qualified

The 2026 Liang–Bao mean first-passage paper supplies the \(\(m=1\)\) edge unit bound and scale identity and, in its Discussion, explicitly calls extension of the local bound to higher moments an open question. Nam–Gunawardena (2025, 2026) already give algebraic formulas for *all* moment orders; Caswell (2011) already gives general moment elasticity calculus. Thus originality is confined to the sharp, universal, network-independent \(m\)-order local bound, its exact sharpness, finite factor consequences, and the joint state-clock covariance Hessian. Comparisons used the motivating paper's main text, discussion and appendix, Nam–Gunawardena's complete open article and selected theorem/appendix sections of its 2026 extension, a set of actual semantic-index queries, and accessible earlier claim statements. No direct stronger or equivalent coverage was identified. The Caswell full text was inaccessible and may contain a related special result, so publication priority is qualified, not certified.

## Value — PASS

The recent mean-response theorem explicitly raises higher-moment bounds as an unsolved structural question. Moments of order \(m\ge2\) quantify rare, long completion trajectories relevant to stochastic kinetic reliability, not just mean throughput. The result proves a rate-independent upper limit for how much one kinetic control can alter them, supplies matching examples of speeding and delaying, and provides a global convex design geometry when all state clocks are tuned. These are architectural constraints, not merely recomputations of a particular network or a minor numerical improvement.

## Closest literature and limits

Liang–Bao (arXiv:2608.06368, first posted 2026-08-06) covers the mean unit bound; Nam–Gunawardena (DOI 10.1007/s11538-025-01524-z and arXiv:2608.08375) covers positive algebraic moment formulas; Caswell (DOI 10.1002/nla.791) covers derivative/elasticity calculus. The complete Caswell paper could not be inspected; its abstract was read, and this remains a priority risk. Only integer raw moments, finite absorbing Markov networks, single-source rate groups, and state-clock logarithmic convexity are asserted. Arbitrary multi-source controls and semi-Markov systems remain outside scope.

Self-review: passed. Independent audit: not yet performed.
