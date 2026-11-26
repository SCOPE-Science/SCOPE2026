# Independent mathematical audit

## correctness

PASS

Renewal reward gives the stationary age density S(a)/μ, including lattice clocks with equilibrium phase. From a zero reset the Gaussian variance is (D/κ)(1−e^(−2κa)); the Jacobian of u=e^(−2κa) gives g=q/u. All even moments exist, and after dividing by their Gaussian factors they determine the compact mixing law by polynomial density. The canonical left-continuous q is fixed by its a.e. values and produces a right-continuous survival curve; this picks the correct value at atoms. For the converse, monotonicity plus ∫q/u=1 implies q(0+)=0. Normalizing by c=q(1−)>0 then gives S(0)=1, a proper finite positive law, and the same integral gives mean 1/(2κc). As an independent atomic check, clock masses 1/3,2/3 at times 1,2 give equilibrium age densities 3/5 and 2/5 on the two unit slabs; endpoint normalization and the downward jumps recover the stated masses and mean 5/3. In the alias construction the (K+1)st derivative of a compact bump annihilates every polynomial through degree K; small amplitude keeps both g and q′ strictly positive on its compact support, with the endpoint untouched and hence the mean fixed. In the instability construction ∫δg=0, q(1−)=1, ∥δg∥₁=O(ε/n), but δq′=−εuη cos(nu)+O(ε/n) uniformly. The chosen ε preserves positivity; the Gaussian mixture contracts TV, while the clock-density change has TV exactly (1/2)∫|δq′|du. The zero-mean periodic part of |cos| has a bounded primitive, so integration by parts against the smooth compact weight uη gives the average 2/π and the stated limiting positive distance. Thus the discontinuity is at the smooth exponential baseline with the specified fixed mean, not at every reset law or for unknown dynamical parameters. Replay RESULT.md:38–82. The frozen verify.py was inspected, not executed; its cancellation examples and arithmetic checks do not establish these uniform or infinite-frequency claims.

## originality

PASS

The checked forward renewal theory and general age-filter inversion are substantial prior ingredients; the one-marginal identifiability principle itself is a short composition with compact Gaussian-mixture determinacy. The supported distinct contribution is an exact range in terms of the observable mixing density, together with explicit admissible smooth counterexamples quantifying what is lost even at fixed mean. In particular, the positive limiting TV separation despite full observable-law TV convergence does not follow from a finite moment alias or from the general age/filter identity alone. This judgment is against the inspected statements, not a historical-first claim.

## value

PASS

The position marginal is natural to observe and renewal intervals may be hidden. The theorem separates exact realizability, finite-moment ambiguity, and robustness even with full distributional information. In particular, keeping the mean, smoothness, positivity and OU dynamics fixed still does not yield inverse continuity in the strong TV sense, which is a useful constraint for calibration beyond the standard forward mixture. It does not provide finite-sample estimators or rates and should not be interpreted as an inverse theorem for unknown κ,D or nonequilibrium sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
