# Independent mathematical audit

## correctness

PASS

For the repaired claim joint Gaussianity gives deterministic conditional variance and the stated matrix gain. Continuity of the cross-covariance follows by Cauchy–Schwarz from mean-square continuity. The two inverse norms are at most 1/[eta(1-|rho|)], giving the uniform O(eta^-2) gain error. All four vertices of the cross-covariance square are realized, and strict convexity excludes any other maximizer. Reference minus repeat has sign 2rho-1, and compactness with uniform convergence gives convergence in distance of all optimizer sequences. Only a leading-order tie is asserted at equality. The unchanged symbolic checker checks the matrix algebra, not the Gaussian assumption. To see why the original omission mattered, use independent symmetric +/-sqrt(eta) errors at rho=0 on the bridge. Subtract sqrt(eta) times the sign of the noisy midpoint reading; the estimate is exact when the latent midpoint has absolute value less than sqrt(eta), and its squared error is bounded by 4eta times the Gaussian-tail indicator. The posterior-mean gain for the bridge integral from a midpoint plus an independent endpoint reading tends to 1/16, not zero. This also refutes the original formula if gain is instead averaged over observations.

## originality

PASS

Pass is for the repaired arbitrary-kernel high-noise optimizer theorem, not the Brownian-bridge phase diagram or Gaussian conditioning. The closely matching Resultary theorem gives a stronger finite-noise answer for one specific kernel with pinned endpoints and nonnegative correlations; it does not give the repaired optimizer limit for arbitrary latent kernels, for nonpinned reference sites, or for any fixed negative rho. The general published covariance-aware design formulation is a starting identity, not an optimizer classification. This is best-knowledge originality.

## value

PASS

The sharp universal optimizer transition answers a concrete design question: when to repeat a strong measurement and when to sacrifice a signal measurement for noise calibration. It identifies the full limiting placement set and leading optimal gain, not merely a comparison of two arbitrarily chosen sites. It remains relevant without pinned sites or explicit kernel formulas and does not depend on the removed bridge-specific witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
