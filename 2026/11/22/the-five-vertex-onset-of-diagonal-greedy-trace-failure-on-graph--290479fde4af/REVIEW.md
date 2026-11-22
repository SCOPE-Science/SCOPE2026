# Self-review

## Correctness — PASS

The exact Schur-complement formula follows from a positive-definite \(I+L_G\) and the inverse of its two-by-two selected block. The finite statement quantifies over **all** graphs of the stated sizes and **all** greedy tie outcomes. The bundled Python 3 standard-library certificate exhausts every bit mask for \(n=2,3,4,5\), checks graph connectivity exactly and uses `Fraction` arithmetic for every inversion, pivot comparison and trace objective. The counts are \(1,4,38,728\) connected labelled graphs and \(0,0,0,60\) all-choice greedy failures. Every failing graph is checked explicitly for isomorphism to the diamond-with-leaf witness. Direct rational witness calculations agree with \(37/39\), \(22/23\), \(7/897\), and \(858/851\). Logical limits: no claim for more than five vertices, arbitrary weights, or arbitrary regularization.

## Originality — PASS, with publication-priority uncertainty

published-finding corpus semantic searches targeted the Green kernel \((I+L_G)^{-1}\), smallest graph size, greedy two-column Cholesky selection, trace/V-optimality and the diamond-with-leaf obstruction. The closest retrieved work concerned general pivoted Cholesky failure, general graph V-optimality greedy bounds, other graph landmark problems, or an exponential-covariance two-pivot penalty. Those claims neither imply an exact five-vertex lower bound nor identify the sole exceptional graph class. Primary full text was consulted for Ma–Garnett–Schneider (2012), Liu–Matthies (2015), and Chen–Epperly–Tropp–Webber (2024); the preprint text of Harbrecht–Peters–Schneider (2012) was also inspected. The primary conceptual distinction is true marginal-trace greedy versus residual-diagonal pivoting. Publication databases cannot establish absolute nonexistence of an unindexed equivalent result.

## Value — PASS

The question compares the two most natural low-cost vertex-selection rules for a graph-Gaussian Green kernel under a fixed two-observation budget. The theorem provides a sharp topology-level lower cutoff and unique minimal obstruction, with a full finite classification and a reproducible exact-rational test, not a single arbitrarily selected small matrix. This makes an unambiguous minimal regression test for implementations that substitute conditional variance for integrated trace-risk marginal gain. The additive loss in the witness is small, and the result does not assert large-scale approximation consequences.

## Closest literature and residual risks

The general Cholesky theory already warns that diagonal pivoting need not minimize trace error, so the novel content is exclusively the exact minimal connected graph order and isomorphism classification for the specified graph Green kernel. The Gaussian-random-field work studies a different greedy objective. Residual risks include inaccessible or unindexed historical graph-landmark examples and possible nomenclature differences (V-optimality, Nyström landmarks, graph Green kernel, uncertainty sampling).

Self-review: passed. Independent audit: not yet performed.
