# Independent mathematical audit

## correctness

PASS

PASS for /workspace/repairs/3/RESULT.md, not the frozen Finding's assertion that every stochastic gradient has the same marginal variance if read along actual iterates. With deterministic x_0, g_1 has random part ξ_1−η_0 ξ_0, so Var(g_1)/σ²=1+η_0²−2ρη_0. In the note's own positive-correlation optimum this is 19/25 versus Var(g_0)/σ²=1. The corrected Finding explicitly fixes equality only for the additive oracle errors; the mathematical schedule and hypotheses remain unchanged. Reconstructed the repaired proof: unrolling yields terminal bias coefficient 1−Σw and weights w_j=η_j∏_{l>j}(1−η_l). The stationary AR(1) covariance is strictly positive definite since the innovation transformation ξ↦(ξ_0,ξ_1−ρξ_0,…), invertible triangular, has diagonal covariance with σ² and σ²(1−ρ²)>0. Multiplying by the tridiagonal precision gives C⁻¹1=b/(1+ρ). The unique stationary point of the strictly convex risk is w=kb, with 1−Σw>0, hence each rate is reconstructed uniquely in (0,1) by telescoping. The stationarity equation gives risk/σ²=t(1−Σw). The equal interior weights give strictly decreasing interior rates; positive-denominator cross-multiplication gives the first difference sign t+ρ(1+ρ) and the last upturn sign ρ(1+ρ)−tP_N. P_N(0)=1, P_N(1)=−1 and its upward leading coefficient force one root in (0,1), the other above 1; rationalizing the smaller root gives r_N=2/(N+sqrt(N²−4(N−2))) and the asymptotic. Checked strictness, ties, N=3 and independence. Independently propagated exact Fraction coefficients of uncorrelated innovations for the two witnesses and recovered risks 1/17 and 3/8 and the variance counterexample (private replay: python3 -B /tmp/opencode/frozen_two_reviews_check.py, block record3). Inspected frozen verify.py and VERIFICATION.md without executing them. The repaired verification description correctly identifies some diagnostic perturbations as outside the weight simplex, e.g. subtraction of 0.001 from an interior weight at N=9, ρ=0.9, t=0.01. That is a valid unconstrained quadratic check, not a feasible schedule comparison. No finite probe supports the universal result by itself.

## originality

PASS

Reassessed the narrower, corrected claim: the GLS weight pattern, the scalar shrinkage optimization and telescoping machinery are ingredients, not innovations. The useful distinct claim is classification of the complete optimal-step order for finite-horizon scalar SGD with equal marginal additive-noise variances and AR(1) correlation: first versus last jump with its exact bias/correlation/horizon boundary. The same-date fixed-ladder result is distinguished expressly in the correction. No priority assertion is made over all possible older sequential representations.

## value

PASS

The repaired equal-marginal-additive-noise finding isolates temporal dependence from time-varying error variance, making a motivated stress test of descending optimal steps. The initial/terminal distinction, horizon-independent negative-correlation boundary and horizon-dependent positive-correlation threshold answer an exact sequential design question beyond the GLS fit. No general optimizer, adaptive-step or empirical training claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
