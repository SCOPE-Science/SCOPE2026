# Scientific review: sharp chi-law for nearly uniform spherical one-design weights

## Correctness

**PASS.** The minimax relative-weight problem is an exact finite-dimensional \(\ell_\infty\) interpolation problem. Full affine rank of independent spherical nodes gives a finite attained optimum. Standard finite-dimensional norm duality yields the exact quotient \(\max_{\|u\|=1}|u\cdot S_m|/\min_a\sum_i|a+u\cdot X_i|\). A compact Lipschitz class and finite-net strong law establish uniform denominator convergence to the strictly positive spherical first absolute moment \(c_d\). The multivariate central limit theorem and a uniform quotient squeeze prove the chi-law. For the circle, the Rayleigh survival formula gives the stated coefficient \(4/\pi^2\). Positivity follows at every box radius strictly below one; the statement does not mistakenly assume positive weights when the unconstrained optimum is larger. The supplementary numerical checker passes 72 direct primal-dual comparisons. The probabilistic conclusion is analytical, not inferred from the checker.

## Originality

**PASS, qualified by residual historical-priority uncertainty.** The motivating arXiv:2610.32699v1 proves a general positive box-feasibility *sufficient* condition for random nodes, including spherical designs (Theorem 1.1, Remark 2.6, Corollary 2.13); it neither calculates the minimum feasible random box width nor gives the limiting \(\chi_d\) calibration law. arXiv:2609.09506 considers a different least-squares weight rule, while arXiv:1502.03562 considers near-equal spherical designs using geometrically controlled nodes. Fu–Wang–Yan's minimax projection constant supplies \(c_d\), not the random moment-correcting weight distribution; Wendel's convex-hull probability controls unrestricted nonnegative weights, not their maximal deviation from uniform. Targeted published-claim and mathematical-literature searches found no covering statement. The finite-dimensional LP-dual approach is standard, and an unindexed statistical-calibration theorem might imply this specialization; such priority remains unverified.

## Value

**PASS.** A recent general existence theorem leaves a natural, algorithmically meaningful design parameter uncalibrated: the *smallest* relative change from equal weights needed to make sampled nodes integrate constants and first harmonics exactly. The theorem gives both the exact finite-sample optimization dual and a sharp confidence-versus-tolerance frontier at its natural square-root scale, with an explicit circular probability \(1-e^{-4t^2/\pi^2}\). This resolves a nontrivial probability question for the simplest spherical design instead of merely improving a routine constant. It also distinguishes eventual unrestricted convex-hull feasibility from the much more stringent near-uniform calibration requirement.

## Closest literature and limits

The relevant full-text comparisons are Neumayer–Schäfer–Ullrich (2026) and Bělík–Narayan–Turnage (2026), plus Zhou–Chen (2015/2018), Fu–Wang–Yan (2022/2023), and Wendel (1962). The statement is for iid uniform nodes in a **fixed** sphere dimension and **degree-one** exactness only. It is not a finite-sample tail bound or a joint large-dimension theorem. Reproducible computational tests confirm sample-level LP identities but cannot establish the limiting law by themselves. Generic earlier calibration and empirical-process results may warrant further historical-priority review.

Self-review: passed. Independent audit: not yet performed.
