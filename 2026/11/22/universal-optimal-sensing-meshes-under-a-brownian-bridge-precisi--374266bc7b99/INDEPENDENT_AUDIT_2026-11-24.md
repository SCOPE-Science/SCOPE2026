# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 28–75: the Gaussian conditional mean is the minimum-risk linear estimator. The Wiener representation turns its signal error into the L² distance of 1/2−s from a centered step function; the noise penalty minimizes to (sum |w_i|)²/P by Cauchy–Schwarz. After aggregating coincident jumps and ignoring endpoints, decreasing rearrangement uses no additional sites, cannot increase variation, and strictly improves the signal error for any inversion on positive-length cells. If the decreasing range exceeds 1, clipping then recentering strictly improves the error. For W≤1 the sorted-site objective has Hessian −2(diag(w)−wwᵀ), so the stated stationary nodes are global maximizers of variance reduction, strictly for W<1 with positive weights. Independently, with S_k the cumulative weights, the residual on cell k is (1−W)/2+S_k−s; its zero is w_i/2 on either side of jump i and its outer lengths at the endpoints are (1−W)/2. Integrating the squared residual gives [(1−W)³+sum w_i³]/12. Strict Jensen, including zero padding to n effective jumps, forces n distinct positive-weight jumps at any optimum with W>0; this excludes boundary, coincident and inactive original channels. Cauchy–Schwarz then forces p_i=P/n. The scalar objective is strictly convex, its derivative is negative at 0 and positive at n/(n+1), and its stationary equation gives the stated root, including n=1. Evaluating the objective for n+1 at the old positive minimizer gives strict risk improvement; the scalar equation also gives the stated budget limits. The rational example n=3,P=18 gives both sides of the root equation 2/9 and risk 11/432. The frozen numerical verifier was inspected, not rerun.

## originality

PASS

Credit the known noiseless equally spaced limit and the verified two-site equal-noise overlap. The distinct content established here is the all-n finite-P global result with freely allocated precision, including proof of uniqueness against unequal, inactive and repeated channels. Neither the two-site location result nor the related all-n designs for different covariances gives this joint conclusion.

## value

PASS

The design problem is a nontrivial joint finite-budget optimization even with a fixed Gaussian prior. Its scalar risk law and rigidity translate limited precision directly into a contracted mesh and equal allocation, and exclude all degenerate or asymmetric alternatives. The exact noise-to-noiseless transition, and strict value of adding a sensor even at unchanged total precision, are useful consequences rather than isolated numerical optima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
