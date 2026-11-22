# Self-review

## Correctness: PASS
With independent all-or-nothing sample viability, the two-taxon union-detection probability is the expectation of \((1-e^{-\lambda S})^2\). For two positive unequal efforts, fixing their total reduces the varying objective to a strictly convex quadratic in the sum of their exponential survival factors; at least one of equalizing the pair or setting one effort to zero is strictly superior. This proves the all-global-optimizers equal-active form. The exact factorization of the three-sample score difference and the strictly positive rationally bounded third-versus-second score gap prove the discontinuous support transition. All essential arithmetic identities were checked from the standalone package; exhaustive global optimality comes from the proof, not numerical experiments.

## Originality: PASS on inspected evidence
The 2024 biological-replication paper is empirical and studies different procedures; the 2016 stochastic ecological survey model primarily evaluates single-target detection, and the 2013 identical-sigmoid knapsack corollary covers separable additive utilities, not the cross-sample coupled event of jointly detecting both taxa. Research-record comparisons included separately reported independent-Hill activation staircases and survey-visit optimization; neither contains this statement or a stronger result shown to imply it. Exact coverage by a broad theorem for nonseparable stochastic optimization was not established, so the priority assessment is provisional, not a claim of exhaustive literature absence.

## Value: PASS
Replication versus concentration is a motivated ecological monitoring-design choice, and union-based detection of both taxa is a natural alternative to expected richness or one-taxon detection. The finite reduction avoids nonconvex continuous search, while the exact one-to-three jump shows that intermediate replication counts can be inefficient even without per-bottle overhead. This is more than a routine restatement of the identical-separable-utility theorem because its coupled objective admits a different support transition.

## Closest literature and scientific boundaries
Courtaillac et al. (2024), Moore and McCarthy (2016), and Srivastava and Bullo (2013) provide the most directly inspected empirical and mathematical context. Older stochastic allocation and nonseparable utility theory remain possible undiscovered priority risks. Equal rates, fixed known viability, independent sample processing and absence of fixed costs limit the claim; no validation on real water samples has been attempted.

Self-review: passed. Independent audit: not yet performed.
