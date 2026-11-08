# Review of the exact deterministic-core phase diagram

## Correctness — PASS
The theorem is proved for each real \(1/2\leq\delta\leq2/3\), not extrapolated from numerics. Exact substitution gives the four return branches and their continuous boundaries. The gap-normalizing affine change produces a fixed universal map, so its decreasing orbits converge to zero and the fixed outside region is exhaustive. Pointwise convergence plus bounded convergence and the half-interval exchange classify **all** invariant probabilities. Separate inverse-branch length calculations yield the normalized physical basin \(4-6\delta\); the degenerate upper endpoint has only two-point empirical basins. The geometric-prefix formula follows from exact expansion thresholds. The standard-library checker separately passed 9365 finite rational checks; infinite assertions follow from proof.

## Originality — PASS within inspected literature
Nakamura–Nakano–Toyokawa–Yano, *Arcsine law for random dynamics with a core* (arXiv:2206.00226, §1.2.3, (1.7)), defines the identical family and proves a unique attracting core cycle for \(\delta=1/2\). It does not give the intermediate-parameter invariant simplex, physical basin, or geometric transient law. Their Theorem 1.2 concerns the annealed arcsine law and does not logically entail the present deterministic-core physical measure classification. Gharaei–Homburg (arXiv:1611.07248) studies broader random interval diffeomorphisms. The Hata–Yano 2021 map and its 2022 generalization are different parameter families. Indexed comparisons were made for equivalent maps, stronger results, tables, and implication coverage. Residual risk: an equivalent, elementary reduction may be in unindexed literature, and the 2021 Hata–Yano manuscript was only inspected at abstract level.

## Mathematical value — PASS
The source explicitly motivates core invariant measures and considers the δ=1/2 case. Here the entire natural parameter interval exhibits two distinct qualitative transitions: unique invariant measure to continuum of ergodic two-cycles immediately after \(1/2\), and positive-to-zero physical basin at \(2/3\). An exact linear physical basin probability and parameter-independent geometric expanding-prefix law quantify the transition, making the result useful to the analysis of coexistence between invariant and observable dynamics. This does not purport to solve stationary measures of the original random system.

## Limits of this assessment
No independent mathematical audit has been performed. The return-map formulas and invariant-measure proof remain open to independent checking; priority among unindexed notes remains a residual risk. This review does not assess the originally random system's invariant statistics.

Self-review: passed. Independent audit: not yet performed.
