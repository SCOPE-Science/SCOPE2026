# Independent mathematical audit

## correctness

PASS

The hypergeometric count X of first-symbol sites in the first block gives W=b−a+2X. Its exact mean, variance and span are as stated. Set p=a/n, z=(X−a²/n)/√n. Stirling in the two numerator binomials uses proportions p+z/(p√n) and p−z/((1−p)√n). The entropy linear terms cancel, the quadratic term is −z²/[2p²(1−p)²], and the prefactor is 1/(√(2πn)p(1−p)); the error is uniform on bounded z because p stays away from 0 and 1. The resulting span-two local mass for W is 2φ_v/√n, while Stirling for Poisson at the exact centering gives φ_h/√n on both parities. Bounded rescaled variances control the tails; conditioning Poisson costs a bounded factor since the retained mass tends to 1/2. The retained-lattice and forbidden-lattice contributions give D=(1+∫|2φ_v−φ_h|)/4, and conditioning gives R=∫|φ_v−φ_h|/2. Solving the two density crossing equations gives t and s, and independent evaluation gives 0.5332306879600328 and 0.16606407498351272 in the balanced case. The strictly positive Gaussian transition kernel strictly contracts both signed differences (each has positive and negative mass), while v/h=4[c(1−c)]²/(1−2c(1−c)) is maximized uniquely at balance. The singular small-variance limit gives D→1; it is a limit of the profile, not a uniform endpoint limit for the discrete laws. Verification metadata, script and captured log were inspected without running the script; their finite checks are supplementary.

## originality

PASS

The supported distinction is the exact lattice-sensitive whole-law separation in the two-macroscopic-colour regime, including the parity-conditioned profile and sharp composition minima, not the model, moments, parity constraint or local Gaussian approximation.

## value

PASS

The result resolves how far Poisson approximation fails for a natural macroscopic matching model, separates an exact parity obstruction from the surviving variance obstruction, and supplies attained sharp universal constants over all interior proportions. The conditioned limit is substantive even after the previously known support issue is removed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
