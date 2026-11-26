# Independent mathematical audit

## correctness

PASS

Writing h=−min(x,y)+(x²+y²)/2 gives Δ=∫[2x(1−F)−(1−F)²]dx. My separate symbolic replay from that identity gives d/15−c²/30−d²/210 and verifies the rational zero parametrization. The derivative lower bound 2c(1−3r)>0, positive left endpoint, and factorization F−x=−x(1−x)[c+d(2x−1)] prove admissibility and strict stochastic separation. The derivative of the doubled projection, after dropping an irrelevant constant, is 2(x−(1−F(x))); integrating and taking exact variance gives the stated V, null value 1/45 and r=1/4 fraction. The sign of the displayed derivative follows from 24255−160622/9>0; variance is positive by the nonconstant projection and the positive density. The computed 5% limit is 0.0476118698. For the different linear-density family, the exact mean is −c²/30. The bounded degenerate kernel has remainder variance O(n⁻²) uniformly: distinct unordered pairs have zero covariance even when sharing one index, by conditional centering. First-projection row variances converge to the positive null limit by uniform density/projection convergence, and boundedness gives Lindeberg. The null-scaled drift is −h² n^(1/2−2γ)/(2√5); continuity at the cutoff gives the two finite-shift cases, and tightness plus divergent negative drift gives power one otherwise. For critical nonzero shift the two-sided normal tail is strictly increasing in the absolute shift and below one. The comparison is neither a minimax bound nor a claim about censoring. Own replay: /workspace/reviews/replay_statistics.py and replay_statistics.txt; the frozen script was inspected, not executed.

## originality

PASS

Pass rests on the explicit low-degree monotone zero-target curve with strictly subnominal fixed-alternative power throughout the stated parameter interval and its exact quantitative comparison. There is considerable same-day overlap: zero-target smooth laws, monotone blind laws near the null by implication, subnominal behavior for a different symmetric law, and the exact linear-tilt drift all occur in the retrieved material. Do not credit those constituent facts, or the local scale in isolation as independent evidence of priority. None of the inspected results yields the explicit quadratic strictly increasing subnominal curve and its full variance law. Within-day priority is unresolved.

## value

PASS

The point is not another arbitrary nonuniform zero. A quadratic perturbation (the lowest polynomial degree permitting this cancellation among nonuniform densities) produces strictly increasing densities whose CDFs separate from uniformity in a single direction and whose rejection rate stays below the nominal level throughout the stated branch. This gives a simple calibrated, shape-restricted benchmark for a procedure intended to detect nonuniform laws. The local-power calculation gives scope and a quantitative comparison, not novelty or value by itself over the prior exact tilt drift.

The dated certificate retains the supplied scientific assessment, sources and limitations.
