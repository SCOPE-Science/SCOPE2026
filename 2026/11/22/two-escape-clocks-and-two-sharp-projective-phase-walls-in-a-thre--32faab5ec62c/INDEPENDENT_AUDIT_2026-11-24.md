# Independent mathematical audit

## correctness

PASS

For every separately fixed real (a,b), b≠0, the seed-state map has the polynomial inverse obtained by evaluating x_0,x_1,x_2; hence the positive seed chamber maps onto an open initial-state set. For n≥2 the scalar recurrence is x_(n+1)=a−x_(n−1)^2−b x_(n−2). In the stated log bands the gap 2s_(n−1)−s_(n−2) is at least 0.82L at n=2, 0.75·2^m L at n=2m+2>2 (even predecessor has half the current parity scale), and 0.44·2^m L at n=2m+3. The constant term likewise has a denominator ≥exp(0.4·2^m L). Thus the normalized perturbation is at most (|a|+|b|)exp(−0.4·2^m L). For fixed parameters take L so this is <1/4 and the logarithmic errors are bounded by 0.01L. Each next sign is negative, and summing the geometric weights on errors traps each scaled parity log within 0.01L of its seed, strictly improving both provisional bands and closing the induction. The uniform weighted sums are positive continuous heights. After multiplying the tail by 2^m it is bounded by a constant times exp(−0.4·2^m L), proving additive o(1), not merely convergence of scaled logs. In each state the third log rate is strictly less than the first. At even times the leading comparison is H_e vs H_o, and at odd times it is 2H_o vs H_e. At ties the additive error tends to zero on both axes, so their magnitudes have ratio one and their common negative signs give the bisectors. Taking X_0=X_1=R and X_2=R^q for q in [0.8,2.25] reaches ratios below one and above two under the height bounds. The intermediate value theorem yields all five regimes, continuity gives open strict regimes, and neither smoothness nor codimension is inferred for the two level sets.

## originality

PASS

The supported distinct claim is the two simultaneous parity heights with additive remainder and the two projective walls realized together in an open chamber for each parameter pair. The exact-map and broader escape comparisons inspected do not imply this conjunction. This is a best-of-knowledge comparison, not a priority certificate.

## value

PASS

The two parity scales quantify escape for a published model in which a single escape rate does not determine limiting directions. The tie cases genuinely need the sharp remainder, and the chamber uniformly realizes both transitions without changing parameters. That is concrete geometry at infinity beyond known divergence thresholds and without claiming a full escaping-set census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
