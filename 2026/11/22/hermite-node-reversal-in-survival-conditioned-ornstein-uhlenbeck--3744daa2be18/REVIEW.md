# Self-review

## Correctness — PASS

The derivation starts from the killed OU kernel obtained by odd reflection, with drift, noise, and boundary normalization explicitly fixed. The survival factor and numerator are Gaussian integrals, so the conditional probability and the cancellation of independent Poisson no-reset factors are exact. Analytic even-power expansion of the centered truncated-Gaussian integral gives the coefficients \(w(w-3)/6\) and \(w(3w^3-38w^2+165w-180)/360\). The latter is \(9/20\) at \(w=3\). Analyticity permits differentiation of the late-time expansion, proving sign and speed of convergence. The short-time normal increment establishes initial decline and hence at least one strict interior minimum when \(0<w<3\). The proof does not claim uniqueness. The companion checker passed 56 symbolic and numerical assertions, including independent kernel quadrature, while finite checks are not substituted for proof.

## Originality — PASS, with priority limitations

Dubey and Pal (arXiv:2304.05226v1, 2023-04-11), sections 2, 4, and 5, address first-passage **integrated** residence above the reset point and optimization under repeated resetting, not the age-resolved conditional exceedance and its Hermite-node sign reversal. Kishore and Kundu (arXiv:2010.06262), section 4.1.2, address survival-conditioned OU local time and generic odd-Hermite spectral methods; those formulas could be specialized in principle but no same time-resolved threshold or accelerated conditional tail relaxation was identified. Focused published-record searches on aliases, conditional quasi-stationary tails, and Hermite mode cancellation returned distinct problems without an implying theorem. The formula is indeed elementary once the absorbing Gaussian kernel is recognized; its sharp phase boundary and forced turning behavior, rather than the standard kernel or quasi-stationary law, are the assessed additions. Equivalent unindexed results or unpublished derivations remain possible.

## Mathematical value — PASS

A conditional instantaneous occupancy probability is the age-resolved integrand underlying residence statistics for a partially absorbed and resetting particle, and describes the spatial selection bias among long-lived excursions. The dimensionless quantity \(\kappa a^2/D\) separates two opposite directions of late-time approach to the quasi-stationary tail, with a critical cancellation that doubles the exponential relaxation rate. Its predicted compulsory early decrease followed by late increase in the subcritical regime gives a structural, experimentally interpretable nonmonotonicity, not an arbitrary higher moment or a minor numerical improvement.

## Scientific limits and closest literature

Only fixed-parameter asymptotics are established. Uniqueness of the interior minimum and global monotonicity above threshold are open in this work. The conditional event excludes a reset and is not the unconditional full-reset process. Underlying image kernels and Hermite expansions are classical, with publication-priority uncertainty as noted above. There is no independent audit.

Self-review: passed. Independent audit: not yet performed.
