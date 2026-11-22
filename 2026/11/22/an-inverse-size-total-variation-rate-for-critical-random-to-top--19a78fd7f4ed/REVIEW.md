# Scientific review: inverse-size fixed-point approximation

## Correctness — PASS
The shuffle model is specified by uniform label-selection with replacement from the identity, with exactly \(\lfloor cn\rfloor\) moves for fixed \(c>0\). The proof uses an exact conditional selected-prefix representation, a uniform factorial-moment Poisson inequality for partial injections, a stepwise geometric survival coupling, and an \(\ell^1\)-Taylor expansion of the Poisson–geometric family. The occupancy parameter fluctuates on the \(n^{-1/2}\) scale, but the *averaged signed* linear term depends only on the \(O(n^{-1})\) bias of the occupancy mean, yielding the claimed rate. All edge events, including full selection, are accounted for. The checker separately reconstructs finite conditional and full shuffle laws; those finite checks corroborate but do not replace the proof.

## Originality — PASS subject to residual historical risk
Clay's *On the statistics of random-to-top shuffles* (arXiv:2603.09008v1; first public 2026-03-09) establishes the same Poisson–geometric weak limit and in Section 8 specifically calls for convergence rates. Its exact finite-prefix decomposition is credited. The closely relevant published joint fixed-point/descents result, *Four-way rare–Gaussian factorization and a hidden covariance in random-to-top shuffling*, was examined at full statement-and-proof level: it establishes factorized weak convergence but explicitly does not give a quantitative rate. Another published random-to-top descent/inversion result has different observables. The available descriptions of older Pehlivan and Diaconis–Fill–Pitman works do not assert the inverse-size fixed-point-statistic bound. The record does not exclude unindexed general theorems or a result implicit in an inaccessible thesis; independent historical verification remains necessary.

## Value — PASS
A quantitative total-variation version of a nontrivial critical-window limit is a natural and explicitly identified research question. The inverse-size bound is materially stronger than the weak limit and stronger than a naive \(n^{-1/2}\) parameter-stability estimate; its cancellation mechanism can help guide quantitative analysis of mixtures of occupancy-driven discrete laws. The result is not presented as a sharp asymptotic constant or an all-regimes theory.

## Verification and limits
The exact-data checker in `checks/verify.py` completed 1,712 assertions including full small-shuffle histories, exact partial-injection combinatorics, and numerical total-variation comparisons. The analytic proof covers all sufficiently large dimensions for every fixed positive shuffle ratio, beyond those tests. Primary-paper comparisons were based on inspected mathematical statements; historical originality is not independently certified.

Self-review: passed. Independent audit: not yet performed.
