# Independent mathematical audit

## correctness

PASS

The frozen Finding is correct. For a required copy event, independence leaves unforced incident edges Bernoulli(p). A copy vertex of motif degree d has conditional degree d+Bin(N−d,p); a nonimage vertex is unchanged. Dividing the conditional degree mass by b_r gives (r)_d/[(N)_d p^d] or zero, and the centered contributions sum to the normalized law after summing deterministic weights. Positivity of b_r and μ transfers signs. For δ≤r<N, the sum has a nonzero positive inverse power, strictly decreases from infinity and is less than k at p=1. For fixed p, each active coefficient increases strictly in r, with the first nonzero term entering at r=δ. The endpoint signs and strictness prove both crossing descriptions, including when there are no interior thresholds. Substitution p=q/N gives coefficient errors O(N^−1) at fixed r and a simple limiting root. In the dense regime each coefficient is u^d[1−(1−u)d(d−1)/(2uN)+O(N^−2)]; at the proposed approximant the root equation has O(N^−2) residual and the derivative is bounded away from zero uniformly. The stated regular, path and triangle cases follow. Independent exact enumeration of all 64 graphs on four vertices with two path embeddings of weights 2 and 5 at p=2/9 gave normalized factors (−3,0,39/4,105/4), matching the theorem (python3 /workspace/branches/independent_checks.py). The frozen verification transcript is not reproducible as written: verify.py increments tests 30+3+9+4+12 times, so line 109 would report 42, not 159 (33 exhaustive graph parameter groups and nine threshold-order groups). This discrepancy concerns the claimed replay count, not the proof or the independent exact check; the frozen script was inspected, not run.

## originality

FAIL

An earlier indexed Resultary record, 788dc5430332, already gives the exact normalized covariance law for every fixed simple motif, including nonregular ones, and derives the identical pinned-copy factor. Fixed weights preserve it by linearity. Both sign directions follow immediately from positivity and monotonicity of the known coefficients, and the two threshold profiles result from the ordinary first-order expansion of that same simple-root equation. The earlier record does not print both p-root expansions, but its formula mechanically implies them.

## value

FAIL

This is a natural mixed statistic, but the frozen result adds fixed weights that cancel identically and elementary root consequences of the earlier exact arbitrary-motif formula. The sparse scale and dense shift are useful descriptions but are obtainable by direct first-order expansion with a nonzero derivative. No distinct non-mechanical invariant or regime survives the comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
