# Self-review

## Correctness — PASS

The singleton event requires a retained vertex, a deleted older parent, and no subsequently retained children. Formula (4) follows from independent parent choices, including the separately treated root. The exact multi-mark probability (7) conditions only on genuinely independent retention indicators and independent parent choices. On the scaling window, a logarithmic product comparison gives (10), and independent tilted Bernoulli variables give the conditional deleted-parent fraction \(1-p\), with an explicit \(O(b_n^{-1/2})\) error. Hence the fixed-order marked joint probabilities factorize uniformly; mixed factorial moments and a boundary-first-moment estimate prove the Poisson point process and Weibull/Gamma age limits. The proof treats all fixed \(0<p<1\) and the correct root boundary. The supplied standard-library verifier passed 544 exact and large-size finite comparisons, not used as an infinite proof.

## Originality — PASS, qualified

Kalay–Ben-Naim (arXiv:1409.7106, archival starting point) studies fragmentation/component counts, Gu–Yuan (arXiv:2408.12515) studies the iid-site component-size profile, and the published oldest-leaf point process has a different event and \(\sqrt n\) scale. Those statements and their implications do not supply the retained-singleton birth-label process or its Weibull first arrival. Relevant original full texts and the closest public mathematical note were examined, with statement-level comparisons. Residual risk: a broader, unlocated theorem on marked Bernoulli recursive trees could cover this as a special case; literature search is not proof of universal novelty.

## Value — PASS

A positive fraction of all late-born vertices may be retained singletons, yet the *first* such vertex has an anomalous, parameter-dependent sublinear birth scale. The complete rare-age point process and first-rank Weibull law quantify when fragmentation first leaves a surviving component of size one, not only its eventual density. The exact marked-parent coupling and age-scaling identify a structural phenomenon relevant to sequential random environments; this is more than a global-count recalculation or single-point moment exercise.

## Scope and remaining risks

No extension to fixed-count deletion, edge percolation, dynamic retention, other component sizes, or parameter-uniform limits is claimed. The critical joint factorization is proved asymptotically rather than tested on arbitrarily large finite trees. Historical-priority risk remains as described, and no independent mathematical audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
