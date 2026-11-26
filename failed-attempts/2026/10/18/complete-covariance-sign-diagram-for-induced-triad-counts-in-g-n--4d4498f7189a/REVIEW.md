# Independent mathematical audit

## correctness

PASS

The strict model is undirected independent-edge G(n,p), with unordered triples and induced edge counts. At identical triples the indicator covariance is δ_ij q_i−q_i q_j. Only distinct triples sharing two vertices can contribute otherwise. Given the shared edge the two pairs of remaining edges are independent; the conditional mean difference is d_j=q'_j(p)/3 from the Bernoulli binomial mass. Each first triple has 3(n−3) ordered partners of this kind, giving the asserted exact matrix. Off diagonal the sign is that of (n−3)(i−3p)(j−3p)−3p(1−p). Its linear factors after removing positive p or 1−p give the four stated single thresholds; the empty/triangle expression is −3Dp(1−p), and the one-/two-edge polynomial is 3Dp²−3Dp+2(n−3). For n≥4, 1/9<n/(3D)<1, so both roots are interior and straddle 1/3 and 2/3. At n=3, competition on the sole triple makes all mixed covariances negative. The phrase ‘negative dependence’ is supported here only as negative covariance, not a stronger association assertion. Exact independent check: python3 /workspace/reproductions/frozen_checks.py 4 enumerates 8,64,1024 labeled graphs for n=3,4,5, verifies complete matrices at selected rational p, tests rational zeros and signs including both positive tails and the negative center for the (1,2) pair. This bounded check is not a proof of the irrational thresholds or unbounded parameter claims.

## originality

FAIL

Reinert–Röllin, arXiv:0912.3425, Eq. (5.1), gives the exact finite-n,p covariance in the same model for a basis of the induced triad census after linear scaling. The invertible affine recoding on the fixed-sum census hyperplane gives the whole frozen matrix. The sign regions are mechanical factorizations of that prior matrix, including the reentrant pair. Independently, indexed record 549b3a6afdfa explicitly gives the (2,3) row and its threshold. The failure is demonstrated implication, not an assertion that all six thresholds were previously printed together.

## value

FAIL

The clear sign presentation and conditioning proof are useful exposition, but the entire finite matrix already exists in an equivalent basis and each sign has a routine polynomial check. The most plausible narrowed result, the two-tail (1,2) crossover, is directly forced by the published quadratic after the fixed recoding, as shown above. No nonmechanical precise invariant survives as a justified repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
