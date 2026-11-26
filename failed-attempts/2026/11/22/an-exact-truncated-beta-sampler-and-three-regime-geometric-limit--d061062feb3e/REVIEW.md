# Independent mathematical audit

## correctness

PASS

An independent construction is to draw n=N−1 independent Uniform(−1,1) labeled coordinates, then condition on the p−1 lower labels preceding all q upper labels and on the p-th order statistic being nonnegative. This is precisely uniform coordinate volume on the given polytope. Ranks are independent of sorted values, so the probability of the label event is (p−1)!q!/n!, and the transformed p-th order statistic has Beta(p,q) law. The conditioning yields the asserted volume and first sampler; conditioning on H negative draws instead gives H∼Bin(n,1/2) conditioned on H≤p−1, with k=p−1−H and the printed weights and label permutations. This includes p=1 or q=1. The chain count follows because fixing the signs and strict total ranking splits the slice into chambers of coordinate volume 1/n!. For the asymptotics the log kernel has derivative [(p−q)−(N−2)t]/(1−t²) and second derivative at most −(q−1). The boundary scaling t=z/N gives the stated exponential kernel by dominated convergence. The critical scaling t=z/√N gives exp(λz−z²/2) with integrable Gaussian domination on z≥0. In the interior, expand at t_N with t=t_N+z/√N; the normalized curvature tends to −1/[4α(1−α)] and the same curvature bound dominates globally. The volume constants follow by integrating the kernels, including the q prefactor and the value of the kernel at its interior mode. RESULT.md §§1–6 and verification.py were inspected, not executed; the numerical sampler and quadrature are not the basis of this decision.

## originality

FAIL

The general pointed-polytope triangulation is not by itself a coverage argument, and the related Resultary geometries do not cover this pinned slice. The decisive prior implication instead comes from the exact labeled-order-statistic reduction and classical incomplete-beta formulas, including a stronger uniform transition expansion. The rank/positivity conditioning gives both samplers and the volume directly, and taking a ratio of the same prior beta tails produces all three stated limits with their constants. No separate geometric limit theorem survives this reduction. This is a direct-corollary determination, not a claim that the same title or pinned-slice application was published earlier.

## value

FAIL

The formulas are correct and useful as a worked example of volume sampling. Under the natural rank representation, however, the chain count and samplers are standard ordering and binomial conditioning, and the three limits are evaluations of a stronger uniform beta expansion. The claimed package offers no independent geometric invariant beyond these mechanical consequences. No supported remainder warrants a substantive repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
