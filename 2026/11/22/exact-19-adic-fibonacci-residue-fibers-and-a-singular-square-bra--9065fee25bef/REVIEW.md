# Self-review

## Correctness — PASS

The base matrix identity \(A^{18}=I+19B\) and the nonvanishing reduction of \(B\) establish exactly the matrix order \(18\cdot19^{k-1}\). For each of seventeen regular index classes, the nonzero first analytic derivative modulo \(19\) makes the index-to-value function a bijection onto a full \(19\)-adic residue ball. Their counts reproduce the explicit unweighted baseline \(w\). For the sole critical index class, the Lucas trace is an isometric coordinate. The identity \(5F_n^2=4+L_n^2\) at odd indices and a second isometric coordinate put its values in the exact form \(c+(19^2c/8)x^2\). This proves the targetwise quadratic-root counts at every power, and their maximum follows from the complete valuation classification of squares. The standard-library checker directly enumerates whole least periods for \(k=1,2,3,4\) and matches all target fibers, attained sizes, and extrema. A finite checker does not establish the universal result; the mathematical interpolation and bijection arguments do.

## Originality — PASS on inspected literature

Bragman–Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime* (arXiv:2202.00704, first public 2022-02-01), already provides the \(19\)-adic image counts, density \(441/760\), and general regular/singular image argument. It is therefore not novel to compute the density or image sizes here. In the inspected Abstract, Example 3, Section 5, Propositions 23, 24, 27 and Lemma 26, no corresponding targetwise finite-period multiplicity table or exact growing maximal fiber was stated. Rowland–Yassawi (arXiv:1602.00176, introductory material and Theorem 20) gives the interpolation mechanism and a different prime example. Bundschuh and Bundschuh (2011) previously determined complete Fibonacci and Lucas prime-power fiber frequencies at prime 3, not prime 19. The accessible Somer (1990) abstract concerns recurrence distributions modulo a prime, not necessarily all prime powers; the full text was not available, leaving residual coverage risk. Published mathematical summaries on other prime-adic recurrence fibers and earlier claim records were checked for implication, not merely title similarity. No stronger theorem demonstrably implies the new full fiber law without an additional derivation. Unindexed results or unstated implicit consequences may still affect priority.

## Value — PASS

The image of Fibonacci numbers modulo prime powers is already known quantitatively, but image size alone does not answer how many indices represent a given reachable residue. The exact fiber law distinguishes seventeen regular branches from one singular quadratic critical branch, explains why the maximum representation multiplicity grows without bound, and specifies every target's weight. This is a natural and nontrivial refinement of established \(19\)-adic image-density research, not a recomputation of image counts or an arbitrary finite slice.

## Risks and limits

The priority risk is a possible implicit target-fiber formula in earlier general interpolation literature or in inaccessible recurrence-distribution texts. The proof concerns prime \(19\) alone, and no independent human or external mathematical audit has taken place.

Self-review: passed. Independent audit: not yet performed.
