# Self-review of finite-horizon star-walk variation

## Correctness — PASS

The gradient-space matrix is exactly \(lpha(I-Q)+(2lpha-1)Q\), with \(Q\) a rank-one projection. Its powers and induced column sums prove the formula for all dimensions and horizons, including boundary and sign cases. Splitting the optimization at the branch intersection and differentiating its convex active branch proves the unique parity-dependent parameter in each case. The actual standalone checker ran without error: 4,368 exact direct-iteration/column comparisons, 2,050 signed-input inequalities, 3,150 exact even-step scalar identities, and 300,300 numerical odd-optimum comparisons. Finite experiments are not the infinite proof.

## Originality — PASS (bounded primary comparison)

The closest posted published-finding corpus one-step biclique theorem, dated 2026-11-02, has the same type of graph-edge variation and a one-step optimal holding parameter, but assumes both bipartition sizes at least two; an algebraic extension captures the star one-step value, which is not asserted as a new isolated theorem. A posted finite-horizon directed-triangle result concerns distributional total-variation distance, not variation of real signals; a weighted-tree heat result concerns continuous time rather than powers with an optimized hold probability. The full source text of Kolmogorov–Pock–Rolinek (2015) treats edge-variation denoising, while Sandryhaila–Moura (2013) use another definition of graph variation, and Boyd–Diaconis–Xiao (2003) optimize spectral mixing for a different transition class. None of the inspected claims implies the complete odd/even horizon optimization on stars. Residual risk: an earlier unindexed rank-one computation could coincide with the result.

## Value — PASS

The theorem determines a natural complete family of fixed-horizon nonlinear-norm optimization problems in closed form, identifies the exact four-leaf onset of an interior odd-step optimum, and gives an unexpectedly dimension-independent exact scalar contraction at every even step. The combined results are structural stability-design information beyond a routine one-step matrix norm and beyond asymptotic spectral tuning.

## Limits

The theorem concerns finite unweighted stars, real signals, homogeneous time-independent holding probability, and unweighted edge-sum total variation. It makes no claim of optimality among arbitrary Markov matrices, variable schedules or other variation norms. Self-review is not an independent scientific validation.

Self-review: passed. Independent audit: not yet performed.
