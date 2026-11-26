# Independent mathematical audit

## correctness

PASS

The frozen proof's two justifications for uniqueness are invalid as written. With B=(-1,1), uniform cross-weights, and one A opinion moved from −ε to +ε, the nearest observed median switches from −1 to +1 although the profile changes by only 2ε (0<ε<1). Thus the quoted global nonexpansiveness assertion fails for the specified tie rule even though Han et al. v1 states it. Also, two equal opinions of weight 1/2 have a unique median but arbitrarily small splits give two. The corrected proof replaces both premises: if the comparison profile has unique median m, there is mass >1/2 at or below m and also at or above m, so every median of a profile at sup distance d lies in [m−d,m+d]. Along the explicit solution the medians remain unique by positive affine equivariance. The difference of vector fields against any competing solution is consequently bounded by 2d, and the integral inequality and Grönwall give uniqueness. Differentiating the explicit group shifts gives P′=Q−P and Q′=P−Q; the remaining deviations decay as e^(−t), which checks the ODE and initial data. Their median sum and gap then prove the consensus and both rates, with rates active only for nonzero modes. The K2,2 boundary path has matching signs and strictly closer same-sign medians, so its nonconsensus limit is valid. The verification program was inspected and not run; its sample checks cannot establish uniqueness. The complete corrected files are in repairs/3.

## originality

PASS

The same-model star result already contains the singleton-part consensus specialization, now credited in the corrected result. The checked evidence does not establish the exact selection and two modes for the continuous-time observed-median rule with two nonsingleton groups using arbitrary positive common cross-group profiles. Exact mode calculations for other bipartite drifts do not determine the median invariant.

## value

PASS

The explicit invariant determines which consensus is selected, not just whether a group reaches consensus. For two nonsingleton parts the answer suppresses all within-part nonmedian modes and separates two sharp transient rates, with a concrete two-cluster boundary example showing the risk of dropping uniqueness. The repair preserves this full content and its weighted scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
